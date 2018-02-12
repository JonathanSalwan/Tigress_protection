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
ref_331345 = ref_367 # MOV operation
ref_331357 = ref_331345 # MOV operation
ref_331403 = ref_331345 # MOV operation
ref_331447 = ref_331345 # MOV operation
ref_331534 = (((rol(0xE, (rol(0xE, ((((((((((((0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) + ref_331357) & 0xFFFFFFFFFFFFFFFF) + 0x1F3D5B79) & 0xFFFFFFFFFFFFFFFF)) ^ ref_331403)) ^ 0x1F3D5B79) + ref_331447) & 0xFFFFFFFFFFFFFFFF) # MOV operation
ref_527456 = ref_331534 # MOV operation
ref_592749 = ref_527456 # MOV operation
ref_788657 = ref_592749 # MOV operation
ref_853947 = ref_788657 # MOV operation
ref_853985 = ref_853947 # MOV operation
ref_853997 = ref_853985 # MOV operation
ref_853999 = ref_853997 # MOV operation

print ref_853999 & 0xffffffffffffffff
