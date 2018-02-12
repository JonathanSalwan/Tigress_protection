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
ref_5334 = ref_290 # MOVZX operation
ref_5336 = (ref_5334 & 0xFF) # MOVZX operation
ref_5338 = (((ref_5336 & 0xFFFFFFFF) << (0x8 & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_5345 = (ref_5338 & 0xFFFFFFFF) # MOV operation
ref_5349 = ref_291 # MOVZX operation
ref_5351 = (ref_5349 & 0xFF) # MOVZX operation
ref_5353 = (((ref_5351 & 0xFFFFFFFF) + (ref_5345 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_5391 = ref_288 # MOVZX operation
ref_5393 = (ref_5391 & 0xFF) # MOVZX operation
ref_5395 = (((ref_5393 & 0xFFFFFFFF) << (0x8 & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_5402 = (ref_5395 & 0xFFFFFFFF) # MOV operation
ref_5414 = ref_289 # MOVZX operation
ref_5416 = (ref_5414 & 0xFF) # MOVZX operation
ref_5418 = (((ref_5416 & 0xFFFFFFFF) + (ref_5402 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_5426 = (((ref_5418 & 0xFFFFFFFF) << (0xB & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_5433 = ((ref_5426 & 0xFFFFFFFF) ^ ((((((0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x8) + (ref_5353 & 0xFFFFFFFF)) & 0xFFFFFFFF)) # XOR operation
ref_5446 = ((((((0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x8) + (ref_5353 & 0xFFFFFFFF)) & 0xFFFFFFFF) # MOV operation
ref_5448 = (((ref_5446 & 0xFFFFFFFF) << (0x10 & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_5455 = ((ref_5448 & 0xFFFFFFFF) ^ (ref_5433 & 0xFFFFFFFF)) # XOR operation
ref_5484 = (ref_5455 & 0xFFFFFFFF) # MOV operation
ref_5486 = ((ref_5484 & 0xFFFFFFFF) >> (0xB & 0x1F)) # SHR operation
ref_5536 = ref_286 # MOVZX operation
ref_5538 = (ref_5536 & 0xFF) # MOVZX operation
ref_5540 = (((ref_5538 & 0xFFFFFFFF) << (0x8 & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_5547 = (ref_5540 & 0xFFFFFFFF) # MOV operation
ref_5551 = ref_287 # MOVZX operation
ref_5553 = (ref_5551 & 0xFF) # MOVZX operation
ref_5555 = (((ref_5553 & 0xFFFFFFFF) + (ref_5547 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_5593 = ref_284 # MOVZX operation
ref_5595 = (ref_5593 & 0xFF) # MOVZX operation
ref_5597 = (((ref_5595 & 0xFFFFFFFF) << (0x8 & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_5604 = (ref_5597 & 0xFFFFFFFF) # MOV operation
ref_5616 = ref_285 # MOVZX operation
ref_5618 = (ref_5616 & 0xFF) # MOVZX operation
ref_5620 = (((ref_5618 & 0xFFFFFFFF) + (ref_5604 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_5628 = (((ref_5620 & 0xFFFFFFFF) << (0xB & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_5635 = ((ref_5628 & 0xFFFFFFFF) ^ (((((ref_5455 & 0xFFFFFFFF) + (ref_5486 & 0xFFFFFFFF)) & 0xFFFFFFFF) + (ref_5555 & 0xFFFFFFFF)) & 0xFFFFFFFF)) # XOR operation
ref_5648 = (((((ref_5455 & 0xFFFFFFFF) + (ref_5486 & 0xFFFFFFFF)) & 0xFFFFFFFF) + (ref_5555 & 0xFFFFFFFF)) & 0xFFFFFFFF) # MOV operation
ref_5650 = (((ref_5648 & 0xFFFFFFFF) << (0x10 & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_5657 = ((ref_5650 & 0xFFFFFFFF) ^ (ref_5635 & 0xFFFFFFFF)) # XOR operation
ref_5686 = (ref_5657 & 0xFFFFFFFF) # MOV operation
ref_5688 = ((ref_5686 & 0xFFFFFFFF) >> (0xB & 0x1F)) # SHR operation
ref_5758 = (((ref_5657 & 0xFFFFFFFF) + (ref_5688 & 0xFFFFFFFF)) & 0xFFFFFFFF) # MOV operation
ref_5760 = (((ref_5758 & 0xFFFFFFFF) << (0x3 & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_5778 = ((((ref_5657 & 0xFFFFFFFF) + (ref_5688 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_5760 & 0xFFFFFFFF)) # MOV operation
ref_5780 = ((ref_5778 & 0xFFFFFFFF) >> (0x5 & 0x1F)) # SHR operation
ref_5799 = ((((((ref_5657 & 0xFFFFFFFF) + (ref_5688 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_5760 & 0xFFFFFFFF)) + (ref_5780 & 0xFFFFFFFF)) & 0xFFFFFFFF) # MOV operation
ref_5801 = (((ref_5799 & 0xFFFFFFFF) << (0x4 & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_5819 = (((((((ref_5657 & 0xFFFFFFFF) + (ref_5688 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_5760 & 0xFFFFFFFF)) + (ref_5780 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_5801 & 0xFFFFFFFF)) # MOV operation
ref_5821 = ((ref_5819 & 0xFFFFFFFF) >> (0x11 & 0x1F)) # SHR operation
ref_5840 = (((((((((ref_5657 & 0xFFFFFFFF) + (ref_5688 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_5760 & 0xFFFFFFFF)) + (ref_5780 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_5801 & 0xFFFFFFFF)) + (ref_5821 & 0xFFFFFFFF)) & 0xFFFFFFFF) # MOV operation
ref_5842 = (((ref_5840 & 0xFFFFFFFF) << (0x19 & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_5860 = ((((((((((ref_5657 & 0xFFFFFFFF) + (ref_5688 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_5760 & 0xFFFFFFFF)) + (ref_5780 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_5801 & 0xFFFFFFFF)) + (ref_5821 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_5842 & 0xFFFFFFFF)) # MOV operation
ref_5862 = ((ref_5860 & 0xFFFFFFFF) >> (0x6 & 0x1F)) # SHR operation
ref_5881 = ((((((((((((ref_5657 & 0xFFFFFFFF) + (ref_5688 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_5760 & 0xFFFFFFFF)) + (ref_5780 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_5801 & 0xFFFFFFFF)) + (ref_5821 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_5842 & 0xFFFFFFFF)) + (ref_5862 & 0xFFFFFFFF)) & 0xFFFFFFFF) # MOV operation
ref_5894 = (ref_5881 & 0xFFFFFFFF) # MOV operation
ref_6264 = (ref_5894 & 0xFFFFFFFF) # MOV operation
ref_6349 = (ref_6264 & 0xFFFFFFFF) # MOV operation
ref_6722 = (ref_6349 & 0xFFFFFFFF) # MOV operation
ref_6804 = (ref_6722 & 0xFFFFFFFF) # MOV operation
ref_6838 = (ref_6804 & 0xFFFFFFFF) # MOV operation
ref_6850 = ref_6838 # MOV operation
ref_6852 = ref_6850 # MOV operation

print ref_6852 & 0xffffffffffffffff
