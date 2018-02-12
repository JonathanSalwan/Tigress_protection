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
ref_7686 = ref_367 # MOV operation
ref_7698 = ref_7686 # MOV operation
ref_7744 = ref_7686 # MOV operation
ref_7788 = ref_7686 # MOV operation
ref_7875 = (((rol(0xE, (rol(0xE, ((((((((((((0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) + ref_7698) & 0xFFFFFFFFFFFFFFFF) + 0x1F3D5B79) & 0xFFFFFFFFFFFFFFFF)) ^ ref_7744)) ^ 0x1F3D5B79) + ref_7788) & 0xFFFFFFFFFFFFFFFF) # MOV operation
ref_9523 = ref_7875 # MOV operation
ref_9887 = ref_9523 # MOV operation
ref_11260 = ref_9887 # MOV operation
ref_11612 = ref_11260 # MOV operation
ref_11650 = ref_11612 # MOV operation
ref_11662 = ref_11650 # MOV operation
ref_11664 = ref_11662 # MOV operation

print ref_11664 & 0xffffffffffffffff
