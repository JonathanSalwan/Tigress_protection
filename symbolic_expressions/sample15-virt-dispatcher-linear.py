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
ref_6532 = ref_367 # MOV operation
ref_6544 = ref_6532 # MOV operation
ref_6590 = ref_6532 # MOV operation
ref_6634 = ref_6532 # MOV operation
ref_6721 = (((rol(0xE, (rol(0xE, ((((((((((((0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) + ref_6544) & 0xFFFFFFFFFFFFFFFF) + 0x1F3D5B79) & 0xFFFFFFFFFFFFFFFF)) ^ ref_6590)) ^ 0x1F3D5B79) + ref_6634) & 0xFFFFFFFFFFFFFFFF) # MOV operation
ref_7798 = ref_6721 # MOV operation
ref_8295 = ref_7798 # MOV operation
ref_9374 = ref_8295 # MOV operation
ref_9911 = ref_9374 # MOV operation
ref_9949 = ref_9911 # MOV operation
ref_9961 = ref_9949 # MOV operation
ref_9963 = ref_9961 # MOV operation

print ref_9963 & 0xffffffffffffffff
