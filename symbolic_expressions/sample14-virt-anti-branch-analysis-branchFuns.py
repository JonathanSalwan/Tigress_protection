#!/usr/bin/env python2
## -*- coding: utf-8 -*-

import sys

def sx(bits, value):
    sign_bit = 1 << (bits - 1)
    return (value & (sign_bit - 1)) - (value & sign_bit)

SymVar_0 = int(sys.argv[1])
ref_388 = SymVar_0
ref_399 = ref_388 # MOV operation
ref_411 = ref_399 # MOV operation
ref_413 = ref_411 # MOV operation
ref_458 = ((ref_413 >> 56) & 0xFF) # Byte reference - MOV operation
ref_459 = ((ref_413 >> 48) & 0xFF) # Byte reference - MOV operation
ref_460 = ((ref_413 >> 40) & 0xFF) # Byte reference - MOV operation
ref_461 = ((ref_413 >> 32) & 0xFF) # Byte reference - MOV operation
ref_462 = ((ref_413 >> 24) & 0xFF) # Byte reference - MOV operation
ref_463 = ((ref_413 >> 16) & 0xFF) # Byte reference - MOV operation
ref_464 = ((ref_413 >> 8) & 0xFF) # Byte reference - MOV operation
ref_465 = (ref_413 & 0xFF) # Byte reference - MOV operation
ref_10668 = ((((ref_462) << 8 | ref_463) << 8 | ref_464) << 8 | ref_465) # MOV operation
ref_10676 = (ref_10668 & 0xFFFFFFFF) # MOV operation
ref_10700 = (ref_10676 & 0xFFFFFFFF) # MOV operation
ref_10714 = (ref_10700 & 0xFFFFFFFF) # MOV operation
ref_10851 = ((((ref_458) << 8 | ref_459) << 8 | ref_460) << 8 | ref_461) # MOV operation
ref_10859 = (ref_10851 & 0xFFFFFFFF) # MOV operation
ref_10883 = (ref_10859 & 0xFFFFFFFF) # MOV operation
ref_10897 = (ref_10883 & 0xFFFFFFFF) # MOV operation
ref_10899 = ref_10714 # MOV operation
ref_10901 = ((0x0 + ((0x0 + ((ref_10899 * 0x8) & 0xFFFFFFFFFFFFFFFF)) & 0xFFFFFFFFFFFFFFFF)) & 0xFFFFFFFFFFFFFFFF) # LEA operation
ref_10905 = ((0x8 + ref_10901) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_10913 = ref_10897 # MOV operation
ref_10915 = ref_10905 # MOV operation
ref_10969 = ref_10915 # MOV operation
ref_10981 = ref_10913 # MOV operation
ref_10993 = ref_10969 # MOV operation
ref_10995 = ref_10981 # MOV operation
ref_10997 = ref_10993 # MOV operation
ref_10999 = ref_10995 # MOV operation
ref_11025 = ref_10997 # MOV operation
ref_11027 = ref_10999 # MOV operation
ref_11029 = ref_11027 # MOV operation
ref_11063 = ref_11025 # MOV operation
ref_11065 = ref_11029 # MOV operation
ref_11067 = (ref_11065 ^ ref_11063) # XOR operation
ref_11074 = (((sx(0x40, ref_11067) * sx(0x40, ((((((((0x9D) << 8 | 0xDF) << 8 | 0xEA) << 8 | 0x8) << 8 | 0xEB) << 8 | 0x38) << 8 | 0x2D) << 8 | 0x69))) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_11088 = ref_11074 # MOV operation
ref_11090 = (ref_11088 >> (0x2F & 0x3F)) # SHR operation
ref_11112 = ref_11029 # MOV operation
ref_11114 = (ref_11112 ^ (ref_11074 ^ ref_11090)) # XOR operation
ref_11121 = (((sx(0x40, ref_11114) * sx(0x40, ((((((((0x9D) << 8 | 0xDF) << 8 | 0xEA) << 8 | 0x8) << 8 | 0xEB) << 8 | 0x38) << 8 | 0x2D) << 8 | 0x69))) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_11135 = ref_11121 # MOV operation
ref_11137 = (ref_11135 >> (0x2F & 0x3F)) # SHR operation
ref_11159 = (ref_11121 ^ ref_11137) # MOV operation
ref_11161 = (((sx(0x40, ref_11159) * sx(0x40, ((((((((0x9D) << 8 | 0xDF) << 8 | 0xEA) << 8 | 0x8) << 8 | 0xEB) << 8 | 0x38) << 8 | 0x2D) << 8 | 0x69))) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_11175 = ref_11161 # MOV operation
ref_11192 = ref_11175 # MOV operation
ref_11210 = ref_11192 # MOV operation
ref_11229 = ref_11210 # MOV operation
ref_12456 = ref_11229 # MOV operation
ref_12819 = ref_12456 # MOV operation
ref_14064 = ref_12819 # MOV operation
ref_14459 = ref_14064 # MOV operation
ref_14498 = ref_14459 # MOV operation
ref_14510 = ref_14498 # MOV operation
ref_14512 = ref_14510 # MOV operation

print ref_14512 & 0xffffffffffffffff
