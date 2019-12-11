# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: containerd/events/task.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from containerd.vendor.gogoproto import gogo_pb2 as containerd_dot_vendor_dot_gogoproto_dot_gogo__pb2
from containerd.vendor.google.protobuf import timestamp_pb2 as containerd_dot_vendor_dot_google_dot_protobuf_dot_timestamp__pb2
from containerd.types import mount_pb2 as containerd_dot_types_dot_mount__pb2
from containerd.protobuf.plugin import fieldpath_pb2 as containerd_dot_protobuf_dot_plugin_dot_fieldpath__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='containerd/events/task.proto',
  package='containerd.events',
  syntax='proto3',
  serialized_options=_b('Z2github.com/containerd/containerd/api/events;events\240\364\036\001'),
  serialized_pb=_b('\n\x1c\x63ontainerd/events/task.proto\x12\x11\x63ontainerd.events\x1a&containerd/vendor/gogoproto/gogo.proto\x1a\x31\x63ontainerd/vendor/google/protobuf/timestamp.proto\x1a\x1c\x63ontainerd/types/mount.proto\x1a*containerd/protobuf/plugin/fieldpath.proto\"\xab\x01\n\nTaskCreate\x12\x14\n\x0c\x63ontainer_id\x18\x01 \x01(\t\x12\x0e\n\x06\x62undle\x18\x02 \x01(\t\x12\'\n\x06rootfs\x18\x03 \x03(\x0b\x32\x17.containerd.types.Mount\x12-\n\x02io\x18\x04 \x01(\x0b\x32\x19.containerd.events.TaskIOB\x06\xe2\xde\x1f\x02IO\x12\x12\n\ncheckpoint\x18\x05 \x01(\t\x12\x0b\n\x03pid\x18\x06 \x01(\r\".\n\tTaskStart\x12\x14\n\x0c\x63ontainer_id\x18\x01 \x01(\t\x12\x0b\n\x03pid\x18\x02 \x01(\r\"}\n\nTaskDelete\x12\x14\n\x0c\x63ontainer_id\x18\x01 \x01(\t\x12\x0b\n\x03pid\x18\x02 \x01(\r\x12\x13\n\x0b\x65xit_status\x18\x03 \x01(\r\x12\x37\n\texited_at\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x08\x90\xdf\x1f\x01\xc8\xde\x1f\x00\"I\n\x06TaskIO\x12\r\n\x05stdin\x18\x01 \x01(\t\x12\x0e\n\x06stdout\x18\x02 \x01(\t\x12\x0e\n\x06stderr\x18\x03 \x01(\t\x12\x10\n\x08terminal\x18\x04 \x01(\x08\"\x87\x01\n\x08TaskExit\x12\x14\n\x0c\x63ontainer_id\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\t\x12\x0b\n\x03pid\x18\x03 \x01(\r\x12\x13\n\x0b\x65xit_status\x18\x04 \x01(\r\x12\x37\n\texited_at\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x08\x90\xdf\x1f\x01\xc8\xde\x1f\x00\"\x1f\n\x07TaskOOM\x12\x14\n\x0c\x63ontainer_id\x18\x01 \x01(\t\"6\n\rTaskExecAdded\x12\x14\n\x0c\x63ontainer_id\x18\x01 \x01(\t\x12\x0f\n\x07\x65xec_id\x18\x02 \x01(\t\"E\n\x0fTaskExecStarted\x12\x14\n\x0c\x63ontainer_id\x18\x01 \x01(\t\x12\x0f\n\x07\x65xec_id\x18\x02 \x01(\t\x12\x0b\n\x03pid\x18\x03 \x01(\r\"\"\n\nTaskPaused\x12\x14\n\x0c\x63ontainer_id\x18\x01 \x01(\t\"#\n\x0bTaskResumed\x12\x14\n\x0c\x63ontainer_id\x18\x01 \x01(\t\"<\n\x10TaskCheckpointed\x12\x14\n\x0c\x63ontainer_id\x18\x01 \x01(\t\x12\x12\n\ncheckpoint\x18\x02 \x01(\tB8Z2github.com/containerd/containerd/api/events;events\xa0\xf4\x1e\x01X\x00X\x03\x62\x06proto3')
  ,
  dependencies=[containerd_dot_vendor_dot_gogoproto_dot_gogo__pb2.DESCRIPTOR,containerd_dot_vendor_dot_google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,containerd_dot_types_dot_mount__pb2.DESCRIPTOR,containerd_dot_protobuf_dot_plugin_dot_fieldpath__pb2.DESCRIPTOR,])




_TASKCREATE = _descriptor.Descriptor(
  name='TaskCreate',
  full_name='containerd.events.TaskCreate',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='container_id', full_name='containerd.events.TaskCreate.container_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bundle', full_name='containerd.events.TaskCreate.bundle', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rootfs', full_name='containerd.events.TaskCreate.rootfs', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='io', full_name='containerd.events.TaskCreate.io', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\342\336\037\002IO'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='checkpoint', full_name='containerd.events.TaskCreate.checkpoint', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pid', full_name='containerd.events.TaskCreate.pid', index=5,
      number=6, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=217,
  serialized_end=388,
)


_TASKSTART = _descriptor.Descriptor(
  name='TaskStart',
  full_name='containerd.events.TaskStart',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='container_id', full_name='containerd.events.TaskStart.container_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pid', full_name='containerd.events.TaskStart.pid', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=390,
  serialized_end=436,
)


_TASKDELETE = _descriptor.Descriptor(
  name='TaskDelete',
  full_name='containerd.events.TaskDelete',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='container_id', full_name='containerd.events.TaskDelete.container_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pid', full_name='containerd.events.TaskDelete.pid', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='exit_status', full_name='containerd.events.TaskDelete.exit_status', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='exited_at', full_name='containerd.events.TaskDelete.exited_at', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\220\337\037\001\310\336\037\000'), file=DESCRIPTOR),
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
  serialized_start=438,
  serialized_end=563,
)


_TASKIO = _descriptor.Descriptor(
  name='TaskIO',
  full_name='containerd.events.TaskIO',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='stdin', full_name='containerd.events.TaskIO.stdin', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='stdout', full_name='containerd.events.TaskIO.stdout', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='stderr', full_name='containerd.events.TaskIO.stderr', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='terminal', full_name='containerd.events.TaskIO.terminal', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=565,
  serialized_end=638,
)


_TASKEXIT = _descriptor.Descriptor(
  name='TaskExit',
  full_name='containerd.events.TaskExit',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='container_id', full_name='containerd.events.TaskExit.container_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='id', full_name='containerd.events.TaskExit.id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pid', full_name='containerd.events.TaskExit.pid', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='exit_status', full_name='containerd.events.TaskExit.exit_status', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='exited_at', full_name='containerd.events.TaskExit.exited_at', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\220\337\037\001\310\336\037\000'), file=DESCRIPTOR),
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
  serialized_start=641,
  serialized_end=776,
)


_TASKOOM = _descriptor.Descriptor(
  name='TaskOOM',
  full_name='containerd.events.TaskOOM',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='container_id', full_name='containerd.events.TaskOOM.container_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=778,
  serialized_end=809,
)


_TASKEXECADDED = _descriptor.Descriptor(
  name='TaskExecAdded',
  full_name='containerd.events.TaskExecAdded',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='container_id', full_name='containerd.events.TaskExecAdded.container_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='exec_id', full_name='containerd.events.TaskExecAdded.exec_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=811,
  serialized_end=865,
)


_TASKEXECSTARTED = _descriptor.Descriptor(
  name='TaskExecStarted',
  full_name='containerd.events.TaskExecStarted',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='container_id', full_name='containerd.events.TaskExecStarted.container_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='exec_id', full_name='containerd.events.TaskExecStarted.exec_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pid', full_name='containerd.events.TaskExecStarted.pid', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=867,
  serialized_end=936,
)


_TASKPAUSED = _descriptor.Descriptor(
  name='TaskPaused',
  full_name='containerd.events.TaskPaused',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='container_id', full_name='containerd.events.TaskPaused.container_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=938,
  serialized_end=972,
)


_TASKRESUMED = _descriptor.Descriptor(
  name='TaskResumed',
  full_name='containerd.events.TaskResumed',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='container_id', full_name='containerd.events.TaskResumed.container_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=974,
  serialized_end=1009,
)


_TASKCHECKPOINTED = _descriptor.Descriptor(
  name='TaskCheckpointed',
  full_name='containerd.events.TaskCheckpointed',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='container_id', full_name='containerd.events.TaskCheckpointed.container_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='checkpoint', full_name='containerd.events.TaskCheckpointed.checkpoint', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=1011,
  serialized_end=1071,
)

_TASKCREATE.fields_by_name['rootfs'].message_type = containerd_dot_types_dot_mount__pb2._MOUNT
_TASKCREATE.fields_by_name['io'].message_type = _TASKIO
_TASKDELETE.fields_by_name['exited_at'].message_type = containerd_dot_vendor_dot_google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_TASKEXIT.fields_by_name['exited_at'].message_type = containerd_dot_vendor_dot_google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
DESCRIPTOR.message_types_by_name['TaskCreate'] = _TASKCREATE
DESCRIPTOR.message_types_by_name['TaskStart'] = _TASKSTART
DESCRIPTOR.message_types_by_name['TaskDelete'] = _TASKDELETE
DESCRIPTOR.message_types_by_name['TaskIO'] = _TASKIO
DESCRIPTOR.message_types_by_name['TaskExit'] = _TASKEXIT
DESCRIPTOR.message_types_by_name['TaskOOM'] = _TASKOOM
DESCRIPTOR.message_types_by_name['TaskExecAdded'] = _TASKEXECADDED
DESCRIPTOR.message_types_by_name['TaskExecStarted'] = _TASKEXECSTARTED
DESCRIPTOR.message_types_by_name['TaskPaused'] = _TASKPAUSED
DESCRIPTOR.message_types_by_name['TaskResumed'] = _TASKRESUMED
DESCRIPTOR.message_types_by_name['TaskCheckpointed'] = _TASKCHECKPOINTED
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TaskCreate = _reflection.GeneratedProtocolMessageType('TaskCreate', (_message.Message,), {
  'DESCRIPTOR' : _TASKCREATE,
  '__module__' : 'containerd.events.task_pb2'
  # @@protoc_insertion_point(class_scope:containerd.events.TaskCreate)
  })
_sym_db.RegisterMessage(TaskCreate)

TaskStart = _reflection.GeneratedProtocolMessageType('TaskStart', (_message.Message,), {
  'DESCRIPTOR' : _TASKSTART,
  '__module__' : 'containerd.events.task_pb2'
  # @@protoc_insertion_point(class_scope:containerd.events.TaskStart)
  })
_sym_db.RegisterMessage(TaskStart)

TaskDelete = _reflection.GeneratedProtocolMessageType('TaskDelete', (_message.Message,), {
  'DESCRIPTOR' : _TASKDELETE,
  '__module__' : 'containerd.events.task_pb2'
  # @@protoc_insertion_point(class_scope:containerd.events.TaskDelete)
  })
_sym_db.RegisterMessage(TaskDelete)

TaskIO = _reflection.GeneratedProtocolMessageType('TaskIO', (_message.Message,), {
  'DESCRIPTOR' : _TASKIO,
  '__module__' : 'containerd.events.task_pb2'
  # @@protoc_insertion_point(class_scope:containerd.events.TaskIO)
  })
_sym_db.RegisterMessage(TaskIO)

TaskExit = _reflection.GeneratedProtocolMessageType('TaskExit', (_message.Message,), {
  'DESCRIPTOR' : _TASKEXIT,
  '__module__' : 'containerd.events.task_pb2'
  # @@protoc_insertion_point(class_scope:containerd.events.TaskExit)
  })
_sym_db.RegisterMessage(TaskExit)

TaskOOM = _reflection.GeneratedProtocolMessageType('TaskOOM', (_message.Message,), {
  'DESCRIPTOR' : _TASKOOM,
  '__module__' : 'containerd.events.task_pb2'
  # @@protoc_insertion_point(class_scope:containerd.events.TaskOOM)
  })
_sym_db.RegisterMessage(TaskOOM)

TaskExecAdded = _reflection.GeneratedProtocolMessageType('TaskExecAdded', (_message.Message,), {
  'DESCRIPTOR' : _TASKEXECADDED,
  '__module__' : 'containerd.events.task_pb2'
  # @@protoc_insertion_point(class_scope:containerd.events.TaskExecAdded)
  })
_sym_db.RegisterMessage(TaskExecAdded)

TaskExecStarted = _reflection.GeneratedProtocolMessageType('TaskExecStarted', (_message.Message,), {
  'DESCRIPTOR' : _TASKEXECSTARTED,
  '__module__' : 'containerd.events.task_pb2'
  # @@protoc_insertion_point(class_scope:containerd.events.TaskExecStarted)
  })
_sym_db.RegisterMessage(TaskExecStarted)

TaskPaused = _reflection.GeneratedProtocolMessageType('TaskPaused', (_message.Message,), {
  'DESCRIPTOR' : _TASKPAUSED,
  '__module__' : 'containerd.events.task_pb2'
  # @@protoc_insertion_point(class_scope:containerd.events.TaskPaused)
  })
_sym_db.RegisterMessage(TaskPaused)

TaskResumed = _reflection.GeneratedProtocolMessageType('TaskResumed', (_message.Message,), {
  'DESCRIPTOR' : _TASKRESUMED,
  '__module__' : 'containerd.events.task_pb2'
  # @@protoc_insertion_point(class_scope:containerd.events.TaskResumed)
  })
_sym_db.RegisterMessage(TaskResumed)

TaskCheckpointed = _reflection.GeneratedProtocolMessageType('TaskCheckpointed', (_message.Message,), {
  'DESCRIPTOR' : _TASKCHECKPOINTED,
  '__module__' : 'containerd.events.task_pb2'
  # @@protoc_insertion_point(class_scope:containerd.events.TaskCheckpointed)
  })
_sym_db.RegisterMessage(TaskCheckpointed)


DESCRIPTOR._options = None
_TASKCREATE.fields_by_name['io']._options = None
_TASKDELETE.fields_by_name['exited_at']._options = None
_TASKEXIT.fields_by_name['exited_at']._options = None
# @@protoc_insertion_point(module_scope)
