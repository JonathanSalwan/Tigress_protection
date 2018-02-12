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
ref_7904 = ref_367 # MOV operation
ref_7916 = ref_7904 # MOV operation
ref_7962 = ref_7904 # MOV operation
ref_8006 = ref_7904 # MOV operation
ref_8093 = (((rol(0xE, (rol(0xE, ((((((((((((0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) + ref_7916) & 0xFFFFFFFFFFFFFFFF) + 0x1F3D5B79) & 0xFFFFFFFFFFFFFFFF)) ^ ref_7962)) ^ 0x1F3D5B79) + ref_8006) & 0xFFFFFFFFFFFFFFFF) # MOV operation
ref_10520 = ref_8093 # MOV operation
ref_11250 = ref_10520 # MOV operation
ref_13597 = ref_11250 # MOV operation
ref_14328 = ref_13597 # MOV operation
ref_14369 = ref_14328 # MOV operation
ref_14381 = ref_14369 # MOV operation
ref_14383 = ref_14381 # MOV operation

print ref_14383 & 0xffffffffffffffff
