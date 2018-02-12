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
ref_5393 = ref_367 # MOV operation
ref_5405 = ref_5393 # MOV operation
ref_5451 = ref_5393 # MOV operation
ref_5495 = ref_5393 # MOV operation
ref_5582 = (((rol(0xE, (rol(0xE, ((((((((((((0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) + ref_5405) & 0xFFFFFFFFFFFFFFFF) + 0x1F3D5B79) & 0xFFFFFFFFFFFFFFFF)) ^ ref_5451)) ^ 0x1F3D5B79) + ref_5495) & 0xFFFFFFFFFFFFFFFF) # MOV operation
ref_5819 = ref_5582 # MOV operation
ref_6045 = ref_5819 # MOV operation
ref_6375 = ref_6045 # MOV operation
ref_6497 = ref_6375 # MOV operation
ref_6535 = ref_6497 # MOV operation
ref_6547 = ref_6535 # MOV operation
ref_6549 = ref_6547 # MOV operation

print ref_6549 & 0xffffffffffffffff
