#!/usr/bin/env python2
## -*- coding: utf-8 -*-

import sys

def sx(bits, value):
    sign_bit = 1 << (bits - 1)
    return (value & (sign_bit - 1)) - (value & sign_bit)

SymVar_0 = int(sys.argv[1])
ref_646 = SymVar_0
ref_657 = ref_646 # MOV operation
ref_669 = ref_657 # MOV operation
ref_671 = ref_669 # MOV operation
ref_14514 = ref_671 # MOV operation
ref_14526 = ref_14514 # MOV operation
ref_14554 = ref_14526 # MOV operation
ref_14567 = ref_14554 # MOV operation
ref_14580 = ref_14567 # MOV operation
ref_14582 = ref_14580 # MOV operation
ref_14632 = (((sx(0x40, 0xC2B2AE3D27D4EB4F) * sx(0x40, ref_14582)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_14666 = rol(0x1F, ((((((((((0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) + ref_14632) & 0xFFFFFFFFFFFFFFFF)) # MOV operation
ref_14668 = (((sx(0x40, 0x9E3779B185EBCA87) * sx(0x40, ref_14666)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_14682 = ref_14668 # MOV operation
ref_14699 = ref_14682 # MOV operation
ref_14711 = ref_14699 # MOV operation
ref_14728 = (((((((((0x27) << 8 | 0xD4) << 8 | 0xEB) << 8 | 0x2F) << 8 | 0x16) << 8 | 0x56) << 8 | 0x67) << 8 | 0xCD) ^ ref_14711) # MOV operation
ref_14730 = rol(0x1B, ref_14728) # ROL operation
ref_14734 = ref_14730 # MOV operation
ref_14738 = (((sx(0x40, ref_14734) * sx(0x40, 0x9E3779B185EBCA87)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_14744 = ((0x85EBCA77C2B2AE63 + ref_14738) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_14837 = ref_14744 # MOV operation
ref_14839 = (ref_14837 >> (0x21 & 0x3F)) # SHR operation
ref_14863 = (ref_14744 ^ ref_14839) # MOV operation
ref_14865 = (((sx(0x40, 0xC2B2AE3D27D4EB4F) * sx(0x40, ref_14863)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_14879 = ref_14865 # MOV operation
ref_14881 = (ref_14879 >> (0x1D & 0x3F)) # SHR operation
ref_14905 = (ref_14865 ^ ref_14881) # MOV operation
ref_14907 = (((sx(0x40, 0x165667B19E3779F9) * sx(0x40, ref_14905)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_14921 = ref_14907 # MOV operation
ref_14923 = (ref_14921 >> (0x20 & 0x3F)) # SHR operation
ref_14945 = (ref_14907 ^ ref_14923) # MOV operation
ref_14957 = ref_14945 # MOV operation
ref_16409 = ref_14957 # MOV operation
ref_16825 = ref_16409 # MOV operation
ref_18164 = ref_16825 # MOV operation
ref_18580 = ref_18164 # MOV operation
ref_19919 = ref_18580 # MOV operation
ref_20326 = ref_19919 # MOV operation
ref_20751 = ref_20326 # MOV operation
ref_22137 = ref_20751 # MOV operation
ref_22529 = ref_22137 # MOV operation
ref_22568 = ref_22529 # MOV operation
ref_22580 = ref_22568 # MOV operation
ref_22582 = ref_22580 # MOV operation

print ref_22582 & 0xffffffffffffffff
