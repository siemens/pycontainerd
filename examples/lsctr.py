#!/usr/bin/env python3
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
#
# lsctr -- lists all containers in all containerd namespaces. Compared to the
# (unsupported) ctr CLI tool for containerd, our script (1) works on all
# containerd namespaces and (2) is a simplified combination of "ctr -n $NS
# container ls" and then many "ctr -n $NS container info $ID". It is mainly
# intended for illustration purposes, but has some value for snooping out
# container hosts.

import grpc
from containerd.services.namespaces.v1 import namespace_pb2_grpc, namespace_pb2
from containerd.services.containers.v1 import containers_pb2, containers_pb2_grpc
from containerd.services.tasks.v1 import tasks_pb2, tasks_pb2_grpc
from containerd.types.task import task_pb2

import argparse

def lsctr(args):
    # Connect to containerd using the well-known containerd.sock and location.
    # Please note that this does not really connect yet, but just jots down the
    # grpc server address and the connect will only happen later when the first
    # service is to be called.
    with grpc.insecure_channel(args.containerd_address) as channel:
        # These are the containerd APIs we're going to use below.
        namespacev1 = namespace_pb2_grpc.NamespacesStub(channel)
        containersv1 = containers_pb2_grpc.ContainersStub(channel)
        tasksv1 = tasks_pb2_grpc.TasksStub(channel)

        # First, discover all available containerd namespaces. These namespaces must not
        # be confused with Linux-kernel namespaces, instead, they are a
        # containerd-specific user-space organizational means only.
        try:
            namespaces = namespacev1.List(namespace_pb2.ListNamespacesRequest()).namespaces
        except grpc.RpcError as e:
            print('ERROR: cannot connect: {}'.format(e))
            return
        # Now look for containers and their corresponding tasks in each of the
        # containerd namespaces...
        for namespace in namespaces:
            print('⬚ namespace:', namespace.name)
            print('  ⤏ namespace labels ({}):'.format(len(namespace.labels)))
            for label in namespace.labels:
                print('      "{n}": "{v}"'.format(n=label, v=namespace.labels[label]))

            # The containerd API is slightly "peculiar" in that the list of containers
            # lacks such useful information such as PID and container status. Instead,
            # these nuggets of wisdom are to be gleamed from the tasks lists. Both the
            # list of containers as well as the list of tasks are related by their IDs.
            # That is, the task ID is the same as the container ID. However, there
            # doesn't need to be a task for a container, so be careful. According to
            # https://github.com/containerd/containerd/blob/master/design/architecture.md,
            # the list of containers is considered as metadata (as are images), while
            # tasks are directly associated with the runtime(s).
            tasks = tasksv1.List(tasks_pb2.ListPidsRequest(),
                                metadata=(('containerd-namespace', namespace.name),)).tasks
            taskidx = dict()
            for task in tasks:
                taskidx[task.id] = task

            # We also need the list of containers, and not only the list of tasks, as we
            # need metadata: in particular, the labels of a container. While Docker is
            # giving us not much but a "com.docker/engine.bundle.path", Kubernetes
            # labels all the important metadata, such as pod namespace and name,
            # container name, et cetera. And cri-containerd throws in a kind to indicate
            # Kubernetes' pause sandboxes. Only Docker isn't keen of labeling.
            containers = containersv1.List(containers_pb2.ListContainersRequest(), 
                                        metadata=(('containerd-namespace', namespace.name),)).containers
            for container in containers:
                print('  ▩ container:', container.id)
                if container.id in taskidx:
                    t = taskidx[container.id]
                    print('    ▷ PID:', t.pid, '⚐ status:', task_pb2.Status.Name(t.status))
                print('    ⚙ runtime:', container.runtime.name)
                print('    ⤏ labels ({}):'.format(len(container.labels)))
                for label in container.labels:
                    print('        "{n}": "{v}"'.format(n=label, v=container.labels[label]))
                print('    ◷ created:', container.created_at.ToDatetime(), '◷ updated:', container.updated_at.ToDatetime())
                #print('    extensions:', container.extensions)
                #print('    spec:', container.spec)

            print()

def main():
    from containerd import __api_version__
    
    parser = argparse.ArgumentParser(
        prog='lsctr',
        description='list all containerd containers in all namespaces',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument(
        '--version',
        action='version',
        version='%(prog)s ' + __api_version__,
        help='show version information and exit'
    )
    parser.add_argument(
        '--address', '-a',
        dest='containerd_address', type=str, metavar='A',
        default='unix:///run/containerd/containerd.sock',
        help='address for containerd\'s GRPC server'
    )

    args = parser.parse_args()
    lsctr(args)

if __name__ == '__main__':
    main()
