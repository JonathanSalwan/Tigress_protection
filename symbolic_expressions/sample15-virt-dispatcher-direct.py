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
ref_5478 = ref_367 # MOV operation
ref_5490 = ref_5478 # MOV operation
ref_5536 = ref_5478 # MOV operation
ref_5580 = ref_5478 # MOV operation
ref_5667 = (((rol(0xE, (rol(0xE, ((((((((((((0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) + ref_5490) & 0xFFFFFFFFFFFFFFFF) + 0x1F3D5B79) & 0xFFFFFFFFFFFFFFFF)) ^ ref_5536)) ^ 0x1F3D5B79) + ref_5580) & 0xFFFFFFFFFFFFFFFF) # MOV operation
ref_5929 = ref_5667 # MOV operation
ref_5981 = ref_5929 # MOV operation
ref_6200 = ref_5981 # MOV operation
ref_6240 = ref_6200 # MOV operation
ref_6278 = ref_6240 # MOV operation
ref_6290 = ref_6278 # MOV operation
ref_6292 = ref_6290 # MOV operation

print ref_6292 & 0xffffffffffffffff
