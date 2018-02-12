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
ref_494280 = ref_367 # MOV operation
ref_494292 = ref_494280 # MOV operation
ref_494338 = ref_494280 # MOV operation
ref_494382 = ref_494280 # MOV operation
ref_494469 = (((rol(0xE, (rol(0xE, ((((((((((((0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) + ref_494292) & 0xFFFFFFFFFFFFFFFF) + 0x1F3D5B79) & 0xFFFFFFFFFFFFFFFF)) ^ ref_494338)) ^ 0x1F3D5B79) + ref_494382) & 0xFFFFFFFFFFFFFFFF) # MOV operation
ref_788152 = ref_494469 # MOV operation
ref_886032 = ref_788152 # MOV operation
ref_1179701 = ref_886032 # MOV operation
ref_1277578 = ref_1179701 # MOV operation
ref_1277616 = ref_1277578 # MOV operation
ref_1277628 = ref_1277616 # MOV operation
ref_1277630 = ref_1277628 # MOV operation

print ref_1277630 & 0xffffffffffffffff
