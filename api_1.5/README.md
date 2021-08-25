# containerd API Python package

This repository provides a Python3 API to [containerd's](https://containerd.io)
(gRPC) API, directly generated from the [original containerd `.proto` API
definitions](https://github.com/containerd/containerd/tree/master/api). As it is
generated from the protocol files, this Python package does not aim to be a
fully Pythonesque package. In consequence, the usual idiosyncrasies of gRPC and
protoc shine through.

> **Note:** with Python2 going end-of-life in January 2020 we don't support
> Python2 in this package at this very late time in the lifecycle.

## Versioning

The versioning of this package complies with [PEP
440](https://www.python.org/dev/peps/pep-0440/).

The version is composed of the version of the supported containerd API (e.g. 1.2
or 1.3) and an incremental number for each pycontainerd release for that
specific containerd API version (starting from 0) connected with a '.' (a dot).

Ideally the Python containerd API has to be generated only once per containerd
API version, resulting in x.y.0 package versions.

The result is version numbers like:

- 1.2.1 for the second release for API 1.2
- 1.3.0 for the first release for API 1.3

## License

This project is licensed as [Apache License, Version 2.0](http://www.apache.org/licenses/LICENSE-2.0) (SPDX-License-Identifier: Apache-2.0).

You can obtain the full license text from the file `License` of this repository.

## Install as Python Package

Installation depends on your starting point:

1. You have a `pycontainerd` Python Wheel package (something like
   `containerd-x.y.z-py3-none-any.whl`).
2. You only have the source code (the result of cloning the git repository).

### Dependencies

Python3 PIP is needed for Wheel installations (either from a ready Wheel package
or from a self-built package). PIP takes care of installing all the Python
packages listed as dependencies. Runtime dependencies are nevertheless listed
below.

### Installation from Wheel package

Go to the directory where the wheel package is available and run:

```bash
sudo pip3 install containerd-<x.y.z>-py3-none-any.whl
```

Being `containerd-<x.y.z>-py3-none-any.whl` the filename of the wheel package.

> *NOTE*: a global installation is required (or rather, more convenient) because
the `containerd` API socket is usually only reachable for `root`.

### Installation from source code

Additionally, if building from source code you'll also need `make`.

A Makefile is being provided that takes care of

1. Building the Wheel package
2. Installing the Wheel package

Just run from the toplevel directory of this repository:

```bash
make install
```

The second step is under the hood simply running the installation of the wheel
package explained above. Including the global installation, therefore a `sudo`
execution is asking for the user's password (assuming the user has that right).

## Package Structure and Usage

The resulting Wheel package provides following Python packages (they have to be
imported individually), providing multiple modules:

- containerd.events
- containerd.services.containers.v1
- containerd.services.content.v1
- containerd.services.diff.v1
- containerd.services.events.v1
- containerd.services.images.v1
- containerd.services.introspection.v1
- containerd.services.leases.v1
- containerd.services.namespaces.v1
- containerd.services.snapshots.v1
- containerd.services.tasks.v1
- containerd.services.version.v1
- containerd.types
- containerd.types.tasks
- containerd.protobuf (_note: this is not a protobuf alias_)
- containerd.vendor.gogoproto

In order to get the modules being provided by a package you can run:

```bash
python3 -c 'import <package> ; help(<package>)'
```

For example, for `containerd.events`:

```bash
python3 -c 'import containerd.events ; help(containerd.events)'
```

## Examples

### List All Namespaces

The following simple example queries containerd for its list of available
containerd namespaces. Make sure you have the necessary privileges to connect to
containerd; you may need to run this script as root:

```python
import grpc
from containerd.services.namespaces.v1 import namespace_pb2_grpc, namespace_pb2

with grpc.insecure_channel('unix:///run/containerd/containerd.sock') as channel:
    namespacev1 = namespace_pb2_grpc.NamespacesStub(channel)
    namespaces = namespacev1.List(namespace_pb2.ListNamespacesRequest()).namespaces
    for namespace in namespaces:
        print('namespace:', namespace.name)
```

Usually, you want to add proper error handling. This is just a very simplistic
example to illustrate the principle.

### List Containers in a Specific Namespace

Several of containerd's APIs are namespaced. That is, they work only on a single
namespace at a time. The namespace applies on the level of individual service
calls and needs to be specified as an (additional) metadata element to these
calls. If not specified, it the namespace will default to the namespace named
`default`. The following example lists all containers in the `"moby"` namespace;
this is the containerd namespace used by Docker.

```python
import grpc
from containerd.services.containers.v1 import containers_pb2_grpc, containers_pb2

with grpc.insecure_channel('unix:///run/containerd/containerd.sock') as channel:
    containersv1 = containers_pb2_grpc.ContainersStub(channel)
    containers = containersv1.List(
        containers_pb2.ListContainersRequest(),
        metadata=(('containerd-namespace', 'moby'),)).containers
    for container in containers:
        print('container ID:', container.id)
```

### Watch containerd Events Flowing

Containerd events can be easily read from the endless event stream via the
`containerd.services.events.v1` API, using the `Subscribe` service. The
following example subscribes to all events and then prints their type and
contents as the events come:

```python
import grpc

from containerd.services.events.v1 import unwrap, events_pb2, events_pb2_grpc
from google.protobuf import any_pb2

with grpc.insecure_channel('unix:///run/containerd/containerd.sock') as channel:
    print("waiting for containerd events...")
    eventsv1 = events_pb2_grpc.EventsStub(channel)
    for ev in eventsv1.Subscribe(events_pb2.SubscribeRequest()):
        print('event type: ', ev.event.type_url)
        print('value: ', unwrap(ev))
```

> **Note:** `containerd.services.events.v1.unwrap(envelope)` is a convenience
> function which unwraps the event object inside an event envelope returned by
> `Subscribe()`: the unwrapped event object is returned as a Python object of
> sub class `containerd.events.*` (as opposed to the arbitrary "any" binary
> value inside the event envelope).

## Executable Programs

To help containerd client developers getting started, we've included two simple
examples which are also made available as the CLI programs `lsctr` and
`watchctr` (source code in `examples/`) when cloning the repository.

You first have to install the wheel package for the `containerd` package.

- `lsctr` lists all containerd containers in all namespaces. It is basically
  kind of an all-in-one combination of the `ctr` commands for namespaces,
  containers, and tasks in a single command.
- `watchctr` watches containerd events, such as container creation, start, stop,
  et cetera, and then prints them to the terminal.

To check that it works, run the `lsctr` command: this should list all available
containerd containers, across all containerd namespaces (remember to use `sudo`
in case you don't have the necessary privileges as an ordinary user to talk to
containerd):

```bash
sudo lsctr
```

This should spit out something like this, when running on a recent Docker CE
installation, which uses containerd under the hood:

```txt
moby
  ⤏ labels (0):
  ▩ container: 0eeb9e2862e9f68e832a2e2c60a2e44e74d54b05266532cf19b112f4d959e3fb
    ▷ PID: 3359 ⚐ status: RUNNING
    ⚙ runtime: io.containerd.runtime.v1.linux
    ⤏ labels (1):
        "com.docker/engine.bundle.path": "/var/run/docker/containerd/0eeb9e2862e9f68e832a2e2c60a2e44e74d54b05266532cf19b112f4d959e3fb"
    ◷ created: 2019-09-04 07:24:32.646856 ◷ updated: 2019-09-04 07:24:32.646856
  ▩ container: 1663afd0ddc6e0bba30b7fcc27b26044ece6022d970e32731db5dcb807b168df
    ▷ PID: 66062 ⚐ status: RUNNING
    ⚙ runtime: io.containerd.runtime.v1.linux
    ⤏ labels (1):
        "com.docker/engine.bundle.path": "/var/run/docker/containerd/1663afd0ddc6e0bba30b7fcc27b26044ece6022d970e32731db5dcb807b168df"
    ◷ created: 2019-08-16 08:08:21.471493 ◷ updated: 2019-08-16 08:08:21.471493
...
```

You can use `lsctr -h` to see the few CLI options available.

## Package Requirements

The following Python packages are required:

- [`grpcio`](https://pypi.org/project/grpcio/) – gRPC for Python; required in
  order to communicate with containerd. This is a runtime dependency.
- [`protobuf`](https://pypi.org/project/protobuf/) – protobuf for Python;
  required in order to communicate with containerd. This is a runtime
  dependency.
- (optional) `grpcio-tools` – only required when re-generating the containerd
  API Python code using `genpb2.sh`.

## Python ContainerD API

### API Package (Re)Generation

In case you need to regenerate or update the Python code for the containerd API,
in the top-level directory of this repository, run:

```bash
./genpb2.sh
```

Normally, you should not need to regenerate the grpc/pb2 Python modules unless
you are a project contributor or maintainer.

### Project Organization

The overall directory structure of the Python containerd API package is as
follows (inside the `api_1.x/` directories):

- `containerd/` contains the Python modules generated by protoc as well as a
  very few hand-made modules. In order to avoid polluting the top-level package
  namespace with proto dependencies, `genpb2.sh` "vendorizes" dependencies only
  for such `.proto` files for which no PyPI packages are available, moving such
  dependencies inside the `containerd` top-level Python package namespace.
  - `services/` contains the containerd service API v1.
  - `events/` contains the containerd event definitions.
  - `types/` contains containerd type definitions required by services and
    events.
  - `protobuf/` internal dependency.
  - `vendor/` contains the "vendorized" dependencies.
    - `gogoproto/` modules not available as a PyPI package.
- `genpb2.sh` is a script to recreate or update the `_pb2.py` and `_pb2_grpc.py`
  Python modules from the containerd API `.proto` file definitions and
  dependencies. See `genpb2.sh` for more information on its workings.

## Survival References

- [gRPC Basics – Python](https://grpc.io/docs/tutorials/basic/python/).
- [Protocol Buffers Python Reference: Python Generated
  Code](https://developers.google.com/protocol-buffers/docs/reference/python-generated).
- [containerd API protocol
  definitions](https://github.com/containerd/containerd/tree/master/api).
