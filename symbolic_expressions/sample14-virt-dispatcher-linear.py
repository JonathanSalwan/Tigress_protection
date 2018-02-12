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
ref_6725 = ((((ref_456) << 8 | ref_457) << 8 | ref_458) << 8 | ref_459) # MOV operation
ref_6733 = (ref_6725 & 0xFFFFFFFF) # MOV operation
ref_6757 = (ref_6733 & 0xFFFFFFFF) # MOV operation
ref_6771 = (ref_6757 & 0xFFFFFFFF) # MOV operation
ref_6908 = ((((ref_452) << 8 | ref_453) << 8 | ref_454) << 8 | ref_455) # MOV operation
ref_6916 = (ref_6908 & 0xFFFFFFFF) # MOV operation
ref_6940 = (ref_6916 & 0xFFFFFFFF) # MOV operation
ref_6954 = (ref_6940 & 0xFFFFFFFF) # MOV operation
ref_6956 = ref_6771 # MOV operation
ref_6958 = ((0x0 + ((0x0 + ((ref_6956 * 0x8) & 0xFFFFFFFFFFFFFFFF)) & 0xFFFFFFFFFFFFFFFF)) & 0xFFFFFFFFFFFFFFFF) # LEA operation
ref_6962 = ((0x8 + ref_6958) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_6970 = ref_6954 # MOV operation
ref_6972 = ref_6962 # MOV operation
ref_7026 = ref_6972 # MOV operation
ref_7038 = ref_6970 # MOV operation
ref_7050 = ref_7026 # MOV operation
ref_7052 = ref_7038 # MOV operation
ref_7054 = ref_7050 # MOV operation
ref_7056 = ref_7052 # MOV operation
ref_7082 = ref_7054 # MOV operation
ref_7084 = ref_7056 # MOV operation
ref_7086 = ref_7084 # MOV operation
ref_7120 = ref_7082 # MOV operation
ref_7122 = ref_7086 # MOV operation
ref_7124 = (ref_7122 ^ ref_7120) # XOR operation
ref_7131 = (((sx(0x40, ref_7124) * sx(0x40, ((((((((0x9D) << 8 | 0xDF) << 8 | 0xEA) << 8 | 0x8) << 8 | 0xEB) << 8 | 0x38) << 8 | 0x2D) << 8 | 0x69))) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_7145 = ref_7131 # MOV operation
ref_7147 = (ref_7145 >> (0x2F & 0x3F)) # SHR operation
ref_7169 = ref_7086 # MOV operation
ref_7171 = (ref_7169 ^ (ref_7131 ^ ref_7147)) # XOR operation
ref_7178 = (((sx(0x40, ref_7171) * sx(0x40, ((((((((0x9D) << 8 | 0xDF) << 8 | 0xEA) << 8 | 0x8) << 8 | 0xEB) << 8 | 0x38) << 8 | 0x2D) << 8 | 0x69))) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_7192 = ref_7178 # MOV operation
ref_7194 = (ref_7192 >> (0x2F & 0x3F)) # SHR operation
ref_7216 = (ref_7178 ^ ref_7194) # MOV operation
ref_7218 = (((sx(0x40, ref_7216) * sx(0x40, ((((((((0x9D) << 8 | 0xDF) << 8 | 0xEA) << 8 | 0x8) << 8 | 0xEB) << 8 | 0x38) << 8 | 0x2D) << 8 | 0x69))) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_7232 = ref_7218 # MOV operation
ref_7249 = ref_7232 # MOV operation
ref_7267 = ref_7249 # MOV operation
ref_7286 = ref_7267 # MOV operation
ref_8365 = ref_7286 # MOV operation
ref_8862 = ref_8365 # MOV operation
ref_9941 = ref_8862 # MOV operation
ref_10478 = ref_9941 # MOV operation
ref_10516 = ref_10478 # MOV operation
ref_10528 = ref_10516 # MOV operation
ref_10530 = ref_10528 # MOV operation

print ref_10530 & 0xffffffffffffffff
