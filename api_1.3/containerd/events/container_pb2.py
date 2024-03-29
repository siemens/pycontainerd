# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: containerd/events/container.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from containerd.vendor.gogoproto import gogo_pb2 as containerd_dot_vendor_dot_gogoproto_dot_gogo__pb2
from containerd.protobuf.plugin import fieldpath_pb2 as containerd_dot_protobuf_dot_plugin_dot_fieldpath__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='containerd/events/container.proto',
  package='containerd.events',
  syntax='proto3',
  serialized_options=b'Z2github.com/containerd/containerd/api/events;events\240\364\036\001',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n!containerd/events/container.proto\x12\x11\x63ontainerd.events\x1a\x19google/protobuf/any.proto\x1a&containerd/vendor/gogoproto/gogo.proto\x1a*containerd/protobuf/plugin/fieldpath.proto\"\xa9\x01\n\x0f\x43ontainerCreate\x12\n\n\x02id\x18\x01 \x01(\t\x12\r\n\x05image\x18\x02 \x01(\t\x12;\n\x07runtime\x18\x03 \x01(\x0b\x32*.containerd.events.ContainerCreate.Runtime\x1a>\n\x07Runtime\x12\x0c\n\x04name\x18\x01 \x01(\t\x12%\n\x07options\x18\x02 \x01(\x0b\x32\x14.google.protobuf.Any\"\xb1\x01\n\x0f\x43ontainerUpdate\x12\n\n\x02id\x18\x01 \x01(\t\x12\r\n\x05image\x18\x02 \x01(\t\x12>\n\x06labels\x18\x03 \x03(\x0b\x32..containerd.events.ContainerUpdate.LabelsEntry\x12\x14\n\x0csnapshot_key\x18\x04 \x01(\t\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\x1d\n\x0f\x43ontainerDelete\x12\n\n\x02id\x18\x01 \x01(\tB8Z2github.com/containerd/containerd/api/events;events\xa0\xf4\x1e\x01X\x01X\x02\x62\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_any__pb2.DESCRIPTOR,containerd_dot_vendor_dot_gogoproto_dot_gogo__pb2.DESCRIPTOR,containerd_dot_protobuf_dot_plugin_dot_fieldpath__pb2.DESCRIPTOR,])




_CONTAINERCREATE_RUNTIME = _descriptor.Descriptor(
  name='Runtime',
  full_name='containerd.events.ContainerCreate.Runtime',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='containerd.events.ContainerCreate.Runtime.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='options', full_name='containerd.events.ContainerCreate.Runtime.options', index=1,
      number=2, type=11, cpp_type=10, label=1,
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
  serialized_start=275,
  serialized_end=337,
)

_CONTAINERCREATE = _descriptor.Descriptor(
  name='ContainerCreate',
  full_name='containerd.events.ContainerCreate',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='containerd.events.ContainerCreate.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='image', full_name='containerd.events.ContainerCreate.image', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='runtime', full_name='containerd.events.ContainerCreate.runtime', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_CONTAINERCREATE_RUNTIME, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=168,
  serialized_end=337,
)


_CONTAINERUPDATE_LABELSENTRY = _descriptor.Descriptor(
  name='LabelsEntry',
  full_name='containerd.events.ContainerUpdate.LabelsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='containerd.events.ContainerUpdate.LabelsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='containerd.events.ContainerUpdate.LabelsEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=472,
  serialized_end=517,
)

_CONTAINERUPDATE = _descriptor.Descriptor(
  name='ContainerUpdate',
  full_name='containerd.events.ContainerUpdate',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='containerd.events.ContainerUpdate.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='image', full_name='containerd.events.ContainerUpdate.image', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='labels', full_name='containerd.events.ContainerUpdate.labels', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='snapshot_key', full_name='containerd.events.ContainerUpdate.snapshot_key', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_CONTAINERUPDATE_LABELSENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=340,
  serialized_end=517,
)


_CONTAINERDELETE = _descriptor.Descriptor(
  name='ContainerDelete',
  full_name='containerd.events.ContainerDelete',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='containerd.events.ContainerDelete.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=519,
  serialized_end=548,
)

_CONTAINERCREATE_RUNTIME.fields_by_name['options'].message_type = google_dot_protobuf_dot_any__pb2._ANY
_CONTAINERCREATE_RUNTIME.containing_type = _CONTAINERCREATE
_CONTAINERCREATE.fields_by_name['runtime'].message_type = _CONTAINERCREATE_RUNTIME
_CONTAINERUPDATE_LABELSENTRY.containing_type = _CONTAINERUPDATE
_CONTAINERUPDATE.fields_by_name['labels'].message_type = _CONTAINERUPDATE_LABELSENTRY
DESCRIPTOR.message_types_by_name['ContainerCreate'] = _CONTAINERCREATE
DESCRIPTOR.message_types_by_name['ContainerUpdate'] = _CONTAINERUPDATE
DESCRIPTOR.message_types_by_name['ContainerDelete'] = _CONTAINERDELETE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ContainerCreate = _reflection.GeneratedProtocolMessageType('ContainerCreate', (_message.Message,), {

  'Runtime' : _reflection.GeneratedProtocolMessageType('Runtime', (_message.Message,), {
    'DESCRIPTOR' : _CONTAINERCREATE_RUNTIME,
    '__module__' : 'containerd.events.container_pb2'
    # @@protoc_insertion_point(class_scope:containerd.events.ContainerCreate.Runtime)
    })
  ,
  'DESCRIPTOR' : _CONTAINERCREATE,
  '__module__' : 'containerd.events.container_pb2'
  # @@protoc_insertion_point(class_scope:containerd.events.ContainerCreate)
  })
_sym_db.RegisterMessage(ContainerCreate)
_sym_db.RegisterMessage(ContainerCreate.Runtime)

ContainerUpdate = _reflection.GeneratedProtocolMessageType('ContainerUpdate', (_message.Message,), {

  'LabelsEntry' : _reflection.GeneratedProtocolMessageType('LabelsEntry', (_message.Message,), {
    'DESCRIPTOR' : _CONTAINERUPDATE_LABELSENTRY,
    '__module__' : 'containerd.events.container_pb2'
    # @@protoc_insertion_point(class_scope:containerd.events.ContainerUpdate.LabelsEntry)
    })
  ,
  'DESCRIPTOR' : _CONTAINERUPDATE,
  '__module__' : 'containerd.events.container_pb2'
  # @@protoc_insertion_point(class_scope:containerd.events.ContainerUpdate)
  })
_sym_db.RegisterMessage(ContainerUpdate)
_sym_db.RegisterMessage(ContainerUpdate.LabelsEntry)

ContainerDelete = _reflection.GeneratedProtocolMessageType('ContainerDelete', (_message.Message,), {
  'DESCRIPTOR' : _CONTAINERDELETE,
  '__module__' : 'containerd.events.container_pb2'
  # @@protoc_insertion_point(class_scope:containerd.events.ContainerDelete)
  })
_sym_db.RegisterMessage(ContainerDelete)


DESCRIPTOR._options = None
_CONTAINERUPDATE_LABELSENTRY._options = None
# @@protoc_insertion_point(module_scope)
