#!/usr/bin/env python2
## -*- coding: utf-8 -*-

import sys

def sx(bits, value):
    sign_bit = 1 << (bits - 1)
    return (value & (sign_bit - 1)) - (value & sign_bit)

SymVar_0 = int(sys.argv[1])
ref_1210 = SymVar_0
ref_1221 = ref_1210 # MOV operation
ref_1233 = ref_1221 # MOV operation
ref_1235 = ref_1233 # MOV operation
ref_8679 = ref_1235 # MOV operation
ref_8691 = ref_8679 # MOV operation
ref_8719 = ref_8691 # MOV operation
ref_8732 = ref_8719 # MOV operation
ref_8745 = ref_8732 # MOV operation
ref_8747 = ref_8745 # MOV operation
ref_8797 = (((sx(0x40, 0xC2B2AE3D27D4EB4F) * sx(0x40, ref_8747)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_8831 = rol(0x1F, ((((((((((0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) + ref_8797) & 0xFFFFFFFFFFFFFFFF)) # MOV operation
ref_8833 = (((sx(0x40, 0x9E3779B185EBCA87) * sx(0x40, ref_8831)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_8847 = ref_8833 # MOV operation
ref_8864 = ref_8847 # MOV operation
ref_8876 = ref_8864 # MOV operation
ref_8893 = (((((((((0x27) << 8 | 0xD4) << 8 | 0xEB) << 8 | 0x2F) << 8 | 0x16) << 8 | 0x56) << 8 | 0x67) << 8 | 0xCD) ^ ref_8876) # MOV operation
ref_8895 = rol(0x1B, ref_8893) # ROL operation
ref_8899 = ref_8895 # MOV operation
ref_8903 = (((sx(0x40, ref_8899) * sx(0x40, 0x9E3779B185EBCA87)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_8909 = ((0x85EBCA77C2B2AE63 + ref_8903) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_9002 = ref_8909 # MOV operation
ref_9004 = (ref_9002 >> (0x21 & 0x3F)) # SHR operation
ref_9028 = (ref_8909 ^ ref_9004) # MOV operation
ref_9030 = (((sx(0x40, 0xC2B2AE3D27D4EB4F) * sx(0x40, ref_9028)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_9044 = ref_9030 # MOV operation
ref_9046 = (ref_9044 >> (0x1D & 0x3F)) # SHR operation
ref_9070 = (ref_9030 ^ ref_9046) # MOV operation
ref_9072 = (((sx(0x40, 0x165667B19E3779F9) * sx(0x40, ref_9070)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_9086 = ref_9072 # MOV operation
ref_9088 = (ref_9086 >> (0x20 & 0x3F)) # SHR operation
ref_9110 = (ref_9072 ^ ref_9088) # MOV operation
ref_9122 = ref_9110 # MOV operation
ref_9849 = ref_9122 # MOV operation
ref_10055 = ref_9849 # MOV operation
ref_10763 = ref_10055 # MOV operation
ref_10969 = ref_10763 # MOV operation
ref_11677 = ref_10969 # MOV operation
ref_11873 = ref_11677 # MOV operation
ref_12079 = ref_11873 # MOV operation
ref_12756 = ref_12079 # MOV operation
ref_12948 = ref_12756 # MOV operation
ref_12992 = ref_12948 # MOV operation
ref_13020 = ref_12992 # MOV operation
ref_13032 = ref_13020 # MOV operation
ref_13034 = ref_13032 # MOV operation

print ref_13034 & 0xffffffffffffffff
