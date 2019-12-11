import grpc
from containerd.services.namespaces.v1 import namespace_pb2_grpc, namespace_pb2

def test_namespaces(containerd_server):
    with grpc.insecure_channel(containerd_server) as channel:
        namespacev1 = namespace_pb2_grpc.NamespacesStub(channel)

        namespaces = namespacev1.List(namespace_pb2.ListNamespacesRequest()).namespaces
        namespace_names = [namespace.name for namespace in namespaces]
        assert namespace_names == ['ns_one', 'ns_two', 'ns_three']

