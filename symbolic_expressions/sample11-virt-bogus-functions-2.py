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
ref_6894 = ref_301 # MOVZX operation
ref_6896 = (ref_6894 & 0xFF) # MOVZX operation
ref_6898 = (((ref_6896 & 0xFFFFFFFF) << (0x8 & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_6905 = (ref_6898 & 0xFFFFFFFF) # MOV operation
ref_6909 = ref_302 # MOVZX operation
ref_6911 = (ref_6909 & 0xFF) # MOVZX operation
ref_6913 = (((ref_6911 & 0xFFFFFFFF) + (ref_6905 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_6951 = ref_299 # MOVZX operation
ref_6953 = (ref_6951 & 0xFF) # MOVZX operation
ref_6955 = (((ref_6953 & 0xFFFFFFFF) << (0x8 & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_6962 = (ref_6955 & 0xFFFFFFFF) # MOV operation
ref_6974 = ref_300 # MOVZX operation
ref_6976 = (ref_6974 & 0xFF) # MOVZX operation
ref_6978 = (((ref_6976 & 0xFFFFFFFF) + (ref_6962 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_6986 = (((ref_6978 & 0xFFFFFFFF) << (0xB & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_6993 = ((ref_6986 & 0xFFFFFFFF) ^ ((((((0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x8) + (ref_6913 & 0xFFFFFFFF)) & 0xFFFFFFFF)) # XOR operation
ref_7006 = ((((((0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x8) + (ref_6913 & 0xFFFFFFFF)) & 0xFFFFFFFF) # MOV operation
ref_7008 = (((ref_7006 & 0xFFFFFFFF) << (0x10 & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_7015 = ((ref_7008 & 0xFFFFFFFF) ^ (ref_6993 & 0xFFFFFFFF)) # XOR operation
ref_7044 = (ref_7015 & 0xFFFFFFFF) # MOV operation
ref_7046 = ((ref_7044 & 0xFFFFFFFF) >> (0xB & 0x1F)) # SHR operation
ref_7096 = ref_297 # MOVZX operation
ref_7098 = (ref_7096 & 0xFF) # MOVZX operation
ref_7100 = (((ref_7098 & 0xFFFFFFFF) << (0x8 & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_7107 = (ref_7100 & 0xFFFFFFFF) # MOV operation
ref_7111 = ref_298 # MOVZX operation
ref_7113 = (ref_7111 & 0xFF) # MOVZX operation
ref_7115 = (((ref_7113 & 0xFFFFFFFF) + (ref_7107 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_7153 = ref_295 # MOVZX operation
ref_7155 = (ref_7153 & 0xFF) # MOVZX operation
ref_7157 = (((ref_7155 & 0xFFFFFFFF) << (0x8 & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_7164 = (ref_7157 & 0xFFFFFFFF) # MOV operation
ref_7176 = ref_296 # MOVZX operation
ref_7178 = (ref_7176 & 0xFF) # MOVZX operation
ref_7180 = (((ref_7178 & 0xFFFFFFFF) + (ref_7164 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_7188 = (((ref_7180 & 0xFFFFFFFF) << (0xB & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_7195 = ((ref_7188 & 0xFFFFFFFF) ^ (((((ref_7015 & 0xFFFFFFFF) + (ref_7046 & 0xFFFFFFFF)) & 0xFFFFFFFF) + (ref_7115 & 0xFFFFFFFF)) & 0xFFFFFFFF)) # XOR operation
ref_7208 = (((((ref_7015 & 0xFFFFFFFF) + (ref_7046 & 0xFFFFFFFF)) & 0xFFFFFFFF) + (ref_7115 & 0xFFFFFFFF)) & 0xFFFFFFFF) # MOV operation
ref_7210 = (((ref_7208 & 0xFFFFFFFF) << (0x10 & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_7217 = ((ref_7210 & 0xFFFFFFFF) ^ (ref_7195 & 0xFFFFFFFF)) # XOR operation
ref_7246 = (ref_7217 & 0xFFFFFFFF) # MOV operation
ref_7248 = ((ref_7246 & 0xFFFFFFFF) >> (0xB & 0x1F)) # SHR operation
ref_7318 = (((ref_7217 & 0xFFFFFFFF) + (ref_7248 & 0xFFFFFFFF)) & 0xFFFFFFFF) # MOV operation
ref_7320 = (((ref_7318 & 0xFFFFFFFF) << (0x3 & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_7338 = ((((ref_7217 & 0xFFFFFFFF) + (ref_7248 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_7320 & 0xFFFFFFFF)) # MOV operation
ref_7340 = ((ref_7338 & 0xFFFFFFFF) >> (0x5 & 0x1F)) # SHR operation
ref_7359 = ((((((ref_7217 & 0xFFFFFFFF) + (ref_7248 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_7320 & 0xFFFFFFFF)) + (ref_7340 & 0xFFFFFFFF)) & 0xFFFFFFFF) # MOV operation
ref_7361 = (((ref_7359 & 0xFFFFFFFF) << (0x4 & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_7379 = (((((((ref_7217 & 0xFFFFFFFF) + (ref_7248 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_7320 & 0xFFFFFFFF)) + (ref_7340 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_7361 & 0xFFFFFFFF)) # MOV operation
ref_7381 = ((ref_7379 & 0xFFFFFFFF) >> (0x11 & 0x1F)) # SHR operation
ref_7400 = (((((((((ref_7217 & 0xFFFFFFFF) + (ref_7248 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_7320 & 0xFFFFFFFF)) + (ref_7340 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_7361 & 0xFFFFFFFF)) + (ref_7381 & 0xFFFFFFFF)) & 0xFFFFFFFF) # MOV operation
ref_7402 = (((ref_7400 & 0xFFFFFFFF) << (0x19 & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_7420 = ((((((((((ref_7217 & 0xFFFFFFFF) + (ref_7248 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_7320 & 0xFFFFFFFF)) + (ref_7340 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_7361 & 0xFFFFFFFF)) + (ref_7381 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_7402 & 0xFFFFFFFF)) # MOV operation
ref_7422 = ((ref_7420 & 0xFFFFFFFF) >> (0x6 & 0x1F)) # SHR operation
ref_7441 = ((((((((((((ref_7217 & 0xFFFFFFFF) + (ref_7248 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_7320 & 0xFFFFFFFF)) + (ref_7340 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_7361 & 0xFFFFFFFF)) + (ref_7381 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_7402 & 0xFFFFFFFF)) + (ref_7422 & 0xFFFFFFFF)) & 0xFFFFFFFF) # MOV operation
ref_7454 = (ref_7441 & 0xFFFFFFFF) # MOV operation
ref_8952 = (ref_7454 & 0xFFFFFFFF) # MOV operation
ref_9383 = (ref_8952 & 0xFFFFFFFF) # MOV operation
ref_10692 = (ref_9383 & 0xFFFFFFFF) # MOV operation
ref_10975 = (ref_10692 & 0xFFFFFFFF) # MOV operation
ref_11012 = (ref_10975 & 0xFFFFFFFF) # MOV operation
ref_11024 = ref_11012 # MOV operation
ref_11026 = ref_11024 # MOV operation

print ref_11026 & 0xffffffffffffffff
