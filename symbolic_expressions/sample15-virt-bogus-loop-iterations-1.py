#!/usr/bin/env python2
## -*- coding: utf-8 -*-

import sys

def sx(bits, value):
    sign_bit = 1 << (bits - 1)
    return (value & (sign_bit - 1)) - (value & sign_bit)

SymVar_0 = int(sys.argv[1])
ref_342 = SymVar_0
ref_353 = ref_342 # MOV operation
ref_365 = ref_353 # MOV operation
ref_367 = ref_365 # MOV operation
ref_168410 = ref_367 # MOV operation
ref_168422 = ref_168410 # MOV operation
ref_168468 = ref_168410 # MOV operation
ref_168512 = ref_168410 # MOV operation
ref_168599 = (((rol(0xE, (rol(0xE, ((((((((((((0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) + ref_168422) & 0xFFFFFFFFFFFFFFFF) + 0x1F3D5B79) & 0xFFFFFFFFFFFFFFFF)) ^ ref_168468)) ^ 0x1F3D5B79) + ref_168512) & 0xFFFFFFFFFFFFFFFF) # MOV operation
ref_266760 = ref_168599 # MOV operation
ref_299466 = ref_266760 # MOV operation
ref_397613 = ref_299466 # MOV operation
ref_430316 = ref_397613 # MOV operation
ref_430354 = ref_430316 # MOV operation
ref_430366 = ref_430354 # MOV operation
ref_430368 = ref_430366 # MOV operation

print ref_430368 & 0xffffffffffffffff
