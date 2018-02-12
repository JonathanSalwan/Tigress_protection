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
ref_7256 = ref_367 # MOV operation
ref_7268 = ref_7256 # MOV operation
ref_7314 = ref_7256 # MOV operation
ref_7358 = ref_7256 # MOV operation
ref_7445 = (((rol(0xE, (rol(0xE, ((((((((((((0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) + ref_7268) & 0xFFFFFFFFFFFFFFFF) + 0x1F3D5B79) & 0xFFFFFFFFFFFFFFFF)) ^ ref_7314)) ^ 0x1F3D5B79) + ref_7358) & 0xFFFFFFFFFFFFFFFF) # MOV operation
ref_8668 = ref_7445 # MOV operation
ref_9137 = ref_8668 # MOV operation
ref_10570 = ref_9137 # MOV operation
ref_11137 = ref_10570 # MOV operation
ref_11175 = ref_11137 # MOV operation
ref_11187 = ref_11175 # MOV operation
ref_11189 = ref_11187 # MOV operation

print ref_11189 & 0xffffffffffffffff
