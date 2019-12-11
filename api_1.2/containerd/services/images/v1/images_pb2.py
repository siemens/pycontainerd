# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: containerd/services/images/v1/images.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from containerd.vendor.gogoproto import gogo_pb2 as containerd_dot_vendor_dot_gogoproto_dot_gogo__pb2
from containerd.vendor.google.protobuf import empty_pb2 as containerd_dot_vendor_dot_google_dot_protobuf_dot_empty__pb2
from containerd.vendor.google.protobuf import field_mask_pb2 as containerd_dot_vendor_dot_google_dot_protobuf_dot_field__mask__pb2
from containerd.vendor.google.protobuf import timestamp_pb2 as containerd_dot_vendor_dot_google_dot_protobuf_dot_timestamp__pb2
from containerd.types import descriptor_pb2 as containerd_dot_types_dot_descriptor__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='containerd/services/images/v1/images.proto',
  package='containerd.services.images.v1',
  syntax='proto3',
  serialized_options=_b('Z>github.com/containerd/containerd/api/services/images/v1;images'),
  serialized_pb=_b('\n*containerd/services/images/v1/images.proto\x12\x1d\x63ontainerd.services.images.v1\x1a&containerd/vendor/gogoproto/gogo.proto\x1a-containerd/vendor/google/protobuf/empty.proto\x1a\x32\x63ontainerd/vendor/google/protobuf/field_mask.proto\x1a\x31\x63ontainerd/vendor/google/protobuf/timestamp.proto\x1a!containerd/types/descriptor.proto\"\xae\x02\n\x05Image\x12\x0c\n\x04name\x18\x01 \x01(\t\x12@\n\x06labels\x18\x02 \x03(\x0b\x32\x30.containerd.services.images.v1.Image.LabelsEntry\x12\x32\n\x06target\x18\x03 \x01(\x0b\x32\x1c.containerd.types.DescriptorB\x04\xc8\xde\x1f\x00\x12\x38\n\ncreated_at\x18\x07 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x08\x90\xdf\x1f\x01\xc8\xde\x1f\x00\x12\x38\n\nupdated_at\x18\x08 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x08\x90\xdf\x1f\x01\xc8\xde\x1f\x00\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\x1f\n\x0fGetImageRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"G\n\x10GetImageResponse\x12\x33\n\x05image\x18\x01 \x01(\x0b\x32$.containerd.services.images.v1.Image\"O\n\x12\x43reateImageRequest\x12\x39\n\x05image\x18\x01 \x01(\x0b\x32$.containerd.services.images.v1.ImageB\x04\xc8\xde\x1f\x00\"P\n\x13\x43reateImageResponse\x12\x39\n\x05image\x18\x01 \x01(\x0b\x32$.containerd.services.images.v1.ImageB\x04\xc8\xde\x1f\x00\"\x80\x01\n\x12UpdateImageRequest\x12\x39\n\x05image\x18\x01 \x01(\x0b\x32$.containerd.services.images.v1.ImageB\x04\xc8\xde\x1f\x00\x12/\n\x0bupdate_mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\"P\n\x13UpdateImageResponse\x12\x39\n\x05image\x18\x01 \x01(\x0b\x32$.containerd.services.images.v1.ImageB\x04\xc8\xde\x1f\x00\"$\n\x11ListImagesRequest\x12\x0f\n\x07\x66ilters\x18\x01 \x03(\t\"P\n\x12ListImagesResponse\x12:\n\x06images\x18\x01 \x03(\x0b\x32$.containerd.services.images.v1.ImageB\x04\xc8\xde\x1f\x00\"0\n\x12\x44\x65leteImageRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04sync\x18\x02 \x01(\x08\x32\x94\x04\n\x06Images\x12\x66\n\x03Get\x12..containerd.services.images.v1.GetImageRequest\x1a/.containerd.services.images.v1.GetImageResponse\x12k\n\x04List\x12\x30.containerd.services.images.v1.ListImagesRequest\x1a\x31.containerd.services.images.v1.ListImagesResponse\x12o\n\x06\x43reate\x12\x31.containerd.services.images.v1.CreateImageRequest\x1a\x32.containerd.services.images.v1.CreateImageResponse\x12o\n\x06Update\x12\x31.containerd.services.images.v1.UpdateImageRequest\x1a\x32.containerd.services.images.v1.UpdateImageResponse\x12S\n\x06\x44\x65lete\x12\x31.containerd.services.images.v1.DeleteImageRequest\x1a\x16.google.protobuf.EmptyB@Z>github.com/containerd/containerd/api/services/images/v1;imagesX\x00\x62\x06proto3')
  ,
  dependencies=[containerd_dot_vendor_dot_gogoproto_dot_gogo__pb2.DESCRIPTOR,containerd_dot_vendor_dot_google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,containerd_dot_vendor_dot_google_dot_protobuf_dot_field__mask__pb2.DESCRIPTOR,containerd_dot_vendor_dot_google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,containerd_dot_types_dot_descriptor__pb2.DESCRIPTOR,])




_IMAGE_LABELSENTRY = _descriptor.Descriptor(
  name='LabelsEntry',
  full_name='containerd.services.images.v1.Image.LabelsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='containerd.services.images.v1.Image.LabelsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='containerd.services.images.v1.Image.LabelsEntry.value', index=1,
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
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=560,
  serialized_end=605,
)

_IMAGE = _descriptor.Descriptor(
  name='Image',
  full_name='containerd.services.images.v1.Image',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='containerd.services.images.v1.Image.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='labels', full_name='containerd.services.images.v1.Image.labels', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='target', full_name='containerd.services.images.v1.Image.target', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\310\336\037\000'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='created_at', full_name='containerd.services.images.v1.Image.created_at', index=3,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\220\337\037\001\310\336\037\000'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='updated_at', full_name='containerd.services.images.v1.Image.updated_at', index=4,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\220\337\037\001\310\336\037\000'), file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_IMAGE_LABELSENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=303,
  serialized_end=605,
)


_GETIMAGEREQUEST = _descriptor.Descriptor(
  name='GetImageRequest',
  full_name='containerd.services.images.v1.GetImageRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='containerd.services.images.v1.GetImageRequest.name', index=0,
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
  serialized_start=607,
  serialized_end=638,
)


_GETIMAGERESPONSE = _descriptor.Descriptor(
  name='GetImageResponse',
  full_name='containerd.services.images.v1.GetImageResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='image', full_name='containerd.services.images.v1.GetImageResponse.image', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=640,
  serialized_end=711,
)


_CREATEIMAGEREQUEST = _descriptor.Descriptor(
  name='CreateImageRequest',
  full_name='containerd.services.images.v1.CreateImageRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='image', full_name='containerd.services.images.v1.CreateImageRequest.image', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\310\336\037\000'), file=DESCRIPTOR),
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
  serialized_start=713,
  serialized_end=792,
)


_CREATEIMAGERESPONSE = _descriptor.Descriptor(
  name='CreateImageResponse',
  full_name='containerd.services.images.v1.CreateImageResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='image', full_name='containerd.services.images.v1.CreateImageResponse.image', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\310\336\037\000'), file=DESCRIPTOR),
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
  serialized_start=794,
  serialized_end=874,
)


_UPDATEIMAGEREQUEST = _descriptor.Descriptor(
  name='UpdateImageRequest',
  full_name='containerd.services.images.v1.UpdateImageRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='image', full_name='containerd.services.images.v1.UpdateImageRequest.image', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\310\336\037\000'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='update_mask', full_name='containerd.services.images.v1.UpdateImageRequest.update_mask', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=877,
  serialized_end=1005,
)


_UPDATEIMAGERESPONSE = _descriptor.Descriptor(
  name='UpdateImageResponse',
  full_name='containerd.services.images.v1.UpdateImageResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='image', full_name='containerd.services.images.v1.UpdateImageResponse.image', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\310\336\037\000'), file=DESCRIPTOR),
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
  serialized_start=1007,
  serialized_end=1087,
)


_LISTIMAGESREQUEST = _descriptor.Descriptor(
  name='ListImagesRequest',
  full_name='containerd.services.images.v1.ListImagesRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='filters', full_name='containerd.services.images.v1.ListImagesRequest.filters', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=1089,
  serialized_end=1125,
)


_LISTIMAGESRESPONSE = _descriptor.Descriptor(
  name='ListImagesResponse',
  full_name='containerd.services.images.v1.ListImagesResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='images', full_name='containerd.services.images.v1.ListImagesResponse.images', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\310\336\037\000'), file=DESCRIPTOR),
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
  serialized_start=1127,
  serialized_end=1207,
)


_DELETEIMAGEREQUEST = _descriptor.Descriptor(
  name='DeleteImageRequest',
  full_name='containerd.services.images.v1.DeleteImageRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='containerd.services.images.v1.DeleteImageRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sync', full_name='containerd.services.images.v1.DeleteImageRequest.sync', index=1,
      number=2, type=8, cpp_type=7, label=1,
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
  serialized_start=1209,
  serialized_end=1257,
)

_IMAGE_LABELSENTRY.containing_type = _IMAGE
_IMAGE.fields_by_name['labels'].message_type = _IMAGE_LABELSENTRY
_IMAGE.fields_by_name['target'].message_type = containerd_dot_types_dot_descriptor__pb2._DESCRIPTOR
_IMAGE.fields_by_name['created_at'].message_type = containerd_dot_vendor_dot_google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_IMAGE.fields_by_name['updated_at'].message_type = containerd_dot_vendor_dot_google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_GETIMAGERESPONSE.fields_by_name['image'].message_type = _IMAGE
_CREATEIMAGEREQUEST.fields_by_name['image'].message_type = _IMAGE
_CREATEIMAGERESPONSE.fields_by_name['image'].message_type = _IMAGE
_UPDATEIMAGEREQUEST.fields_by_name['image'].message_type = _IMAGE
_UPDATEIMAGEREQUEST.fields_by_name['update_mask'].message_type = containerd_dot_vendor_dot_google_dot_protobuf_dot_field__mask__pb2._FIELDMASK
_UPDATEIMAGERESPONSE.fields_by_name['image'].message_type = _IMAGE
_LISTIMAGESRESPONSE.fields_by_name['images'].message_type = _IMAGE
DESCRIPTOR.message_types_by_name['Image'] = _IMAGE
DESCRIPTOR.message_types_by_name['GetImageRequest'] = _GETIMAGEREQUEST
DESCRIPTOR.message_types_by_name['GetImageResponse'] = _GETIMAGERESPONSE
DESCRIPTOR.message_types_by_name['CreateImageRequest'] = _CREATEIMAGEREQUEST
DESCRIPTOR.message_types_by_name['CreateImageResponse'] = _CREATEIMAGERESPONSE
DESCRIPTOR.message_types_by_name['UpdateImageRequest'] = _UPDATEIMAGEREQUEST
DESCRIPTOR.message_types_by_name['UpdateImageResponse'] = _UPDATEIMAGERESPONSE
DESCRIPTOR.message_types_by_name['ListImagesRequest'] = _LISTIMAGESREQUEST
DESCRIPTOR.message_types_by_name['ListImagesResponse'] = _LISTIMAGESRESPONSE
DESCRIPTOR.message_types_by_name['DeleteImageRequest'] = _DELETEIMAGEREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Image = _reflection.GeneratedProtocolMessageType('Image', (_message.Message,), {

  'LabelsEntry' : _reflection.GeneratedProtocolMessageType('LabelsEntry', (_message.Message,), {
    'DESCRIPTOR' : _IMAGE_LABELSENTRY,
    '__module__' : 'containerd.services.images.v1.images_pb2'
    # @@protoc_insertion_point(class_scope:containerd.services.images.v1.Image.LabelsEntry)
    })
  ,
  'DESCRIPTOR' : _IMAGE,
  '__module__' : 'containerd.services.images.v1.images_pb2'
  # @@protoc_insertion_point(class_scope:containerd.services.images.v1.Image)
  })
_sym_db.RegisterMessage(Image)
_sym_db.RegisterMessage(Image.LabelsEntry)

GetImageRequest = _reflection.GeneratedProtocolMessageType('GetImageRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETIMAGEREQUEST,
  '__module__' : 'containerd.services.images.v1.images_pb2'
  # @@protoc_insertion_point(class_scope:containerd.services.images.v1.GetImageRequest)
  })
_sym_db.RegisterMessage(GetImageRequest)

GetImageResponse = _reflection.GeneratedProtocolMessageType('GetImageResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETIMAGERESPONSE,
  '__module__' : 'containerd.services.images.v1.images_pb2'
  # @@protoc_insertion_point(class_scope:containerd.services.images.v1.GetImageResponse)
  })
_sym_db.RegisterMessage(GetImageResponse)

CreateImageRequest = _reflection.GeneratedProtocolMessageType('CreateImageRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATEIMAGEREQUEST,
  '__module__' : 'containerd.services.images.v1.images_pb2'
  # @@protoc_insertion_point(class_scope:containerd.services.images.v1.CreateImageRequest)
  })
_sym_db.RegisterMessage(CreateImageRequest)

CreateImageResponse = _reflection.GeneratedProtocolMessageType('CreateImageResponse', (_message.Message,), {
  'DESCRIPTOR' : _CREATEIMAGERESPONSE,
  '__module__' : 'containerd.services.images.v1.images_pb2'
  # @@protoc_insertion_point(class_scope:containerd.services.images.v1.CreateImageResponse)
  })
_sym_db.RegisterMessage(CreateImageResponse)

UpdateImageRequest = _reflection.GeneratedProtocolMessageType('UpdateImageRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEIMAGEREQUEST,
  '__module__' : 'containerd.services.images.v1.images_pb2'
  # @@protoc_insertion_point(class_scope:containerd.services.images.v1.UpdateImageRequest)
  })
_sym_db.RegisterMessage(UpdateImageRequest)

UpdateImageResponse = _reflection.GeneratedProtocolMessageType('UpdateImageResponse', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEIMAGERESPONSE,
  '__module__' : 'containerd.services.images.v1.images_pb2'
  # @@protoc_insertion_point(class_scope:containerd.services.images.v1.UpdateImageResponse)
  })
_sym_db.RegisterMessage(UpdateImageResponse)

ListImagesRequest = _reflection.GeneratedProtocolMessageType('ListImagesRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTIMAGESREQUEST,
  '__module__' : 'containerd.services.images.v1.images_pb2'
  # @@protoc_insertion_point(class_scope:containerd.services.images.v1.ListImagesRequest)
  })
_sym_db.RegisterMessage(ListImagesRequest)

ListImagesResponse = _reflection.GeneratedProtocolMessageType('ListImagesResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTIMAGESRESPONSE,
  '__module__' : 'containerd.services.images.v1.images_pb2'
  # @@protoc_insertion_point(class_scope:containerd.services.images.v1.ListImagesResponse)
  })
_sym_db.RegisterMessage(ListImagesResponse)

DeleteImageRequest = _reflection.GeneratedProtocolMessageType('DeleteImageRequest', (_message.Message,), {
  'DESCRIPTOR' : _DELETEIMAGEREQUEST,
  '__module__' : 'containerd.services.images.v1.images_pb2'
  # @@protoc_insertion_point(class_scope:containerd.services.images.v1.DeleteImageRequest)
  })
_sym_db.RegisterMessage(DeleteImageRequest)


DESCRIPTOR._options = None
_IMAGE_LABELSENTRY._options = None
_IMAGE.fields_by_name['target']._options = None
_IMAGE.fields_by_name['created_at']._options = None
_IMAGE.fields_by_name['updated_at']._options = None
_CREATEIMAGEREQUEST.fields_by_name['image']._options = None
_CREATEIMAGERESPONSE.fields_by_name['image']._options = None
_UPDATEIMAGEREQUEST.fields_by_name['image']._options = None
_UPDATEIMAGERESPONSE.fields_by_name['image']._options = None
_LISTIMAGESRESPONSE.fields_by_name['images']._options = None

_IMAGES = _descriptor.ServiceDescriptor(
  name='Images',
  full_name='containerd.services.images.v1.Images',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=1260,
  serialized_end=1792,
  methods=[
  _descriptor.MethodDescriptor(
    name='Get',
    full_name='containerd.services.images.v1.Images.Get',
    index=0,
    containing_service=None,
    input_type=_GETIMAGEREQUEST,
    output_type=_GETIMAGERESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='List',
    full_name='containerd.services.images.v1.Images.List',
    index=1,
    containing_service=None,
    input_type=_LISTIMAGESREQUEST,
    output_type=_LISTIMAGESRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Create',
    full_name='containerd.services.images.v1.Images.Create',
    index=2,
    containing_service=None,
    input_type=_CREATEIMAGEREQUEST,
    output_type=_CREATEIMAGERESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Update',
    full_name='containerd.services.images.v1.Images.Update',
    index=3,
    containing_service=None,
    input_type=_UPDATEIMAGEREQUEST,
    output_type=_UPDATEIMAGERESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Delete',
    full_name='containerd.services.images.v1.Images.Delete',
    index=4,
    containing_service=None,
    input_type=_DELETEIMAGEREQUEST,
    output_type=containerd_dot_vendor_dot_google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_IMAGES)

DESCRIPTOR.services_by_name['Images'] = _IMAGES

# @@protoc_insertion_point(module_scope)
