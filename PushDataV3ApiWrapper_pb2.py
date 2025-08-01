# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: PushDataV3ApiWrapper.proto
# Protobuf Python Version: 6.31.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    6,
    31,
    1,
    '',
    'PushDataV3ApiWrapper.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import PublicDealsV3Api_pb2 as PublicDealsV3Api__pb2
import PublicIncreaseDepthsV3Api_pb2 as PublicIncreaseDepthsV3Api__pb2
import PublicLimitDepthsV3Api_pb2 as PublicLimitDepthsV3Api__pb2
import PrivateOrdersV3Api_pb2 as PrivateOrdersV3Api__pb2
import PublicBookTickerV3Api_pb2 as PublicBookTickerV3Api__pb2
import PrivateDealsV3Api_pb2 as PrivateDealsV3Api__pb2
import PrivateAccountV3Api_pb2 as PrivateAccountV3Api__pb2
import PublicSpotKlineV3Api_pb2 as PublicSpotKlineV3Api__pb2
import PublicMiniTickerV3Api_pb2 as PublicMiniTickerV3Api__pb2
import PublicMiniTickersV3Api_pb2 as PublicMiniTickersV3Api__pb2
import PublicBookTickerBatchV3Api_pb2 as PublicBookTickerBatchV3Api__pb2
import PublicIncreaseDepthsBatchV3Api_pb2 as PublicIncreaseDepthsBatchV3Api__pb2
import PublicAggreDepthsV3Api_pb2 as PublicAggreDepthsV3Api__pb2
import PublicAggreDealsV3Api_pb2 as PublicAggreDealsV3Api__pb2
import PublicAggreBookTickerV3Api_pb2 as PublicAggreBookTickerV3Api__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1aPushDataV3ApiWrapper.proto\x1a\x16PublicDealsV3Api.proto\x1a\x1fPublicIncreaseDepthsV3Api.proto\x1a\x1cPublicLimitDepthsV3Api.proto\x1a\x18PrivateOrdersV3Api.proto\x1a\x1bPublicBookTickerV3Api.proto\x1a\x17PrivateDealsV3Api.proto\x1a\x19PrivateAccountV3Api.proto\x1a\x1aPublicSpotKlineV3Api.proto\x1a\x1bPublicMiniTickerV3Api.proto\x1a\x1cPublicMiniTickersV3Api.proto\x1a PublicBookTickerBatchV3Api.proto\x1a$PublicIncreaseDepthsBatchV3Api.proto\x1a\x1cPublicAggreDepthsV3Api.proto\x1a\x1bPublicAggreDealsV3Api.proto\x1a PublicAggreBookTickerV3Api.proto\"\xf0\x07\n\x14PushDataV3ApiWrapper\x12\x0f\n\x07\x63hannel\x18\x01 \x01(\t\x12)\n\x0bpublicDeals\x18\xad\x02 \x01(\x0b\x32\x11.PublicDealsV3ApiH\x00\x12;\n\x14publicIncreaseDepths\x18\xae\x02 \x01(\x0b\x32\x1a.PublicIncreaseDepthsV3ApiH\x00\x12\x35\n\x11publicLimitDepths\x18\xaf\x02 \x01(\x0b\x32\x17.PublicLimitDepthsV3ApiH\x00\x12-\n\rprivateOrders\x18\xb0\x02 \x01(\x0b\x32\x13.PrivateOrdersV3ApiH\x00\x12\x33\n\x10publicBookTicker\x18\xb1\x02 \x01(\x0b\x32\x16.PublicBookTickerV3ApiH\x00\x12+\n\x0cprivateDeals\x18\xb2\x02 \x01(\x0b\x32\x12.PrivateDealsV3ApiH\x00\x12/\n\x0eprivateAccount\x18\xb3\x02 \x01(\x0b\x32\x14.PrivateAccountV3ApiH\x00\x12\x31\n\x0fpublicSpotKline\x18\xb4\x02 \x01(\x0b\x32\x15.PublicSpotKlineV3ApiH\x00\x12\x33\n\x10publicMiniTicker\x18\xb5\x02 \x01(\x0b\x32\x16.PublicMiniTickerV3ApiH\x00\x12\x35\n\x11publicMiniTickers\x18\xb6\x02 \x01(\x0b\x32\x17.PublicMiniTickersV3ApiH\x00\x12=\n\x15publicBookTickerBatch\x18\xb7\x02 \x01(\x0b\x32\x1b.PublicBookTickerBatchV3ApiH\x00\x12\x45\n\x19publicIncreaseDepthsBatch\x18\xb8\x02 \x01(\x0b\x32\x1f.PublicIncreaseDepthsBatchV3ApiH\x00\x12\x35\n\x11publicAggreDepths\x18\xb9\x02 \x01(\x0b\x32\x17.PublicAggreDepthsV3ApiH\x00\x12\x33\n\x10publicAggreDeals\x18\xba\x02 \x01(\x0b\x32\x16.PublicAggreDealsV3ApiH\x00\x12=\n\x15publicAggreBookTicker\x18\xbb\x02 \x01(\x0b\x32\x1b.PublicAggreBookTickerV3ApiH\x00\x12\x13\n\x06symbol\x18\x03 \x01(\tH\x01\x88\x01\x01\x12\x15\n\x08symbolId\x18\x04 \x01(\tH\x02\x88\x01\x01\x12\x17\n\ncreateTime\x18\x05 \x01(\x03H\x03\x88\x01\x01\x12\x15\n\x08sendTime\x18\x06 \x01(\x03H\x04\x88\x01\x01\x42\x06\n\x04\x62odyB\t\n\x07_symbolB\x0b\n\t_symbolIdB\r\n\x0b_createTimeB\x0b\n\t_sendTimeB=\n\x1c\x63om.mxc.push.common.protobufB\x19PushDataV3ApiWrapperProtoH\x01P\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'PushDataV3ApiWrapper_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\034com.mxc.push.common.protobufB\031PushDataV3ApiWrapperProtoH\001P\001'
  _globals['_PUSHDATAV3APIWRAPPER']._serialized_start=477
  _globals['_PUSHDATAV3APIWRAPPER']._serialized_end=1485
# @@protoc_insertion_point(module_scope)
