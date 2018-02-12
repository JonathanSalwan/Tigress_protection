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
ref_5299 = ref_290 # MOVZX operation
ref_5301 = (ref_5299 & 0xFF) # MOVZX operation
ref_5303 = (((ref_5301 & 0xFFFFFFFF) << (0x8 & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_5310 = (ref_5303 & 0xFFFFFFFF) # MOV operation
ref_5314 = ref_291 # MOVZX operation
ref_5316 = (ref_5314 & 0xFF) # MOVZX operation
ref_5318 = (((ref_5316 & 0xFFFFFFFF) + (ref_5310 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_5356 = ref_288 # MOVZX operation
ref_5358 = (ref_5356 & 0xFF) # MOVZX operation
ref_5360 = (((ref_5358 & 0xFFFFFFFF) << (0x8 & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_5367 = (ref_5360 & 0xFFFFFFFF) # MOV operation
ref_5379 = ref_289 # MOVZX operation
ref_5381 = (ref_5379 & 0xFF) # MOVZX operation
ref_5383 = (((ref_5381 & 0xFFFFFFFF) + (ref_5367 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_5391 = (((ref_5383 & 0xFFFFFFFF) << (0xB & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_5398 = ((ref_5391 & 0xFFFFFFFF) ^ ((((((0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x8) + (ref_5318 & 0xFFFFFFFF)) & 0xFFFFFFFF)) # XOR operation
ref_5411 = ((((((0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x8) + (ref_5318 & 0xFFFFFFFF)) & 0xFFFFFFFF) # MOV operation
ref_5413 = (((ref_5411 & 0xFFFFFFFF) << (0x10 & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_5420 = ((ref_5413 & 0xFFFFFFFF) ^ (ref_5398 & 0xFFFFFFFF)) # XOR operation
ref_5449 = (ref_5420 & 0xFFFFFFFF) # MOV operation
ref_5451 = ((ref_5449 & 0xFFFFFFFF) >> (0xB & 0x1F)) # SHR operation
ref_5501 = ref_286 # MOVZX operation
ref_5503 = (ref_5501 & 0xFF) # MOVZX operation
ref_5505 = (((ref_5503 & 0xFFFFFFFF) << (0x8 & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_5512 = (ref_5505 & 0xFFFFFFFF) # MOV operation
ref_5516 = ref_287 # MOVZX operation
ref_5518 = (ref_5516 & 0xFF) # MOVZX operation
ref_5520 = (((ref_5518 & 0xFFFFFFFF) + (ref_5512 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_5558 = ref_284 # MOVZX operation
ref_5560 = (ref_5558 & 0xFF) # MOVZX operation
ref_5562 = (((ref_5560 & 0xFFFFFFFF) << (0x8 & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_5569 = (ref_5562 & 0xFFFFFFFF) # MOV operation
ref_5581 = ref_285 # MOVZX operation
ref_5583 = (ref_5581 & 0xFF) # MOVZX operation
ref_5585 = (((ref_5583 & 0xFFFFFFFF) + (ref_5569 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_5593 = (((ref_5585 & 0xFFFFFFFF) << (0xB & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_5600 = ((ref_5593 & 0xFFFFFFFF) ^ (((((ref_5420 & 0xFFFFFFFF) + (ref_5451 & 0xFFFFFFFF)) & 0xFFFFFFFF) + (ref_5520 & 0xFFFFFFFF)) & 0xFFFFFFFF)) # XOR operation
ref_5613 = (((((ref_5420 & 0xFFFFFFFF) + (ref_5451 & 0xFFFFFFFF)) & 0xFFFFFFFF) + (ref_5520 & 0xFFFFFFFF)) & 0xFFFFFFFF) # MOV operation
ref_5615 = (((ref_5613 & 0xFFFFFFFF) << (0x10 & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_5622 = ((ref_5615 & 0xFFFFFFFF) ^ (ref_5600 & 0xFFFFFFFF)) # XOR operation
ref_5651 = (ref_5622 & 0xFFFFFFFF) # MOV operation
ref_5653 = ((ref_5651 & 0xFFFFFFFF) >> (0xB & 0x1F)) # SHR operation
ref_5723 = (((ref_5622 & 0xFFFFFFFF) + (ref_5653 & 0xFFFFFFFF)) & 0xFFFFFFFF) # MOV operation
ref_5725 = (((ref_5723 & 0xFFFFFFFF) << (0x3 & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_5743 = ((((ref_5622 & 0xFFFFFFFF) + (ref_5653 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_5725 & 0xFFFFFFFF)) # MOV operation
ref_5745 = ((ref_5743 & 0xFFFFFFFF) >> (0x5 & 0x1F)) # SHR operation
ref_5764 = ((((((ref_5622 & 0xFFFFFFFF) + (ref_5653 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_5725 & 0xFFFFFFFF)) + (ref_5745 & 0xFFFFFFFF)) & 0xFFFFFFFF) # MOV operation
ref_5766 = (((ref_5764 & 0xFFFFFFFF) << (0x4 & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_5784 = (((((((ref_5622 & 0xFFFFFFFF) + (ref_5653 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_5725 & 0xFFFFFFFF)) + (ref_5745 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_5766 & 0xFFFFFFFF)) # MOV operation
ref_5786 = ((ref_5784 & 0xFFFFFFFF) >> (0x11 & 0x1F)) # SHR operation
ref_5805 = (((((((((ref_5622 & 0xFFFFFFFF) + (ref_5653 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_5725 & 0xFFFFFFFF)) + (ref_5745 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_5766 & 0xFFFFFFFF)) + (ref_5786 & 0xFFFFFFFF)) & 0xFFFFFFFF) # MOV operation
ref_5807 = (((ref_5805 & 0xFFFFFFFF) << (0x19 & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_5825 = ((((((((((ref_5622 & 0xFFFFFFFF) + (ref_5653 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_5725 & 0xFFFFFFFF)) + (ref_5745 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_5766 & 0xFFFFFFFF)) + (ref_5786 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_5807 & 0xFFFFFFFF)) # MOV operation
ref_5827 = ((ref_5825 & 0xFFFFFFFF) >> (0x6 & 0x1F)) # SHR operation
ref_5846 = ((((((((((((ref_5622 & 0xFFFFFFFF) + (ref_5653 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_5725 & 0xFFFFFFFF)) + (ref_5745 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_5766 & 0xFFFFFFFF)) + (ref_5786 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_5807 & 0xFFFFFFFF)) + (ref_5827 & 0xFFFFFFFF)) & 0xFFFFFFFF) # MOV operation
ref_5859 = (ref_5846 & 0xFFFFFFFF) # MOV operation
ref_6086 = (ref_5859 & 0xFFFFFFFF) # MOV operation
ref_6294 = (ref_6086 & 0xFFFFFFFF) # MOV operation
ref_6598 = (ref_6294 & 0xFFFFFFFF) # MOV operation
ref_6666 = (ref_6598 & 0xFFFFFFFF) # MOV operation
ref_6700 = (ref_6666 & 0xFFFFFFFF) # MOV operation
ref_6712 = ref_6700 # MOV operation
ref_6714 = ref_6712 # MOV operation

print ref_6714 & 0xffffffffffffffff
