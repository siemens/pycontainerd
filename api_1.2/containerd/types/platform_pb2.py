# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: containerd/types/platform.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from containerd.gogoproto import gogo_pb2 as containerd_dot_gogoproto_dot_gogo__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='containerd/types/platform.proto',
  package='containerd.types',
  syntax='proto3',
  serialized_options=b'Z0github.com/containerd/containerd/api/types;types',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1f\x63ontainerd/types/platform.proto\x12\x10\x63ontainerd.types\x1a\x1f\x63ontainerd/gogoproto/gogo.proto\"E\n\x08Platform\x12\x12\n\x02os\x18\x01 \x01(\tB\x06\xe2\xde\x1f\x02OS\x12\x14\n\x0c\x61rchitecture\x18\x02 \x01(\t\x12\x0f\n\x07variant\x18\x03 \x01(\tB2Z0github.com/containerd/containerd/api/types;typesX\x00\x62\x06proto3'
  ,
  dependencies=[containerd_dot_gogoproto_dot_gogo__pb2.DESCRIPTOR,])




_PLATFORM = _descriptor.Descriptor(
  name='Platform',
  full_name='containerd.types.Platform',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='os', full_name='containerd.types.Platform.os', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342\336\037\002OS', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='architecture', full_name='containerd.types.Platform.architecture', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='variant', full_name='containerd.types.Platform.variant', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=86,
  serialized_end=155,
)

DESCRIPTOR.message_types_by_name['Platform'] = _PLATFORM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Platform = _reflection.GeneratedProtocolMessageType('Platform', (_message.Message,), {
  'DESCRIPTOR' : _PLATFORM,
  '__module__' : 'containerd.types.platform_pb2'
  # @@protoc_insertion_point(class_scope:containerd.types.Platform)
  })
_sym_db.RegisterMessage(Platform)


DESCRIPTOR._options = None
_PLATFORM.fields_by_name['os']._options = None
# @@protoc_insertion_point(module_scope)
