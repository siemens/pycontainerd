# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: containerd/types/mount.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from containerd.vendor.gogoproto import gogo_pb2 as containerd_dot_vendor_dot_gogoproto_dot_gogo__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='containerd/types/mount.proto',
  package='containerd.types',
  syntax='proto3',
  serialized_options=b'Z0github.com/containerd/containerd/api/types;types',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1c\x63ontainerd/types/mount.proto\x12\x10\x63ontainerd.types\x1a&containerd/vendor/gogoproto/gogo.proto\"F\n\x05Mount\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\x0e\n\x06source\x18\x02 \x01(\t\x12\x0e\n\x06target\x18\x03 \x01(\t\x12\x0f\n\x07options\x18\x04 \x03(\tB2Z0github.com/containerd/containerd/api/types;typesX\x00\x62\x06proto3'
  ,
  dependencies=[containerd_dot_vendor_dot_gogoproto_dot_gogo__pb2.DESCRIPTOR,])




_MOUNT = _descriptor.Descriptor(
  name='Mount',
  full_name='containerd.types.Mount',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='containerd.types.Mount.type', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='source', full_name='containerd.types.Mount.source', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='target', full_name='containerd.types.Mount.target', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='options', full_name='containerd.types.Mount.options', index=3,
      number=4, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=90,
  serialized_end=160,
)

DESCRIPTOR.message_types_by_name['Mount'] = _MOUNT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Mount = _reflection.GeneratedProtocolMessageType('Mount', (_message.Message,), {
  'DESCRIPTOR' : _MOUNT,
  '__module__' : 'containerd.types.mount_pb2'
  # @@protoc_insertion_point(class_scope:containerd.types.Mount)
  })
_sym_db.RegisterMessage(Mount)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)