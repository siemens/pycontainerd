#!/usr/bin/env bash
#
# Copyright 2019 Siemens AG
# SPDX-License-Identifier: Apache-2.0

set -u

last_release=$(git describe --exact-match 2>/dev/null)

if [ ! -z ${last_release} ] ; then
    echo ${last_release}
else
    last_release="$(git describe | rev | cut -d '-' -f 3- | rev )"
    if [ $# -eq 1 ] && [ $1 = '-r' ] ; then
        echo ${last_release}
    else
        echo ${last_release}.dev0
    fi
fi

