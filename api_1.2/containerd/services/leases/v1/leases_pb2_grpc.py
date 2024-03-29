# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from containerd.services.leases.v1 import leases_pb2 as containerd_dot_services_dot_leases_dot_v1_dot_leases__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


class LeasesStub(object):
    """Leases service manages resources leases within the metadata store.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Create = channel.unary_unary(
                '/containerd.services.leases.v1.Leases/Create',
                request_serializer=containerd_dot_services_dot_leases_dot_v1_dot_leases__pb2.CreateRequest.SerializeToString,
                response_deserializer=containerd_dot_services_dot_leases_dot_v1_dot_leases__pb2.CreateResponse.FromString,
                )
        self.Delete = channel.unary_unary(
                '/containerd.services.leases.v1.Leases/Delete',
                request_serializer=containerd_dot_services_dot_leases_dot_v1_dot_leases__pb2.DeleteRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.List = channel.unary_unary(
                '/containerd.services.leases.v1.Leases/List',
                request_serializer=containerd_dot_services_dot_leases_dot_v1_dot_leases__pb2.ListRequest.SerializeToString,
                response_deserializer=containerd_dot_services_dot_leases_dot_v1_dot_leases__pb2.ListResponse.FromString,
                )


class LeasesServicer(object):
    """Leases service manages resources leases within the metadata store.
    """

    def Create(self, request, context):
        """Create creates a new lease for managing changes to metadata. A lease
        can be used to protect objects from being removed.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Delete(self, request, context):
        """Delete deletes the lease and makes any unreferenced objects created
        during the lease eligible for garbage collection if not referenced
        or retained by other resources during the lease.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def List(self, request, context):
        """List lists all active leases, returning the full list of
        leases and optionally including the referenced resources.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_LeasesServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Create': grpc.unary_unary_rpc_method_handler(
                    servicer.Create,
                    request_deserializer=containerd_dot_services_dot_leases_dot_v1_dot_leases__pb2.CreateRequest.FromString,
                    response_serializer=containerd_dot_services_dot_leases_dot_v1_dot_leases__pb2.CreateResponse.SerializeToString,
            ),
            'Delete': grpc.unary_unary_rpc_method_handler(
                    servicer.Delete,
                    request_deserializer=containerd_dot_services_dot_leases_dot_v1_dot_leases__pb2.DeleteRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'List': grpc.unary_unary_rpc_method_handler(
                    servicer.List,
                    request_deserializer=containerd_dot_services_dot_leases_dot_v1_dot_leases__pb2.ListRequest.FromString,
                    response_serializer=containerd_dot_services_dot_leases_dot_v1_dot_leases__pb2.ListResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'containerd.services.leases.v1.Leases', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Leases(object):
    """Leases service manages resources leases within the metadata store.
    """

    @staticmethod
    def Create(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/containerd.services.leases.v1.Leases/Create',
            containerd_dot_services_dot_leases_dot_v1_dot_leases__pb2.CreateRequest.SerializeToString,
            containerd_dot_services_dot_leases_dot_v1_dot_leases__pb2.CreateResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Delete(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/containerd.services.leases.v1.Leases/Delete',
            containerd_dot_services_dot_leases_dot_v1_dot_leases__pb2.DeleteRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def List(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/containerd.services.leases.v1.Leases/List',
            containerd_dot_services_dot_leases_dot_v1_dot_leases__pb2.ListRequest.SerializeToString,
            containerd_dot_services_dot_leases_dot_v1_dot_leases__pb2.ListResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
