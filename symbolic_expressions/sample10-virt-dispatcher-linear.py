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
ref_10916 = ref_665 # MOV operation
ref_10928 = ref_10916 # MOV operation
ref_10956 = ref_10928 # MOV operation
ref_10969 = ref_10956 # MOV operation
ref_10982 = ref_10969 # MOV operation
ref_10984 = ref_10982 # MOV operation
ref_11034 = (((sx(0x40, 0xC2B2AE3D27D4EB4F) * sx(0x40, ref_10984)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_11068 = rol(0x1F, ((((((((((0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) + ref_11034) & 0xFFFFFFFFFFFFFFFF)) # MOV operation
ref_11070 = (((sx(0x40, 0x9E3779B185EBCA87) * sx(0x40, ref_11068)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_11084 = ref_11070 # MOV operation
ref_11101 = ref_11084 # MOV operation
ref_11113 = ref_11101 # MOV operation
ref_11130 = (((((((((0x27) << 8 | 0xD4) << 8 | 0xEB) << 8 | 0x2F) << 8 | 0x16) << 8 | 0x56) << 8 | 0x67) << 8 | 0xCD) ^ ref_11113) # MOV operation
ref_11132 = rol(0x1B, ref_11130) # ROL operation
ref_11136 = ref_11132 # MOV operation
ref_11140 = (((sx(0x40, ref_11136) * sx(0x40, 0x9E3779B185EBCA87)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_11146 = ((0x85EBCA77C2B2AE63 + ref_11140) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_11239 = ref_11146 # MOV operation
ref_11241 = (ref_11239 >> (0x21 & 0x3F)) # SHR operation
ref_11265 = (ref_11146 ^ ref_11241) # MOV operation
ref_11267 = (((sx(0x40, 0xC2B2AE3D27D4EB4F) * sx(0x40, ref_11265)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_11281 = ref_11267 # MOV operation
ref_11283 = (ref_11281 >> (0x1D & 0x3F)) # SHR operation
ref_11307 = (ref_11267 ^ ref_11283) # MOV operation
ref_11309 = (((sx(0x40, 0x165667B19E3779F9) * sx(0x40, ref_11307)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_11323 = ref_11309 # MOV operation
ref_11325 = (ref_11323 >> (0x20 & 0x3F)) # SHR operation
ref_11347 = (ref_11309 ^ ref_11325) # MOV operation
ref_11359 = ref_11347 # MOV operation
ref_12386 = ref_11359 # MOV operation
ref_12623 = ref_12386 # MOV operation
ref_13642 = ref_12623 # MOV operation
ref_13879 = ref_13642 # MOV operation
ref_14898 = ref_13879 # MOV operation
ref_15073 = ref_14898 # MOV operation
ref_15726 = ref_15073 # MOV operation
ref_16961 = ref_15726 # MOV operation
ref_17654 = ref_16961 # MOV operation
ref_17692 = ref_17654 # MOV operation
ref_17704 = ref_17692 # MOV operation
ref_17706 = ref_17704 # MOV operation

print ref_17706 & 0xffffffffffffffff
