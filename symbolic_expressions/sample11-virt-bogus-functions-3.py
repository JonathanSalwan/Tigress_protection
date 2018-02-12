#!/usr/bin/env python2
## -*- coding: utf-8 -*-

import sys

def sx(bits, value):
    sign_bit = 1 << (bits - 1)
    return (value & (sign_bit - 1)) - (value & sign_bit)

SymVar_0 = int(sys.argv[1])
ref_214 = SymVar_0
ref_225 = ref_214 # MOV operation
ref_237 = ref_225 # MOV operation
ref_239 = ref_237 # MOV operation
ref_295 = ((ref_239 >> 56) & 0xFF) # Byte reference - MOV operation
ref_296 = ((ref_239 >> 48) & 0xFF) # Byte reference - MOV operation
ref_297 = ((ref_239 >> 40) & 0xFF) # Byte reference - MOV operation
ref_298 = ((ref_239 >> 32) & 0xFF) # Byte reference - MOV operation
ref_299 = ((ref_239 >> 24) & 0xFF) # Byte reference - MOV operation
ref_300 = ((ref_239 >> 16) & 0xFF) # Byte reference - MOV operation
ref_301 = ((ref_239 >> 8) & 0xFF) # Byte reference - MOV operation
ref_302 = (ref_239 & 0xFF) # Byte reference - MOV operation
ref_7837 = ref_301 # MOVZX operation
ref_7839 = (ref_7837 & 0xFF) # MOVZX operation
ref_7841 = (((ref_7839 & 0xFFFFFFFF) << (0x8 & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_7848 = (ref_7841 & 0xFFFFFFFF) # MOV operation
ref_7852 = ref_302 # MOVZX operation
ref_7854 = (ref_7852 & 0xFF) # MOVZX operation
ref_7856 = (((ref_7854 & 0xFFFFFFFF) + (ref_7848 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_7894 = ref_299 # MOVZX operation
ref_7896 = (ref_7894 & 0xFF) # MOVZX operation
ref_7898 = (((ref_7896 & 0xFFFFFFFF) << (0x8 & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_7905 = (ref_7898 & 0xFFFFFFFF) # MOV operation
ref_7917 = ref_300 # MOVZX operation
ref_7919 = (ref_7917 & 0xFF) # MOVZX operation
ref_7921 = (((ref_7919 & 0xFFFFFFFF) + (ref_7905 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_7929 = (((ref_7921 & 0xFFFFFFFF) << (0xB & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_7936 = ((ref_7929 & 0xFFFFFFFF) ^ ((((((0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x8) + (ref_7856 & 0xFFFFFFFF)) & 0xFFFFFFFF)) # XOR operation
ref_7949 = ((((((0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x8) + (ref_7856 & 0xFFFFFFFF)) & 0xFFFFFFFF) # MOV operation
ref_7951 = (((ref_7949 & 0xFFFFFFFF) << (0x10 & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_7958 = ((ref_7951 & 0xFFFFFFFF) ^ (ref_7936 & 0xFFFFFFFF)) # XOR operation
ref_7987 = (ref_7958 & 0xFFFFFFFF) # MOV operation
ref_7989 = ((ref_7987 & 0xFFFFFFFF) >> (0xB & 0x1F)) # SHR operation
ref_8039 = ref_297 # MOVZX operation
ref_8041 = (ref_8039 & 0xFF) # MOVZX operation
ref_8043 = (((ref_8041 & 0xFFFFFFFF) << (0x8 & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_8050 = (ref_8043 & 0xFFFFFFFF) # MOV operation
ref_8054 = ref_298 # MOVZX operation
ref_8056 = (ref_8054 & 0xFF) # MOVZX operation
ref_8058 = (((ref_8056 & 0xFFFFFFFF) + (ref_8050 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_8096 = ref_295 # MOVZX operation
ref_8098 = (ref_8096 & 0xFF) # MOVZX operation
ref_8100 = (((ref_8098 & 0xFFFFFFFF) << (0x8 & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_8107 = (ref_8100 & 0xFFFFFFFF) # MOV operation
ref_8119 = ref_296 # MOVZX operation
ref_8121 = (ref_8119 & 0xFF) # MOVZX operation
ref_8123 = (((ref_8121 & 0xFFFFFFFF) + (ref_8107 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_8131 = (((ref_8123 & 0xFFFFFFFF) << (0xB & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_8138 = ((ref_8131 & 0xFFFFFFFF) ^ (((((ref_7958 & 0xFFFFFFFF) + (ref_7989 & 0xFFFFFFFF)) & 0xFFFFFFFF) + (ref_8058 & 0xFFFFFFFF)) & 0xFFFFFFFF)) # XOR operation
ref_8151 = (((((ref_7958 & 0xFFFFFFFF) + (ref_7989 & 0xFFFFFFFF)) & 0xFFFFFFFF) + (ref_8058 & 0xFFFFFFFF)) & 0xFFFFFFFF) # MOV operation
ref_8153 = (((ref_8151 & 0xFFFFFFFF) << (0x10 & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_8160 = ((ref_8153 & 0xFFFFFFFF) ^ (ref_8138 & 0xFFFFFFFF)) # XOR operation
ref_8189 = (ref_8160 & 0xFFFFFFFF) # MOV operation
ref_8191 = ((ref_8189 & 0xFFFFFFFF) >> (0xB & 0x1F)) # SHR operation
ref_8261 = (((ref_8160 & 0xFFFFFFFF) + (ref_8191 & 0xFFFFFFFF)) & 0xFFFFFFFF) # MOV operation
ref_8263 = (((ref_8261 & 0xFFFFFFFF) << (0x3 & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_8281 = ((((ref_8160 & 0xFFFFFFFF) + (ref_8191 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_8263 & 0xFFFFFFFF)) # MOV operation
ref_8283 = ((ref_8281 & 0xFFFFFFFF) >> (0x5 & 0x1F)) # SHR operation
ref_8302 = ((((((ref_8160 & 0xFFFFFFFF) + (ref_8191 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_8263 & 0xFFFFFFFF)) + (ref_8283 & 0xFFFFFFFF)) & 0xFFFFFFFF) # MOV operation
ref_8304 = (((ref_8302 & 0xFFFFFFFF) << (0x4 & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_8322 = (((((((ref_8160 & 0xFFFFFFFF) + (ref_8191 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_8263 & 0xFFFFFFFF)) + (ref_8283 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_8304 & 0xFFFFFFFF)) # MOV operation
ref_8324 = ((ref_8322 & 0xFFFFFFFF) >> (0x11 & 0x1F)) # SHR operation
ref_8343 = (((((((((ref_8160 & 0xFFFFFFFF) + (ref_8191 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_8263 & 0xFFFFFFFF)) + (ref_8283 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_8304 & 0xFFFFFFFF)) + (ref_8324 & 0xFFFFFFFF)) & 0xFFFFFFFF) # MOV operation
ref_8345 = (((ref_8343 & 0xFFFFFFFF) << (0x19 & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_8363 = ((((((((((ref_8160 & 0xFFFFFFFF) + (ref_8191 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_8263 & 0xFFFFFFFF)) + (ref_8283 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_8304 & 0xFFFFFFFF)) + (ref_8324 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_8345 & 0xFFFFFFFF)) # MOV operation
ref_8365 = ((ref_8363 & 0xFFFFFFFF) >> (0x6 & 0x1F)) # SHR operation
ref_8384 = ((((((((((((ref_8160 & 0xFFFFFFFF) + (ref_8191 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_8263 & 0xFFFFFFFF)) + (ref_8283 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_8304 & 0xFFFFFFFF)) + (ref_8324 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_8345 & 0xFFFFFFFF)) + (ref_8365 & 0xFFFFFFFF)) & 0xFFFFFFFF) # MOV operation
ref_8397 = (ref_8384 & 0xFFFFFFFF) # MOV operation
ref_10740 = (ref_8397 & 0xFFFFFFFF) # MOV operation
ref_11547 = (ref_10740 & 0xFFFFFFFF) # MOV operation
ref_13890 = (ref_11547 & 0xFFFFFFFF) # MOV operation
ref_14617 = (ref_13890 & 0xFFFFFFFF) # MOV operation
ref_14654 = (ref_14617 & 0xFFFFFFFF) # MOV operation
ref_14666 = ref_14654 # MOV operation
ref_14668 = ref_14666 # MOV operation

print ref_14668 & 0xffffffffffffffff
