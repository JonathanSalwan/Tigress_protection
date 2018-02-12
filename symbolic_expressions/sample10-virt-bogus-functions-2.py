#!/usr/bin/env python2
## -*- coding: utf-8 -*-

import sys

def sx(bits, value):
    sign_bit = 1 << (bits - 1)
    return (value & (sign_bit - 1)) - (value & sign_bit)

SymVar_0 = int(sys.argv[1])
ref_640 = SymVar_0
ref_651 = ref_640 # MOV operation
ref_663 = ref_651 # MOV operation
ref_665 = ref_663 # MOV operation
ref_9948 = ref_665 # MOV operation
ref_9960 = ref_9948 # MOV operation
ref_9988 = ref_9960 # MOV operation
ref_10001 = ref_9988 # MOV operation
ref_10014 = ref_10001 # MOV operation
ref_10016 = ref_10014 # MOV operation
ref_10066 = (((sx(0x40, 0xC2B2AE3D27D4EB4F) * sx(0x40, ref_10016)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_10100 = rol(0x1F, ((((((((((0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) + ref_10066) & 0xFFFFFFFFFFFFFFFF)) # MOV operation
ref_10102 = (((sx(0x40, 0x9E3779B185EBCA87) * sx(0x40, ref_10100)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_10116 = ref_10102 # MOV operation
ref_10133 = ref_10116 # MOV operation
ref_10145 = ref_10133 # MOV operation
ref_10162 = (((((((((0x27) << 8 | 0xD4) << 8 | 0xEB) << 8 | 0x2F) << 8 | 0x16) << 8 | 0x56) << 8 | 0x67) << 8 | 0xCD) ^ ref_10145) # MOV operation
ref_10164 = rol(0x1B, ref_10162) # ROL operation
ref_10168 = ref_10164 # MOV operation
ref_10172 = (((sx(0x40, ref_10168) * sx(0x40, 0x9E3779B185EBCA87)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_10178 = ((0x85EBCA77C2B2AE63 + ref_10172) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_10271 = ref_10178 # MOV operation
ref_10273 = (ref_10271 >> (0x21 & 0x3F)) # SHR operation
ref_10297 = (ref_10178 ^ ref_10273) # MOV operation
ref_10299 = (((sx(0x40, 0xC2B2AE3D27D4EB4F) * sx(0x40, ref_10297)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_10313 = ref_10299 # MOV operation
ref_10315 = (ref_10313 >> (0x1D & 0x3F)) # SHR operation
ref_10339 = (ref_10299 ^ ref_10315) # MOV operation
ref_10341 = (((sx(0x40, 0x165667B19E3779F9) * sx(0x40, ref_10339)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_10355 = ref_10341 # MOV operation
ref_10357 = (ref_10355 >> (0x20 & 0x3F)) # SHR operation
ref_10379 = (ref_10341 ^ ref_10357) # MOV operation
ref_10391 = ref_10379 # MOV operation
ref_11703 = ref_10391 # MOV operation
ref_12093 = ref_11703 # MOV operation
ref_13137 = ref_12093 # MOV operation
ref_13511 = ref_13137 # MOV operation
ref_14283 = ref_13511 # MOV operation
ref_14613 = ref_14283 # MOV operation
ref_15373 = ref_14613 # MOV operation
ref_16495 = ref_15373 # MOV operation
ref_16841 = ref_16495 # MOV operation
ref_16882 = ref_16841 # MOV operation
ref_16894 = ref_16882 # MOV operation
ref_16896 = ref_16894 # MOV operation

print ref_16896 & 0xffffffffffffffff
