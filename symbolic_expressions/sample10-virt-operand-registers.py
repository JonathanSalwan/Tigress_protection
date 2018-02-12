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
ref_6929 = ref_665 # MOV operation
ref_6941 = ref_6929 # MOV operation
ref_6969 = ref_6941 # MOV operation
ref_6982 = ref_6969 # MOV operation
ref_6995 = ref_6982 # MOV operation
ref_6997 = ref_6995 # MOV operation
ref_7047 = (((sx(0x40, 0xC2B2AE3D27D4EB4F) * sx(0x40, ref_6997)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_7081 = rol(0x1F, ((((((((((0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) + ref_7047) & 0xFFFFFFFFFFFFFFFF)) # MOV operation
ref_7083 = (((sx(0x40, 0x9E3779B185EBCA87) * sx(0x40, ref_7081)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_7097 = ref_7083 # MOV operation
ref_7114 = ref_7097 # MOV operation
ref_7126 = ref_7114 # MOV operation
ref_7143 = (((((((((0x27) << 8 | 0xD4) << 8 | 0xEB) << 8 | 0x2F) << 8 | 0x16) << 8 | 0x56) << 8 | 0x67) << 8 | 0xCD) ^ ref_7126) # MOV operation
ref_7145 = rol(0x1B, ref_7143) # ROL operation
ref_7149 = ref_7145 # MOV operation
ref_7153 = (((sx(0x40, ref_7149) * sx(0x40, 0x9E3779B185EBCA87)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_7159 = ((0x85EBCA77C2B2AE63 + ref_7153) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_7252 = ref_7159 # MOV operation
ref_7254 = (ref_7252 >> (0x21 & 0x3F)) # SHR operation
ref_7278 = (ref_7159 ^ ref_7254) # MOV operation
ref_7280 = (((sx(0x40, 0xC2B2AE3D27D4EB4F) * sx(0x40, ref_7278)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_7294 = ref_7280 # MOV operation
ref_7296 = (ref_7294 >> (0x1D & 0x3F)) # SHR operation
ref_7320 = (ref_7280 ^ ref_7296) # MOV operation
ref_7322 = (((sx(0x40, 0x165667B19E3779F9) * sx(0x40, ref_7320)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_7336 = ref_7322 # MOV operation
ref_7338 = (ref_7336 >> (0x20 & 0x3F)) # SHR operation
ref_7360 = (ref_7322 ^ ref_7338) # MOV operation
ref_7372 = ref_7360 # MOV operation
ref_7647 = ref_7372 # MOV operation
ref_7900 = ref_7647 # MOV operation
ref_8167 = ref_7900 # MOV operation
ref_8420 = ref_8167 # MOV operation
ref_8687 = ref_8420 # MOV operation
ref_8821 = ref_8687 # MOV operation
ref_9110 = ref_8821 # MOV operation
ref_9440 = ref_9110 # MOV operation
ref_9553 = ref_9440 # MOV operation
ref_9591 = ref_9553 # MOV operation
ref_9603 = ref_9591 # MOV operation
ref_9605 = ref_9603 # MOV operation

print ref_9605 & 0xffffffffffffffff
