#!/usr/bin/env python3

import argparse
import concurrent.futures
import grpc
import time

from containerd.services.namespaces.v1 import namespace_pb2_grpc, namespace_pb2
from containerd.services.containers.v1 import containers_pb2, containers_pb2_grpc
from containerd.services.tasks.v1 import tasks_pb2, tasks_pb2_grpc
from containerd.types.task import task_pb2

class NamespacesServicer(namespace_pb2_grpc.NamespacesServicer):
    def List(self, request, context):
        response = namespace_pb2.ListNamespacesResponse()
        for ns_name in ['ns_one', 'ns_two', 'ns_three']:
            response.namespaces.add().name = ns_name
        return response

class TasksServicer(tasks_pb2_grpc.TasksServicer):
    def List(self, request, context):
        response = tasks_pb2.ListTasksResponse()
        for container_id in ['c_one', 'c_three']:
            response.tasks.add().container_id = container_id
        return response

class ContainersServicer(containers_pb2_grpc.ContainersServicer):
    def List(self, request, context):
        response = containers_pb2.ListContainersResponse()
        for container_id in ['c_one', 'c_two', 'c_three']:
            response.containers.add().id = container_id
        return response

def serve(address):
    server = grpc.server(concurrent.futures.ThreadPoolExecutor(max_workers=2))
    namespace_pb2_grpc.add_NamespacesServicer_to_server( \
                                                NamespacesServicer(), server)
    tasks_pb2_grpc.add_TasksServicer_to_server( \
                                                TasksServicer(), server)
    containers_pb2_grpc.add_ContainersServicer_to_server( \
                                                ContainersServicer(), server)
    server.add_insecure_port(address)
    server.start()
    print('Serving on %s' % (address,))
    try:
        while True:
            time.sleep(60 * 60 * 24)
    except KeyboardInterrupt:
        server.stop(0)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--address', '-a',
        default='unix:///run/user/1000/pycontainerd-mock.sock',
        help='address for containerd\'s GRPC server'
    )

    args = parser.parse_args()
    serve(args.address)

if __name__ == '__main__':
    main()

