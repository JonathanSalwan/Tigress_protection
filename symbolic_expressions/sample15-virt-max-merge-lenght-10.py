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
ref_5368 = ref_367 # MOV operation
ref_5380 = ref_5368 # MOV operation
ref_5426 = ref_5368 # MOV operation
ref_5470 = ref_5368 # MOV operation
ref_5557 = (((rol(0xE, (rol(0xE, ((((((((((((0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) + ref_5380) & 0xFFFFFFFFFFFFFFFF) + 0x1F3D5B79) & 0xFFFFFFFFFFFFFFFF)) ^ ref_5426)) ^ 0x1F3D5B79) + ref_5470) & 0xFFFFFFFFFFFFFFFF) # MOV operation
ref_5740 = ref_5557 # MOV operation
ref_5774 = ref_5740 # MOV operation
ref_5970 = ref_5774 # MOV operation
ref_6097 = ref_5970 # MOV operation
ref_6135 = ref_6097 # MOV operation
ref_6147 = ref_6135 # MOV operation
ref_6149 = ref_6147 # MOV operation

print ref_6149 & 0xffffffffffffffff
