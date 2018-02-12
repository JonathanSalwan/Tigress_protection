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
ref_12592 = ref_665 # MOV operation
ref_12604 = ref_12592 # MOV operation
ref_12632 = ref_12604 # MOV operation
ref_12645 = ref_12632 # MOV operation
ref_12658 = ref_12645 # MOV operation
ref_12660 = ref_12658 # MOV operation
ref_12710 = (((sx(0x40, 0xC2B2AE3D27D4EB4F) * sx(0x40, ref_12660)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_12744 = rol(0x1F, ((((((((((0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) + ref_12710) & 0xFFFFFFFFFFFFFFFF)) # MOV operation
ref_12746 = (((sx(0x40, 0x9E3779B185EBCA87) * sx(0x40, ref_12744)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_12760 = ref_12746 # MOV operation
ref_12777 = ref_12760 # MOV operation
ref_12789 = ref_12777 # MOV operation
ref_12806 = (((((((((0x27) << 8 | 0xD4) << 8 | 0xEB) << 8 | 0x2F) << 8 | 0x16) << 8 | 0x56) << 8 | 0x67) << 8 | 0xCD) ^ ref_12789) # MOV operation
ref_12808 = rol(0x1B, ref_12806) # ROL operation
ref_12812 = ref_12808 # MOV operation
ref_12816 = (((sx(0x40, ref_12812) * sx(0x40, 0x9E3779B185EBCA87)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_12822 = ((0x85EBCA77C2B2AE63 + ref_12816) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_12915 = ref_12822 # MOV operation
ref_12917 = (ref_12915 >> (0x21 & 0x3F)) # SHR operation
ref_12941 = (ref_12822 ^ ref_12917) # MOV operation
ref_12943 = (((sx(0x40, 0xC2B2AE3D27D4EB4F) * sx(0x40, ref_12941)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_12957 = ref_12943 # MOV operation
ref_12959 = (ref_12957 >> (0x1D & 0x3F)) # SHR operation
ref_12983 = (ref_12943 ^ ref_12959) # MOV operation
ref_12985 = (((sx(0x40, 0x165667B19E3779F9) * sx(0x40, ref_12983)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_12999 = ref_12985 # MOV operation
ref_13001 = (ref_12999 >> (0x20 & 0x3F)) # SHR operation
ref_13023 = (ref_12985 ^ ref_13001) # MOV operation
ref_13035 = ref_13023 # MOV operation
ref_14930 = ref_13035 # MOV operation
ref_15329 = ref_14930 # MOV operation
ref_17216 = ref_15329 # MOV operation
ref_17615 = ref_17216 # MOV operation
ref_19502 = ref_17615 # MOV operation
ref_20151 = ref_19502 # MOV operation
ref_20770 = ref_20151 # MOV operation
ref_22203 = ref_20770 # MOV operation
ref_22660 = ref_22203 # MOV operation
ref_22698 = ref_22660 # MOV operation
ref_22710 = ref_22698 # MOV operation
ref_22712 = ref_22710 # MOV operation

print ref_22712 & 0xffffffffffffffff
