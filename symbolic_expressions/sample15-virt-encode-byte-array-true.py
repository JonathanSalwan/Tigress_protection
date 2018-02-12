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
ref_7191 = ref_367 # MOV operation
ref_7203 = ref_7191 # MOV operation
ref_7249 = ref_7191 # MOV operation
ref_7293 = ref_7191 # MOV operation
ref_7380 = (((rol(0xE, (rol(0xE, ((((((((((((0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) + ref_7203) & 0xFFFFFFFFFFFFFFFF) + 0x1F3D5B79) & 0xFFFFFFFFFFFFFFFF)) ^ ref_7249)) ^ 0x1F3D5B79) + ref_7293) & 0xFFFFFFFFFFFFFFFF) # MOV operation
ref_7720 = ref_7380 # MOV operation
ref_7819 = ref_7720 # MOV operation
ref_8145 = ref_7819 # MOV operation
ref_8241 = ref_8145 # MOV operation
ref_8279 = ref_8241 # MOV operation
ref_8291 = ref_8279 # MOV operation
ref_8293 = ref_8291 # MOV operation

print ref_8293 & 0xffffffffffffffff
