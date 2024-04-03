# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: fedn/network/grpc/fedn.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1c\x66\x65\x64n/network/grpc/fedn.proto\x12\x04\x66\x65\x64n\x1a\x1fgoogle/protobuf/timestamp.proto\":\n\x08Response\x12\x1c\n\x06sender\x18\x01 \x01(\x0b\x32\x0c.fedn.Client\x12\x10\n\x08response\x18\x02 \x01(\t\"\xbc\x02\n\x06Status\x12\x1c\n\x06sender\x18\x01 \x01(\x0b\x32\x0c.fedn.Client\x12\x0e\n\x06status\x18\x02 \x01(\t\x12(\n\tlog_level\x18\x03 \x01(\x0e\x32\x15.fedn.Status.LogLevel\x12\x0c\n\x04\x64\x61ta\x18\x04 \x01(\t\x12\x16\n\x0e\x63orrelation_id\x18\x05 \x01(\t\x12-\n\ttimestamp\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x1e\n\x04type\x18\x07 \x01(\x0e\x32\x10.fedn.StatusType\x12\r\n\x05\x65xtra\x18\x08 \x01(\t\x12\x12\n\nsession_id\x18\t \x01(\t\"B\n\x08LogLevel\x12\x08\n\x04INFO\x10\x00\x12\t\n\x05\x44\x45\x42UG\x10\x01\x12\x0b\n\x07WARNING\x10\x02\x12\t\n\x05\x45RROR\x10\x03\x12\t\n\x05\x41UDIT\x10\x04\"\xd8\x01\n\x0bTaskRequest\x12\x1c\n\x06sender\x18\x01 \x01(\x0b\x32\x0c.fedn.Client\x12\x1e\n\x08receiver\x18\x02 \x01(\x0b\x32\x0c.fedn.Client\x12\x10\n\x08model_id\x18\x03 \x01(\t\x12\x0c\n\x04\x64\x61ta\x18\x04 \x01(\t\x12\x16\n\x0e\x63orrelation_id\x18\x05 \x01(\t\x12\x11\n\ttimestamp\x18\x06 \x01(\t\x12\x0c\n\x04meta\x18\x07 \x01(\t\x12\x12\n\nsession_id\x18\x08 \x01(\t\x12\x1e\n\x04type\x18\t \x01(\x0e\x32\x10.fedn.StatusType\"\xbf\x01\n\x0bModelUpdate\x12\x1c\n\x06sender\x18\x01 \x01(\x0b\x32\x0c.fedn.Client\x12\x1e\n\x08receiver\x18\x02 \x01(\x0b\x32\x0c.fedn.Client\x12\x10\n\x08model_id\x18\x03 \x01(\t\x12\x17\n\x0fmodel_update_id\x18\x04 \x01(\t\x12\x16\n\x0e\x63orrelation_id\x18\x05 \x01(\t\x12\x11\n\ttimestamp\x18\x06 \x01(\t\x12\x0c\n\x04meta\x18\x07 \x01(\t\x12\x0e\n\x06\x63onfig\x18\x08 \x01(\t\"\xd8\x01\n\x0fModelValidation\x12\x1c\n\x06sender\x18\x01 \x01(\x0b\x32\x0c.fedn.Client\x12\x1e\n\x08receiver\x18\x02 \x01(\x0b\x32\x0c.fedn.Client\x12\x10\n\x08model_id\x18\x03 \x01(\t\x12\x0c\n\x04\x64\x61ta\x18\x04 \x01(\t\x12\x16\n\x0e\x63orrelation_id\x18\x05 \x01(\t\x12-\n\ttimestamp\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0c\n\x04meta\x18\x07 \x01(\t\x12\x12\n\nsession_id\x18\x08 \x01(\t\"\x89\x01\n\x0cModelRequest\x12\x1c\n\x06sender\x18\x01 \x01(\x0b\x32\x0c.fedn.Client\x12\x1e\n\x08receiver\x18\x02 \x01(\x0b\x32\x0c.fedn.Client\x12\x0c\n\x04\x64\x61ta\x18\x03 \x01(\x0c\x12\n\n\x02id\x18\x04 \x01(\t\x12!\n\x06status\x18\x05 \x01(\x0e\x32\x11.fedn.ModelStatus\"]\n\rModelResponse\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\x0c\x12\n\n\x02id\x18\x02 \x01(\t\x12!\n\x06status\x18\x03 \x01(\x0e\x32\x11.fedn.ModelStatus\x12\x0f\n\x07message\x18\x04 \x01(\t\"U\n\x15GetGlobalModelRequest\x12\x1c\n\x06sender\x18\x01 \x01(\x0b\x32\x0c.fedn.Client\x12\x1e\n\x08receiver\x18\x02 \x01(\x0b\x32\x0c.fedn.Client\"h\n\x16GetGlobalModelResponse\x12\x1c\n\x06sender\x18\x01 \x01(\x0b\x32\x0c.fedn.Client\x12\x1e\n\x08receiver\x18\x02 \x01(\x0b\x32\x0c.fedn.Client\x12\x10\n\x08model_id\x18\x03 \x01(\t\")\n\tHeartbeat\x12\x1c\n\x06sender\x18\x01 \x01(\x0b\x32\x0c.fedn.Client\"W\n\x16\x43lientAvailableMessage\x12\x1c\n\x06sender\x18\x01 \x01(\x0b\x32\x0c.fedn.Client\x12\x0c\n\x04\x64\x61ta\x18\x02 \x01(\t\x12\x11\n\ttimestamp\x18\x03 \x01(\t\"P\n\x12ListClientsRequest\x12\x1c\n\x06sender\x18\x01 \x01(\x0b\x32\x0c.fedn.Client\x12\x1c\n\x07\x63hannel\x18\x02 \x01(\x0e\x32\x0b.fedn.Queue\"*\n\nClientList\x12\x1c\n\x06\x63lient\x18\x01 \x03(\x0b\x32\x0c.fedn.Client\"0\n\x06\x43lient\x12\x18\n\x04role\x18\x01 \x01(\x0e\x32\n.fedn.Role\x12\x0c\n\x04name\x18\x02 \x01(\t\"m\n\x0fReassignRequest\x12\x1c\n\x06sender\x18\x01 \x01(\x0b\x32\x0c.fedn.Client\x12\x1e\n\x08receiver\x18\x02 \x01(\x0b\x32\x0c.fedn.Client\x12\x0e\n\x06server\x18\x03 \x01(\t\x12\x0c\n\x04port\x18\x04 \x01(\r\"c\n\x10ReconnectRequest\x12\x1c\n\x06sender\x18\x01 \x01(\x0b\x32\x0c.fedn.Client\x12\x1e\n\x08receiver\x18\x02 \x01(\x0b\x32\x0c.fedn.Client\x12\x11\n\treconnect\x18\x03 \x01(\r\"\'\n\tParameter\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t\"T\n\x0e\x43ontrolRequest\x12\x1e\n\x07\x63ommand\x18\x01 \x01(\x0e\x32\r.fedn.Command\x12\"\n\tparameter\x18\x02 \x03(\x0b\x32\x0f.fedn.Parameter\"F\n\x0f\x43ontrolResponse\x12\x0f\n\x07message\x18\x01 \x01(\t\x12\"\n\tparameter\x18\x02 \x03(\x0b\x32\x0f.fedn.Parameter\"\x13\n\x11\x43onnectionRequest\"<\n\x12\x43onnectionResponse\x12&\n\x06status\x18\x01 \x01(\x0e\x32\x16.fedn.ConnectionStatus*\x84\x01\n\nStatusType\x12\x07\n\x03LOG\x10\x00\x12\x18\n\x14MODEL_UPDATE_REQUEST\x10\x01\x12\x10\n\x0cMODEL_UPDATE\x10\x02\x12\x1c\n\x18MODEL_VALIDATION_REQUEST\x10\x03\x12\x14\n\x10MODEL_VALIDATION\x10\x04\x12\r\n\tINFERENCE\x10\x05*$\n\x05Queue\x12\x0b\n\x07\x44\x45\x46\x41ULT\x10\x00\x12\x0e\n\nTASK_QUEUE\x10\x01*S\n\x0bModelStatus\x12\x06\n\x02OK\x10\x00\x12\x0f\n\x0bIN_PROGRESS\x10\x01\x12\x12\n\x0eIN_PROGRESS_OK\x10\x02\x12\n\n\x06\x46\x41ILED\x10\x03\x12\x0b\n\x07UNKNOWN\x10\x04*8\n\x04Role\x12\n\n\x06WORKER\x10\x00\x12\x0c\n\x08\x43OMBINER\x10\x01\x12\x0b\n\x07REDUCER\x10\x02\x12\t\n\x05OTHER\x10\x03*J\n\x07\x43ommand\x12\x08\n\x04IDLE\x10\x00\x12\t\n\x05START\x10\x01\x12\t\n\x05PAUSE\x10\x02\x12\x08\n\x04STOP\x10\x03\x12\t\n\x05RESET\x10\x04\x12\n\n\x06REPORT\x10\x05*I\n\x10\x43onnectionStatus\x12\x11\n\rNOT_ACCEPTING\x10\x00\x12\r\n\tACCEPTING\x10\x01\x12\x13\n\x0fTRY_AGAIN_LATER\x10\x02\x32z\n\x0cModelService\x12\x33\n\x06Upload\x12\x12.fedn.ModelRequest\x1a\x13.fedn.ModelResponse(\x01\x12\x35\n\x08\x44ownload\x12\x12.fedn.ModelRequest\x1a\x13.fedn.ModelResponse0\x01\x32\xf8\x01\n\x07\x43ontrol\x12\x34\n\x05Start\x12\x14.fedn.ControlRequest\x1a\x15.fedn.ControlResponse\x12\x33\n\x04Stop\x12\x14.fedn.ControlRequest\x1a\x15.fedn.ControlResponse\x12\x44\n\x15\x46lushAggregationQueue\x12\x14.fedn.ControlRequest\x1a\x15.fedn.ControlResponse\x12<\n\rSetAggregator\x12\x14.fedn.ControlRequest\x1a\x15.fedn.ControlResponse2V\n\x07Reducer\x12K\n\x0eGetGlobalModel\x12\x1b.fedn.GetGlobalModelRequest\x1a\x1c.fedn.GetGlobalModelResponse2\xab\x03\n\tConnector\x12\x44\n\x14\x41llianceStatusStream\x12\x1c.fedn.ClientAvailableMessage\x1a\x0c.fedn.Status0\x01\x12*\n\nSendStatus\x12\x0c.fedn.Status\x1a\x0e.fedn.Response\x12?\n\x11ListActiveClients\x12\x18.fedn.ListClientsRequest\x1a\x10.fedn.ClientList\x12\x45\n\x10\x41\x63\x63\x65ptingClients\x12\x17.fedn.ConnectionRequest\x1a\x18.fedn.ConnectionResponse\x12\x30\n\rSendHeartbeat\x12\x0f.fedn.Heartbeat\x1a\x0e.fedn.Response\x12\x37\n\x0eReassignClient\x12\x15.fedn.ReassignRequest\x1a\x0e.fedn.Response\x12\x39\n\x0fReconnectClient\x12\x16.fedn.ReconnectRequest\x1a\x0e.fedn.Response2\xbf\x01\n\x08\x43ombiner\x12?\n\nTaskStream\x12\x1c.fedn.ClientAvailableMessage\x1a\x11.fedn.TaskRequest0\x01\x12\x34\n\x0fSendModelUpdate\x12\x11.fedn.ModelUpdate\x1a\x0e.fedn.Response\x12<\n\x13SendModelValidation\x12\x15.fedn.ModelValidation\x1a\x0e.fedn.Responseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'fedn.network.grpc.fedn_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _globals['_STATUSTYPE']._serialized_start=2313
  _globals['_STATUSTYPE']._serialized_end=2445
  _globals['_QUEUE']._serialized_start=2447
  _globals['_QUEUE']._serialized_end=2483
  _globals['_MODELSTATUS']._serialized_start=2485
  _globals['_MODELSTATUS']._serialized_end=2568
  _globals['_ROLE']._serialized_start=2570
  _globals['_ROLE']._serialized_end=2626
  _globals['_COMMAND']._serialized_start=2628
  _globals['_COMMAND']._serialized_end=2702
  _globals['_CONNECTIONSTATUS']._serialized_start=2704
  _globals['_CONNECTIONSTATUS']._serialized_end=2777
  _globals['_RESPONSE']._serialized_start=71
  _globals['_RESPONSE']._serialized_end=129
  _globals['_STATUS']._serialized_start=132
  _globals['_STATUS']._serialized_end=448
  _globals['_STATUS_LOGLEVEL']._serialized_start=382
  _globals['_STATUS_LOGLEVEL']._serialized_end=448
  _globals['_TASKREQUEST']._serialized_start=451
  _globals['_TASKREQUEST']._serialized_end=667
  _globals['_MODELUPDATE']._serialized_start=670
  _globals['_MODELUPDATE']._serialized_end=861
  _globals['_MODELVALIDATION']._serialized_start=864
  _globals['_MODELVALIDATION']._serialized_end=1080
  _globals['_MODELREQUEST']._serialized_start=1083
  _globals['_MODELREQUEST']._serialized_end=1220
  _globals['_MODELRESPONSE']._serialized_start=1222
  _globals['_MODELRESPONSE']._serialized_end=1315
  _globals['_GETGLOBALMODELREQUEST']._serialized_start=1317
  _globals['_GETGLOBALMODELREQUEST']._serialized_end=1402
  _globals['_GETGLOBALMODELRESPONSE']._serialized_start=1404
  _globals['_GETGLOBALMODELRESPONSE']._serialized_end=1508
  _globals['_HEARTBEAT']._serialized_start=1510
  _globals['_HEARTBEAT']._serialized_end=1551
  _globals['_CLIENTAVAILABLEMESSAGE']._serialized_start=1553
  _globals['_CLIENTAVAILABLEMESSAGE']._serialized_end=1640
  _globals['_LISTCLIENTSREQUEST']._serialized_start=1642
  _globals['_LISTCLIENTSREQUEST']._serialized_end=1722
  _globals['_CLIENTLIST']._serialized_start=1724
  _globals['_CLIENTLIST']._serialized_end=1766
  _globals['_CLIENT']._serialized_start=1768
  _globals['_CLIENT']._serialized_end=1816
  _globals['_REASSIGNREQUEST']._serialized_start=1818
  _globals['_REASSIGNREQUEST']._serialized_end=1927
  _globals['_RECONNECTREQUEST']._serialized_start=1929
  _globals['_RECONNECTREQUEST']._serialized_end=2028
  _globals['_PARAMETER']._serialized_start=2030
  _globals['_PARAMETER']._serialized_end=2069
  _globals['_CONTROLREQUEST']._serialized_start=2071
  _globals['_CONTROLREQUEST']._serialized_end=2155
  _globals['_CONTROLRESPONSE']._serialized_start=2157
  _globals['_CONTROLRESPONSE']._serialized_end=2227
  _globals['_CONNECTIONREQUEST']._serialized_start=2229
  _globals['_CONNECTIONREQUEST']._serialized_end=2248
  _globals['_CONNECTIONRESPONSE']._serialized_start=2250
  _globals['_CONNECTIONRESPONSE']._serialized_end=2310
  _globals['_MODELSERVICE']._serialized_start=2779
  _globals['_MODELSERVICE']._serialized_end=2901
  _globals['_CONTROL']._serialized_start=2904
  _globals['_CONTROL']._serialized_end=3152
  _globals['_REDUCER']._serialized_start=3154
  _globals['_REDUCER']._serialized_end=3240
  _globals['_CONNECTOR']._serialized_start=3243
  _globals['_CONNECTOR']._serialized_end=3670
  _globals['_COMBINER']._serialized_start=3673
  _globals['_COMBINER']._serialized_end=3864
# @@protoc_insertion_point(module_scope)