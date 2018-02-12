#!/usr/bin/env python2
## -*- coding: utf-8 -*-

import sys

def sx(bits, value):
    sign_bit = 1 << (bits - 1)
    return (value & (sign_bit - 1)) - (value & sign_bit)

SymVar_0 = int(sys.argv[1])
ref_214 = SymVar_0
ref_225 = ref_214 # MOV operation
ref_237 = ref_225 # MOV operation
ref_239 = ref_237 # MOV operation
ref_284 = ((ref_239 >> 56) & 0xFF) # Byte reference - MOV operation
ref_285 = ((ref_239 >> 48) & 0xFF) # Byte reference - MOV operation
ref_286 = ((ref_239 >> 40) & 0xFF) # Byte reference - MOV operation
ref_287 = ((ref_239 >> 32) & 0xFF) # Byte reference - MOV operation
ref_288 = ((ref_239 >> 24) & 0xFF) # Byte reference - MOV operation
ref_289 = ((ref_239 >> 16) & 0xFF) # Byte reference - MOV operation
ref_290 = ((ref_239 >> 8) & 0xFF) # Byte reference - MOV operation
ref_291 = (ref_239 & 0xFF) # Byte reference - MOV operation
ref_26198 = ref_290 # MOVZX operation
ref_26200 = (ref_26198 & 0xFF) # MOVZX operation
ref_26202 = (((ref_26200 & 0xFFFFFFFF) << (0x8 & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_26209 = (ref_26202 & 0xFFFFFFFF) # MOV operation
ref_26213 = ref_291 # MOVZX operation
ref_26215 = (ref_26213 & 0xFF) # MOVZX operation
ref_26217 = (((ref_26215 & 0xFFFFFFFF) + (ref_26209 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_26255 = ref_288 # MOVZX operation
ref_26257 = (ref_26255 & 0xFF) # MOVZX operation
ref_26259 = (((ref_26257 & 0xFFFFFFFF) << (0x8 & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_26266 = (ref_26259 & 0xFFFFFFFF) # MOV operation
ref_26278 = ref_289 # MOVZX operation
ref_26280 = (ref_26278 & 0xFF) # MOVZX operation
ref_26282 = (((ref_26280 & 0xFFFFFFFF) + (ref_26266 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_26290 = (((ref_26282 & 0xFFFFFFFF) << (0xB & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_26297 = ((ref_26290 & 0xFFFFFFFF) ^ ((((((0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x8) + (ref_26217 & 0xFFFFFFFF)) & 0xFFFFFFFF)) # XOR operation
ref_26310 = ((((((0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x8) + (ref_26217 & 0xFFFFFFFF)) & 0xFFFFFFFF) # MOV operation
ref_26312 = (((ref_26310 & 0xFFFFFFFF) << (0x10 & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_26319 = ((ref_26312 & 0xFFFFFFFF) ^ (ref_26297 & 0xFFFFFFFF)) # XOR operation
ref_26348 = (ref_26319 & 0xFFFFFFFF) # MOV operation
ref_26350 = ((ref_26348 & 0xFFFFFFFF) >> (0xB & 0x1F)) # SHR operation
ref_26400 = ref_286 # MOVZX operation
ref_26402 = (ref_26400 & 0xFF) # MOVZX operation
ref_26404 = (((ref_26402 & 0xFFFFFFFF) << (0x8 & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_26411 = (ref_26404 & 0xFFFFFFFF) # MOV operation
ref_26415 = ref_287 # MOVZX operation
ref_26417 = (ref_26415 & 0xFF) # MOVZX operation
ref_26419 = (((ref_26417 & 0xFFFFFFFF) + (ref_26411 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_26457 = ref_284 # MOVZX operation
ref_26459 = (ref_26457 & 0xFF) # MOVZX operation
ref_26461 = (((ref_26459 & 0xFFFFFFFF) << (0x8 & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_26468 = (ref_26461 & 0xFFFFFFFF) # MOV operation
ref_26480 = ref_285 # MOVZX operation
ref_26482 = (ref_26480 & 0xFF) # MOVZX operation
ref_26484 = (((ref_26482 & 0xFFFFFFFF) + (ref_26468 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_26492 = (((ref_26484 & 0xFFFFFFFF) << (0xB & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_26499 = ((ref_26492 & 0xFFFFFFFF) ^ (((((ref_26319 & 0xFFFFFFFF) + (ref_26350 & 0xFFFFFFFF)) & 0xFFFFFFFF) + (ref_26419 & 0xFFFFFFFF)) & 0xFFFFFFFF)) # XOR operation
ref_26512 = (((((ref_26319 & 0xFFFFFFFF) + (ref_26350 & 0xFFFFFFFF)) & 0xFFFFFFFF) + (ref_26419 & 0xFFFFFFFF)) & 0xFFFFFFFF) # MOV operation
ref_26514 = (((ref_26512 & 0xFFFFFFFF) << (0x10 & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_26521 = ((ref_26514 & 0xFFFFFFFF) ^ (ref_26499 & 0xFFFFFFFF)) # XOR operation
ref_26550 = (ref_26521 & 0xFFFFFFFF) # MOV operation
ref_26552 = ((ref_26550 & 0xFFFFFFFF) >> (0xB & 0x1F)) # SHR operation
ref_26622 = (((ref_26521 & 0xFFFFFFFF) + (ref_26552 & 0xFFFFFFFF)) & 0xFFFFFFFF) # MOV operation
ref_26624 = (((ref_26622 & 0xFFFFFFFF) << (0x3 & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_26642 = ((((ref_26521 & 0xFFFFFFFF) + (ref_26552 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_26624 & 0xFFFFFFFF)) # MOV operation
ref_26644 = ((ref_26642 & 0xFFFFFFFF) >> (0x5 & 0x1F)) # SHR operation
ref_26663 = ((((((ref_26521 & 0xFFFFFFFF) + (ref_26552 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_26624 & 0xFFFFFFFF)) + (ref_26644 & 0xFFFFFFFF)) & 0xFFFFFFFF) # MOV operation
ref_26665 = (((ref_26663 & 0xFFFFFFFF) << (0x4 & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_26683 = (((((((ref_26521 & 0xFFFFFFFF) + (ref_26552 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_26624 & 0xFFFFFFFF)) + (ref_26644 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_26665 & 0xFFFFFFFF)) # MOV operation
ref_26685 = ((ref_26683 & 0xFFFFFFFF) >> (0x11 & 0x1F)) # SHR operation
ref_26704 = (((((((((ref_26521 & 0xFFFFFFFF) + (ref_26552 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_26624 & 0xFFFFFFFF)) + (ref_26644 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_26665 & 0xFFFFFFFF)) + (ref_26685 & 0xFFFFFFFF)) & 0xFFFFFFFF) # MOV operation
ref_26706 = (((ref_26704 & 0xFFFFFFFF) << (0x19 & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_26724 = ((((((((((ref_26521 & 0xFFFFFFFF) + (ref_26552 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_26624 & 0xFFFFFFFF)) + (ref_26644 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_26665 & 0xFFFFFFFF)) + (ref_26685 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_26706 & 0xFFFFFFFF)) # MOV operation
ref_26726 = ((ref_26724 & 0xFFFFFFFF) >> (0x6 & 0x1F)) # SHR operation
ref_26745 = ((((((((((((ref_26521 & 0xFFFFFFFF) + (ref_26552 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_26624 & 0xFFFFFFFF)) + (ref_26644 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_26665 & 0xFFFFFFFF)) + (ref_26685 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_26706 & 0xFFFFFFFF)) + (ref_26726 & 0xFFFFFFFF)) & 0xFFFFFFFF) # MOV operation
ref_26758 = (ref_26745 & 0xFFFFFFFF) # MOV operation
ref_39629 = (ref_26758 & 0xFFFFFFFF) # MOV operation
ref_43902 = (ref_39629 & 0xFFFFFFFF) # MOV operation
ref_56758 = (ref_43902 & 0xFFFFFFFF) # MOV operation
ref_61028 = (ref_56758 & 0xFFFFFFFF) # MOV operation
ref_61062 = (ref_61028 & 0xFFFFFFFF) # MOV operation
ref_61074 = ref_61062 # MOV operation
ref_61076 = ref_61074 # MOV operation

print ref_61076 & 0xffffffffffffffff
