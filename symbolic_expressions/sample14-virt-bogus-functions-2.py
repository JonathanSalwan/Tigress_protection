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
ref_7154 = ((((ref_467) << 8 | ref_468) << 8 | ref_469) << 8 | ref_470) # MOV operation
ref_7162 = (ref_7154 & 0xFFFFFFFF) # MOV operation
ref_7186 = (ref_7162 & 0xFFFFFFFF) # MOV operation
ref_7200 = (ref_7186 & 0xFFFFFFFF) # MOV operation
ref_7337 = ((((ref_463) << 8 | ref_464) << 8 | ref_465) << 8 | ref_466) # MOV operation
ref_7345 = (ref_7337 & 0xFFFFFFFF) # MOV operation
ref_7369 = (ref_7345 & 0xFFFFFFFF) # MOV operation
ref_7383 = (ref_7369 & 0xFFFFFFFF) # MOV operation
ref_7385 = ref_7200 # MOV operation
ref_7387 = ((0x0 + ((0x0 + ((ref_7385 * 0x8) & 0xFFFFFFFFFFFFFFFF)) & 0xFFFFFFFFFFFFFFFF)) & 0xFFFFFFFFFFFFFFFF) # LEA operation
ref_7391 = ((0x8 + ref_7387) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_7399 = ref_7383 # MOV operation
ref_7401 = ref_7391 # MOV operation
ref_7455 = ref_7401 # MOV operation
ref_7467 = ref_7399 # MOV operation
ref_7479 = ref_7455 # MOV operation
ref_7481 = ref_7467 # MOV operation
ref_7483 = ref_7479 # MOV operation
ref_7485 = ref_7481 # MOV operation
ref_7511 = ref_7483 # MOV operation
ref_7513 = ref_7485 # MOV operation
ref_7515 = ref_7513 # MOV operation
ref_7549 = ref_7511 # MOV operation
ref_7551 = ref_7515 # MOV operation
ref_7553 = (ref_7551 ^ ref_7549) # XOR operation
ref_7560 = (((sx(0x40, ref_7553) * sx(0x40, ((((((((0x9D) << 8 | 0xDF) << 8 | 0xEA) << 8 | 0x8) << 8 | 0xEB) << 8 | 0x38) << 8 | 0x2D) << 8 | 0x69))) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_7574 = ref_7560 # MOV operation
ref_7576 = (ref_7574 >> (0x2F & 0x3F)) # SHR operation
ref_7598 = ref_7515 # MOV operation
ref_7600 = (ref_7598 ^ (ref_7560 ^ ref_7576)) # XOR operation
ref_7607 = (((sx(0x40, ref_7600) * sx(0x40, ((((((((0x9D) << 8 | 0xDF) << 8 | 0xEA) << 8 | 0x8) << 8 | 0xEB) << 8 | 0x38) << 8 | 0x2D) << 8 | 0x69))) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_7621 = ref_7607 # MOV operation
ref_7623 = (ref_7621 >> (0x2F & 0x3F)) # SHR operation
ref_7645 = (ref_7607 ^ ref_7623) # MOV operation
ref_7647 = (((sx(0x40, ref_7645) * sx(0x40, ((((((((0x9D) << 8 | 0xDF) << 8 | 0xEA) << 8 | 0x8) << 8 | 0xEB) << 8 | 0x38) << 8 | 0x2D) << 8 | 0x69))) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_7661 = ref_7647 # MOV operation
ref_7678 = ref_7661 # MOV operation
ref_7696 = ref_7678 # MOV operation
ref_7715 = ref_7696 # MOV operation
ref_9218 = ref_7715 # MOV operation
ref_9653 = ref_9218 # MOV operation
ref_10966 = ref_9653 # MOV operation
ref_11253 = ref_10966 # MOV operation
ref_11294 = ref_11253 # MOV operation
ref_11306 = ref_11294 # MOV operation
ref_11308 = ref_11306 # MOV operation

print ref_11308 & 0xffffffffffffffff
