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
ref_7429 = ref_665 # MOV operation
ref_7441 = ref_7429 # MOV operation
ref_7469 = ref_7441 # MOV operation
ref_7482 = ref_7469 # MOV operation
ref_7495 = ref_7482 # MOV operation
ref_7497 = ref_7495 # MOV operation
ref_7547 = (((sx(0x40, 0xC2B2AE3D27D4EB4F) * sx(0x40, ref_7497)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_7581 = rol(0x1F, ((((((((((0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) + ref_7547) & 0xFFFFFFFFFFFFFFFF)) # MOV operation
ref_7583 = (((sx(0x40, 0x9E3779B185EBCA87) * sx(0x40, ref_7581)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_7597 = ref_7583 # MOV operation
ref_7614 = ref_7597 # MOV operation
ref_7626 = ref_7614 # MOV operation
ref_7643 = (((((((((0x27) << 8 | 0xD4) << 8 | 0xEB) << 8 | 0x2F) << 8 | 0x16) << 8 | 0x56) << 8 | 0x67) << 8 | 0xCD) ^ ref_7626) # MOV operation
ref_7645 = rol(0x1B, ref_7643) # ROL operation
ref_7649 = ref_7645 # MOV operation
ref_7653 = (((sx(0x40, ref_7649) * sx(0x40, 0x9E3779B185EBCA87)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_7659 = ((0x85EBCA77C2B2AE63 + ref_7653) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_7752 = ref_7659 # MOV operation
ref_7754 = (ref_7752 >> (0x21 & 0x3F)) # SHR operation
ref_7778 = (ref_7659 ^ ref_7754) # MOV operation
ref_7780 = (((sx(0x40, 0xC2B2AE3D27D4EB4F) * sx(0x40, ref_7778)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_7794 = ref_7780 # MOV operation
ref_7796 = (ref_7794 >> (0x1D & 0x3F)) # SHR operation
ref_7820 = (ref_7780 ^ ref_7796) # MOV operation
ref_7822 = (((sx(0x40, 0x165667B19E3779F9) * sx(0x40, ref_7820)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_7836 = ref_7822 # MOV operation
ref_7838 = (ref_7836 >> (0x20 & 0x3F)) # SHR operation
ref_7860 = (ref_7822 ^ ref_7838) # MOV operation
ref_7872 = ref_7860 # MOV operation
ref_8416 = ref_7872 # MOV operation
ref_8550 = ref_8416 # MOV operation
ref_9086 = ref_8550 # MOV operation
ref_9220 = ref_9086 # MOV operation
ref_9756 = ref_9220 # MOV operation
ref_9907 = ref_9756 # MOV operation
ref_10079 = ref_9907 # MOV operation
ref_10527 = ref_10079 # MOV operation
ref_10673 = ref_10527 # MOV operation
ref_10711 = ref_10673 # MOV operation
ref_10723 = ref_10711 # MOV operation
ref_10725 = ref_10723 # MOV operation

print ref_10725 & 0xffffffffffffffff
