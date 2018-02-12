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
ref_5199 = ref_290 # MOVZX operation
ref_5201 = (ref_5199 & 0xFF) # MOVZX operation
ref_5203 = (((ref_5201 & 0xFFFFFFFF) << (0x8 & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_5210 = (ref_5203 & 0xFFFFFFFF) # MOV operation
ref_5214 = ref_291 # MOVZX operation
ref_5216 = (ref_5214 & 0xFF) # MOVZX operation
ref_5218 = (((ref_5216 & 0xFFFFFFFF) + (ref_5210 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_5256 = ref_288 # MOVZX operation
ref_5258 = (ref_5256 & 0xFF) # MOVZX operation
ref_5260 = (((ref_5258 & 0xFFFFFFFF) << (0x8 & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_5267 = (ref_5260 & 0xFFFFFFFF) # MOV operation
ref_5279 = ref_289 # MOVZX operation
ref_5281 = (ref_5279 & 0xFF) # MOVZX operation
ref_5283 = (((ref_5281 & 0xFFFFFFFF) + (ref_5267 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_5291 = (((ref_5283 & 0xFFFFFFFF) << (0xB & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_5298 = ((ref_5291 & 0xFFFFFFFF) ^ ((((((0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x8) + (ref_5218 & 0xFFFFFFFF)) & 0xFFFFFFFF)) # XOR operation
ref_5311 = ((((((0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x8) + (ref_5218 & 0xFFFFFFFF)) & 0xFFFFFFFF) # MOV operation
ref_5313 = (((ref_5311 & 0xFFFFFFFF) << (0x10 & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_5320 = ((ref_5313 & 0xFFFFFFFF) ^ (ref_5298 & 0xFFFFFFFF)) # XOR operation
ref_5349 = (ref_5320 & 0xFFFFFFFF) # MOV operation
ref_5351 = ((ref_5349 & 0xFFFFFFFF) >> (0xB & 0x1F)) # SHR operation
ref_5401 = ref_286 # MOVZX operation
ref_5403 = (ref_5401 & 0xFF) # MOVZX operation
ref_5405 = (((ref_5403 & 0xFFFFFFFF) << (0x8 & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_5412 = (ref_5405 & 0xFFFFFFFF) # MOV operation
ref_5416 = ref_287 # MOVZX operation
ref_5418 = (ref_5416 & 0xFF) # MOVZX operation
ref_5420 = (((ref_5418 & 0xFFFFFFFF) + (ref_5412 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_5458 = ref_284 # MOVZX operation
ref_5460 = (ref_5458 & 0xFF) # MOVZX operation
ref_5462 = (((ref_5460 & 0xFFFFFFFF) << (0x8 & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_5469 = (ref_5462 & 0xFFFFFFFF) # MOV operation
ref_5481 = ref_285 # MOVZX operation
ref_5483 = (ref_5481 & 0xFF) # MOVZX operation
ref_5485 = (((ref_5483 & 0xFFFFFFFF) + (ref_5469 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_5493 = (((ref_5485 & 0xFFFFFFFF) << (0xB & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_5500 = ((ref_5493 & 0xFFFFFFFF) ^ (((((ref_5320 & 0xFFFFFFFF) + (ref_5351 & 0xFFFFFFFF)) & 0xFFFFFFFF) + (ref_5420 & 0xFFFFFFFF)) & 0xFFFFFFFF)) # XOR operation
ref_5513 = (((((ref_5320 & 0xFFFFFFFF) + (ref_5351 & 0xFFFFFFFF)) & 0xFFFFFFFF) + (ref_5420 & 0xFFFFFFFF)) & 0xFFFFFFFF) # MOV operation
ref_5515 = (((ref_5513 & 0xFFFFFFFF) << (0x10 & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_5522 = ((ref_5515 & 0xFFFFFFFF) ^ (ref_5500 & 0xFFFFFFFF)) # XOR operation
ref_5551 = (ref_5522 & 0xFFFFFFFF) # MOV operation
ref_5553 = ((ref_5551 & 0xFFFFFFFF) >> (0xB & 0x1F)) # SHR operation
ref_5623 = (((ref_5522 & 0xFFFFFFFF) + (ref_5553 & 0xFFFFFFFF)) & 0xFFFFFFFF) # MOV operation
ref_5625 = (((ref_5623 & 0xFFFFFFFF) << (0x3 & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_5643 = ((((ref_5522 & 0xFFFFFFFF) + (ref_5553 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_5625 & 0xFFFFFFFF)) # MOV operation
ref_5645 = ((ref_5643 & 0xFFFFFFFF) >> (0x5 & 0x1F)) # SHR operation
ref_5664 = ((((((ref_5522 & 0xFFFFFFFF) + (ref_5553 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_5625 & 0xFFFFFFFF)) + (ref_5645 & 0xFFFFFFFF)) & 0xFFFFFFFF) # MOV operation
ref_5666 = (((ref_5664 & 0xFFFFFFFF) << (0x4 & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_5684 = (((((((ref_5522 & 0xFFFFFFFF) + (ref_5553 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_5625 & 0xFFFFFFFF)) + (ref_5645 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_5666 & 0xFFFFFFFF)) # MOV operation
ref_5686 = ((ref_5684 & 0xFFFFFFFF) >> (0x11 & 0x1F)) # SHR operation
ref_5705 = (((((((((ref_5522 & 0xFFFFFFFF) + (ref_5553 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_5625 & 0xFFFFFFFF)) + (ref_5645 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_5666 & 0xFFFFFFFF)) + (ref_5686 & 0xFFFFFFFF)) & 0xFFFFFFFF) # MOV operation
ref_5707 = (((ref_5705 & 0xFFFFFFFF) << (0x19 & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_5725 = ((((((((((ref_5522 & 0xFFFFFFFF) + (ref_5553 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_5625 & 0xFFFFFFFF)) + (ref_5645 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_5666 & 0xFFFFFFFF)) + (ref_5686 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_5707 & 0xFFFFFFFF)) # MOV operation
ref_5727 = ((ref_5725 & 0xFFFFFFFF) >> (0x6 & 0x1F)) # SHR operation
ref_5746 = ((((((((((((ref_5522 & 0xFFFFFFFF) + (ref_5553 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_5625 & 0xFFFFFFFF)) + (ref_5645 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_5666 & 0xFFFFFFFF)) + (ref_5686 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_5707 & 0xFFFFFFFF)) + (ref_5727 & 0xFFFFFFFF)) & 0xFFFFFFFF) # MOV operation
ref_5759 = (ref_5746 & 0xFFFFFFFF) # MOV operation
ref_5921 = (ref_5759 & 0xFFFFFFFF) # MOV operation
ref_5951 = (ref_5921 & 0xFFFFFFFF) # MOV operation
ref_6161 = (ref_5951 & 0xFFFFFFFF) # MOV operation
ref_6275 = (ref_6161 & 0xFFFFFFFF) # MOV operation
ref_6309 = (ref_6275 & 0xFFFFFFFF) # MOV operation
ref_6321 = ref_6309 # MOV operation
ref_6323 = ref_6321 # MOV operation

print ref_6323 & 0xffffffffffffffff
