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
ref_68243 = ((((ref_456) << 8 | ref_457) << 8 | ref_458) << 8 | ref_459) # MOV operation
ref_68251 = (ref_68243 & 0xFFFFFFFF) # MOV operation
ref_68275 = (ref_68251 & 0xFFFFFFFF) # MOV operation
ref_68289 = (ref_68275 & 0xFFFFFFFF) # MOV operation
ref_68426 = ((((ref_452) << 8 | ref_453) << 8 | ref_454) << 8 | ref_455) # MOV operation
ref_68434 = (ref_68426 & 0xFFFFFFFF) # MOV operation
ref_68458 = (ref_68434 & 0xFFFFFFFF) # MOV operation
ref_68472 = (ref_68458 & 0xFFFFFFFF) # MOV operation
ref_68474 = ref_68289 # MOV operation
ref_68476 = ((0x0 + ((0x0 + ((ref_68474 * 0x8) & 0xFFFFFFFFFFFFFFFF)) & 0xFFFFFFFFFFFFFFFF)) & 0xFFFFFFFFFFFFFFFF) # LEA operation
ref_68480 = ((0x8 + ref_68476) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_68488 = ref_68472 # MOV operation
ref_68490 = ref_68480 # MOV operation
ref_68544 = ref_68490 # MOV operation
ref_68556 = ref_68488 # MOV operation
ref_68568 = ref_68544 # MOV operation
ref_68570 = ref_68556 # MOV operation
ref_68572 = ref_68568 # MOV operation
ref_68574 = ref_68570 # MOV operation
ref_68600 = ref_68572 # MOV operation
ref_68602 = ref_68574 # MOV operation
ref_68604 = ref_68602 # MOV operation
ref_68638 = ref_68600 # MOV operation
ref_68640 = ref_68604 # MOV operation
ref_68642 = (ref_68640 ^ ref_68638) # XOR operation
ref_68649 = (((sx(0x40, ref_68642) * sx(0x40, ((((((((0x9D) << 8 | 0xDF) << 8 | 0xEA) << 8 | 0x8) << 8 | 0xEB) << 8 | 0x38) << 8 | 0x2D) << 8 | 0x69))) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_68663 = ref_68649 # MOV operation
ref_68665 = (ref_68663 >> (0x2F & 0x3F)) # SHR operation
ref_68687 = ref_68604 # MOV operation
ref_68689 = (ref_68687 ^ (ref_68649 ^ ref_68665)) # XOR operation
ref_68696 = (((sx(0x40, ref_68689) * sx(0x40, ((((((((0x9D) << 8 | 0xDF) << 8 | 0xEA) << 8 | 0x8) << 8 | 0xEB) << 8 | 0x38) << 8 | 0x2D) << 8 | 0x69))) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_68710 = ref_68696 # MOV operation
ref_68712 = (ref_68710 >> (0x2F & 0x3F)) # SHR operation
ref_68734 = (ref_68696 ^ ref_68712) # MOV operation
ref_68736 = (((sx(0x40, ref_68734) * sx(0x40, ((((((((0x9D) << 8 | 0xDF) << 8 | 0xEA) << 8 | 0x8) << 8 | 0xEB) << 8 | 0x38) << 8 | 0x2D) << 8 | 0x69))) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_68750 = ref_68736 # MOV operation
ref_68767 = ref_68750 # MOV operation
ref_68785 = ref_68767 # MOV operation
ref_68804 = ref_68785 # MOV operation
ref_69102 = ref_68804 # MOV operation
ref_70823 = ref_69102 # MOV operation
ref_109792 = ref_70823 # MOV operation
ref_112101 = ref_109792 # MOV operation
ref_118737 = ref_112101 # MOV operation
ref_121271 = ref_118737 # MOV operation
ref_153412 = ref_121271 # MOV operation
ref_155721 = ref_153412 # MOV operation
ref_162357 = ref_155721 # MOV operation
ref_162635 = ref_162357 # MOV operation
ref_163177 = ref_162635 # MOV operation
ref_163291 = ref_163177 # MOV operation
ref_163329 = ref_163291 # MOV operation
ref_163341 = ref_163329 # MOV operation
ref_163343 = ref_163341 # MOV operation

print ref_163343 & 0xffffffffffffffff
