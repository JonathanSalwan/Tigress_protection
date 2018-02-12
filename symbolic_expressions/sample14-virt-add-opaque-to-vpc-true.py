#!/usr/bin/env python2
## -*- coding: utf-8 -*-

import sys

def sx(bits, value):
    sign_bit = 1 << (bits - 1)
    return (value & (sign_bit - 1)) - (value & sign_bit)

SymVar_0 = int(sys.argv[1])
ref_382 = SymVar_0
ref_393 = ref_382 # MOV operation
ref_405 = ref_393 # MOV operation
ref_407 = ref_405 # MOV operation
ref_452 = ((ref_407 >> 56) & 0xFF) # Byte reference - MOV operation
ref_453 = ((ref_407 >> 48) & 0xFF) # Byte reference - MOV operation
ref_454 = ((ref_407 >> 40) & 0xFF) # Byte reference - MOV operation
ref_455 = ((ref_407 >> 32) & 0xFF) # Byte reference - MOV operation
ref_456 = ((ref_407 >> 24) & 0xFF) # Byte reference - MOV operation
ref_457 = ((ref_407 >> 16) & 0xFF) # Byte reference - MOV operation
ref_458 = ((ref_407 >> 8) & 0xFF) # Byte reference - MOV operation
ref_459 = (ref_407 & 0xFF) # Byte reference - MOV operation
ref_5805 = ((((ref_456) << 8 | ref_457) << 8 | ref_458) << 8 | ref_459) # MOV operation
ref_5813 = (ref_5805 & 0xFFFFFFFF) # MOV operation
ref_5837 = (ref_5813 & 0xFFFFFFFF) # MOV operation
ref_5851 = (ref_5837 & 0xFFFFFFFF) # MOV operation
ref_5988 = ((((ref_452) << 8 | ref_453) << 8 | ref_454) << 8 | ref_455) # MOV operation
ref_5996 = (ref_5988 & 0xFFFFFFFF) # MOV operation
ref_6020 = (ref_5996 & 0xFFFFFFFF) # MOV operation
ref_6034 = (ref_6020 & 0xFFFFFFFF) # MOV operation
ref_6036 = ref_5851 # MOV operation
ref_6038 = ((0x0 + ((0x0 + ((ref_6036 * 0x8) & 0xFFFFFFFFFFFFFFFF)) & 0xFFFFFFFFFFFFFFFF)) & 0xFFFFFFFFFFFFFFFF) # LEA operation
ref_6042 = ((0x8 + ref_6038) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_6050 = ref_6034 # MOV operation
ref_6052 = ref_6042 # MOV operation
ref_6106 = ref_6052 # MOV operation
ref_6118 = ref_6050 # MOV operation
ref_6130 = ref_6106 # MOV operation
ref_6132 = ref_6118 # MOV operation
ref_6134 = ref_6130 # MOV operation
ref_6136 = ref_6132 # MOV operation
ref_6162 = ref_6134 # MOV operation
ref_6164 = ref_6136 # MOV operation
ref_6166 = ref_6164 # MOV operation
ref_6200 = ref_6162 # MOV operation
ref_6202 = ref_6166 # MOV operation
ref_6204 = (ref_6202 ^ ref_6200) # XOR operation
ref_6211 = (((sx(0x40, ref_6204) * sx(0x40, ((((((((0x9D) << 8 | 0xDF) << 8 | 0xEA) << 8 | 0x8) << 8 | 0xEB) << 8 | 0x38) << 8 | 0x2D) << 8 | 0x69))) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_6225 = ref_6211 # MOV operation
ref_6227 = (ref_6225 >> (0x2F & 0x3F)) # SHR operation
ref_6249 = ref_6166 # MOV operation
ref_6251 = (ref_6249 ^ (ref_6211 ^ ref_6227)) # XOR operation
ref_6258 = (((sx(0x40, ref_6251) * sx(0x40, ((((((((0x9D) << 8 | 0xDF) << 8 | 0xEA) << 8 | 0x8) << 8 | 0xEB) << 8 | 0x38) << 8 | 0x2D) << 8 | 0x69))) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_6272 = ref_6258 # MOV operation
ref_6274 = (ref_6272 >> (0x2F & 0x3F)) # SHR operation
ref_6296 = (ref_6258 ^ ref_6274) # MOV operation
ref_6298 = (((sx(0x40, ref_6296) * sx(0x40, ((((((((0x9D) << 8 | 0xDF) << 8 | 0xEA) << 8 | 0x8) << 8 | 0xEB) << 8 | 0x38) << 8 | 0x2D) << 8 | 0x69))) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_6312 = ref_6298 # MOV operation
ref_6329 = ref_6312 # MOV operation
ref_6347 = ref_6329 # MOV operation
ref_6366 = ref_6347 # MOV operation
ref_6841 = ref_6366 # MOV operation
ref_7002 = ref_6841 # MOV operation
ref_7490 = ref_7002 # MOV operation
ref_7645 = ref_7490 # MOV operation
ref_7683 = ref_7645 # MOV operation
ref_7695 = ref_7683 # MOV operation
ref_7697 = ref_7695 # MOV operation

print ref_7697 & 0xffffffffffffffff
