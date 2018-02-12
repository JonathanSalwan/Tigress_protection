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
ref_6236 = ref_665 # MOV operation
ref_6248 = ref_6236 # MOV operation
ref_6294 = ref_6236 # MOV operation
ref_6338 = ref_6236 # MOV operation
ref_6425 = (((rol(0xE, (rol(0xE, ((((((((((((0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) + ref_6248) & 0xFFFFFFFFFFFFFFFF) + 0x1F3D5B79) & 0xFFFFFFFFFFFFFFFF)) ^ ref_6294)) ^ 0x1F3D5B79) + ref_6338) & 0xFFFFFFFFFFFFFFFF) # MOV operation
ref_7150 = ref_6425 # MOV operation
ref_7356 = ref_7150 # MOV operation
ref_8033 = ref_7356 # MOV operation
ref_8225 = ref_8033 # MOV operation
ref_8269 = ref_8225 # MOV operation
ref_8297 = ref_8269 # MOV operation
ref_8309 = ref_8297 # MOV operation
ref_8311 = ref_8309 # MOV operation

print ref_8311 & 0xffffffffffffffff
