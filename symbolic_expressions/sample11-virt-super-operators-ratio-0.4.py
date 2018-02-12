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
ref_5302 = ref_290 # MOVZX operation
ref_5304 = (ref_5302 & 0xFF) # MOVZX operation
ref_5306 = (((ref_5304 & 0xFFFFFFFF) << (0x8 & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_5313 = (ref_5306 & 0xFFFFFFFF) # MOV operation
ref_5317 = ref_291 # MOVZX operation
ref_5319 = (ref_5317 & 0xFF) # MOVZX operation
ref_5321 = (((ref_5319 & 0xFFFFFFFF) + (ref_5313 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_5359 = ref_288 # MOVZX operation
ref_5361 = (ref_5359 & 0xFF) # MOVZX operation
ref_5363 = (((ref_5361 & 0xFFFFFFFF) << (0x8 & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_5370 = (ref_5363 & 0xFFFFFFFF) # MOV operation
ref_5382 = ref_289 # MOVZX operation
ref_5384 = (ref_5382 & 0xFF) # MOVZX operation
ref_5386 = (((ref_5384 & 0xFFFFFFFF) + (ref_5370 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_5394 = (((ref_5386 & 0xFFFFFFFF) << (0xB & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_5401 = ((ref_5394 & 0xFFFFFFFF) ^ ((((((0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x8) + (ref_5321 & 0xFFFFFFFF)) & 0xFFFFFFFF)) # XOR operation
ref_5414 = ((((((0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x8) + (ref_5321 & 0xFFFFFFFF)) & 0xFFFFFFFF) # MOV operation
ref_5416 = (((ref_5414 & 0xFFFFFFFF) << (0x10 & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_5423 = ((ref_5416 & 0xFFFFFFFF) ^ (ref_5401 & 0xFFFFFFFF)) # XOR operation
ref_5452 = (ref_5423 & 0xFFFFFFFF) # MOV operation
ref_5454 = ((ref_5452 & 0xFFFFFFFF) >> (0xB & 0x1F)) # SHR operation
ref_5504 = ref_286 # MOVZX operation
ref_5506 = (ref_5504 & 0xFF) # MOVZX operation
ref_5508 = (((ref_5506 & 0xFFFFFFFF) << (0x8 & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_5515 = (ref_5508 & 0xFFFFFFFF) # MOV operation
ref_5519 = ref_287 # MOVZX operation
ref_5521 = (ref_5519 & 0xFF) # MOVZX operation
ref_5523 = (((ref_5521 & 0xFFFFFFFF) + (ref_5515 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_5561 = ref_284 # MOVZX operation
ref_5563 = (ref_5561 & 0xFF) # MOVZX operation
ref_5565 = (((ref_5563 & 0xFFFFFFFF) << (0x8 & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_5572 = (ref_5565 & 0xFFFFFFFF) # MOV operation
ref_5584 = ref_285 # MOVZX operation
ref_5586 = (ref_5584 & 0xFF) # MOVZX operation
ref_5588 = (((ref_5586 & 0xFFFFFFFF) + (ref_5572 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_5596 = (((ref_5588 & 0xFFFFFFFF) << (0xB & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_5603 = ((ref_5596 & 0xFFFFFFFF) ^ (((((ref_5423 & 0xFFFFFFFF) + (ref_5454 & 0xFFFFFFFF)) & 0xFFFFFFFF) + (ref_5523 & 0xFFFFFFFF)) & 0xFFFFFFFF)) # XOR operation
ref_5616 = (((((ref_5423 & 0xFFFFFFFF) + (ref_5454 & 0xFFFFFFFF)) & 0xFFFFFFFF) + (ref_5523 & 0xFFFFFFFF)) & 0xFFFFFFFF) # MOV operation
ref_5618 = (((ref_5616 & 0xFFFFFFFF) << (0x10 & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_5625 = ((ref_5618 & 0xFFFFFFFF) ^ (ref_5603 & 0xFFFFFFFF)) # XOR operation
ref_5654 = (ref_5625 & 0xFFFFFFFF) # MOV operation
ref_5656 = ((ref_5654 & 0xFFFFFFFF) >> (0xB & 0x1F)) # SHR operation
ref_5726 = (((ref_5625 & 0xFFFFFFFF) + (ref_5656 & 0xFFFFFFFF)) & 0xFFFFFFFF) # MOV operation
ref_5728 = (((ref_5726 & 0xFFFFFFFF) << (0x3 & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_5746 = ((((ref_5625 & 0xFFFFFFFF) + (ref_5656 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_5728 & 0xFFFFFFFF)) # MOV operation
ref_5748 = ((ref_5746 & 0xFFFFFFFF) >> (0x5 & 0x1F)) # SHR operation
ref_5767 = ((((((ref_5625 & 0xFFFFFFFF) + (ref_5656 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_5728 & 0xFFFFFFFF)) + (ref_5748 & 0xFFFFFFFF)) & 0xFFFFFFFF) # MOV operation
ref_5769 = (((ref_5767 & 0xFFFFFFFF) << (0x4 & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_5787 = (((((((ref_5625 & 0xFFFFFFFF) + (ref_5656 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_5728 & 0xFFFFFFFF)) + (ref_5748 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_5769 & 0xFFFFFFFF)) # MOV operation
ref_5789 = ((ref_5787 & 0xFFFFFFFF) >> (0x11 & 0x1F)) # SHR operation
ref_5808 = (((((((((ref_5625 & 0xFFFFFFFF) + (ref_5656 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_5728 & 0xFFFFFFFF)) + (ref_5748 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_5769 & 0xFFFFFFFF)) + (ref_5789 & 0xFFFFFFFF)) & 0xFFFFFFFF) # MOV operation
ref_5810 = (((ref_5808 & 0xFFFFFFFF) << (0x19 & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_5828 = ((((((((((ref_5625 & 0xFFFFFFFF) + (ref_5656 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_5728 & 0xFFFFFFFF)) + (ref_5748 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_5769 & 0xFFFFFFFF)) + (ref_5789 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_5810 & 0xFFFFFFFF)) # MOV operation
ref_5830 = ((ref_5828 & 0xFFFFFFFF) >> (0x6 & 0x1F)) # SHR operation
ref_5849 = ((((((((((((ref_5625 & 0xFFFFFFFF) + (ref_5656 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_5728 & 0xFFFFFFFF)) + (ref_5748 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_5769 & 0xFFFFFFFF)) + (ref_5789 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_5810 & 0xFFFFFFFF)) + (ref_5830 & 0xFFFFFFFF)) & 0xFFFFFFFF) # MOV operation
ref_5862 = (ref_5849 & 0xFFFFFFFF) # MOV operation
ref_6199 = (ref_5862 & 0xFFFFFFFF) # MOV operation
ref_6294 = (ref_6199 & 0xFFFFFFFF) # MOV operation
ref_6616 = (ref_6294 & 0xFFFFFFFF) # MOV operation
ref_6708 = (ref_6616 & 0xFFFFFFFF) # MOV operation
ref_6742 = (ref_6708 & 0xFFFFFFFF) # MOV operation
ref_6754 = ref_6742 # MOV operation
ref_6756 = ref_6754 # MOV operation

print ref_6756 & 0xffffffffffffffff
