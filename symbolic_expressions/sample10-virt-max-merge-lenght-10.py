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
ref_6214 = ref_665 # MOV operation
ref_6226 = ref_6214 # MOV operation
ref_6254 = ref_6226 # MOV operation
ref_6267 = ref_6254 # MOV operation
ref_6280 = ref_6267 # MOV operation
ref_6282 = ref_6280 # MOV operation
ref_6332 = (((sx(0x40, 0xC2B2AE3D27D4EB4F) * sx(0x40, ref_6282)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_6366 = rol(0x1F, ((((((((((0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) + ref_6332) & 0xFFFFFFFFFFFFFFFF)) # MOV operation
ref_6368 = (((sx(0x40, 0x9E3779B185EBCA87) * sx(0x40, ref_6366)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_6382 = ref_6368 # MOV operation
ref_6399 = ref_6382 # MOV operation
ref_6411 = ref_6399 # MOV operation
ref_6428 = (((((((((0x27) << 8 | 0xD4) << 8 | 0xEB) << 8 | 0x2F) << 8 | 0x16) << 8 | 0x56) << 8 | 0x67) << 8 | 0xCD) ^ ref_6411) # MOV operation
ref_6430 = rol(0x1B, ref_6428) # ROL operation
ref_6434 = ref_6430 # MOV operation
ref_6438 = (((sx(0x40, ref_6434) * sx(0x40, 0x9E3779B185EBCA87)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_6444 = ((0x85EBCA77C2B2AE63 + ref_6438) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_6537 = ref_6444 # MOV operation
ref_6539 = (ref_6537 >> (0x21 & 0x3F)) # SHR operation
ref_6563 = (ref_6444 ^ ref_6539) # MOV operation
ref_6565 = (((sx(0x40, 0xC2B2AE3D27D4EB4F) * sx(0x40, ref_6563)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_6579 = ref_6565 # MOV operation
ref_6581 = (ref_6579 >> (0x1D & 0x3F)) # SHR operation
ref_6605 = (ref_6565 ^ ref_6581) # MOV operation
ref_6607 = (((sx(0x40, 0x165667B19E3779F9) * sx(0x40, ref_6605)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_6621 = ref_6607 # MOV operation
ref_6623 = (ref_6621 >> (0x20 & 0x3F)) # SHR operation
ref_6645 = (ref_6607 ^ ref_6623) # MOV operation
ref_6657 = ref_6645 # MOV operation
ref_6869 = ref_6657 # MOV operation
ref_6903 = ref_6869 # MOV operation
ref_7019 = ref_6903 # MOV operation
ref_7053 = ref_7019 # MOV operation
ref_7212 = ref_7053 # MOV operation
ref_7238 = ref_7212 # MOV operation
ref_7272 = ref_7238 # MOV operation
ref_7522 = ref_7272 # MOV operation
ref_7649 = ref_7522 # MOV operation
ref_7687 = ref_7649 # MOV operation
ref_7699 = ref_7687 # MOV operation
ref_7701 = ref_7699 # MOV operation

print ref_7701 & 0xffffffffffffffff
