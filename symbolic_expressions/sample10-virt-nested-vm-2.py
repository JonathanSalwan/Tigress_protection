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
ref_150924 = ref_665 # MOV operation
ref_150936 = ref_150924 # MOV operation
ref_150964 = ref_150936 # MOV operation
ref_150977 = ref_150964 # MOV operation
ref_150990 = ref_150977 # MOV operation
ref_150992 = ref_150990 # MOV operation
ref_151042 = (((sx(0x40, 0xC2B2AE3D27D4EB4F) * sx(0x40, ref_150992)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_151076 = rol(0x1F, ((((((((((0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) + ref_151042) & 0xFFFFFFFFFFFFFFFF)) # MOV operation
ref_151078 = (((sx(0x40, 0x9E3779B185EBCA87) * sx(0x40, ref_151076)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_151092 = ref_151078 # MOV operation
ref_151109 = ref_151092 # MOV operation
ref_151121 = ref_151109 # MOV operation
ref_151138 = (((((((((0x27) << 8 | 0xD4) << 8 | 0xEB) << 8 | 0x2F) << 8 | 0x16) << 8 | 0x56) << 8 | 0x67) << 8 | 0xCD) ^ ref_151121) # MOV operation
ref_151140 = rol(0x1B, ref_151138) # ROL operation
ref_151144 = ref_151140 # MOV operation
ref_151148 = (((sx(0x40, ref_151144) * sx(0x40, 0x9E3779B185EBCA87)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_151154 = ((0x85EBCA77C2B2AE63 + ref_151148) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_151247 = ref_151154 # MOV operation
ref_151249 = (ref_151247 >> (0x21 & 0x3F)) # SHR operation
ref_151273 = (ref_151154 ^ ref_151249) # MOV operation
ref_151275 = (((sx(0x40, 0xC2B2AE3D27D4EB4F) * sx(0x40, ref_151273)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_151289 = ref_151275 # MOV operation
ref_151291 = (ref_151289 >> (0x1D & 0x3F)) # SHR operation
ref_151315 = (ref_151275 ^ ref_151291) # MOV operation
ref_151317 = (((sx(0x40, 0x165667B19E3779F9) * sx(0x40, ref_151315)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_151331 = ref_151317 # MOV operation
ref_151333 = (ref_151331 >> (0x20 & 0x3F)) # SHR operation
ref_151355 = (ref_151317 ^ ref_151333) # MOV operation
ref_151367 = ref_151355 # MOV operation
ref_151615 = ref_151367 # MOV operation
ref_153239 = ref_151615 # MOV operation
ref_176075 = ref_153239 # MOV operation
ref_178197 = ref_176075 # MOV operation
ref_198159 = ref_178197 # MOV operation
ref_200447 = ref_198159 # MOV operation
ref_223099 = ref_200447 # MOV operation
ref_225221 = ref_223099 # MOV operation
ref_245183 = ref_225221 # MOV operation
ref_247471 = ref_245183 # MOV operation
ref_283900 = ref_247471 # MOV operation
ref_286022 = ref_283900 # MOV operation
ref_292207 = ref_286022 # MOV operation
ref_292289 = ref_292207 # MOV operation
ref_294411 = ref_292289 # MOV operation
ref_300596 = ref_294411 # MOV operation
ref_302884 = ref_300596 # MOV operation
ref_333115 = ref_302884 # MOV operation
ref_335237 = ref_333115 # MOV operation
ref_341422 = ref_335237 # MOV operation
ref_341650 = ref_341422 # MOV operation
ref_342074 = ref_341650 # MOV operation
ref_342154 = ref_342074 # MOV operation
ref_342192 = ref_342154 # MOV operation
ref_342204 = ref_342192 # MOV operation
ref_342206 = ref_342204 # MOV operation

print ref_342206 & 0xffffffffffffffff
