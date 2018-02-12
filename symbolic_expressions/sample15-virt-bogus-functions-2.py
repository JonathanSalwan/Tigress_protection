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
ref_6961 = ref_367 # MOV operation
ref_6973 = ref_6961 # MOV operation
ref_7019 = ref_6961 # MOV operation
ref_7063 = ref_6961 # MOV operation
ref_7150 = (((rol(0xE, (rol(0xE, ((((((((((((0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) + ref_6973) & 0xFFFFFFFFFFFFFFFF) + 0x1F3D5B79) & 0xFFFFFFFFFFFFFFFF)) ^ ref_7019)) ^ 0x1F3D5B79) + ref_7063) & 0xFFFFFFFFFFFFFFFF) # MOV operation
ref_8615 = ref_7150 # MOV operation
ref_9086 = ref_8615 # MOV operation
ref_10399 = ref_9086 # MOV operation
ref_10686 = ref_10399 # MOV operation
ref_10727 = ref_10686 # MOV operation
ref_10739 = ref_10727 # MOV operation
ref_10741 = ref_10739 # MOV operation

print ref_10741 & 0xffffffffffffffff
