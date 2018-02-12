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
ref_463 = ((ref_407 >> 56) & 0xFF) # Byte reference - MOV operation
ref_464 = ((ref_407 >> 48) & 0xFF) # Byte reference - MOV operation
ref_465 = ((ref_407 >> 40) & 0xFF) # Byte reference - MOV operation
ref_466 = ((ref_407 >> 32) & 0xFF) # Byte reference - MOV operation
ref_467 = ((ref_407 >> 24) & 0xFF) # Byte reference - MOV operation
ref_468 = ((ref_407 >> 16) & 0xFF) # Byte reference - MOV operation
ref_469 = ((ref_407 >> 8) & 0xFF) # Byte reference - MOV operation
ref_470 = (ref_407 & 0xFF) # Byte reference - MOV operation
ref_6459 = ((((ref_467) << 8 | ref_468) << 8 | ref_469) << 8 | ref_470) # MOV operation
ref_6467 = (ref_6459 & 0xFFFFFFFF) # MOV operation
ref_6491 = (ref_6467 & 0xFFFFFFFF) # MOV operation
ref_6505 = (ref_6491 & 0xFFFFFFFF) # MOV operation
ref_6642 = ((((ref_463) << 8 | ref_464) << 8 | ref_465) << 8 | ref_466) # MOV operation
ref_6650 = (ref_6642 & 0xFFFFFFFF) # MOV operation
ref_6674 = (ref_6650 & 0xFFFFFFFF) # MOV operation
ref_6688 = (ref_6674 & 0xFFFFFFFF) # MOV operation
ref_6690 = ref_6505 # MOV operation
ref_6692 = ((0x0 + ((0x0 + ((ref_6690 * 0x8) & 0xFFFFFFFFFFFFFFFF)) & 0xFFFFFFFFFFFFFFFF)) & 0xFFFFFFFFFFFFFFFF) # LEA operation
ref_6696 = ((0x8 + ref_6692) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_6704 = ref_6688 # MOV operation
ref_6706 = ref_6696 # MOV operation
ref_6760 = ref_6706 # MOV operation
ref_6772 = ref_6704 # MOV operation
ref_6784 = ref_6760 # MOV operation
ref_6786 = ref_6772 # MOV operation
ref_6788 = ref_6784 # MOV operation
ref_6790 = ref_6786 # MOV operation
ref_6816 = ref_6788 # MOV operation
ref_6818 = ref_6790 # MOV operation
ref_6820 = ref_6818 # MOV operation
ref_6854 = ref_6816 # MOV operation
ref_6856 = ref_6820 # MOV operation
ref_6858 = (ref_6856 ^ ref_6854) # XOR operation
ref_6865 = (((sx(0x40, ref_6858) * sx(0x40, ((((((((0x9D) << 8 | 0xDF) << 8 | 0xEA) << 8 | 0x8) << 8 | 0xEB) << 8 | 0x38) << 8 | 0x2D) << 8 | 0x69))) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_6879 = ref_6865 # MOV operation
ref_6881 = (ref_6879 >> (0x2F & 0x3F)) # SHR operation
ref_6903 = ref_6820 # MOV operation
ref_6905 = (ref_6903 ^ (ref_6865 ^ ref_6881)) # XOR operation
ref_6912 = (((sx(0x40, ref_6905) * sx(0x40, ((((((((0x9D) << 8 | 0xDF) << 8 | 0xEA) << 8 | 0x8) << 8 | 0xEB) << 8 | 0x38) << 8 | 0x2D) << 8 | 0x69))) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_6926 = ref_6912 # MOV operation
ref_6928 = (ref_6926 >> (0x2F & 0x3F)) # SHR operation
ref_6950 = (ref_6912 ^ ref_6928) # MOV operation
ref_6952 = (((sx(0x40, ref_6950) * sx(0x40, ((((((((0x9D) << 8 | 0xDF) << 8 | 0xEA) << 8 | 0x8) << 8 | 0xEB) << 8 | 0x38) << 8 | 0x2D) << 8 | 0x69))) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_6966 = ref_6952 # MOV operation
ref_6983 = ref_6966 # MOV operation
ref_7001 = ref_6983 # MOV operation
ref_7020 = ref_7001 # MOV operation
ref_7972 = ref_7020 # MOV operation
ref_8276 = ref_7972 # MOV operation
ref_9173 = ref_8276 # MOV operation
ref_9413 = ref_9173 # MOV operation
ref_9454 = ref_9413 # MOV operation
ref_9466 = ref_9454 # MOV operation
ref_9468 = ref_9466 # MOV operation

print ref_9468 & 0xffffffffffffffff
