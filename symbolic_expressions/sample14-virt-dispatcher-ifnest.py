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
ref_5621 = ((((ref_456) << 8 | ref_457) << 8 | ref_458) << 8 | ref_459) # MOV operation
ref_5629 = (ref_5621 & 0xFFFFFFFF) # MOV operation
ref_5653 = (ref_5629 & 0xFFFFFFFF) # MOV operation
ref_5667 = (ref_5653 & 0xFFFFFFFF) # MOV operation
ref_5804 = ((((ref_452) << 8 | ref_453) << 8 | ref_454) << 8 | ref_455) # MOV operation
ref_5812 = (ref_5804 & 0xFFFFFFFF) # MOV operation
ref_5836 = (ref_5812 & 0xFFFFFFFF) # MOV operation
ref_5850 = (ref_5836 & 0xFFFFFFFF) # MOV operation
ref_5852 = ref_5667 # MOV operation
ref_5854 = ((0x0 + ((0x0 + ((ref_5852 * 0x8) & 0xFFFFFFFFFFFFFFFF)) & 0xFFFFFFFFFFFFFFFF)) & 0xFFFFFFFFFFFFFFFF) # LEA operation
ref_5858 = ((0x8 + ref_5854) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_5866 = ref_5850 # MOV operation
ref_5868 = ref_5858 # MOV operation
ref_5922 = ref_5868 # MOV operation
ref_5934 = ref_5866 # MOV operation
ref_5946 = ref_5922 # MOV operation
ref_5948 = ref_5934 # MOV operation
ref_5950 = ref_5946 # MOV operation
ref_5952 = ref_5948 # MOV operation
ref_5978 = ref_5950 # MOV operation
ref_5980 = ref_5952 # MOV operation
ref_5982 = ref_5980 # MOV operation
ref_6016 = ref_5978 # MOV operation
ref_6018 = ref_5982 # MOV operation
ref_6020 = (ref_6018 ^ ref_6016) # XOR operation
ref_6027 = (((sx(0x40, ref_6020) * sx(0x40, ((((((((0x9D) << 8 | 0xDF) << 8 | 0xEA) << 8 | 0x8) << 8 | 0xEB) << 8 | 0x38) << 8 | 0x2D) << 8 | 0x69))) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_6041 = ref_6027 # MOV operation
ref_6043 = (ref_6041 >> (0x2F & 0x3F)) # SHR operation
ref_6065 = ref_5982 # MOV operation
ref_6067 = (ref_6065 ^ (ref_6027 ^ ref_6043)) # XOR operation
ref_6074 = (((sx(0x40, ref_6067) * sx(0x40, ((((((((0x9D) << 8 | 0xDF) << 8 | 0xEA) << 8 | 0x8) << 8 | 0xEB) << 8 | 0x38) << 8 | 0x2D) << 8 | 0x69))) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_6088 = ref_6074 # MOV operation
ref_6090 = (ref_6088 >> (0x2F & 0x3F)) # SHR operation
ref_6112 = (ref_6074 ^ ref_6090) # MOV operation
ref_6114 = (((sx(0x40, ref_6112) * sx(0x40, ((((((((0x9D) << 8 | 0xDF) << 8 | 0xEA) << 8 | 0x8) << 8 | 0xEB) << 8 | 0x38) << 8 | 0x2D) << 8 | 0x69))) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_6128 = ref_6114 # MOV operation
ref_6145 = ref_6128 # MOV operation
ref_6163 = ref_6145 # MOV operation
ref_6182 = ref_6163 # MOV operation
ref_6548 = ref_6182 # MOV operation
ref_6610 = ref_6548 # MOV operation
ref_6978 = ref_6610 # MOV operation
ref_7073 = ref_6978 # MOV operation
ref_7111 = ref_7073 # MOV operation
ref_7123 = ref_7111 # MOV operation
ref_7125 = ref_7123 # MOV operation

print ref_7125 & 0xffffffffffffffff
