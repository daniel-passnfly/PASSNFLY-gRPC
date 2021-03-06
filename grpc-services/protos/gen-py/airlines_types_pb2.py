# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: airlines_types.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='airlines_types.proto',
  package='airlines',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n\x14\x61irlines_types.proto\x12\x08\x61irlines\"\x0e\n\x0cNoParameters\"3\n\x07\x41irline\x12\x0c\n\x04icao\x18\x01 \x01(\t\x12\x0c\n\x04iata\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\"/\n\x11GetAirlineRequest\x12\x0c\n\x04icao\x18\x01 \x01(\t\x12\x0c\n\x04iata\x18\x02 \x01(\t\"6\n\x10GetAirlineResult\x12\"\n\x07\x61irline\x18\x01 \x01(\x0b\x32\x11.airlines.Airline\"7\n\x11GetAirlinesResult\x12\"\n\x07\x61irline\x18\x01 \x03(\x0b\x32\x11.airlines.Airlineb\x06proto3'
)




_NOPARAMETERS = _descriptor.Descriptor(
  name='NoParameters',
  full_name='airlines.NoParameters',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=34,
  serialized_end=48,
)


_AIRLINE = _descriptor.Descriptor(
  name='Airline',
  full_name='airlines.Airline',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='icao', full_name='airlines.Airline.icao', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='iata', full_name='airlines.Airline.iata', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='airlines.Airline.name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=50,
  serialized_end=101,
)


_GETAIRLINEREQUEST = _descriptor.Descriptor(
  name='GetAirlineRequest',
  full_name='airlines.GetAirlineRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='icao', full_name='airlines.GetAirlineRequest.icao', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='iata', full_name='airlines.GetAirlineRequest.iata', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=103,
  serialized_end=150,
)


_GETAIRLINERESULT = _descriptor.Descriptor(
  name='GetAirlineResult',
  full_name='airlines.GetAirlineResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='airline', full_name='airlines.GetAirlineResult.airline', index=0,
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
  serialized_start=152,
  serialized_end=206,
)


_GETAIRLINESRESULT = _descriptor.Descriptor(
  name='GetAirlinesResult',
  full_name='airlines.GetAirlinesResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='airline', full_name='airlines.GetAirlinesResult.airline', index=0,
      number=1, type=11, cpp_type=10, label=3,
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
  serialized_start=208,
  serialized_end=263,
)

_GETAIRLINERESULT.fields_by_name['airline'].message_type = _AIRLINE
_GETAIRLINESRESULT.fields_by_name['airline'].message_type = _AIRLINE
DESCRIPTOR.message_types_by_name['NoParameters'] = _NOPARAMETERS
DESCRIPTOR.message_types_by_name['Airline'] = _AIRLINE
DESCRIPTOR.message_types_by_name['GetAirlineRequest'] = _GETAIRLINEREQUEST
DESCRIPTOR.message_types_by_name['GetAirlineResult'] = _GETAIRLINERESULT
DESCRIPTOR.message_types_by_name['GetAirlinesResult'] = _GETAIRLINESRESULT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

NoParameters = _reflection.GeneratedProtocolMessageType('NoParameters', (_message.Message,), {
  'DESCRIPTOR' : _NOPARAMETERS,
  '__module__' : 'airlines_types_pb2'
  # @@protoc_insertion_point(class_scope:airlines.NoParameters)
  })
_sym_db.RegisterMessage(NoParameters)

Airline = _reflection.GeneratedProtocolMessageType('Airline', (_message.Message,), {
  'DESCRIPTOR' : _AIRLINE,
  '__module__' : 'airlines_types_pb2'
  # @@protoc_insertion_point(class_scope:airlines.Airline)
  })
_sym_db.RegisterMessage(Airline)

GetAirlineRequest = _reflection.GeneratedProtocolMessageType('GetAirlineRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETAIRLINEREQUEST,
  '__module__' : 'airlines_types_pb2'
  # @@protoc_insertion_point(class_scope:airlines.GetAirlineRequest)
  })
_sym_db.RegisterMessage(GetAirlineRequest)

GetAirlineResult = _reflection.GeneratedProtocolMessageType('GetAirlineResult', (_message.Message,), {
  'DESCRIPTOR' : _GETAIRLINERESULT,
  '__module__' : 'airlines_types_pb2'
  # @@protoc_insertion_point(class_scope:airlines.GetAirlineResult)
  })
_sym_db.RegisterMessage(GetAirlineResult)

GetAirlinesResult = _reflection.GeneratedProtocolMessageType('GetAirlinesResult', (_message.Message,), {
  'DESCRIPTOR' : _GETAIRLINESRESULT,
  '__module__' : 'airlines_types_pb2'
  # @@protoc_insertion_point(class_scope:airlines.GetAirlinesResult)
  })
_sym_db.RegisterMessage(GetAirlinesResult)


# @@protoc_insertion_point(module_scope)
