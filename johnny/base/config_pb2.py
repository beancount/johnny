# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: config.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='config.proto',
  package='johnny',
  syntax='proto2',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0c\x63onfig.proto\x12\x06johnny\"\xa9\x01\n\x06\x43onfig\x12\x1d\n\x05input\x18\x01 \x01(\x0b\x32\x0e.johnny.Inputs\x12\x1f\n\x06output\x18\x02 \x01(\x0b\x32\x0f.johnny.Outputs\x12@\n\x1c\x66utures_option_month_mapping\x18\x03 \x01(\x0b\x32\x1a.johnny.FutOptMonthMapping\x12\x1d\n\x06\x63hains\x18\x04 \x03(\x0b\x32\r.johnny.Chain\"+\n\x06Inputs\x12!\n\x08\x61\x63\x63ounts\x18\x01 \x03(\x0b\x32\x0f.johnny.Account\"$\n\x07Outputs\x12\x19\n\x11imported_filename\x18\x01 \x01(\t\"\xa9\x01\n\x12\x46utOptMonthMapping\x12/\n\x06months\x18\x01 \x03(\x0b\x32\x1f.johnny.FutOptMonthMapping.Item\x1a\x62\n\x04Item\x12\x16\n\x0eoption_product\x18\x01 \x01(\t\x12\x14\n\x0coption_month\x18\x02 \x01(\t\x12\x16\n\x0e\x66uture_product\x18\x03 \x01(\t\x12\x14\n\x0c\x66uture_month\x18\x04 \x01(\t\"\xa2\x01\n\x07\x41\x63\x63ount\x12\x10\n\x08nickname\x18\x01 \x01(\t\x12(\n\x07logtype\x18\x02 \x01(\x0e\x32\x17.johnny.Account.LogType\x12\x0e\n\x06module\x18\x03 \x01(\t\x12\x0e\n\x06source\x18\x04 \x01(\t\x12\x0f\n\x07initial\x18\x05 \x01(\t\"*\n\x07LogType\x12\x10\n\x0cTRANSACTIONS\x10\x01\x12\r\n\tPOSITIONS\x10\x02\"\xa6\x01\n\x05\x43hain\x12\x10\n\x08\x63hain_id\x18\x01 \x01(\t\x12#\n\x06status\x18\x02 \x01(\x0e\x32\x13.johnny.ChainStatus\x12\r\n\x05group\x18\x03 \x01(\t\x12\x0f\n\x07\x63omment\x18\x06 \x01(\t\x12\x10\n\x08strategy\x18\x04 \x01(\t\x12\x15\n\rauto_strategy\x18\x05 \x01(\t\x12\x0b\n\x03ids\x18\x07 \x03(\t\x12\x10\n\x08\x61uto_ids\x18\x08 \x03(\t\":\n\x05\x41sset\x12\x12\n\ninstrument\x18\x01 \x01(\t\x12\r\n\x05\x63lass\x18\x02 \x01(\t\x12\x0e\n\x06\x66\x61\x63tor\x18\x03 \x01(\t*<\n\x0b\x43hainStatus\x12\n\n\x06\x41\x43TIVE\x10\x00\x12\n\n\x06\x43LOSED\x10\x01\x12\t\n\x05\x46INAL\x10\x02\x12\n\n\x06IGNORE\x10\x03'
)

_CHAINSTATUS = _descriptor.EnumDescriptor(
  name='ChainStatus',
  full_name='johnny.ChainStatus',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ACTIVE', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CLOSED', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='FINAL', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='IGNORE', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=845,
  serialized_end=905,
)
_sym_db.RegisterEnumDescriptor(_CHAINSTATUS)

ChainStatus = enum_type_wrapper.EnumTypeWrapper(_CHAINSTATUS)
ACTIVE = 0
CLOSED = 1
FINAL = 2
IGNORE = 3


_ACCOUNT_LOGTYPE = _descriptor.EnumDescriptor(
  name='LogType',
  full_name='johnny.Account.LogType',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='TRANSACTIONS', index=0, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='POSITIONS', index=1, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=572,
  serialized_end=614,
)
_sym_db.RegisterEnumDescriptor(_ACCOUNT_LOGTYPE)


_CONFIG = _descriptor.Descriptor(
  name='Config',
  full_name='johnny.Config',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='input', full_name='johnny.Config.input', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='output', full_name='johnny.Config.output', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='futures_option_month_mapping', full_name='johnny.Config.futures_option_month_mapping', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='chains', full_name='johnny.Config.chains', index=3,
      number=4, type=11, cpp_type=10, label=3,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=25,
  serialized_end=194,
)


_INPUTS = _descriptor.Descriptor(
  name='Inputs',
  full_name='johnny.Inputs',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='accounts', full_name='johnny.Inputs.accounts', index=0,
      number=1, type=11, cpp_type=10, label=3,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=196,
  serialized_end=239,
)


_OUTPUTS = _descriptor.Descriptor(
  name='Outputs',
  full_name='johnny.Outputs',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='imported_filename', full_name='johnny.Outputs.imported_filename', index=0,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=241,
  serialized_end=277,
)


_FUTOPTMONTHMAPPING_ITEM = _descriptor.Descriptor(
  name='Item',
  full_name='johnny.FutOptMonthMapping.Item',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='option_product', full_name='johnny.FutOptMonthMapping.Item.option_product', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='option_month', full_name='johnny.FutOptMonthMapping.Item.option_month', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='future_product', full_name='johnny.FutOptMonthMapping.Item.future_product', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='future_month', full_name='johnny.FutOptMonthMapping.Item.future_month', index=3,
      number=4, type=9, cpp_type=9, label=1,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=351,
  serialized_end=449,
)

_FUTOPTMONTHMAPPING = _descriptor.Descriptor(
  name='FutOptMonthMapping',
  full_name='johnny.FutOptMonthMapping',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='months', full_name='johnny.FutOptMonthMapping.months', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_FUTOPTMONTHMAPPING_ITEM, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=280,
  serialized_end=449,
)


_ACCOUNT = _descriptor.Descriptor(
  name='Account',
  full_name='johnny.Account',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='nickname', full_name='johnny.Account.nickname', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='logtype', full_name='johnny.Account.logtype', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='module', full_name='johnny.Account.module', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='source', full_name='johnny.Account.source', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='initial', full_name='johnny.Account.initial', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _ACCOUNT_LOGTYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=452,
  serialized_end=614,
)


_CHAIN = _descriptor.Descriptor(
  name='Chain',
  full_name='johnny.Chain',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='chain_id', full_name='johnny.Chain.chain_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='status', full_name='johnny.Chain.status', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='group', full_name='johnny.Chain.group', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='comment', full_name='johnny.Chain.comment', index=3,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='strategy', full_name='johnny.Chain.strategy', index=4,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='auto_strategy', full_name='johnny.Chain.auto_strategy', index=5,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ids', full_name='johnny.Chain.ids', index=6,
      number=7, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='auto_ids', full_name='johnny.Chain.auto_ids', index=7,
      number=8, type=9, cpp_type=9, label=3,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=617,
  serialized_end=783,
)


_ASSET = _descriptor.Descriptor(
  name='Asset',
  full_name='johnny.Asset',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='instrument', full_name='johnny.Asset.instrument', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='class', full_name='johnny.Asset.class', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='factor', full_name='johnny.Asset.factor', index=2,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=785,
  serialized_end=843,
)

_CONFIG.fields_by_name['input'].message_type = _INPUTS
_CONFIG.fields_by_name['output'].message_type = _OUTPUTS
_CONFIG.fields_by_name['futures_option_month_mapping'].message_type = _FUTOPTMONTHMAPPING
_CONFIG.fields_by_name['chains'].message_type = _CHAIN
_INPUTS.fields_by_name['accounts'].message_type = _ACCOUNT
_FUTOPTMONTHMAPPING_ITEM.containing_type = _FUTOPTMONTHMAPPING
_FUTOPTMONTHMAPPING.fields_by_name['months'].message_type = _FUTOPTMONTHMAPPING_ITEM
_ACCOUNT.fields_by_name['logtype'].enum_type = _ACCOUNT_LOGTYPE
_ACCOUNT_LOGTYPE.containing_type = _ACCOUNT
_CHAIN.fields_by_name['status'].enum_type = _CHAINSTATUS
DESCRIPTOR.message_types_by_name['Config'] = _CONFIG
DESCRIPTOR.message_types_by_name['Inputs'] = _INPUTS
DESCRIPTOR.message_types_by_name['Outputs'] = _OUTPUTS
DESCRIPTOR.message_types_by_name['FutOptMonthMapping'] = _FUTOPTMONTHMAPPING
DESCRIPTOR.message_types_by_name['Account'] = _ACCOUNT
DESCRIPTOR.message_types_by_name['Chain'] = _CHAIN
DESCRIPTOR.message_types_by_name['Asset'] = _ASSET
DESCRIPTOR.enum_types_by_name['ChainStatus'] = _CHAINSTATUS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Config = _reflection.GeneratedProtocolMessageType('Config', (_message.Message,), {
  'DESCRIPTOR' : _CONFIG,
  '__module__' : 'config_pb2'
  # @@protoc_insertion_point(class_scope:johnny.Config)
  })
_sym_db.RegisterMessage(Config)

Inputs = _reflection.GeneratedProtocolMessageType('Inputs', (_message.Message,), {
  'DESCRIPTOR' : _INPUTS,
  '__module__' : 'config_pb2'
  # @@protoc_insertion_point(class_scope:johnny.Inputs)
  })
_sym_db.RegisterMessage(Inputs)

Outputs = _reflection.GeneratedProtocolMessageType('Outputs', (_message.Message,), {
  'DESCRIPTOR' : _OUTPUTS,
  '__module__' : 'config_pb2'
  # @@protoc_insertion_point(class_scope:johnny.Outputs)
  })
_sym_db.RegisterMessage(Outputs)

FutOptMonthMapping = _reflection.GeneratedProtocolMessageType('FutOptMonthMapping', (_message.Message,), {

  'Item' : _reflection.GeneratedProtocolMessageType('Item', (_message.Message,), {
    'DESCRIPTOR' : _FUTOPTMONTHMAPPING_ITEM,
    '__module__' : 'config_pb2'
    # @@protoc_insertion_point(class_scope:johnny.FutOptMonthMapping.Item)
    })
  ,
  'DESCRIPTOR' : _FUTOPTMONTHMAPPING,
  '__module__' : 'config_pb2'
  # @@protoc_insertion_point(class_scope:johnny.FutOptMonthMapping)
  })
_sym_db.RegisterMessage(FutOptMonthMapping)
_sym_db.RegisterMessage(FutOptMonthMapping.Item)

Account = _reflection.GeneratedProtocolMessageType('Account', (_message.Message,), {
  'DESCRIPTOR' : _ACCOUNT,
  '__module__' : 'config_pb2'
  # @@protoc_insertion_point(class_scope:johnny.Account)
  })
_sym_db.RegisterMessage(Account)

Chain = _reflection.GeneratedProtocolMessageType('Chain', (_message.Message,), {
  'DESCRIPTOR' : _CHAIN,
  '__module__' : 'config_pb2'
  # @@protoc_insertion_point(class_scope:johnny.Chain)
  })
_sym_db.RegisterMessage(Chain)

Asset = _reflection.GeneratedProtocolMessageType('Asset', (_message.Message,), {
  'DESCRIPTOR' : _ASSET,
  '__module__' : 'config_pb2'
  # @@protoc_insertion_point(class_scope:johnny.Asset)
  })
_sym_db.RegisterMessage(Asset)


# @@protoc_insertion_point(module_scope)
