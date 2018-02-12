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
ref_284 = ((ref_239 >> 56) & 0xFF) # Byte reference - MOV operation
ref_285 = ((ref_239 >> 48) & 0xFF) # Byte reference - MOV operation
ref_286 = ((ref_239 >> 40) & 0xFF) # Byte reference - MOV operation
ref_287 = ((ref_239 >> 32) & 0xFF) # Byte reference - MOV operation
ref_288 = ((ref_239 >> 24) & 0xFF) # Byte reference - MOV operation
ref_289 = ((ref_239 >> 16) & 0xFF) # Byte reference - MOV operation
ref_290 = ((ref_239 >> 8) & 0xFF) # Byte reference - MOV operation
ref_291 = (ref_239 & 0xFF) # Byte reference - MOV operation
ref_67983 = ref_290 # MOVZX operation
ref_67985 = (ref_67983 & 0xFF) # MOVZX operation
ref_67987 = (((ref_67985 & 0xFFFFFFFF) << (0x8 & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_67994 = (ref_67987 & 0xFFFFFFFF) # MOV operation
ref_67998 = ref_291 # MOVZX operation
ref_68000 = (ref_67998 & 0xFF) # MOVZX operation
ref_68002 = (((ref_68000 & 0xFFFFFFFF) + (ref_67994 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_68040 = ref_288 # MOVZX operation
ref_68042 = (ref_68040 & 0xFF) # MOVZX operation
ref_68044 = (((ref_68042 & 0xFFFFFFFF) << (0x8 & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_68051 = (ref_68044 & 0xFFFFFFFF) # MOV operation
ref_68063 = ref_289 # MOVZX operation
ref_68065 = (ref_68063 & 0xFF) # MOVZX operation
ref_68067 = (((ref_68065 & 0xFFFFFFFF) + (ref_68051 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_68075 = (((ref_68067 & 0xFFFFFFFF) << (0xB & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_68082 = ((ref_68075 & 0xFFFFFFFF) ^ ((((((0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x8) + (ref_68002 & 0xFFFFFFFF)) & 0xFFFFFFFF)) # XOR operation
ref_68095 = ((((((0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x8) + (ref_68002 & 0xFFFFFFFF)) & 0xFFFFFFFF) # MOV operation
ref_68097 = (((ref_68095 & 0xFFFFFFFF) << (0x10 & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_68104 = ((ref_68097 & 0xFFFFFFFF) ^ (ref_68082 & 0xFFFFFFFF)) # XOR operation
ref_68133 = (ref_68104 & 0xFFFFFFFF) # MOV operation
ref_68135 = ((ref_68133 & 0xFFFFFFFF) >> (0xB & 0x1F)) # SHR operation
ref_68185 = ref_286 # MOVZX operation
ref_68187 = (ref_68185 & 0xFF) # MOVZX operation
ref_68189 = (((ref_68187 & 0xFFFFFFFF) << (0x8 & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_68196 = (ref_68189 & 0xFFFFFFFF) # MOV operation
ref_68200 = ref_287 # MOVZX operation
ref_68202 = (ref_68200 & 0xFF) # MOVZX operation
ref_68204 = (((ref_68202 & 0xFFFFFFFF) + (ref_68196 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_68242 = ref_284 # MOVZX operation
ref_68244 = (ref_68242 & 0xFF) # MOVZX operation
ref_68246 = (((ref_68244 & 0xFFFFFFFF) << (0x8 & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_68253 = (ref_68246 & 0xFFFFFFFF) # MOV operation
ref_68265 = ref_285 # MOVZX operation
ref_68267 = (ref_68265 & 0xFF) # MOVZX operation
ref_68269 = (((ref_68267 & 0xFFFFFFFF) + (ref_68253 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_68277 = (((ref_68269 & 0xFFFFFFFF) << (0xB & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_68284 = ((ref_68277 & 0xFFFFFFFF) ^ (((((ref_68104 & 0xFFFFFFFF) + (ref_68135 & 0xFFFFFFFF)) & 0xFFFFFFFF) + (ref_68204 & 0xFFFFFFFF)) & 0xFFFFFFFF)) # XOR operation
ref_68297 = (((((ref_68104 & 0xFFFFFFFF) + (ref_68135 & 0xFFFFFFFF)) & 0xFFFFFFFF) + (ref_68204 & 0xFFFFFFFF)) & 0xFFFFFFFF) # MOV operation
ref_68299 = (((ref_68297 & 0xFFFFFFFF) << (0x10 & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_68306 = ((ref_68299 & 0xFFFFFFFF) ^ (ref_68284 & 0xFFFFFFFF)) # XOR operation
ref_68335 = (ref_68306 & 0xFFFFFFFF) # MOV operation
ref_68337 = ((ref_68335 & 0xFFFFFFFF) >> (0xB & 0x1F)) # SHR operation
ref_68407 = (((ref_68306 & 0xFFFFFFFF) + (ref_68337 & 0xFFFFFFFF)) & 0xFFFFFFFF) # MOV operation
ref_68409 = (((ref_68407 & 0xFFFFFFFF) << (0x3 & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_68427 = ((((ref_68306 & 0xFFFFFFFF) + (ref_68337 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_68409 & 0xFFFFFFFF)) # MOV operation
ref_68429 = ((ref_68427 & 0xFFFFFFFF) >> (0x5 & 0x1F)) # SHR operation
ref_68448 = ((((((ref_68306 & 0xFFFFFFFF) + (ref_68337 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_68409 & 0xFFFFFFFF)) + (ref_68429 & 0xFFFFFFFF)) & 0xFFFFFFFF) # MOV operation
ref_68450 = (((ref_68448 & 0xFFFFFFFF) << (0x4 & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_68468 = (((((((ref_68306 & 0xFFFFFFFF) + (ref_68337 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_68409 & 0xFFFFFFFF)) + (ref_68429 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_68450 & 0xFFFFFFFF)) # MOV operation
ref_68470 = ((ref_68468 & 0xFFFFFFFF) >> (0x11 & 0x1F)) # SHR operation
ref_68489 = (((((((((ref_68306 & 0xFFFFFFFF) + (ref_68337 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_68409 & 0xFFFFFFFF)) + (ref_68429 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_68450 & 0xFFFFFFFF)) + (ref_68470 & 0xFFFFFFFF)) & 0xFFFFFFFF) # MOV operation
ref_68491 = (((ref_68489 & 0xFFFFFFFF) << (0x19 & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_68509 = ((((((((((ref_68306 & 0xFFFFFFFF) + (ref_68337 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_68409 & 0xFFFFFFFF)) + (ref_68429 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_68450 & 0xFFFFFFFF)) + (ref_68470 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_68491 & 0xFFFFFFFF)) # MOV operation
ref_68511 = ((ref_68509 & 0xFFFFFFFF) >> (0x6 & 0x1F)) # SHR operation
ref_68530 = ((((((((((((ref_68306 & 0xFFFFFFFF) + (ref_68337 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_68409 & 0xFFFFFFFF)) + (ref_68429 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_68450 & 0xFFFFFFFF)) + (ref_68470 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_68491 & 0xFFFFFFFF)) + (ref_68511 & 0xFFFFFFFF)) & 0xFFFFFFFF) # MOV operation
ref_68543 = (ref_68530 & 0xFFFFFFFF) # MOV operation
ref_70440 = (ref_68543 & 0xFFFFFFFF) # MOV operation
ref_70553 = (ref_70440 & 0xFFFFFFFF) # MOV operation
ref_111710 = (ref_70553 & 0xFFFFFFFF) # MOV operation
ref_111823 = (ref_111710 & 0xFFFFFFFF) # MOV operation
ref_120872 = (ref_111823 & 0xFFFFFFFF) # MOV operation
ref_120985 = (ref_120872 & 0xFFFFFFFF) # MOV operation
ref_155314 = (ref_120985 & 0xFFFFFFFF) # MOV operation
ref_155427 = (ref_155314 & 0xFFFFFFFF) # MOV operation
ref_162220 = (ref_155427 & 0xFFFFFFFF) # MOV operation
ref_162333 = (ref_162220 & 0xFFFFFFFF) # MOV operation
ref_162871 = (ref_162333 & 0xFFFFFFFF) # MOV operation
ref_162981 = (ref_162871 & 0xFFFFFFFF) # MOV operation
ref_163015 = (ref_162981 & 0xFFFFFFFF) # MOV operation
ref_163027 = ref_163015 # MOV operation
ref_163029 = ref_163027 # MOV operation

print ref_163029 & 0xffffffffffffffff
