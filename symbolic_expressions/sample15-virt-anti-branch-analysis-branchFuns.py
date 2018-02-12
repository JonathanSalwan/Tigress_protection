#!/usr/bin/env python2
## -*- coding: utf-8 -*-

import sys

def sx(bits, value):
    sign_bit = 1 << (bits - 1)
    return (value & (sign_bit - 1)) - (value & sign_bit)

SymVar_0 = int(sys.argv[1])
ref_348 = SymVar_0
ref_359 = ref_348 # MOV operation
ref_371 = ref_359 # MOV operation
ref_373 = ref_371 # MOV operation
ref_10515 = ref_373 # MOV operation
ref_10527 = ref_10515 # MOV operation
ref_10573 = ref_10515 # MOV operation
ref_10617 = ref_10515 # MOV operation
ref_10704 = (((rol(0xE, (rol(0xE, ((((((((((((0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) + ref_10527) & 0xFFFFFFFFFFFFFFFF) + 0x1F3D5B79) & 0xFFFFFFFFFFFFFFFF)) ^ ref_10573)) ^ 0x1F3D5B79) + ref_10617) & 0xFFFFFFFFFFFFFFFF) # MOV operation
ref_11939 = ref_10704 # MOV operation
ref_12319 = ref_11939 # MOV operation
ref_13523 = ref_12319 # MOV operation
ref_13938 = ref_13523 # MOV operation
ref_13977 = ref_13938 # MOV operation
ref_13989 = ref_13977 # MOV operation
ref_13991 = ref_13989 # MOV operation

print ref_13991 & 0xffffffffffffffff
