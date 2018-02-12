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
ref_76624 = ref_367 # MOV operation
ref_76636 = ref_76624 # MOV operation
ref_76682 = ref_76624 # MOV operation
ref_76726 = ref_76624 # MOV operation
ref_76813 = (((rol(0xE, (rol(0xE, ((((((((((((0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) + ref_76636) & 0xFFFFFFFFFFFFFFFF) + 0x1F3D5B79) & 0xFFFFFFFFFFFFFFFF)) ^ ref_76682)) ^ 0x1F3D5B79) + ref_76726) & 0xFFFFFFFFFFFFFFFF) # MOV operation
ref_78939 = ref_76813 # MOV operation
ref_79038 = ref_78939 # MOV operation
ref_125894 = ref_79038 # MOV operation
ref_125993 = ref_125894 # MOV operation
ref_136104 = ref_125993 # MOV operation
ref_136203 = ref_136104 # MOV operation
ref_175345 = ref_136203 # MOV operation
ref_175444 = ref_175345 # MOV operation
ref_183117 = ref_175444 # MOV operation
ref_183216 = ref_183117 # MOV operation
ref_183749 = ref_183216 # MOV operation
ref_183863 = ref_183749 # MOV operation
ref_183901 = ref_183863 # MOV operation
ref_183913 = ref_183901 # MOV operation
ref_183915 = ref_183913 # MOV operation

print ref_183915 & 0xffffffffffffffff
