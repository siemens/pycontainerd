# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: containerd/services/ttrpc/events/v1/events.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from containerd.protobuf.plugin import fieldpath_pb2 as containerd_dot_protobuf_dot_plugin_dot_fieldpath__pb2
from containerd.vendor.gogoproto import gogo_pb2 as containerd_dot_vendor_dot_gogoproto_dot_gogo__pb2
from containerd.vendor.google.protobuf import any_pb2 as containerd_dot_vendor_dot_google_dot_protobuf_dot_any__pb2
from containerd.vendor.google.protobuf import empty_pb2 as containerd_dot_vendor_dot_google_dot_protobuf_dot_empty__pb2
from containerd.vendor.google.protobuf import timestamp_pb2 as containerd_dot_vendor_dot_google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='containerd/services/ttrpc/events/v1/events.proto',
  package='containerd.services.events.ttrpc.v1',
  syntax='proto3',
  serialized_options=b'ZDgithub.com/containerd/containerd/api/services/ttrpc/events/v1;events',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n0containerd/services/ttrpc/events/v1/events.proto\x12#containerd.services.events.ttrpc.v1\x1a*containerd/protobuf/plugin/fieldpath.proto\x1a&containerd/vendor/gogoproto/gogo.proto\x1a+containerd/vendor/google/protobuf/any.proto\x1a-containerd/vendor/google/protobuf/empty.proto\x1a\x31\x63ontainerd/vendor/google/protobuf/timestamp.proto\"Q\n\x0e\x46orwardRequest\x12?\n\x08\x65nvelope\x18\x01 \x01(\x0b\x32-.containerd.services.events.ttrpc.v1.Envelope\"\x90\x01\n\x08\x45nvelope\x12\x37\n\ttimestamp\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x08\x90\xdf\x1f\x01\xc8\xde\x1f\x00\x12\x11\n\tnamespace\x18\x02 \x01(\t\x12\r\n\x05topic\x18\x03 \x01(\t\x12#\n\x05\x65vent\x18\x04 \x01(\x0b\x32\x14.google.protobuf.Any:\x04\x80\xb9\x1f\x01\x32`\n\x06\x45vents\x12V\n\x07\x46orward\x12\x33.containerd.services.events.ttrpc.v1.ForwardRequest\x1a\x16.google.protobuf.EmptyBFZDgithub.com/containerd/containerd/api/services/ttrpc/events/v1;eventsX\x00X\x01\x62\x06proto3'
  ,
  dependencies=[containerd_dot_protobuf_dot_plugin_dot_fieldpath__pb2.DESCRIPTOR,containerd_dot_vendor_dot_gogoproto_dot_gogo__pb2.DESCRIPTOR,containerd_dot_vendor_dot_google_dot_protobuf_dot_any__pb2.DESCRIPTOR,containerd_dot_vendor_dot_google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,containerd_dot_vendor_dot_google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,])




_FORWARDREQUEST = _descriptor.Descriptor(
  name='ForwardRequest',
  full_name='containerd.services.events.ttrpc.v1.ForwardRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='envelope', full_name='containerd.services.events.ttrpc.v1.ForwardRequest.envelope', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=316,
  serialized_end=397,
)


_ENVELOPE = _descriptor.Descriptor(
  name='Envelope',
  full_name='containerd.services.events.ttrpc.v1.Envelope',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='containerd.services.events.ttrpc.v1.Envelope.timestamp', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\220\337\037\001\310\336\037\000', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='namespace', full_name='containerd.services.events.ttrpc.v1.Envelope.namespace', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='topic', full_name='containerd.services.events.ttrpc.v1.Envelope.topic', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='event', full_name='containerd.services.events.ttrpc.v1.Envelope.event', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'\200\271\037\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=400,
  serialized_end=544,
)

_FORWARDREQUEST.fields_by_name['envelope'].message_type = _ENVELOPE
_ENVELOPE.fields_by_name['timestamp'].message_type = containerd_dot_vendor_dot_google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_ENVELOPE.fields_by_name['event'].message_type = containerd_dot_vendor_dot_google_dot_protobuf_dot_any__pb2._ANY
DESCRIPTOR.message_types_by_name['ForwardRequest'] = _FORWARDREQUEST
DESCRIPTOR.message_types_by_name['Envelope'] = _ENVELOPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ForwardRequest = _reflection.GeneratedProtocolMessageType('ForwardRequest', (_message.Message,), {
  'DESCRIPTOR' : _FORWARDREQUEST,
  '__module__' : 'containerd.services.ttrpc.events.v1.events_pb2'
  # @@protoc_insertion_point(class_scope:containerd.services.events.ttrpc.v1.ForwardRequest)
  })
_sym_db.RegisterMessage(ForwardRequest)

Envelope = _reflection.GeneratedProtocolMessageType('Envelope', (_message.Message,), {
  'DESCRIPTOR' : _ENVELOPE,
  '__module__' : 'containerd.services.ttrpc.events.v1.events_pb2'
  # @@protoc_insertion_point(class_scope:containerd.services.events.ttrpc.v1.Envelope)
  })
_sym_db.RegisterMessage(Envelope)


DESCRIPTOR._options = None
_ENVELOPE.fields_by_name['timestamp']._options = None
_ENVELOPE._options = None

_EVENTS = _descriptor.ServiceDescriptor(
  name='Events',
  full_name='containerd.services.events.ttrpc.v1.Events',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=546,
  serialized_end=642,
  methods=[
  _descriptor.MethodDescriptor(
    name='Forward',
    full_name='containerd.services.events.ttrpc.v1.Events.Forward',
    index=0,
    containing_service=None,
    input_type=_FORWARDREQUEST,
    output_type=containerd_dot_vendor_dot_google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_EVENTS)

DESCRIPTOR.services_by_name['Events'] = _EVENTS

# @@protoc_insertion_point(module_scope)
