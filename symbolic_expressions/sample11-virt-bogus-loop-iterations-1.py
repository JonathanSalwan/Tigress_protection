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
ref_15803 = ref_290 # MOVZX operation
ref_15805 = (ref_15803 & 0xFF) # MOVZX operation
ref_15807 = (((ref_15805 & 0xFFFFFFFF) << (0x8 & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_15814 = (ref_15807 & 0xFFFFFFFF) # MOV operation
ref_15818 = ref_291 # MOVZX operation
ref_15820 = (ref_15818 & 0xFF) # MOVZX operation
ref_15822 = (((ref_15820 & 0xFFFFFFFF) + (ref_15814 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_15860 = ref_288 # MOVZX operation
ref_15862 = (ref_15860 & 0xFF) # MOVZX operation
ref_15864 = (((ref_15862 & 0xFFFFFFFF) << (0x8 & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_15871 = (ref_15864 & 0xFFFFFFFF) # MOV operation
ref_15883 = ref_289 # MOVZX operation
ref_15885 = (ref_15883 & 0xFF) # MOVZX operation
ref_15887 = (((ref_15885 & 0xFFFFFFFF) + (ref_15871 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_15895 = (((ref_15887 & 0xFFFFFFFF) << (0xB & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_15902 = ((ref_15895 & 0xFFFFFFFF) ^ ((((((0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x8) + (ref_15822 & 0xFFFFFFFF)) & 0xFFFFFFFF)) # XOR operation
ref_15915 = ((((((0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x8) + (ref_15822 & 0xFFFFFFFF)) & 0xFFFFFFFF) # MOV operation
ref_15917 = (((ref_15915 & 0xFFFFFFFF) << (0x10 & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_15924 = ((ref_15917 & 0xFFFFFFFF) ^ (ref_15902 & 0xFFFFFFFF)) # XOR operation
ref_15953 = (ref_15924 & 0xFFFFFFFF) # MOV operation
ref_15955 = ((ref_15953 & 0xFFFFFFFF) >> (0xB & 0x1F)) # SHR operation
ref_16005 = ref_286 # MOVZX operation
ref_16007 = (ref_16005 & 0xFF) # MOVZX operation
ref_16009 = (((ref_16007 & 0xFFFFFFFF) << (0x8 & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_16016 = (ref_16009 & 0xFFFFFFFF) # MOV operation
ref_16020 = ref_287 # MOVZX operation
ref_16022 = (ref_16020 & 0xFF) # MOVZX operation
ref_16024 = (((ref_16022 & 0xFFFFFFFF) + (ref_16016 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_16062 = ref_284 # MOVZX operation
ref_16064 = (ref_16062 & 0xFF) # MOVZX operation
ref_16066 = (((ref_16064 & 0xFFFFFFFF) << (0x8 & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_16073 = (ref_16066 & 0xFFFFFFFF) # MOV operation
ref_16085 = ref_285 # MOVZX operation
ref_16087 = (ref_16085 & 0xFF) # MOVZX operation
ref_16089 = (((ref_16087 & 0xFFFFFFFF) + (ref_16073 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_16097 = (((ref_16089 & 0xFFFFFFFF) << (0xB & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_16104 = ((ref_16097 & 0xFFFFFFFF) ^ (((((ref_15924 & 0xFFFFFFFF) + (ref_15955 & 0xFFFFFFFF)) & 0xFFFFFFFF) + (ref_16024 & 0xFFFFFFFF)) & 0xFFFFFFFF)) # XOR operation
ref_16117 = (((((ref_15924 & 0xFFFFFFFF) + (ref_15955 & 0xFFFFFFFF)) & 0xFFFFFFFF) + (ref_16024 & 0xFFFFFFFF)) & 0xFFFFFFFF) # MOV operation
ref_16119 = (((ref_16117 & 0xFFFFFFFF) << (0x10 & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_16126 = ((ref_16119 & 0xFFFFFFFF) ^ (ref_16104 & 0xFFFFFFFF)) # XOR operation
ref_16155 = (ref_16126 & 0xFFFFFFFF) # MOV operation
ref_16157 = ((ref_16155 & 0xFFFFFFFF) >> (0xB & 0x1F)) # SHR operation
ref_16227 = (((ref_16126 & 0xFFFFFFFF) + (ref_16157 & 0xFFFFFFFF)) & 0xFFFFFFFF) # MOV operation
ref_16229 = (((ref_16227 & 0xFFFFFFFF) << (0x3 & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_16247 = ((((ref_16126 & 0xFFFFFFFF) + (ref_16157 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_16229 & 0xFFFFFFFF)) # MOV operation
ref_16249 = ((ref_16247 & 0xFFFFFFFF) >> (0x5 & 0x1F)) # SHR operation
ref_16268 = ((((((ref_16126 & 0xFFFFFFFF) + (ref_16157 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_16229 & 0xFFFFFFFF)) + (ref_16249 & 0xFFFFFFFF)) & 0xFFFFFFFF) # MOV operation
ref_16270 = (((ref_16268 & 0xFFFFFFFF) << (0x4 & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_16288 = (((((((ref_16126 & 0xFFFFFFFF) + (ref_16157 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_16229 & 0xFFFFFFFF)) + (ref_16249 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_16270 & 0xFFFFFFFF)) # MOV operation
ref_16290 = ((ref_16288 & 0xFFFFFFFF) >> (0x11 & 0x1F)) # SHR operation
ref_16309 = (((((((((ref_16126 & 0xFFFFFFFF) + (ref_16157 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_16229 & 0xFFFFFFFF)) + (ref_16249 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_16270 & 0xFFFFFFFF)) + (ref_16290 & 0xFFFFFFFF)) & 0xFFFFFFFF) # MOV operation
ref_16311 = (((ref_16309 & 0xFFFFFFFF) << (0x19 & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_16329 = ((((((((((ref_16126 & 0xFFFFFFFF) + (ref_16157 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_16229 & 0xFFFFFFFF)) + (ref_16249 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_16270 & 0xFFFFFFFF)) + (ref_16290 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_16311 & 0xFFFFFFFF)) # MOV operation
ref_16331 = ((ref_16329 & 0xFFFFFFFF) >> (0x6 & 0x1F)) # SHR operation
ref_16350 = ((((((((((((ref_16126 & 0xFFFFFFFF) + (ref_16157 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_16229 & 0xFFFFFFFF)) + (ref_16249 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_16270 & 0xFFFFFFFF)) + (ref_16290 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_16311 & 0xFFFFFFFF)) + (ref_16331 & 0xFFFFFFFF)) & 0xFFFFFFFF) # MOV operation
ref_16363 = (ref_16350 & 0xFFFFFFFF) # MOV operation
ref_22997 = (ref_16363 & 0xFFFFFFFF) # MOV operation
ref_25191 = (ref_22997 & 0xFFFFFFFF) # MOV operation
ref_31810 = (ref_25191 & 0xFFFFFFFF) # MOV operation
ref_34001 = (ref_31810 & 0xFFFFFFFF) # MOV operation
ref_34035 = (ref_34001 & 0xFFFFFFFF) # MOV operation
ref_34047 = ref_34035 # MOV operation
ref_34049 = ref_34047 # MOV operation

print ref_34049 & 0xffffffffffffffff
