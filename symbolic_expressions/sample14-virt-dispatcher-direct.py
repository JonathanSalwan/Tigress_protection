#!/usr/bin/env python2
## -*- coding: utf-8 -*-

import sys

def sx(bits, value):
    sign_bit = 1 << (bits - 1)
    return (value & (sign_bit - 1)) - (value & sign_bit)

SymVar_0 = int(sys.argv[1])
ref_382 = SymVar_0
ref_393 = ref_382 # MOV operation
ref_405 = ref_393 # MOV operation
ref_407 = ref_405 # MOV operation
ref_452 = ((ref_407 >> 56) & 0xFF) # Byte reference - MOV operation
ref_453 = ((ref_407 >> 48) & 0xFF) # Byte reference - MOV operation
ref_454 = ((ref_407 >> 40) & 0xFF) # Byte reference - MOV operation
ref_455 = ((ref_407 >> 32) & 0xFF) # Byte reference - MOV operation
ref_456 = ((ref_407 >> 24) & 0xFF) # Byte reference - MOV operation
ref_457 = ((ref_407 >> 16) & 0xFF) # Byte reference - MOV operation
ref_458 = ((ref_407 >> 8) & 0xFF) # Byte reference - MOV operation
ref_459 = (ref_407 & 0xFF) # Byte reference - MOV operation
ref_5671 = ((((ref_456) << 8 | ref_457) << 8 | ref_458) << 8 | ref_459) # MOV operation
ref_5679 = (ref_5671 & 0xFFFFFFFF) # MOV operation
ref_5703 = (ref_5679 & 0xFFFFFFFF) # MOV operation
ref_5717 = (ref_5703 & 0xFFFFFFFF) # MOV operation
ref_5854 = ((((ref_452) << 8 | ref_453) << 8 | ref_454) << 8 | ref_455) # MOV operation
ref_5862 = (ref_5854 & 0xFFFFFFFF) # MOV operation
ref_5886 = (ref_5862 & 0xFFFFFFFF) # MOV operation
ref_5900 = (ref_5886 & 0xFFFFFFFF) # MOV operation
ref_5902 = ref_5717 # MOV operation
ref_5904 = ((0x0 + ((0x0 + ((ref_5902 * 0x8) & 0xFFFFFFFFFFFFFFFF)) & 0xFFFFFFFFFFFFFFFF)) & 0xFFFFFFFFFFFFFFFF) # LEA operation
ref_5908 = ((0x8 + ref_5904) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_5916 = ref_5900 # MOV operation
ref_5918 = ref_5908 # MOV operation
ref_5972 = ref_5918 # MOV operation
ref_5984 = ref_5916 # MOV operation
ref_5996 = ref_5972 # MOV operation
ref_5998 = ref_5984 # MOV operation
ref_6000 = ref_5996 # MOV operation
ref_6002 = ref_5998 # MOV operation
ref_6028 = ref_6000 # MOV operation
ref_6030 = ref_6002 # MOV operation
ref_6032 = ref_6030 # MOV operation
ref_6066 = ref_6028 # MOV operation
ref_6068 = ref_6032 # MOV operation
ref_6070 = (ref_6068 ^ ref_6066) # XOR operation
ref_6077 = (((sx(0x40, ref_6070) * sx(0x40, ((((((((0x9D) << 8 | 0xDF) << 8 | 0xEA) << 8 | 0x8) << 8 | 0xEB) << 8 | 0x38) << 8 | 0x2D) << 8 | 0x69))) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_6091 = ref_6077 # MOV operation
ref_6093 = (ref_6091 >> (0x2F & 0x3F)) # SHR operation
ref_6115 = ref_6032 # MOV operation
ref_6117 = (ref_6115 ^ (ref_6077 ^ ref_6093)) # XOR operation
ref_6124 = (((sx(0x40, ref_6117) * sx(0x40, ((((((((0x9D) << 8 | 0xDF) << 8 | 0xEA) << 8 | 0x8) << 8 | 0xEB) << 8 | 0x38) << 8 | 0x2D) << 8 | 0x69))) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_6138 = ref_6124 # MOV operation
ref_6140 = (ref_6138 >> (0x2F & 0x3F)) # SHR operation
ref_6162 = (ref_6124 ^ ref_6140) # MOV operation
ref_6164 = (((sx(0x40, ref_6162) * sx(0x40, ((((((((0x9D) << 8 | 0xDF) << 8 | 0xEA) << 8 | 0x8) << 8 | 0xEB) << 8 | 0x38) << 8 | 0x2D) << 8 | 0x69))) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_6178 = ref_6164 # MOV operation
ref_6195 = ref_6178 # MOV operation
ref_6213 = ref_6195 # MOV operation
ref_6232 = ref_6213 # MOV operation
ref_6496 = ref_6232 # MOV operation
ref_6548 = ref_6496 # MOV operation
ref_6767 = ref_6548 # MOV operation
ref_6807 = ref_6767 # MOV operation
ref_6845 = ref_6807 # MOV operation
ref_6857 = ref_6845 # MOV operation
ref_6859 = ref_6857 # MOV operation

print ref_6859 & 0xffffffffffffffff
