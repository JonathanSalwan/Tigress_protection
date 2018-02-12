#!/usr/bin/env python2
## -*- coding: utf-8 -*-

import sys

def sx(bits, value):
    sign_bit = 1 << (bits - 1)
    return (value & (sign_bit - 1)) - (value & sign_bit)

SymVar_0 = int(sys.argv[1])
ref_286 = SymVar_0
ref_297 = ref_286 # MOV operation
ref_309 = ref_297 # MOV operation
ref_311 = ref_309 # MOV operation
ref_7501 = ref_311 # MOV operation
ref_7590 = ref_7501 # MOV operation
ref_7667 = (ref_7590 & 0xFFFFFFFF) # MOV operation
ref_8367 = (ref_7667 & 0xFFFFFFFF) # MOV operation
ref_8371 = (ref_8367 & 0xFFFFFFFF) # MOV operation
ref_8405 = (((ref_8371 & 0xFFFFFFFF) >> 24) & 0xFF) # Byte reference - MOV operation
ref_8406 = (((ref_8371 & 0xFFFFFFFF) >> 16) & 0xFF) # Byte reference - MOV operation
ref_8407 = (((ref_8371 & 0xFFFFFFFF) >> 8) & 0xFF) # Byte reference - MOV operation
ref_8408 = ((ref_8371 & 0xFFFFFFFF) & 0xFF) # Byte reference - MOV operation
ref_8459 = ref_8408 # MOVZX operation
ref_8461 = (ref_8459 & 0xFF) # MOVZX operation
ref_8467 = (ref_8461 & 0xFFFFFFFF) # MOV operation
ref_8493 = (ref_8467 & 0xFFFFFFFF) # MOV operation
ref_8503 = (ref_8493 & 0xFF) # MOVZX operation
ref_8505 = ((ref_8503 & 0xFFFFFFFF) ^ ((((0x81) << 8 | 0x1C) << 8 | 0x9D) << 8 | 0xC5)) # XOR operation
ref_8512 = (ref_8505 & 0xFFFFFFFF) # MOV operation
ref_8516 = (((sx(0x20, 0x1000193) * sx(0x20, (ref_8512 & 0xFFFFFFFF))) & 0xFFFFFFFFFFFFFFFF) & 0xFFFFFFFF) # IMUL operation
ref_8561 = ref_8407 # MOVZX operation
ref_8563 = (ref_8561 & 0xFF) # MOVZX operation
ref_8565 = (ref_8516 & 0xFFFFFFFF) # MOV operation
ref_8567 = (ref_8565 & 0xFFFFFFFF) # MOV operation
ref_8569 = (ref_8563 & 0xFFFFFFFF) # MOV operation
ref_8595 = (ref_8569 & 0xFFFFFFFF) # MOV operation
ref_8605 = (ref_8595 & 0xFF) # MOVZX operation
ref_8607 = ((ref_8605 & 0xFFFFFFFF) ^ (ref_8567 & 0xFFFFFFFF)) # XOR operation
ref_8614 = (ref_8607 & 0xFFFFFFFF) # MOV operation
ref_8618 = (((sx(0x20, 0x1000193) * sx(0x20, (ref_8614 & 0xFFFFFFFF))) & 0xFFFFFFFFFFFFFFFF) & 0xFFFFFFFF) # IMUL operation
ref_8663 = ref_8406 # MOVZX operation
ref_8665 = (ref_8663 & 0xFF) # MOVZX operation
ref_8667 = (ref_8618 & 0xFFFFFFFF) # MOV operation
ref_8669 = (ref_8667 & 0xFFFFFFFF) # MOV operation
ref_8671 = (ref_8665 & 0xFFFFFFFF) # MOV operation
ref_8697 = (ref_8671 & 0xFFFFFFFF) # MOV operation
ref_8707 = (ref_8697 & 0xFF) # MOVZX operation
ref_8709 = ((ref_8707 & 0xFFFFFFFF) ^ (ref_8669 & 0xFFFFFFFF)) # XOR operation
ref_8716 = (ref_8709 & 0xFFFFFFFF) # MOV operation
ref_8720 = (((sx(0x20, 0x1000193) * sx(0x20, (ref_8716 & 0xFFFFFFFF))) & 0xFFFFFFFFFFFFFFFF) & 0xFFFFFFFF) # IMUL operation
ref_8737 = ref_8405 # MOVZX operation
ref_8739 = (ref_8737 & 0xFF) # MOVZX operation
ref_8741 = (ref_8720 & 0xFFFFFFFF) # MOV operation
ref_8743 = (ref_8741 & 0xFFFFFFFF) # MOV operation
ref_8745 = (ref_8739 & 0xFFFFFFFF) # MOV operation
ref_8771 = (ref_8745 & 0xFFFFFFFF) # MOV operation
ref_8781 = (ref_8771 & 0xFF) # MOVZX operation
ref_8783 = ((ref_8781 & 0xFFFFFFFF) ^ (ref_8743 & 0xFFFFFFFF)) # XOR operation
ref_8790 = (ref_8783 & 0xFFFFFFFF) # MOV operation
ref_8794 = (((sx(0x20, 0x1000193) * sx(0x20, (ref_8790 & 0xFFFFFFFF))) & 0xFFFFFFFFFFFFFFFF) & 0xFFFFFFFF) # IMUL operation
ref_8809 = (ref_8794 & 0xFFFFFFFF) # MOV operation
ref_9227 = (ref_8809 & 0xFFFFFFFF) # MOV operation
ref_9304 = (ref_9227 & 0xFFFFFFFF) # MOV operation
ref_9626 = (ref_9304 & 0xFFFFFFFF) # MOV operation
ref_9709 = (ref_9626 & 0xFFFFFFFF) # MOV operation
ref_9743 = (ref_9709 & 0xFFFFFFFF) # MOV operation
ref_9755 = ref_9743 # MOV operation
ref_9757 = ref_9755 # MOV operation

print ref_9757 & 0xffffffffffffffff
