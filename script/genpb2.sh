#!/bin/bash
#
# Copyright 2019 Siemens AG
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#
# SPDX-License-Identifier: Apache-2.0
#------------

# This script generates the necessary Python grpc/protobuf modules from a set of
# .proto files describing the containerd API and the required dependencies
# dependencies. It first downloads the .proto definitions from its source
# repositories, in specific versions. It then generates a temporary .proto file
# hierarchy from only the ones actually required to build the Python containerd
# API modules. The .proto files are getting edited automatically to correctly
# reference their dependencies without import path aliasing (which would then
# result in runtime errors due to the same gRPC elements getting registered more
# than once). Finally, the script runs the protoc compile to generate the Python
# packages/modules for the Python containerd API.
#
# The overall structure is as follows:
#
# - 1.x/containerd/: contains the Python containerd binding packages for API
#       version 1.x. Please note that we skip the "api" package element in order
#       to avoid stuttering.
#    - services/
#    - events/
#    - types/
#    - protobuf/plugin/ -- fieldpath
#    - gogoproto/ -- gogo

# Only generation engine mechanics beyond this point.
shopt -s globstar

# Exit immediately if a pipeline (which may consist of a single simple
# command), a list, or a compound command (see SHELL GRAMMAR above), exits
# with a non-zero status.
set -e

# Treat  unset variables and parameters other than the special parameters "@"
# and "*" as an error when performing parameter expansion.
set -u

# Get fullpath of script directory to generate all paths that can be absolute
BASE_DIR=$(dirname $(dirname $(readlink -f $0)))

# Where to download the repositories with the .proto sources to...
usage="genpb2.sh [-k] [-n] [-a <API version>]"
usage+="\n\t-k: keep temporary files"
usage+="\n\t-n: new bindings generation"
usage+="\n\t-a: generate the bindings for <API version>"
keep_temp=false
generate_anew=false
API_VERSION=1.3
while getopts kna: opt ; do
    case ${opt} in
        k)
            keep_temp=true
            ;;
        n)
            generate_anew=true
            ;;
        a)
            API_VERSION="${OPTARG}"
            ;;
        *)
            echo -e "${usage}"
            exit 1
            ;;
    esac
done

if [ "${keep_temp}" = false ] ; then
    TEMP_DIR=$(mktemp -d)
else
    TEMP_DIR="${BASE_DIR}/tmp"
    rm -rf "$TEMP_DIR"
    mkdir -p "${TEMP_DIR}"
fi

# Where to prepare the .proto sources ready for compiling with protoc...
PROTO_DIR="$TEMP_DIR/protos"
rm -rf "$PROTO_DIR"

# The following sed stream editing expressions fix "absolute" imports of
# containerd's own API protocol files, removing the "github.com/containerd" and
# "api" import path elements. Doing so avoids (1) import path aliasing and
# removes the (2) stuttering "api". These expressions additionally "vendorize"
# the "github.com/containerd/containerd/protobuf" import path to just
# "containerd/protobuf".
VENDORIZE=(
    "-e" 's/import( weak)? "containerd\/api\//import\1 "containerd\//g'
    "-e" 's/import( weak)? "github.com\/containerd\/containerd\/api\//import\1 "containerd\//g'
    "-e" 's/import( weak)? "github.com\/containerd\/containerd\/protobuf\//import\1 "containerd\/protobuf\//g'
    "-e" 's/import( weak)? "gogoproto\//import\1 "containerd\/vendor\/gogoproto\//g'
)

# Copies a set of .proto source files from a source directory (and its
# subdirectories) into a destination tree, and edits the .proto files during the
# copy operation. The .proto files are edited with import paths to dependencies
# getting "vendorized" in order to avoid later global package name conflicts.
#
# - $1: path to directory (and its subdirectories) containing .proto files to be
#   moved into place.
# - $2: destination directory.
# - $3: optional rebase root directory.
function prepprotos {
    # Make sure that the directory path to the source .proto files always has
    # a trailing "/". Same for the destination directory.
    DIR=$1
    [[ "$DIR" != */ ]] && DIR="$DIR/"
    DESTDIR=$2
    [[ "$DESTDIR" != */ ]] && DESTDIR="$DESTDIR/"
    # Allow "vendoring" so that we can move those global packages out of the
    # top-level package hierarchy which are dependencies in order to later
    # avoid Python package conflicts with some other Python package also
    # bringing in these global dependencies. Three cheers to venv and
    # containers, though.
    REBASE=$3
    [[ -n "$REBASE" && "$REBASE" != */ ]] && REBASE="$REBASE/"
    # New process each .proto file inside $DIR and place the processed result
    # into $DESTDIR $REBASE ...
    echo "preparing .proto files from $DIR..."
    for PROTO in $DIR**/*.proto; do
        RELPROTO=${PROTO#"$DIR"}
        NEWPROTO="$DESTDIR$REBASE$RELPROTO"
        NEWDIR=${NEWPROTO%/*}
        echo "  ... $RELPROTO --> $NEWPROTO"
        mkdir -p $NEWDIR
        sed -r "${VENDORIZE[@]}" "$PROTO" > "$NEWPROTO"
    done
}

generate_api () {
    CONTAINERD_TAG="v${API_VERSION}.0"

    # Clean up the Python package area, just to be on the safe side.
    rm -rf ${BASE_DIR}/api_${API_VERSION}/containerd
    mkdir -p ${BASE_DIR}/api_${API_VERSION}/containerd

    if [ -f api_${API_VERSION}/version ] ; then
        decl_api_version=$(grep -oP '^__api_version__\s*=\s*.*' api_${API_VERSION}/version | grep -oP '\d+\.\d+')
        if [ "${API_VERSION}" != "${decl_api_version}" ] ; then
            echo "API version declared in 'api_${API_VERSION}/version' is '${decl_api_version}', it doesn't match"
            exit 1
        fi
        GENERATION=$(grep -oP '^__generation__\s*=\s*.*' api_${API_VERSION}/version | grep -oP '\d+')
        GENERATION=$(expr ${GENERATION} + 1)
    else
        GENERATION=1
    fi

    # Fetches a specificly tagged release version of containerd and clones into
    # our temporary working area. Usually, we will only need vx.y.0 releases, as
    # containerd keeps its service API locked during the lifecycle of a specific
    # minor version, regardless of the patch series. See also:
    # https://github.com/containerd/containerd/blob/master/api/README.md
    git -c advice.detachedHead=false \
        clone --branch "$CONTAINERD_TAG" --depth 1 \
        https://github.com/containerd/containerd.git "$TEMP_DIR/containerd"

    prepprotos "$TEMP_DIR/containerd/api/services" "$PROTO_DIR" "containerd/services"
    prepprotos "$TEMP_DIR/containerd/api/types" "$PROTO_DIR" "containerd/types"
    prepprotos "$TEMP_DIR/containerd/api/events" "$PROTO_DIR" "containerd/events"
    prepprotos "$TEMP_DIR/containerd/protobuf" "$PROTO_DIR" "containerd/protobuf"
    mkdir -p "$PROTO_DIR/containerd/vendor"
    cp -R "$TEMP_DIR/containerd/vendor/github.com/gogo/protobuf/gogoproto" "$PROTO_DIR/containerd/vendor"
    # We need the google/rpc .proto definitions in order to compile everything,
    # but we don't want to get packages for them generated, as these are to be
    # supplied by the existing pip grpcio and protobuf packages instead.
    cp -R "$TEMP_DIR/containerd/vendor/github.com/gogo/googleapis/google" "$PROTO_DIR"

    # With everything correctly in place, we can now generate the Python modules
    # in one single go (erm, not that Go, but go). Please note that we only
    # generate Python modules for things inside containerd/, but not for the
    # google/ stuff.
    echo "generating Python containerd modules..."
    echo "in $PROTO_DIR"
    (
        cd api_${API_VERSION}
        python3 -m grpc.tools.protoc \
            -I="$PROTO_DIR" \
            --python_out=. --grpc_python_out=. \
            $PROTO_DIR/containerd/**/*.proto
    )

    # Add setup.py and README.md
    cp -f ${BASE_DIR}/resources/setup.py \
        ${BASE_DIR}/api_${API_VERSION}/
    cp -f ${BASE_DIR}/README.md \
        ${BASE_DIR}/api_${API_VERSION}/

    # Add needed __init__.py to get Python packages
    for package in $(find ${BASE_DIR}/api_${API_VERSION}/containerd -type d) ; do
        touch ${package}/__init__.py
    done
    cp -f ${BASE_DIR}/resources/containerd/services/events/v1/__init__.py \
        ${BASE_DIR}/api_${API_VERSION}/containerd/services/events/v1/

    export API_VERSION GENERATION
    envsubst '${API_VERSION} ${GENERATION}' < \
        resources/containerd/__init__.py.in > \
        api_${API_VERSION}/version
    cp api_${API_VERSION}/version api_${API_VERSION}/containerd/__init__.py

    # Clean up.
    if [ "${keep_temp}" = false ] ; then
        rm -rf "$TEMP_DIR"
    fi
}

if [ -d ${BASE_DIR}/api_${API_VERSION} ] && [ "${generate_anew}" = false ] ; then
    echo "pycontainerd ${API_VERSION} is already available"
else
    echo "Generating pycontainerd ${API_VERSION}"
    generate_api ${API_VERSION}
fi

echo "done."
