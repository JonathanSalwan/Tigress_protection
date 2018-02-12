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
ref_5571 = ref_367 # MOV operation
ref_5583 = ref_5571 # MOV operation
ref_5629 = ref_5571 # MOV operation
ref_5673 = ref_5571 # MOV operation
ref_5760 = (((rol(0xE, (rol(0xE, ((((((((((((0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) + ref_5583) & 0xFFFFFFFFFFFFFFFF) + 0x1F3D5B79) & 0xFFFFFFFFFFFFFFFF)) ^ ref_5629)) ^ 0x1F3D5B79) + ref_5673) & 0xFFFFFFFFFFFFFFFF) # MOV operation
ref_6249 = ref_5760 # MOV operation
ref_6375 = ref_6249 # MOV operation
ref_6850 = ref_6375 # MOV operation
ref_6970 = ref_6850 # MOV operation
ref_7008 = ref_6970 # MOV operation
ref_7020 = ref_7008 # MOV operation
ref_7022 = ref_7020 # MOV operation

print ref_7022 & 0xffffffffffffffff
