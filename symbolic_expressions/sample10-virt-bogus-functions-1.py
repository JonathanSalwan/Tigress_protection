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
ref_9800 = ref_665 # MOV operation
ref_9812 = ref_9800 # MOV operation
ref_9840 = ref_9812 # MOV operation
ref_9853 = ref_9840 # MOV operation
ref_9866 = ref_9853 # MOV operation
ref_9868 = ref_9866 # MOV operation
ref_9918 = (((sx(0x40, 0xC2B2AE3D27D4EB4F) * sx(0x40, ref_9868)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_9952 = rol(0x1F, ((((((((((0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) + ref_9918) & 0xFFFFFFFFFFFFFFFF)) # MOV operation
ref_9954 = (((sx(0x40, 0x9E3779B185EBCA87) * sx(0x40, ref_9952)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_9968 = ref_9954 # MOV operation
ref_9985 = ref_9968 # MOV operation
ref_9997 = ref_9985 # MOV operation
ref_10014 = (((((((((0x27) << 8 | 0xD4) << 8 | 0xEB) << 8 | 0x2F) << 8 | 0x16) << 8 | 0x56) << 8 | 0x67) << 8 | 0xCD) ^ ref_9997) # MOV operation
ref_10016 = rol(0x1B, ref_10014) # ROL operation
ref_10020 = ref_10016 # MOV operation
ref_10024 = (((sx(0x40, ref_10020) * sx(0x40, 0x9E3779B185EBCA87)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_10030 = ((0x85EBCA77C2B2AE63 + ref_10024) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_10123 = ref_10030 # MOV operation
ref_10125 = (ref_10123 >> (0x21 & 0x3F)) # SHR operation
ref_10149 = (ref_10030 ^ ref_10125) # MOV operation
ref_10151 = (((sx(0x40, 0xC2B2AE3D27D4EB4F) * sx(0x40, ref_10149)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_10165 = ref_10151 # MOV operation
ref_10167 = (ref_10165 >> (0x1D & 0x3F)) # SHR operation
ref_10191 = (ref_10151 ^ ref_10167) # MOV operation
ref_10193 = (((sx(0x40, 0x165667B19E3779F9) * sx(0x40, ref_10191)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_10207 = ref_10193 # MOV operation
ref_10209 = (ref_10207 >> (0x20 & 0x3F)) # SHR operation
ref_10231 = (ref_10193 ^ ref_10209) # MOV operation
ref_10243 = ref_10231 # MOV operation
ref_11074 = ref_10243 # MOV operation
ref_11792 = ref_11074 # MOV operation
ref_12599 = ref_11792 # MOV operation
ref_13345 = ref_12599 # MOV operation
ref_14088 = ref_13345 # MOV operation
ref_14421 = ref_14088 # MOV operation
ref_15099 = ref_14421 # MOV operation
ref_16229 = ref_15099 # MOV operation
ref_16558 = ref_16229 # MOV operation
ref_16599 = ref_16558 # MOV operation
ref_16611 = ref_16599 # MOV operation
ref_16613 = ref_16611 # MOV operation

print ref_16613 & 0xffffffffffffffff
