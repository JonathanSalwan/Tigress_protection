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
ref_5366 = ref_367 # MOV operation
ref_5378 = ref_5366 # MOV operation
ref_5424 = ref_5366 # MOV operation
ref_5468 = ref_5366 # MOV operation
ref_5555 = (((rol(0xE, (rol(0xE, ((((((((((((0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) + ref_5378) & 0xFFFFFFFFFFFFFFFF) + 0x1F3D5B79) & 0xFFFFFFFFFFFFFFFF)) ^ ref_5424)) ^ 0x1F3D5B79) + ref_5468) & 0xFFFFFFFFFFFFFFFF) # MOV operation
ref_5785 = ref_5555 # MOV operation
ref_5997 = ref_5785 # MOV operation
ref_6305 = ref_5997 # MOV operation
ref_6377 = ref_6305 # MOV operation
ref_6415 = ref_6377 # MOV operation
ref_6427 = ref_6415 # MOV operation
ref_6429 = ref_6427 # MOV operation

print ref_6429 & 0xffffffffffffffff
