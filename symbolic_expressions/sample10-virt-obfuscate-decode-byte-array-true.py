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
ref_13346 = ref_665 # MOV operation
ref_13358 = ref_13346 # MOV operation
ref_13386 = ref_13358 # MOV operation
ref_13399 = ref_13386 # MOV operation
ref_13412 = ref_13399 # MOV operation
ref_13414 = ref_13412 # MOV operation
ref_13464 = (((sx(0x40, 0xC2B2AE3D27D4EB4F) * sx(0x40, ref_13414)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_13498 = rol(0x1F, ((((((((((0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) + ref_13464) & 0xFFFFFFFFFFFFFFFF)) # MOV operation
ref_13500 = (((sx(0x40, 0x9E3779B185EBCA87) * sx(0x40, ref_13498)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_13514 = ref_13500 # MOV operation
ref_13531 = ref_13514 # MOV operation
ref_13543 = ref_13531 # MOV operation
ref_13560 = (((((((((0x27) << 8 | 0xD4) << 8 | 0xEB) << 8 | 0x2F) << 8 | 0x16) << 8 | 0x56) << 8 | 0x67) << 8 | 0xCD) ^ ref_13543) # MOV operation
ref_13562 = rol(0x1B, ref_13560) # ROL operation
ref_13566 = ref_13562 # MOV operation
ref_13570 = (((sx(0x40, ref_13566) * sx(0x40, 0x9E3779B185EBCA87)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_13576 = ((0x85EBCA77C2B2AE63 + ref_13570) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_13669 = ref_13576 # MOV operation
ref_13671 = (ref_13669 >> (0x21 & 0x3F)) # SHR operation
ref_13695 = (ref_13576 ^ ref_13671) # MOV operation
ref_13697 = (((sx(0x40, 0xC2B2AE3D27D4EB4F) * sx(0x40, ref_13695)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_13711 = ref_13697 # MOV operation
ref_13713 = (ref_13711 >> (0x1D & 0x3F)) # SHR operation
ref_13737 = (ref_13697 ^ ref_13713) # MOV operation
ref_13739 = (((sx(0x40, 0x165667B19E3779F9) * sx(0x40, ref_13737)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_13753 = ref_13739 # MOV operation
ref_13755 = (ref_13753 >> (0x20 & 0x3F)) # SHR operation
ref_13777 = (ref_13739 ^ ref_13755) # MOV operation
ref_13789 = ref_13777 # MOV operation
ref_14203 = ref_13789 # MOV operation
ref_14266 = ref_14203 # MOV operation
ref_14672 = ref_14266 # MOV operation
ref_14735 = ref_14672 # MOV operation
ref_15141 = ref_14735 # MOV operation
ref_15248 = ref_15141 # MOV operation
ref_15329 = ref_15248 # MOV operation
ref_15691 = ref_15329 # MOV operation
ref_15778 = ref_15691 # MOV operation
ref_15816 = ref_15778 # MOV operation
ref_15828 = ref_15816 # MOV operation
ref_15830 = ref_15828 # MOV operation

print ref_15830 & 0xffffffffffffffff
