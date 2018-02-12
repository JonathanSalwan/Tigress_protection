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
ref_5473 = ref_367 # MOV operation
ref_5485 = ref_5473 # MOV operation
ref_5531 = ref_5473 # MOV operation
ref_5575 = ref_5473 # MOV operation
ref_5662 = (((rol(0xE, (rol(0xE, ((((((((((((0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) + ref_5485) & 0xFFFFFFFFFFFFFFFF) + 0x1F3D5B79) & 0xFFFFFFFFFFFFFFFF)) ^ ref_5531)) ^ 0x1F3D5B79) + ref_5575) & 0xFFFFFFFFFFFFFFFF) # MOV operation
ref_6053 = ref_5662 # MOV operation
ref_6187 = ref_6053 # MOV operation
ref_6501 = ref_6187 # MOV operation
ref_6551 = ref_6501 # MOV operation
ref_6589 = ref_6551 # MOV operation
ref_6601 = ref_6589 # MOV operation
ref_6603 = ref_6601 # MOV operation

print ref_6603 & 0xffffffffffffffff
