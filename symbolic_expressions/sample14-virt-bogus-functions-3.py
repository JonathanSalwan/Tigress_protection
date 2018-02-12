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
ref_8097 = ((((ref_467) << 8 | ref_468) << 8 | ref_469) << 8 | ref_470) # MOV operation
ref_8105 = (ref_8097 & 0xFFFFFFFF) # MOV operation
ref_8129 = (ref_8105 & 0xFFFFFFFF) # MOV operation
ref_8143 = (ref_8129 & 0xFFFFFFFF) # MOV operation
ref_8280 = ((((ref_463) << 8 | ref_464) << 8 | ref_465) << 8 | ref_466) # MOV operation
ref_8288 = (ref_8280 & 0xFFFFFFFF) # MOV operation
ref_8312 = (ref_8288 & 0xFFFFFFFF) # MOV operation
ref_8326 = (ref_8312 & 0xFFFFFFFF) # MOV operation
ref_8328 = ref_8143 # MOV operation
ref_8330 = ((0x0 + ((0x0 + ((ref_8328 * 0x8) & 0xFFFFFFFFFFFFFFFF)) & 0xFFFFFFFFFFFFFFFF)) & 0xFFFFFFFFFFFFFFFF) # LEA operation
ref_8334 = ((0x8 + ref_8330) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_8342 = ref_8326 # MOV operation
ref_8344 = ref_8334 # MOV operation
ref_8398 = ref_8344 # MOV operation
ref_8410 = ref_8342 # MOV operation
ref_8422 = ref_8398 # MOV operation
ref_8424 = ref_8410 # MOV operation
ref_8426 = ref_8422 # MOV operation
ref_8428 = ref_8424 # MOV operation
ref_8454 = ref_8426 # MOV operation
ref_8456 = ref_8428 # MOV operation
ref_8458 = ref_8456 # MOV operation
ref_8492 = ref_8454 # MOV operation
ref_8494 = ref_8458 # MOV operation
ref_8496 = (ref_8494 ^ ref_8492) # XOR operation
ref_8503 = (((sx(0x40, ref_8496) * sx(0x40, ((((((((0x9D) << 8 | 0xDF) << 8 | 0xEA) << 8 | 0x8) << 8 | 0xEB) << 8 | 0x38) << 8 | 0x2D) << 8 | 0x69))) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_8517 = ref_8503 # MOV operation
ref_8519 = (ref_8517 >> (0x2F & 0x3F)) # SHR operation
ref_8541 = ref_8458 # MOV operation
ref_8543 = (ref_8541 ^ (ref_8503 ^ ref_8519)) # XOR operation
ref_8550 = (((sx(0x40, ref_8543) * sx(0x40, ((((((((0x9D) << 8 | 0xDF) << 8 | 0xEA) << 8 | 0x8) << 8 | 0xEB) << 8 | 0x38) << 8 | 0x2D) << 8 | 0x69))) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_8564 = ref_8550 # MOV operation
ref_8566 = (ref_8564 >> (0x2F & 0x3F)) # SHR operation
ref_8588 = (ref_8550 ^ ref_8566) # MOV operation
ref_8590 = (((sx(0x40, ref_8588) * sx(0x40, ((((((((0x9D) << 8 | 0xDF) << 8 | 0xEA) << 8 | 0x8) << 8 | 0xEB) << 8 | 0x38) << 8 | 0x2D) << 8 | 0x69))) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_8604 = ref_8590 # MOV operation
ref_8621 = ref_8604 # MOV operation
ref_8639 = ref_8621 # MOV operation
ref_8658 = ref_8639 # MOV operation
ref_11006 = ref_8658 # MOV operation
ref_11817 = ref_11006 # MOV operation
ref_14164 = ref_11817 # MOV operation
ref_14895 = ref_14164 # MOV operation
ref_14936 = ref_14895 # MOV operation
ref_14948 = ref_14936 # MOV operation
ref_14950 = ref_14948 # MOV operation

print ref_14950 & 0xffffffffffffffff
