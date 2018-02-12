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
ref_16063 = ((((ref_456) << 8 | ref_457) << 8 | ref_458) << 8 | ref_459) # MOV operation
ref_16071 = (ref_16063 & 0xFFFFFFFF) # MOV operation
ref_16095 = (ref_16071 & 0xFFFFFFFF) # MOV operation
ref_16109 = (ref_16095 & 0xFFFFFFFF) # MOV operation
ref_16246 = ((((ref_452) << 8 | ref_453) << 8 | ref_454) << 8 | ref_455) # MOV operation
ref_16254 = (ref_16246 & 0xFFFFFFFF) # MOV operation
ref_16278 = (ref_16254 & 0xFFFFFFFF) # MOV operation
ref_16292 = (ref_16278 & 0xFFFFFFFF) # MOV operation
ref_16294 = ref_16109 # MOV operation
ref_16296 = ((0x0 + ((0x0 + ((ref_16294 * 0x8) & 0xFFFFFFFFFFFFFFFF)) & 0xFFFFFFFFFFFFFFFF)) & 0xFFFFFFFFFFFFFFFF) # LEA operation
ref_16300 = ((0x8 + ref_16296) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_16308 = ref_16292 # MOV operation
ref_16310 = ref_16300 # MOV operation
ref_16364 = ref_16310 # MOV operation
ref_16376 = ref_16308 # MOV operation
ref_16388 = ref_16364 # MOV operation
ref_16390 = ref_16376 # MOV operation
ref_16392 = ref_16388 # MOV operation
ref_16394 = ref_16390 # MOV operation
ref_16420 = ref_16392 # MOV operation
ref_16422 = ref_16394 # MOV operation
ref_16424 = ref_16422 # MOV operation
ref_16458 = ref_16420 # MOV operation
ref_16460 = ref_16424 # MOV operation
ref_16462 = (ref_16460 ^ ref_16458) # XOR operation
ref_16469 = (((sx(0x40, ref_16462) * sx(0x40, ((((((((0x9D) << 8 | 0xDF) << 8 | 0xEA) << 8 | 0x8) << 8 | 0xEB) << 8 | 0x38) << 8 | 0x2D) << 8 | 0x69))) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_16483 = ref_16469 # MOV operation
ref_16485 = (ref_16483 >> (0x2F & 0x3F)) # SHR operation
ref_16507 = ref_16424 # MOV operation
ref_16509 = (ref_16507 ^ (ref_16469 ^ ref_16485)) # XOR operation
ref_16516 = (((sx(0x40, ref_16509) * sx(0x40, ((((((((0x9D) << 8 | 0xDF) << 8 | 0xEA) << 8 | 0x8) << 8 | 0xEB) << 8 | 0x38) << 8 | 0x2D) << 8 | 0x69))) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_16530 = ref_16516 # MOV operation
ref_16532 = (ref_16530 >> (0x2F & 0x3F)) # SHR operation
ref_16554 = (ref_16516 ^ ref_16532) # MOV operation
ref_16556 = (((sx(0x40, ref_16554) * sx(0x40, ((((((((0x9D) << 8 | 0xDF) << 8 | 0xEA) << 8 | 0x8) << 8 | 0xEB) << 8 | 0x38) << 8 | 0x2D) << 8 | 0x69))) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_16570 = ref_16556 # MOV operation
ref_16587 = ref_16570 # MOV operation
ref_16605 = ref_16587 # MOV operation
ref_16624 = ref_16605 # MOV operation
ref_23263 = ref_16624 # MOV operation
ref_25461 = ref_23263 # MOV operation
ref_32084 = ref_25461 # MOV operation
ref_34279 = ref_32084 # MOV operation
ref_34317 = ref_34279 # MOV operation
ref_34329 = ref_34317 # MOV operation
ref_34331 = ref_34329 # MOV operation

print ref_34331 & 0xffffffffffffffff
