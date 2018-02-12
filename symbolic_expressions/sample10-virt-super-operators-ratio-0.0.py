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
ref_6901 = ref_665 # MOV operation
ref_6913 = ref_6901 # MOV operation
ref_6941 = ref_6913 # MOV operation
ref_6954 = ref_6941 # MOV operation
ref_6967 = ref_6954 # MOV operation
ref_6969 = ref_6967 # MOV operation
ref_7019 = (((sx(0x40, 0xC2B2AE3D27D4EB4F) * sx(0x40, ref_6969)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_7053 = rol(0x1F, ((((((((((0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) + ref_7019) & 0xFFFFFFFFFFFFFFFF)) # MOV operation
ref_7055 = (((sx(0x40, 0x9E3779B185EBCA87) * sx(0x40, ref_7053)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_7069 = ref_7055 # MOV operation
ref_7086 = ref_7069 # MOV operation
ref_7098 = ref_7086 # MOV operation
ref_7115 = (((((((((0x27) << 8 | 0xD4) << 8 | 0xEB) << 8 | 0x2F) << 8 | 0x16) << 8 | 0x56) << 8 | 0x67) << 8 | 0xCD) ^ ref_7098) # MOV operation
ref_7117 = rol(0x1B, ref_7115) # ROL operation
ref_7121 = ref_7117 # MOV operation
ref_7125 = (((sx(0x40, ref_7121) * sx(0x40, 0x9E3779B185EBCA87)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_7131 = ((0x85EBCA77C2B2AE63 + ref_7125) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_7224 = ref_7131 # MOV operation
ref_7226 = (ref_7224 >> (0x21 & 0x3F)) # SHR operation
ref_7250 = (ref_7131 ^ ref_7226) # MOV operation
ref_7252 = (((sx(0x40, 0xC2B2AE3D27D4EB4F) * sx(0x40, ref_7250)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_7266 = ref_7252 # MOV operation
ref_7268 = (ref_7266 >> (0x1D & 0x3F)) # SHR operation
ref_7292 = (ref_7252 ^ ref_7268) # MOV operation
ref_7294 = (((sx(0x40, 0x165667B19E3779F9) * sx(0x40, ref_7292)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_7308 = ref_7294 # MOV operation
ref_7310 = (ref_7308 >> (0x20 & 0x3F)) # SHR operation
ref_7332 = (ref_7294 ^ ref_7310) # MOV operation
ref_7344 = ref_7332 # MOV operation
ref_7767 = ref_7344 # MOV operation
ref_7848 = ref_7767 # MOV operation
ref_8263 = ref_7848 # MOV operation
ref_8344 = ref_8263 # MOV operation
ref_8759 = ref_8344 # MOV operation
ref_8857 = ref_8759 # MOV operation
ref_8974 = ref_8857 # MOV operation
ref_9354 = ref_8974 # MOV operation
ref_9441 = ref_9354 # MOV operation
ref_9479 = ref_9441 # MOV operation
ref_9491 = ref_9479 # MOV operation
ref_9493 = ref_9491 # MOV operation

print ref_9493 & 0xffffffffffffffff
