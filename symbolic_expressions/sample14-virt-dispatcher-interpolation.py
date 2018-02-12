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
ref_7879 = ((((ref_456) << 8 | ref_457) << 8 | ref_458) << 8 | ref_459) # MOV operation
ref_7887 = (ref_7879 & 0xFFFFFFFF) # MOV operation
ref_7911 = (ref_7887 & 0xFFFFFFFF) # MOV operation
ref_7925 = (ref_7911 & 0xFFFFFFFF) # MOV operation
ref_8062 = ((((ref_452) << 8 | ref_453) << 8 | ref_454) << 8 | ref_455) # MOV operation
ref_8070 = (ref_8062 & 0xFFFFFFFF) # MOV operation
ref_8094 = (ref_8070 & 0xFFFFFFFF) # MOV operation
ref_8108 = (ref_8094 & 0xFFFFFFFF) # MOV operation
ref_8110 = ref_7925 # MOV operation
ref_8112 = ((0x0 + ((0x0 + ((ref_8110 * 0x8) & 0xFFFFFFFFFFFFFFFF)) & 0xFFFFFFFFFFFFFFFF)) & 0xFFFFFFFFFFFFFFFF) # LEA operation
ref_8116 = ((0x8 + ref_8112) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_8124 = ref_8108 # MOV operation
ref_8126 = ref_8116 # MOV operation
ref_8180 = ref_8126 # MOV operation
ref_8192 = ref_8124 # MOV operation
ref_8204 = ref_8180 # MOV operation
ref_8206 = ref_8192 # MOV operation
ref_8208 = ref_8204 # MOV operation
ref_8210 = ref_8206 # MOV operation
ref_8236 = ref_8208 # MOV operation
ref_8238 = ref_8210 # MOV operation
ref_8240 = ref_8238 # MOV operation
ref_8274 = ref_8236 # MOV operation
ref_8276 = ref_8240 # MOV operation
ref_8278 = (ref_8276 ^ ref_8274) # XOR operation
ref_8285 = (((sx(0x40, ref_8278) * sx(0x40, ((((((((0x9D) << 8 | 0xDF) << 8 | 0xEA) << 8 | 0x8) << 8 | 0xEB) << 8 | 0x38) << 8 | 0x2D) << 8 | 0x69))) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_8299 = ref_8285 # MOV operation
ref_8301 = (ref_8299 >> (0x2F & 0x3F)) # SHR operation
ref_8323 = ref_8240 # MOV operation
ref_8325 = (ref_8323 ^ (ref_8285 ^ ref_8301)) # XOR operation
ref_8332 = (((sx(0x40, ref_8325) * sx(0x40, ((((((((0x9D) << 8 | 0xDF) << 8 | 0xEA) << 8 | 0x8) << 8 | 0xEB) << 8 | 0x38) << 8 | 0x2D) << 8 | 0x69))) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_8346 = ref_8332 # MOV operation
ref_8348 = (ref_8346 >> (0x2F & 0x3F)) # SHR operation
ref_8370 = (ref_8332 ^ ref_8348) # MOV operation
ref_8372 = (((sx(0x40, ref_8370) * sx(0x40, ((((((((0x9D) << 8 | 0xDF) << 8 | 0xEA) << 8 | 0x8) << 8 | 0xEB) << 8 | 0x38) << 8 | 0x2D) << 8 | 0x69))) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_8386 = ref_8372 # MOV operation
ref_8403 = ref_8386 # MOV operation
ref_8421 = ref_8403 # MOV operation
ref_8440 = ref_8421 # MOV operation
ref_10090 = ref_8440 # MOV operation
ref_10454 = ref_10090 # MOV operation
ref_11827 = ref_10454 # MOV operation
ref_12179 = ref_11827 # MOV operation
ref_12217 = ref_12179 # MOV operation
ref_12229 = ref_12217 # MOV operation
ref_12231 = ref_12229 # MOV operation

print ref_12231 & 0xffffffffffffffff
