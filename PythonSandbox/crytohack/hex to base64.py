import base64

HEX_STRING = '72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf'

BYTE_ARRAY = bytearray.fromhex(HEX_STRING)
print(BYTE_ARRAY)
BASE64_VAL = base64.b64encode(BYTE_ARRAY)
print(BASE64_VAL)