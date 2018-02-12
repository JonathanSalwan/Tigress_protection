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
ref_5326 = ref_290 # MOVZX operation
ref_5328 = (ref_5326 & 0xFF) # MOVZX operation
ref_5330 = (((ref_5328 & 0xFFFFFFFF) << (0x8 & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_5337 = (ref_5330 & 0xFFFFFFFF) # MOV operation
ref_5341 = ref_291 # MOVZX operation
ref_5343 = (ref_5341 & 0xFF) # MOVZX operation
ref_5345 = (((ref_5343 & 0xFFFFFFFF) + (ref_5337 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_5383 = ref_288 # MOVZX operation
ref_5385 = (ref_5383 & 0xFF) # MOVZX operation
ref_5387 = (((ref_5385 & 0xFFFFFFFF) << (0x8 & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_5394 = (ref_5387 & 0xFFFFFFFF) # MOV operation
ref_5406 = ref_289 # MOVZX operation
ref_5408 = (ref_5406 & 0xFF) # MOVZX operation
ref_5410 = (((ref_5408 & 0xFFFFFFFF) + (ref_5394 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_5418 = (((ref_5410 & 0xFFFFFFFF) << (0xB & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_5425 = ((ref_5418 & 0xFFFFFFFF) ^ ((((((0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x8) + (ref_5345 & 0xFFFFFFFF)) & 0xFFFFFFFF)) # XOR operation
ref_5438 = ((((((0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x8) + (ref_5345 & 0xFFFFFFFF)) & 0xFFFFFFFF) # MOV operation
ref_5440 = (((ref_5438 & 0xFFFFFFFF) << (0x10 & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_5447 = ((ref_5440 & 0xFFFFFFFF) ^ (ref_5425 & 0xFFFFFFFF)) # XOR operation
ref_5476 = (ref_5447 & 0xFFFFFFFF) # MOV operation
ref_5478 = ((ref_5476 & 0xFFFFFFFF) >> (0xB & 0x1F)) # SHR operation
ref_5528 = ref_286 # MOVZX operation
ref_5530 = (ref_5528 & 0xFF) # MOVZX operation
ref_5532 = (((ref_5530 & 0xFFFFFFFF) << (0x8 & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_5539 = (ref_5532 & 0xFFFFFFFF) # MOV operation
ref_5543 = ref_287 # MOVZX operation
ref_5545 = (ref_5543 & 0xFF) # MOVZX operation
ref_5547 = (((ref_5545 & 0xFFFFFFFF) + (ref_5539 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_5585 = ref_284 # MOVZX operation
ref_5587 = (ref_5585 & 0xFF) # MOVZX operation
ref_5589 = (((ref_5587 & 0xFFFFFFFF) << (0x8 & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_5596 = (ref_5589 & 0xFFFFFFFF) # MOV operation
ref_5608 = ref_285 # MOVZX operation
ref_5610 = (ref_5608 & 0xFF) # MOVZX operation
ref_5612 = (((ref_5610 & 0xFFFFFFFF) + (ref_5596 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_5620 = (((ref_5612 & 0xFFFFFFFF) << (0xB & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_5627 = ((ref_5620 & 0xFFFFFFFF) ^ (((((ref_5447 & 0xFFFFFFFF) + (ref_5478 & 0xFFFFFFFF)) & 0xFFFFFFFF) + (ref_5547 & 0xFFFFFFFF)) & 0xFFFFFFFF)) # XOR operation
ref_5640 = (((((ref_5447 & 0xFFFFFFFF) + (ref_5478 & 0xFFFFFFFF)) & 0xFFFFFFFF) + (ref_5547 & 0xFFFFFFFF)) & 0xFFFFFFFF) # MOV operation
ref_5642 = (((ref_5640 & 0xFFFFFFFF) << (0x10 & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_5649 = ((ref_5642 & 0xFFFFFFFF) ^ (ref_5627 & 0xFFFFFFFF)) # XOR operation
ref_5678 = (ref_5649 & 0xFFFFFFFF) # MOV operation
ref_5680 = ((ref_5678 & 0xFFFFFFFF) >> (0xB & 0x1F)) # SHR operation
ref_5750 = (((ref_5649 & 0xFFFFFFFF) + (ref_5680 & 0xFFFFFFFF)) & 0xFFFFFFFF) # MOV operation
ref_5752 = (((ref_5750 & 0xFFFFFFFF) << (0x3 & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_5770 = ((((ref_5649 & 0xFFFFFFFF) + (ref_5680 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_5752 & 0xFFFFFFFF)) # MOV operation
ref_5772 = ((ref_5770 & 0xFFFFFFFF) >> (0x5 & 0x1F)) # SHR operation
ref_5791 = ((((((ref_5649 & 0xFFFFFFFF) + (ref_5680 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_5752 & 0xFFFFFFFF)) + (ref_5772 & 0xFFFFFFFF)) & 0xFFFFFFFF) # MOV operation
ref_5793 = (((ref_5791 & 0xFFFFFFFF) << (0x4 & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_5811 = (((((((ref_5649 & 0xFFFFFFFF) + (ref_5680 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_5752 & 0xFFFFFFFF)) + (ref_5772 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_5793 & 0xFFFFFFFF)) # MOV operation
ref_5813 = ((ref_5811 & 0xFFFFFFFF) >> (0x11 & 0x1F)) # SHR operation
ref_5832 = (((((((((ref_5649 & 0xFFFFFFFF) + (ref_5680 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_5752 & 0xFFFFFFFF)) + (ref_5772 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_5793 & 0xFFFFFFFF)) + (ref_5813 & 0xFFFFFFFF)) & 0xFFFFFFFF) # MOV operation
ref_5834 = (((ref_5832 & 0xFFFFFFFF) << (0x19 & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_5852 = ((((((((((ref_5649 & 0xFFFFFFFF) + (ref_5680 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_5752 & 0xFFFFFFFF)) + (ref_5772 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_5793 & 0xFFFFFFFF)) + (ref_5813 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_5834 & 0xFFFFFFFF)) # MOV operation
ref_5854 = ((ref_5852 & 0xFFFFFFFF) >> (0x6 & 0x1F)) # SHR operation
ref_5873 = ((((((((((((ref_5649 & 0xFFFFFFFF) + (ref_5680 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_5752 & 0xFFFFFFFF)) + (ref_5772 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_5793 & 0xFFFFFFFF)) + (ref_5813 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_5834 & 0xFFFFFFFF)) + (ref_5854 & 0xFFFFFFFF)) & 0xFFFFFFFF) # MOV operation
ref_5886 = (ref_5873 & 0xFFFFFFFF) # MOV operation
ref_6120 = (ref_5886 & 0xFFFFFFFF) # MOV operation
ref_6342 = (ref_6120 & 0xFFFFFFFF) # MOV operation
ref_6668 = (ref_6342 & 0xFFFFFFFF) # MOV operation
ref_6786 = (ref_6668 & 0xFFFFFFFF) # MOV operation
ref_6820 = (ref_6786 & 0xFFFFFFFF) # MOV operation
ref_6832 = ref_6820 # MOV operation
ref_6834 = ref_6832 # MOV operation

print ref_6834 & 0xffffffffffffffff
