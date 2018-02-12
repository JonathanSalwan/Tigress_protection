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
ref_6160 = ref_665 # MOV operation
ref_6172 = ref_6160 # MOV operation
ref_6200 = ref_6172 # MOV operation
ref_6213 = ref_6200 # MOV operation
ref_6226 = ref_6213 # MOV operation
ref_6228 = ref_6226 # MOV operation
ref_6278 = (((sx(0x40, 0xC2B2AE3D27D4EB4F) * sx(0x40, ref_6228)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_6312 = rol(0x1F, ((((((((((0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) + ref_6278) & 0xFFFFFFFFFFFFFFFF)) # MOV operation
ref_6314 = (((sx(0x40, 0x9E3779B185EBCA87) * sx(0x40, ref_6312)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_6328 = ref_6314 # MOV operation
ref_6345 = ref_6328 # MOV operation
ref_6357 = ref_6345 # MOV operation
ref_6374 = (((((((((0x27) << 8 | 0xD4) << 8 | 0xEB) << 8 | 0x2F) << 8 | 0x16) << 8 | 0x56) << 8 | 0x67) << 8 | 0xCD) ^ ref_6357) # MOV operation
ref_6376 = rol(0x1B, ref_6374) # ROL operation
ref_6380 = ref_6376 # MOV operation
ref_6384 = (((sx(0x40, ref_6380) * sx(0x40, 0x9E3779B185EBCA87)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_6390 = ((0x85EBCA77C2B2AE63 + ref_6384) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_6483 = ref_6390 # MOV operation
ref_6485 = (ref_6483 >> (0x21 & 0x3F)) # SHR operation
ref_6509 = (ref_6390 ^ ref_6485) # MOV operation
ref_6511 = (((sx(0x40, 0xC2B2AE3D27D4EB4F) * sx(0x40, ref_6509)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_6525 = ref_6511 # MOV operation
ref_6527 = (ref_6525 >> (0x1D & 0x3F)) # SHR operation
ref_6551 = (ref_6511 ^ ref_6527) # MOV operation
ref_6553 = (((sx(0x40, 0x165667B19E3779F9) * sx(0x40, ref_6551)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_6567 = ref_6553 # MOV operation
ref_6569 = (ref_6567 >> (0x20 & 0x3F)) # SHR operation
ref_6591 = (ref_6553 ^ ref_6569) # MOV operation
ref_6603 = ref_6591 # MOV operation
ref_6806 = ref_6603 # MOV operation
ref_6840 = ref_6806 # MOV operation
ref_6956 = ref_6840 # MOV operation
ref_6990 = ref_6956 # MOV operation
ref_7106 = ref_6990 # MOV operation
ref_7132 = ref_7106 # MOV operation
ref_7166 = ref_7132 # MOV operation
ref_7425 = ref_7166 # MOV operation
ref_7561 = ref_7425 # MOV operation
ref_7599 = ref_7561 # MOV operation
ref_7611 = ref_7599 # MOV operation
ref_7613 = ref_7611 # MOV operation

print ref_7613 & 0xffffffffffffffff
