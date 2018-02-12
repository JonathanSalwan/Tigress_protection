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
ref_9803 = ((((ref_456) << 8 | ref_457) << 8 | ref_458) << 8 | ref_459) # MOV operation
ref_9811 = (ref_9803 & 0xFFFFFFFF) # MOV operation
ref_9835 = (ref_9811 & 0xFFFFFFFF) # MOV operation
ref_9849 = (ref_9835 & 0xFFFFFFFF) # MOV operation
ref_9986 = ((((ref_452) << 8 | ref_453) << 8 | ref_454) << 8 | ref_455) # MOV operation
ref_9994 = (ref_9986 & 0xFFFFFFFF) # MOV operation
ref_10018 = (ref_9994 & 0xFFFFFFFF) # MOV operation
ref_10032 = (ref_10018 & 0xFFFFFFFF) # MOV operation
ref_10034 = ref_9849 # MOV operation
ref_10036 = ((0x0 + ((0x0 + ((ref_10034 * 0x8) & 0xFFFFFFFFFFFFFFFF)) & 0xFFFFFFFFFFFFFFFF)) & 0xFFFFFFFFFFFFFFFF) # LEA operation
ref_10040 = ((0x8 + ref_10036) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_10048 = ref_10032 # MOV operation
ref_10050 = ref_10040 # MOV operation
ref_10104 = ref_10050 # MOV operation
ref_10116 = ref_10048 # MOV operation
ref_10128 = ref_10104 # MOV operation
ref_10130 = ref_10116 # MOV operation
ref_10132 = ref_10128 # MOV operation
ref_10134 = ref_10130 # MOV operation
ref_10160 = ref_10132 # MOV operation
ref_10162 = ref_10134 # MOV operation
ref_10164 = ref_10162 # MOV operation
ref_10198 = ref_10160 # MOV operation
ref_10200 = ref_10164 # MOV operation
ref_10202 = (ref_10200 ^ ref_10198) # XOR operation
ref_10209 = (((sx(0x40, ref_10202) * sx(0x40, ((((((((0x9D) << 8 | 0xDF) << 8 | 0xEA) << 8 | 0x8) << 8 | 0xEB) << 8 | 0x38) << 8 | 0x2D) << 8 | 0x69))) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_10223 = ref_10209 # MOV operation
ref_10225 = (ref_10223 >> (0x2F & 0x3F)) # SHR operation
ref_10247 = ref_10164 # MOV operation
ref_10249 = (ref_10247 ^ (ref_10209 ^ ref_10225)) # XOR operation
ref_10256 = (((sx(0x40, ref_10249) * sx(0x40, ((((((((0x9D) << 8 | 0xDF) << 8 | 0xEA) << 8 | 0x8) << 8 | 0xEB) << 8 | 0x38) << 8 | 0x2D) << 8 | 0x69))) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_10270 = ref_10256 # MOV operation
ref_10272 = (ref_10270 >> (0x2F & 0x3F)) # SHR operation
ref_10294 = (ref_10256 ^ ref_10272) # MOV operation
ref_10296 = (((sx(0x40, ref_10294) * sx(0x40, ((((((((0x9D) << 8 | 0xDF) << 8 | 0xEA) << 8 | 0x8) << 8 | 0xEB) << 8 | 0x38) << 8 | 0x2D) << 8 | 0x69))) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_10310 = ref_10296 # MOV operation
ref_10327 = ref_10310 # MOV operation
ref_10345 = ref_10327 # MOV operation
ref_10364 = ref_10345 # MOV operation
ref_10706 = ref_10364 # MOV operation
ref_10805 = ref_10706 # MOV operation
ref_11131 = ref_10805 # MOV operation
ref_11218 = ref_11131 # MOV operation
ref_11256 = ref_11218 # MOV operation
ref_11268 = ref_11256 # MOV operation
ref_11270 = ref_11268 # MOV operation

print ref_11270 & 0xffffffffffffffff
