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
ref_36853 = ((((ref_456) << 8 | ref_457) << 8 | ref_458) << 8 | ref_459) # MOV operation
ref_36861 = (ref_36853 & 0xFFFFFFFF) # MOV operation
ref_36885 = (ref_36861 & 0xFFFFFFFF) # MOV operation
ref_36899 = (ref_36885 & 0xFFFFFFFF) # MOV operation
ref_37036 = ((((ref_452) << 8 | ref_453) << 8 | ref_454) << 8 | ref_455) # MOV operation
ref_37044 = (ref_37036 & 0xFFFFFFFF) # MOV operation
ref_37068 = (ref_37044 & 0xFFFFFFFF) # MOV operation
ref_37082 = (ref_37068 & 0xFFFFFFFF) # MOV operation
ref_37084 = ref_36899 # MOV operation
ref_37086 = ((0x0 + ((0x0 + ((ref_37084 * 0x8) & 0xFFFFFFFFFFFFFFFF)) & 0xFFFFFFFFFFFFFFFF)) & 0xFFFFFFFFFFFFFFFF) # LEA operation
ref_37090 = ((0x8 + ref_37086) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_37098 = ref_37082 # MOV operation
ref_37100 = ref_37090 # MOV operation
ref_37154 = ref_37100 # MOV operation
ref_37166 = ref_37098 # MOV operation
ref_37178 = ref_37154 # MOV operation
ref_37180 = ref_37166 # MOV operation
ref_37182 = ref_37178 # MOV operation
ref_37184 = ref_37180 # MOV operation
ref_37210 = ref_37182 # MOV operation
ref_37212 = ref_37184 # MOV operation
ref_37214 = ref_37212 # MOV operation
ref_37248 = ref_37210 # MOV operation
ref_37250 = ref_37214 # MOV operation
ref_37252 = (ref_37250 ^ ref_37248) # XOR operation
ref_37259 = (((sx(0x40, ref_37252) * sx(0x40, ((((((((0x9D) << 8 | 0xDF) << 8 | 0xEA) << 8 | 0x8) << 8 | 0xEB) << 8 | 0x38) << 8 | 0x2D) << 8 | 0x69))) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_37273 = ref_37259 # MOV operation
ref_37275 = (ref_37273 >> (0x2F & 0x3F)) # SHR operation
ref_37297 = ref_37214 # MOV operation
ref_37299 = (ref_37297 ^ (ref_37259 ^ ref_37275)) # XOR operation
ref_37306 = (((sx(0x40, ref_37299) * sx(0x40, ((((((((0x9D) << 8 | 0xDF) << 8 | 0xEA) << 8 | 0x8) << 8 | 0xEB) << 8 | 0x38) << 8 | 0x2D) << 8 | 0x69))) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_37320 = ref_37306 # MOV operation
ref_37322 = (ref_37320 >> (0x2F & 0x3F)) # SHR operation
ref_37344 = (ref_37306 ^ ref_37322) # MOV operation
ref_37346 = (((sx(0x40, ref_37344) * sx(0x40, ((((((((0x9D) << 8 | 0xDF) << 8 | 0xEA) << 8 | 0x8) << 8 | 0xEB) << 8 | 0x38) << 8 | 0x2D) << 8 | 0x69))) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_37360 = ref_37346 # MOV operation
ref_37377 = ref_37360 # MOV operation
ref_37395 = ref_37377 # MOV operation
ref_37414 = ref_37395 # MOV operation
ref_56527 = ref_37414 # MOV operation
ref_62883 = ref_56527 # MOV operation
ref_81980 = ref_62883 # MOV operation
ref_88333 = ref_81980 # MOV operation
ref_88371 = ref_88333 # MOV operation
ref_88383 = ref_88371 # MOV operation
ref_88385 = ref_88383 # MOV operation

print ref_88385 & 0xffffffffffffffff
