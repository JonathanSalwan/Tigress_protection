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
ref_6937 = ref_665 # MOV operation
ref_6949 = ref_6937 # MOV operation
ref_6977 = ref_6949 # MOV operation
ref_6990 = ref_6977 # MOV operation
ref_7003 = ref_6990 # MOV operation
ref_7005 = ref_7003 # MOV operation
ref_7055 = (((sx(0x40, 0xC2B2AE3D27D4EB4F) * sx(0x40, ref_7005)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_7089 = rol(0x1F, ((((((((((0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) + ref_7055) & 0xFFFFFFFFFFFFFFFF)) # MOV operation
ref_7091 = (((sx(0x40, 0x9E3779B185EBCA87) * sx(0x40, ref_7089)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_7105 = ref_7091 # MOV operation
ref_7122 = ref_7105 # MOV operation
ref_7134 = ref_7122 # MOV operation
ref_7151 = (((((((((0x27) << 8 | 0xD4) << 8 | 0xEB) << 8 | 0x2F) << 8 | 0x16) << 8 | 0x56) << 8 | 0x67) << 8 | 0xCD) ^ ref_7134) # MOV operation
ref_7153 = rol(0x1B, ref_7151) # ROL operation
ref_7157 = ref_7153 # MOV operation
ref_7161 = (((sx(0x40, ref_7157) * sx(0x40, 0x9E3779B185EBCA87)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_7167 = ((0x85EBCA77C2B2AE63 + ref_7161) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_7260 = ref_7167 # MOV operation
ref_7262 = (ref_7260 >> (0x21 & 0x3F)) # SHR operation
ref_7286 = (ref_7167 ^ ref_7262) # MOV operation
ref_7288 = (((sx(0x40, 0xC2B2AE3D27D4EB4F) * sx(0x40, ref_7286)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_7302 = ref_7288 # MOV operation
ref_7304 = (ref_7302 >> (0x1D & 0x3F)) # SHR operation
ref_7328 = (ref_7288 ^ ref_7304) # MOV operation
ref_7330 = (((sx(0x40, 0x165667B19E3779F9) * sx(0x40, ref_7328)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_7344 = ref_7330 # MOV operation
ref_7346 = (ref_7344 >> (0x20 & 0x3F)) # SHR operation
ref_7368 = (ref_7330 ^ ref_7346) # MOV operation
ref_7380 = ref_7368 # MOV operation
ref_7651 = ref_7380 # MOV operation
ref_7884 = ref_7651 # MOV operation
ref_8147 = ref_7884 # MOV operation
ref_8380 = ref_8147 # MOV operation
ref_8795 = ref_8380 # MOV operation
ref_8893 = ref_8795 # MOV operation
ref_9010 = ref_8893 # MOV operation
ref_9336 = ref_9010 # MOV operation
ref_9423 = ref_9336 # MOV operation
ref_9461 = ref_9423 # MOV operation
ref_9473 = ref_9461 # MOV operation
ref_9475 = ref_9473 # MOV operation

print ref_9475 & 0xffffffffffffffff
