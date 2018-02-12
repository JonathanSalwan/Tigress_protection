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
ref_6903 = ref_665 # MOV operation
ref_6915 = ref_6903 # MOV operation
ref_6943 = ref_6915 # MOV operation
ref_6956 = ref_6943 # MOV operation
ref_6969 = ref_6956 # MOV operation
ref_6971 = ref_6969 # MOV operation
ref_7021 = (((sx(0x40, 0xC2B2AE3D27D4EB4F) * sx(0x40, ref_6971)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_7055 = rol(0x1F, ((((((((((0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) + ref_7021) & 0xFFFFFFFFFFFFFFFF)) # MOV operation
ref_7057 = (((sx(0x40, 0x9E3779B185EBCA87) * sx(0x40, ref_7055)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_7071 = ref_7057 # MOV operation
ref_7088 = ref_7071 # MOV operation
ref_7100 = ref_7088 # MOV operation
ref_7117 = (((((((((0x27) << 8 | 0xD4) << 8 | 0xEB) << 8 | 0x2F) << 8 | 0x16) << 8 | 0x56) << 8 | 0x67) << 8 | 0xCD) ^ ref_7100) # MOV operation
ref_7119 = rol(0x1B, ref_7117) # ROL operation
ref_7123 = ref_7119 # MOV operation
ref_7127 = (((sx(0x40, ref_7123) * sx(0x40, 0x9E3779B185EBCA87)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_7133 = ((0x85EBCA77C2B2AE63 + ref_7127) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_7226 = ref_7133 # MOV operation
ref_7228 = (ref_7226 >> (0x21 & 0x3F)) # SHR operation
ref_7252 = (ref_7133 ^ ref_7228) # MOV operation
ref_7254 = (((sx(0x40, 0xC2B2AE3D27D4EB4F) * sx(0x40, ref_7252)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_7268 = ref_7254 # MOV operation
ref_7270 = (ref_7268 >> (0x1D & 0x3F)) # SHR operation
ref_7294 = (ref_7254 ^ ref_7270) # MOV operation
ref_7296 = (((sx(0x40, 0x165667B19E3779F9) * sx(0x40, ref_7294)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_7310 = ref_7296 # MOV operation
ref_7312 = (ref_7310 >> (0x20 & 0x3F)) # SHR operation
ref_7334 = (ref_7296 ^ ref_7312) # MOV operation
ref_7346 = ref_7334 # MOV operation
ref_7610 = ref_7346 # MOV operation
ref_7662 = ref_7610 # MOV operation
ref_7918 = ref_7662 # MOV operation
ref_7970 = ref_7918 # MOV operation
ref_8226 = ref_7970 # MOV operation
ref_8268 = ref_8226 # MOV operation
ref_8320 = ref_8268 # MOV operation
ref_8539 = ref_8320 # MOV operation
ref_8579 = ref_8539 # MOV operation
ref_8617 = ref_8579 # MOV operation
ref_8629 = ref_8617 # MOV operation
ref_8631 = ref_8629 # MOV operation

print ref_8631 & 0xffffffffffffffff
