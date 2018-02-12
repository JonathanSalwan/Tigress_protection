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
ref_7384 = ((((ref_456) << 8 | ref_457) << 8 | ref_458) << 8 | ref_459) # MOV operation
ref_7392 = (ref_7384 & 0xFFFFFFFF) # MOV operation
ref_7416 = (ref_7392 & 0xFFFFFFFF) # MOV operation
ref_7430 = (ref_7416 & 0xFFFFFFFF) # MOV operation
ref_7567 = ((((ref_452) << 8 | ref_453) << 8 | ref_454) << 8 | ref_455) # MOV operation
ref_7575 = (ref_7567 & 0xFFFFFFFF) # MOV operation
ref_7599 = (ref_7575 & 0xFFFFFFFF) # MOV operation
ref_7613 = (ref_7599 & 0xFFFFFFFF) # MOV operation
ref_7615 = ref_7430 # MOV operation
ref_7617 = ((0x0 + ((0x0 + ((ref_7615 * 0x8) & 0xFFFFFFFFFFFFFFFF)) & 0xFFFFFFFFFFFFFFFF)) & 0xFFFFFFFFFFFFFFFF) # LEA operation
ref_7621 = ((0x8 + ref_7617) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_7629 = ref_7613 # MOV operation
ref_7631 = ref_7621 # MOV operation
ref_7685 = ref_7631 # MOV operation
ref_7697 = ref_7629 # MOV operation
ref_7709 = ref_7685 # MOV operation
ref_7711 = ref_7697 # MOV operation
ref_7713 = ref_7709 # MOV operation
ref_7715 = ref_7711 # MOV operation
ref_7741 = ref_7713 # MOV operation
ref_7743 = ref_7715 # MOV operation
ref_7745 = ref_7743 # MOV operation
ref_7779 = ref_7741 # MOV operation
ref_7781 = ref_7745 # MOV operation
ref_7783 = (ref_7781 ^ ref_7779) # XOR operation
ref_7790 = (((sx(0x40, ref_7783) * sx(0x40, ((((((((0x9D) << 8 | 0xDF) << 8 | 0xEA) << 8 | 0x8) << 8 | 0xEB) << 8 | 0x38) << 8 | 0x2D) << 8 | 0x69))) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_7804 = ref_7790 # MOV operation
ref_7806 = (ref_7804 >> (0x2F & 0x3F)) # SHR operation
ref_7828 = ref_7745 # MOV operation
ref_7830 = (ref_7828 ^ (ref_7790 ^ ref_7806)) # XOR operation
ref_7837 = (((sx(0x40, ref_7830) * sx(0x40, ((((((((0x9D) << 8 | 0xDF) << 8 | 0xEA) << 8 | 0x8) << 8 | 0xEB) << 8 | 0x38) << 8 | 0x2D) << 8 | 0x69))) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_7851 = ref_7837 # MOV operation
ref_7853 = (ref_7851 >> (0x2F & 0x3F)) # SHR operation
ref_7875 = (ref_7837 ^ ref_7853) # MOV operation
ref_7877 = (((sx(0x40, ref_7875) * sx(0x40, ((((((((0x9D) << 8 | 0xDF) << 8 | 0xEA) << 8 | 0x8) << 8 | 0xEB) << 8 | 0x38) << 8 | 0x2D) << 8 | 0x69))) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_7891 = ref_7877 # MOV operation
ref_7908 = ref_7891 # MOV operation
ref_7926 = ref_7908 # MOV operation
ref_7945 = ref_7926 # MOV operation
ref_8287 = ref_7945 # MOV operation
ref_8386 = ref_8287 # MOV operation
ref_8712 = ref_8386 # MOV operation
ref_8808 = ref_8712 # MOV operation
ref_8846 = ref_8808 # MOV operation
ref_8858 = ref_8846 # MOV operation
ref_8860 = ref_8858 # MOV operation

print ref_8860 & 0xffffffffffffffff
