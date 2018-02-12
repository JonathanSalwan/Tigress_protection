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
ref_26458 = ((((ref_456) << 8 | ref_457) << 8 | ref_458) << 8 | ref_459) # MOV operation
ref_26466 = (ref_26458 & 0xFFFFFFFF) # MOV operation
ref_26490 = (ref_26466 & 0xFFFFFFFF) # MOV operation
ref_26504 = (ref_26490 & 0xFFFFFFFF) # MOV operation
ref_26641 = ((((ref_452) << 8 | ref_453) << 8 | ref_454) << 8 | ref_455) # MOV operation
ref_26649 = (ref_26641 & 0xFFFFFFFF) # MOV operation
ref_26673 = (ref_26649 & 0xFFFFFFFF) # MOV operation
ref_26687 = (ref_26673 & 0xFFFFFFFF) # MOV operation
ref_26689 = ref_26504 # MOV operation
ref_26691 = ((0x0 + ((0x0 + ((ref_26689 * 0x8) & 0xFFFFFFFFFFFFFFFF)) & 0xFFFFFFFFFFFFFFFF)) & 0xFFFFFFFFFFFFFFFF) # LEA operation
ref_26695 = ((0x8 + ref_26691) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_26703 = ref_26687 # MOV operation
ref_26705 = ref_26695 # MOV operation
ref_26759 = ref_26705 # MOV operation
ref_26771 = ref_26703 # MOV operation
ref_26783 = ref_26759 # MOV operation
ref_26785 = ref_26771 # MOV operation
ref_26787 = ref_26783 # MOV operation
ref_26789 = ref_26785 # MOV operation
ref_26815 = ref_26787 # MOV operation
ref_26817 = ref_26789 # MOV operation
ref_26819 = ref_26817 # MOV operation
ref_26853 = ref_26815 # MOV operation
ref_26855 = ref_26819 # MOV operation
ref_26857 = (ref_26855 ^ ref_26853) # XOR operation
ref_26864 = (((sx(0x40, ref_26857) * sx(0x40, ((((((((0x9D) << 8 | 0xDF) << 8 | 0xEA) << 8 | 0x8) << 8 | 0xEB) << 8 | 0x38) << 8 | 0x2D) << 8 | 0x69))) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_26878 = ref_26864 # MOV operation
ref_26880 = (ref_26878 >> (0x2F & 0x3F)) # SHR operation
ref_26902 = ref_26819 # MOV operation
ref_26904 = (ref_26902 ^ (ref_26864 ^ ref_26880)) # XOR operation
ref_26911 = (((sx(0x40, ref_26904) * sx(0x40, ((((((((0x9D) << 8 | 0xDF) << 8 | 0xEA) << 8 | 0x8) << 8 | 0xEB) << 8 | 0x38) << 8 | 0x2D) << 8 | 0x69))) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_26925 = ref_26911 # MOV operation
ref_26927 = (ref_26925 >> (0x2F & 0x3F)) # SHR operation
ref_26949 = (ref_26911 ^ ref_26927) # MOV operation
ref_26951 = (((sx(0x40, ref_26949) * sx(0x40, ((((((((0x9D) << 8 | 0xDF) << 8 | 0xEA) << 8 | 0x8) << 8 | 0xEB) << 8 | 0x38) << 8 | 0x2D) << 8 | 0x69))) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_26965 = ref_26951 # MOV operation
ref_26982 = ref_26965 # MOV operation
ref_27000 = ref_26982 # MOV operation
ref_27019 = ref_27000 # MOV operation
ref_39895 = ref_27019 # MOV operation
ref_44172 = ref_39895 # MOV operation
ref_57032 = ref_44172 # MOV operation
ref_61306 = ref_57032 # MOV operation
ref_61344 = ref_61306 # MOV operation
ref_61356 = ref_61344 # MOV operation
ref_61358 = ref_61356 # MOV operation

print ref_61358 & 0xffffffffffffffff
