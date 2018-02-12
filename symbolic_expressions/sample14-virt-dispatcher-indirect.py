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
ref_8769 = ((((ref_456) << 8 | ref_457) << 8 | ref_458) << 8 | ref_459) # MOV operation
ref_8777 = (ref_8769 & 0xFFFFFFFF) # MOV operation
ref_8801 = (ref_8777 & 0xFFFFFFFF) # MOV operation
ref_8815 = (ref_8801 & 0xFFFFFFFF) # MOV operation
ref_8952 = ((((ref_452) << 8 | ref_453) << 8 | ref_454) << 8 | ref_455) # MOV operation
ref_8960 = (ref_8952 & 0xFFFFFFFF) # MOV operation
ref_8984 = (ref_8960 & 0xFFFFFFFF) # MOV operation
ref_8998 = (ref_8984 & 0xFFFFFFFF) # MOV operation
ref_9000 = ref_8815 # MOV operation
ref_9002 = ((0x0 + ((0x0 + ((ref_9000 * 0x8) & 0xFFFFFFFFFFFFFFFF)) & 0xFFFFFFFFFFFFFFFF)) & 0xFFFFFFFFFFFFFFFF) # LEA operation
ref_9006 = ((0x8 + ref_9002) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_9014 = ref_8998 # MOV operation
ref_9016 = ref_9006 # MOV operation
ref_9070 = ref_9016 # MOV operation
ref_9082 = ref_9014 # MOV operation
ref_9094 = ref_9070 # MOV operation
ref_9096 = ref_9082 # MOV operation
ref_9098 = ref_9094 # MOV operation
ref_9100 = ref_9096 # MOV operation
ref_9126 = ref_9098 # MOV operation
ref_9128 = ref_9100 # MOV operation
ref_9130 = ref_9128 # MOV operation
ref_9164 = ref_9126 # MOV operation
ref_9166 = ref_9130 # MOV operation
ref_9168 = (ref_9166 ^ ref_9164) # XOR operation
ref_9175 = (((sx(0x40, ref_9168) * sx(0x40, ((((((((0x9D) << 8 | 0xDF) << 8 | 0xEA) << 8 | 0x8) << 8 | 0xEB) << 8 | 0x38) << 8 | 0x2D) << 8 | 0x69))) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_9189 = ref_9175 # MOV operation
ref_9191 = (ref_9189 >> (0x2F & 0x3F)) # SHR operation
ref_9213 = ref_9130 # MOV operation
ref_9215 = (ref_9213 ^ (ref_9175 ^ ref_9191)) # XOR operation
ref_9222 = (((sx(0x40, ref_9215) * sx(0x40, ((((((((0x9D) << 8 | 0xDF) << 8 | 0xEA) << 8 | 0x8) << 8 | 0xEB) << 8 | 0x38) << 8 | 0x2D) << 8 | 0x69))) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_9236 = ref_9222 # MOV operation
ref_9238 = (ref_9236 >> (0x2F & 0x3F)) # SHR operation
ref_9260 = (ref_9222 ^ ref_9238) # MOV operation
ref_9262 = (((sx(0x40, ref_9260) * sx(0x40, ((((((((0x9D) << 8 | 0xDF) << 8 | 0xEA) << 8 | 0x8) << 8 | 0xEB) << 8 | 0x38) << 8 | 0x2D) << 8 | 0x69))) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_9276 = ref_9262 # MOV operation
ref_9293 = ref_9276 # MOV operation
ref_9311 = ref_9293 # MOV operation
ref_9330 = ref_9311 # MOV operation
ref_9612 = ref_9330 # MOV operation
ref_9670 = ref_9612 # MOV operation
ref_9900 = ref_9670 # MOV operation
ref_9946 = ref_9900 # MOV operation
ref_9984 = ref_9946 # MOV operation
ref_9996 = ref_9984 # MOV operation
ref_9998 = ref_9996 # MOV operation

print ref_9998 & 0xffffffffffffffff
