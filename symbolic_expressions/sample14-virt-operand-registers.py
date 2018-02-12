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
ref_5586 = ((((ref_456) << 8 | ref_457) << 8 | ref_458) << 8 | ref_459) # MOV operation
ref_5594 = (ref_5586 & 0xFFFFFFFF) # MOV operation
ref_5618 = (ref_5594 & 0xFFFFFFFF) # MOV operation
ref_5632 = (ref_5618 & 0xFFFFFFFF) # MOV operation
ref_5769 = ((((ref_452) << 8 | ref_453) << 8 | ref_454) << 8 | ref_455) # MOV operation
ref_5777 = (ref_5769 & 0xFFFFFFFF) # MOV operation
ref_5801 = (ref_5777 & 0xFFFFFFFF) # MOV operation
ref_5815 = (ref_5801 & 0xFFFFFFFF) # MOV operation
ref_5817 = ref_5632 # MOV operation
ref_5819 = ((0x0 + ((0x0 + ((ref_5817 * 0x8) & 0xFFFFFFFFFFFFFFFF)) & 0xFFFFFFFFFFFFFFFF)) & 0xFFFFFFFFFFFFFFFF) # LEA operation
ref_5823 = ((0x8 + ref_5819) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_5831 = ref_5815 # MOV operation
ref_5833 = ref_5823 # MOV operation
ref_5887 = ref_5833 # MOV operation
ref_5899 = ref_5831 # MOV operation
ref_5911 = ref_5887 # MOV operation
ref_5913 = ref_5899 # MOV operation
ref_5915 = ref_5911 # MOV operation
ref_5917 = ref_5913 # MOV operation
ref_5943 = ref_5915 # MOV operation
ref_5945 = ref_5917 # MOV operation
ref_5947 = ref_5945 # MOV operation
ref_5981 = ref_5943 # MOV operation
ref_5983 = ref_5947 # MOV operation
ref_5985 = (ref_5983 ^ ref_5981) # XOR operation
ref_5992 = (((sx(0x40, ref_5985) * sx(0x40, ((((((((0x9D) << 8 | 0xDF) << 8 | 0xEA) << 8 | 0x8) << 8 | 0xEB) << 8 | 0x38) << 8 | 0x2D) << 8 | 0x69))) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_6006 = ref_5992 # MOV operation
ref_6008 = (ref_6006 >> (0x2F & 0x3F)) # SHR operation
ref_6030 = ref_5947 # MOV operation
ref_6032 = (ref_6030 ^ (ref_5992 ^ ref_6008)) # XOR operation
ref_6039 = (((sx(0x40, ref_6032) * sx(0x40, ((((((((0x9D) << 8 | 0xDF) << 8 | 0xEA) << 8 | 0x8) << 8 | 0xEB) << 8 | 0x38) << 8 | 0x2D) << 8 | 0x69))) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_6053 = ref_6039 # MOV operation
ref_6055 = (ref_6053 >> (0x2F & 0x3F)) # SHR operation
ref_6077 = (ref_6039 ^ ref_6055) # MOV operation
ref_6079 = (((sx(0x40, ref_6077) * sx(0x40, ((((((((0x9D) << 8 | 0xDF) << 8 | 0xEA) << 8 | 0x8) << 8 | 0xEB) << 8 | 0x38) << 8 | 0x2D) << 8 | 0x69))) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_6093 = ref_6079 # MOV operation
ref_6110 = ref_6093 # MOV operation
ref_6128 = ref_6110 # MOV operation
ref_6147 = ref_6128 # MOV operation
ref_6386 = ref_6147 # MOV operation
ref_6612 = ref_6386 # MOV operation
ref_6942 = ref_6612 # MOV operation
ref_7064 = ref_6942 # MOV operation
ref_7102 = ref_7064 # MOV operation
ref_7114 = ref_7102 # MOV operation
ref_7116 = ref_7114 # MOV operation

print ref_7116 & 0xffffffffffffffff
