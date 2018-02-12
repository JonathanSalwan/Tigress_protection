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
ref_7449 = ((((ref_456) << 8 | ref_457) << 8 | ref_458) << 8 | ref_459) # MOV operation
ref_7457 = (ref_7449 & 0xFFFFFFFF) # MOV operation
ref_7481 = (ref_7457 & 0xFFFFFFFF) # MOV operation
ref_7495 = (ref_7481 & 0xFFFFFFFF) # MOV operation
ref_7632 = ((((ref_452) << 8 | ref_453) << 8 | ref_454) << 8 | ref_455) # MOV operation
ref_7640 = (ref_7632 & 0xFFFFFFFF) # MOV operation
ref_7664 = (ref_7640 & 0xFFFFFFFF) # MOV operation
ref_7678 = (ref_7664 & 0xFFFFFFFF) # MOV operation
ref_7680 = ref_7495 # MOV operation
ref_7682 = ((0x0 + ((0x0 + ((ref_7680 * 0x8) & 0xFFFFFFFFFFFFFFFF)) & 0xFFFFFFFFFFFFFFFF)) & 0xFFFFFFFFFFFFFFFF) # LEA operation
ref_7686 = ((0x8 + ref_7682) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_7694 = ref_7678 # MOV operation
ref_7696 = ref_7686 # MOV operation
ref_7750 = ref_7696 # MOV operation
ref_7762 = ref_7694 # MOV operation
ref_7774 = ref_7750 # MOV operation
ref_7776 = ref_7762 # MOV operation
ref_7778 = ref_7774 # MOV operation
ref_7780 = ref_7776 # MOV operation
ref_7806 = ref_7778 # MOV operation
ref_7808 = ref_7780 # MOV operation
ref_7810 = ref_7808 # MOV operation
ref_7844 = ref_7806 # MOV operation
ref_7846 = ref_7810 # MOV operation
ref_7848 = (ref_7846 ^ ref_7844) # XOR operation
ref_7855 = (((sx(0x40, ref_7848) * sx(0x40, ((((((((0x9D) << 8 | 0xDF) << 8 | 0xEA) << 8 | 0x8) << 8 | 0xEB) << 8 | 0x38) << 8 | 0x2D) << 8 | 0x69))) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_7869 = ref_7855 # MOV operation
ref_7871 = (ref_7869 >> (0x2F & 0x3F)) # SHR operation
ref_7893 = ref_7810 # MOV operation
ref_7895 = (ref_7893 ^ (ref_7855 ^ ref_7871)) # XOR operation
ref_7902 = (((sx(0x40, ref_7895) * sx(0x40, ((((((((0x9D) << 8 | 0xDF) << 8 | 0xEA) << 8 | 0x8) << 8 | 0xEB) << 8 | 0x38) << 8 | 0x2D) << 8 | 0x69))) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_7916 = ref_7902 # MOV operation
ref_7918 = (ref_7916 >> (0x2F & 0x3F)) # SHR operation
ref_7940 = (ref_7902 ^ ref_7918) # MOV operation
ref_7942 = (((sx(0x40, ref_7940) * sx(0x40, ((((((((0x9D) << 8 | 0xDF) << 8 | 0xEA) << 8 | 0x8) << 8 | 0xEB) << 8 | 0x38) << 8 | 0x2D) << 8 | 0x69))) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_7956 = ref_7942 # MOV operation
ref_7973 = ref_7956 # MOV operation
ref_7991 = ref_7973 # MOV operation
ref_8010 = ref_7991 # MOV operation
ref_9235 = ref_8010 # MOV operation
ref_9704 = ref_9235 # MOV operation
ref_11137 = ref_9704 # MOV operation
ref_11704 = ref_11137 # MOV operation
ref_11742 = ref_11704 # MOV operation
ref_11754 = ref_11742 # MOV operation
ref_11756 = ref_11754 # MOV operation

print ref_11756 & 0xffffffffffffffff
