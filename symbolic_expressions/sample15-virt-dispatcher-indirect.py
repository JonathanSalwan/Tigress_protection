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
ref_8576 = ref_367 # MOV operation
ref_8588 = ref_8576 # MOV operation
ref_8634 = ref_8576 # MOV operation
ref_8678 = ref_8576 # MOV operation
ref_8765 = (((rol(0xE, (rol(0xE, ((((((((((((0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) + ref_8588) & 0xFFFFFFFFFFFFFFFF) + 0x1F3D5B79) & 0xFFFFFFFFFFFFFFFF)) ^ ref_8634)) ^ 0x1F3D5B79) + ref_8678) & 0xFFFFFFFFFFFFFFFF) # MOV operation
ref_9045 = ref_8765 # MOV operation
ref_9103 = ref_9045 # MOV operation
ref_9333 = ref_9103 # MOV operation
ref_9379 = ref_9333 # MOV operation
ref_9417 = ref_9379 # MOV operation
ref_9429 = ref_9417 # MOV operation
ref_9431 = ref_9429 # MOV operation

print ref_9431 & 0xffffffffffffffff
