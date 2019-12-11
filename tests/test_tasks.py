import grpc
from containerd.services.namespaces.v1 import namespace_pb2_grpc, namespace_pb2
from containerd.services.tasks.v1 import tasks_pb2, tasks_pb2_grpc

def test_tasks(containerd_server):
    with grpc.insecure_channel(containerd_server) as channel:
        namespacev1 = namespace_pb2_grpc.NamespacesStub(channel)
        tasksv1 = tasks_pb2_grpc.TasksStub(channel)

        namespaces = namespacev1.List(namespace_pb2.ListNamespacesRequest()).namespaces
        namespace_names = [namespace.name for namespace in namespaces]
        assert namespace_names == ['ns_one', 'ns_two', 'ns_three']
        for namespace in namespaces:
            tasks = tasksv1.List(tasks_pb2.ListPidsRequest(),
                                metadata=(('containerd-namespace', namespace.name),)).tasks
            task_ids = [task.container_id for task in tasks]
            assert task_ids == ['c_one', 'c_three']

