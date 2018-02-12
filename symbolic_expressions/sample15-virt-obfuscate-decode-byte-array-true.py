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
ref_9598 = ref_367 # MOV operation
ref_9610 = ref_9598 # MOV operation
ref_9656 = ref_9598 # MOV operation
ref_9700 = ref_9598 # MOV operation
ref_9787 = (((rol(0xE, (rol(0xE, ((((((((((((0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) + ref_9610) & 0xFFFFFFFFFFFFFFFF) + 0x1F3D5B79) & 0xFFFFFFFFFFFFFFFF)) ^ ref_9656)) ^ 0x1F3D5B79) + ref_9700) & 0xFFFFFFFFFFFFFFFF) # MOV operation
ref_10127 = ref_9787 # MOV operation
ref_10226 = ref_10127 # MOV operation
ref_10552 = ref_10226 # MOV operation
ref_10639 = ref_10552 # MOV operation
ref_10677 = ref_10639 # MOV operation
ref_10689 = ref_10677 # MOV operation
ref_10691 = ref_10689 # MOV operation

print ref_10691 & 0xffffffffffffffff
