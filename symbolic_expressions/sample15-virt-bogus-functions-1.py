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
ref_6266 = ref_367 # MOV operation
ref_6278 = ref_6266 # MOV operation
ref_6324 = ref_6266 # MOV operation
ref_6368 = ref_6266 # MOV operation
ref_6455 = (((rol(0xE, (rol(0xE, ((((((((((((0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) + ref_6278) & 0xFFFFFFFFFFFFFFFF) + 0x1F3D5B79) & 0xFFFFFFFFFFFFFFFF)) ^ ref_6324)) ^ 0x1F3D5B79) + ref_6368) & 0xFFFFFFFFFFFFFFFF) # MOV operation
ref_7405 = ref_6455 # MOV operation
ref_7709 = ref_7405 # MOV operation
ref_8606 = ref_7709 # MOV operation
ref_8846 = ref_8606 # MOV operation
ref_8887 = ref_8846 # MOV operation
ref_8899 = ref_8887 # MOV operation
ref_8901 = ref_8899 # MOV operation

print ref_8901 & 0xffffffffffffffff
