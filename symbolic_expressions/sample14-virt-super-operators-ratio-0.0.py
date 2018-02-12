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
ref_5562 = ((((ref_456) << 8 | ref_457) << 8 | ref_458) << 8 | ref_459) # MOV operation
ref_5570 = (ref_5562 & 0xFFFFFFFF) # MOV operation
ref_5594 = (ref_5570 & 0xFFFFFFFF) # MOV operation
ref_5608 = (ref_5594 & 0xFFFFFFFF) # MOV operation
ref_5745 = ((((ref_452) << 8 | ref_453) << 8 | ref_454) << 8 | ref_455) # MOV operation
ref_5753 = (ref_5745 & 0xFFFFFFFF) # MOV operation
ref_5777 = (ref_5753 & 0xFFFFFFFF) # MOV operation
ref_5791 = (ref_5777 & 0xFFFFFFFF) # MOV operation
ref_5793 = ref_5608 # MOV operation
ref_5795 = ((0x0 + ((0x0 + ((ref_5793 * 0x8) & 0xFFFFFFFFFFFFFFFF)) & 0xFFFFFFFFFFFFFFFF)) & 0xFFFFFFFFFFFFFFFF) # LEA operation
ref_5799 = ((0x8 + ref_5795) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_5807 = ref_5791 # MOV operation
ref_5809 = ref_5799 # MOV operation
ref_5863 = ref_5809 # MOV operation
ref_5875 = ref_5807 # MOV operation
ref_5887 = ref_5863 # MOV operation
ref_5889 = ref_5875 # MOV operation
ref_5891 = ref_5887 # MOV operation
ref_5893 = ref_5889 # MOV operation
ref_5919 = ref_5891 # MOV operation
ref_5921 = ref_5893 # MOV operation
ref_5923 = ref_5921 # MOV operation
ref_5957 = ref_5919 # MOV operation
ref_5959 = ref_5923 # MOV operation
ref_5961 = (ref_5959 ^ ref_5957) # XOR operation
ref_5968 = (((sx(0x40, ref_5961) * sx(0x40, ((((((((0x9D) << 8 | 0xDF) << 8 | 0xEA) << 8 | 0x8) << 8 | 0xEB) << 8 | 0x38) << 8 | 0x2D) << 8 | 0x69))) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_5982 = ref_5968 # MOV operation
ref_5984 = (ref_5982 >> (0x2F & 0x3F)) # SHR operation
ref_6006 = ref_5923 # MOV operation
ref_6008 = (ref_6006 ^ (ref_5968 ^ ref_5984)) # XOR operation
ref_6015 = (((sx(0x40, ref_6008) * sx(0x40, ((((((((0x9D) << 8 | 0xDF) << 8 | 0xEA) << 8 | 0x8) << 8 | 0xEB) << 8 | 0x38) << 8 | 0x2D) << 8 | 0x69))) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_6029 = ref_6015 # MOV operation
ref_6031 = (ref_6029 >> (0x2F & 0x3F)) # SHR operation
ref_6053 = (ref_6015 ^ ref_6031) # MOV operation
ref_6055 = (((sx(0x40, ref_6053) * sx(0x40, ((((((((0x9D) << 8 | 0xDF) << 8 | 0xEA) << 8 | 0x8) << 8 | 0xEB) << 8 | 0x38) << 8 | 0x2D) << 8 | 0x69))) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_6069 = ref_6055 # MOV operation
ref_6086 = ref_6069 # MOV operation
ref_6104 = ref_6086 # MOV operation
ref_6123 = ref_6104 # MOV operation
ref_6465 = ref_6123 # MOV operation
ref_6564 = ref_6465 # MOV operation
ref_6899 = ref_6564 # MOV operation
ref_6995 = ref_6899 # MOV operation
ref_7033 = ref_6995 # MOV operation
ref_7045 = ref_7033 # MOV operation
ref_7047 = ref_7045 # MOV operation

print ref_7047 & 0xffffffffffffffff
