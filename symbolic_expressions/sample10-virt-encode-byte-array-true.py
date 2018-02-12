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
ref_11011 = ref_665 # MOV operation
ref_11023 = ref_11011 # MOV operation
ref_11051 = ref_11023 # MOV operation
ref_11064 = ref_11051 # MOV operation
ref_11077 = ref_11064 # MOV operation
ref_11079 = ref_11077 # MOV operation
ref_11129 = (((sx(0x40, 0xC2B2AE3D27D4EB4F) * sx(0x40, ref_11079)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_11163 = rol(0x1F, ((((((((((0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) + ref_11129) & 0xFFFFFFFFFFFFFFFF)) # MOV operation
ref_11165 = (((sx(0x40, 0x9E3779B185EBCA87) * sx(0x40, ref_11163)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_11179 = ref_11165 # MOV operation
ref_11196 = ref_11179 # MOV operation
ref_11208 = ref_11196 # MOV operation
ref_11225 = (((((((((0x27) << 8 | 0xD4) << 8 | 0xEB) << 8 | 0x2F) << 8 | 0x16) << 8 | 0x56) << 8 | 0x67) << 8 | 0xCD) ^ ref_11208) # MOV operation
ref_11227 = rol(0x1B, ref_11225) # ROL operation
ref_11231 = ref_11227 # MOV operation
ref_11235 = (((sx(0x40, ref_11231) * sx(0x40, 0x9E3779B185EBCA87)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_11241 = ((0x85EBCA77C2B2AE63 + ref_11235) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_11334 = ref_11241 # MOV operation
ref_11336 = (ref_11334 >> (0x21 & 0x3F)) # SHR operation
ref_11360 = (ref_11241 ^ ref_11336) # MOV operation
ref_11362 = (((sx(0x40, 0xC2B2AE3D27D4EB4F) * sx(0x40, ref_11360)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_11376 = ref_11362 # MOV operation
ref_11378 = (ref_11376 >> (0x1D & 0x3F)) # SHR operation
ref_11402 = (ref_11362 ^ ref_11378) # MOV operation
ref_11404 = (((sx(0x40, 0x165667B19E3779F9) * sx(0x40, ref_11402)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_11418 = ref_11404 # MOV operation
ref_11420 = (ref_11418 >> (0x20 & 0x3F)) # SHR operation
ref_11442 = (ref_11404 ^ ref_11420) # MOV operation
ref_11454 = ref_11442 # MOV operation
ref_11877 = ref_11454 # MOV operation
ref_11958 = ref_11877 # MOV operation
ref_12373 = ref_11958 # MOV operation
ref_12454 = ref_12373 # MOV operation
ref_12869 = ref_12454 # MOV operation
ref_12967 = ref_12869 # MOV operation
ref_13084 = ref_12967 # MOV operation
ref_13410 = ref_13084 # MOV operation
ref_13497 = ref_13410 # MOV operation
ref_13535 = ref_13497 # MOV operation
ref_13547 = ref_13535 # MOV operation
ref_13549 = ref_13547 # MOV operation

print ref_13549 & 0xffffffffffffffff
