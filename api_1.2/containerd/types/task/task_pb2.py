# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: containerd/types/task/task.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from containerd.vendor.gogoproto import gogo_pb2 as containerd_dot_vendor_dot_gogoproto_dot_gogo__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='containerd/types/task/task.proto',
  package='containerd.v1.types',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n containerd/types/task/task.proto\x12\x13\x63ontainerd.v1.types\x1a&containerd/vendor/gogoproto/gogo.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x19google/protobuf/any.proto\"\xf4\x01\n\x07Process\x12\x14\n\x0c\x63ontainer_id\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\t\x12\x0b\n\x03pid\x18\x03 \x01(\r\x12+\n\x06status\x18\x04 \x01(\x0e\x32\x1b.containerd.v1.types.Status\x12\r\n\x05stdin\x18\x05 \x01(\t\x12\x0e\n\x06stdout\x18\x06 \x01(\t\x12\x0e\n\x06stderr\x18\x07 \x01(\t\x12\x10\n\x08terminal\x18\x08 \x01(\x08\x12\x13\n\x0b\x65xit_status\x18\t \x01(\r\x12\x37\n\texited_at\x18\n \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x08\x90\xdf\x1f\x01\xc8\xde\x1f\x00\">\n\x0bProcessInfo\x12\x0b\n\x03pid\x18\x01 \x01(\r\x12\"\n\x04info\x18\x02 \x01(\x0b\x32\x14.google.protobuf.Any*\xd6\x01\n\x06Status\x12\x1e\n\x07UNKNOWN\x10\x00\x1a\x11\x8a\x9d \rStatusUnknown\x12\x1e\n\x07\x43REATED\x10\x01\x1a\x11\x8a\x9d \rStatusCreated\x12\x1e\n\x07RUNNING\x10\x02\x1a\x11\x8a\x9d \rStatusRunning\x12\x1e\n\x07STOPPED\x10\x03\x1a\x11\x8a\x9d \rStatusStopped\x12\x1c\n\x06PAUSED\x10\x04\x1a\x10\x8a\x9d \x0cStatusPaused\x12\x1e\n\x07PAUSING\x10\x05\x1a\x11\x8a\x9d \rStatusPausing\x1a\x0e\x88\xa3\x1e\x00\xba\xa4\x1e\x06StatusX\x00\x62\x06proto3'
  ,
  dependencies=[containerd_dot_vendor_dot_gogoproto_dot_gogo__pb2.DESCRIPTOR,google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,google_dot_protobuf_dot_any__pb2.DESCRIPTOR,])

_STATUS = _descriptor.EnumDescriptor(
  name='Status',
  full_name='containerd.v1.types.Status',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=0, number=0,
      serialized_options=b'\212\235 \rStatusUnknown',
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CREATED', index=1, number=1,
      serialized_options=b'\212\235 \rStatusCreated',
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='RUNNING', index=2, number=2,
      serialized_options=b'\212\235 \rStatusRunning',
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='STOPPED', index=3, number=3,
      serialized_options=b'\212\235 \rStatusStopped',
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='PAUSED', index=4, number=4,
      serialized_options=b'\212\235 \014StatusPaused',
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='PAUSING', index=5, number=5,
      serialized_options=b'\212\235 \rStatusPausing',
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=b'\210\243\036\000\272\244\036\006Status',
  serialized_start=469,
  serialized_end=683,
)
_sym_db.RegisterEnumDescriptor(_STATUS)

Status = enum_type_wrapper.EnumTypeWrapper(_STATUS)
UNKNOWN = 0
CREATED = 1
RUNNING = 2
STOPPED = 3
PAUSED = 4
PAUSING = 5



_PROCESS = _descriptor.Descriptor(
  name='Process',
  full_name='containerd.v1.types.Process',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='container_id', full_name='containerd.v1.types.Process.container_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='id', full_name='containerd.v1.types.Process.id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='pid', full_name='containerd.v1.types.Process.pid', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='status', full_name='containerd.v1.types.Process.status', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='stdin', full_name='containerd.v1.types.Process.stdin', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='stdout', full_name='containerd.v1.types.Process.stdout', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='stderr', full_name='containerd.v1.types.Process.stderr', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='terminal', full_name='containerd.v1.types.Process.terminal', index=7,
      number=8, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='exit_status', full_name='containerd.v1.types.Process.exit_status', index=8,
      number=9, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='exited_at', full_name='containerd.v1.types.Process.exited_at', index=9,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\220\337\037\001\310\336\037\000', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=158,
  serialized_end=402,
)


_PROCESSINFO = _descriptor.Descriptor(
  name='ProcessInfo',
  full_name='containerd.v1.types.ProcessInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='pid', full_name='containerd.v1.types.ProcessInfo.pid', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='info', full_name='containerd.v1.types.ProcessInfo.info', index=1,
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
  serialized_start=404,
  serialized_end=466,
)

_PROCESS.fields_by_name['status'].enum_type = _STATUS
_PROCESS.fields_by_name['exited_at'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_PROCESSINFO.fields_by_name['info'].message_type = google_dot_protobuf_dot_any__pb2._ANY
DESCRIPTOR.message_types_by_name['Process'] = _PROCESS
DESCRIPTOR.message_types_by_name['ProcessInfo'] = _PROCESSINFO
DESCRIPTOR.enum_types_by_name['Status'] = _STATUS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Process = _reflection.GeneratedProtocolMessageType('Process', (_message.Message,), {
  'DESCRIPTOR' : _PROCESS,
  '__module__' : 'containerd.types.task.task_pb2'
  # @@protoc_insertion_point(class_scope:containerd.v1.types.Process)
  })
_sym_db.RegisterMessage(Process)

ProcessInfo = _reflection.GeneratedProtocolMessageType('ProcessInfo', (_message.Message,), {
  'DESCRIPTOR' : _PROCESSINFO,
  '__module__' : 'containerd.types.task.task_pb2'
  # @@protoc_insertion_point(class_scope:containerd.v1.types.ProcessInfo)
  })
_sym_db.RegisterMessage(ProcessInfo)


_STATUS._options = None
_STATUS.values_by_name["UNKNOWN"]._options = None
_STATUS.values_by_name["CREATED"]._options = None
_STATUS.values_by_name["RUNNING"]._options = None
_STATUS.values_by_name["STOPPED"]._options = None
_STATUS.values_by_name["PAUSED"]._options = None
_STATUS.values_by_name["PAUSING"]._options = None
_PROCESS.fields_by_name['exited_at']._options = None
# @@protoc_insertion_point(module_scope)
