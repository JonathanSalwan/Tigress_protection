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
ref_7189 = ref_290 # MOVZX operation
ref_7191 = (ref_7189 & 0xFF) # MOVZX operation
ref_7193 = (((ref_7191 & 0xFFFFFFFF) << (0x8 & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_7200 = (ref_7193 & 0xFFFFFFFF) # MOV operation
ref_7204 = ref_291 # MOVZX operation
ref_7206 = (ref_7204 & 0xFF) # MOVZX operation
ref_7208 = (((ref_7206 & 0xFFFFFFFF) + (ref_7200 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_7246 = ref_288 # MOVZX operation
ref_7248 = (ref_7246 & 0xFF) # MOVZX operation
ref_7250 = (((ref_7248 & 0xFFFFFFFF) << (0x8 & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_7257 = (ref_7250 & 0xFFFFFFFF) # MOV operation
ref_7269 = ref_289 # MOVZX operation
ref_7271 = (ref_7269 & 0xFF) # MOVZX operation
ref_7273 = (((ref_7271 & 0xFFFFFFFF) + (ref_7257 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_7281 = (((ref_7273 & 0xFFFFFFFF) << (0xB & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_7288 = ((ref_7281 & 0xFFFFFFFF) ^ ((((((0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x8) + (ref_7208 & 0xFFFFFFFF)) & 0xFFFFFFFF)) # XOR operation
ref_7301 = ((((((0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x8) + (ref_7208 & 0xFFFFFFFF)) & 0xFFFFFFFF) # MOV operation
ref_7303 = (((ref_7301 & 0xFFFFFFFF) << (0x10 & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_7310 = ((ref_7303 & 0xFFFFFFFF) ^ (ref_7288 & 0xFFFFFFFF)) # XOR operation
ref_7339 = (ref_7310 & 0xFFFFFFFF) # MOV operation
ref_7341 = ((ref_7339 & 0xFFFFFFFF) >> (0xB & 0x1F)) # SHR operation
ref_7391 = ref_286 # MOVZX operation
ref_7393 = (ref_7391 & 0xFF) # MOVZX operation
ref_7395 = (((ref_7393 & 0xFFFFFFFF) << (0x8 & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_7402 = (ref_7395 & 0xFFFFFFFF) # MOV operation
ref_7406 = ref_287 # MOVZX operation
ref_7408 = (ref_7406 & 0xFF) # MOVZX operation
ref_7410 = (((ref_7408 & 0xFFFFFFFF) + (ref_7402 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_7448 = ref_284 # MOVZX operation
ref_7450 = (ref_7448 & 0xFF) # MOVZX operation
ref_7452 = (((ref_7450 & 0xFFFFFFFF) << (0x8 & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_7459 = (ref_7452 & 0xFFFFFFFF) # MOV operation
ref_7471 = ref_285 # MOVZX operation
ref_7473 = (ref_7471 & 0xFF) # MOVZX operation
ref_7475 = (((ref_7473 & 0xFFFFFFFF) + (ref_7459 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_7483 = (((ref_7475 & 0xFFFFFFFF) << (0xB & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_7490 = ((ref_7483 & 0xFFFFFFFF) ^ (((((ref_7310 & 0xFFFFFFFF) + (ref_7341 & 0xFFFFFFFF)) & 0xFFFFFFFF) + (ref_7410 & 0xFFFFFFFF)) & 0xFFFFFFFF)) # XOR operation
ref_7503 = (((((ref_7310 & 0xFFFFFFFF) + (ref_7341 & 0xFFFFFFFF)) & 0xFFFFFFFF) + (ref_7410 & 0xFFFFFFFF)) & 0xFFFFFFFF) # MOV operation
ref_7505 = (((ref_7503 & 0xFFFFFFFF) << (0x10 & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_7512 = ((ref_7505 & 0xFFFFFFFF) ^ (ref_7490 & 0xFFFFFFFF)) # XOR operation
ref_7541 = (ref_7512 & 0xFFFFFFFF) # MOV operation
ref_7543 = ((ref_7541 & 0xFFFFFFFF) >> (0xB & 0x1F)) # SHR operation
ref_7613 = (((ref_7512 & 0xFFFFFFFF) + (ref_7543 & 0xFFFFFFFF)) & 0xFFFFFFFF) # MOV operation
ref_7615 = (((ref_7613 & 0xFFFFFFFF) << (0x3 & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_7633 = ((((ref_7512 & 0xFFFFFFFF) + (ref_7543 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_7615 & 0xFFFFFFFF)) # MOV operation
ref_7635 = ((ref_7633 & 0xFFFFFFFF) >> (0x5 & 0x1F)) # SHR operation
ref_7654 = ((((((ref_7512 & 0xFFFFFFFF) + (ref_7543 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_7615 & 0xFFFFFFFF)) + (ref_7635 & 0xFFFFFFFF)) & 0xFFFFFFFF) # MOV operation
ref_7656 = (((ref_7654 & 0xFFFFFFFF) << (0x4 & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_7674 = (((((((ref_7512 & 0xFFFFFFFF) + (ref_7543 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_7615 & 0xFFFFFFFF)) + (ref_7635 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_7656 & 0xFFFFFFFF)) # MOV operation
ref_7676 = ((ref_7674 & 0xFFFFFFFF) >> (0x11 & 0x1F)) # SHR operation
ref_7695 = (((((((((ref_7512 & 0xFFFFFFFF) + (ref_7543 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_7615 & 0xFFFFFFFF)) + (ref_7635 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_7656 & 0xFFFFFFFF)) + (ref_7676 & 0xFFFFFFFF)) & 0xFFFFFFFF) # MOV operation
ref_7697 = (((ref_7695 & 0xFFFFFFFF) << (0x19 & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_7715 = ((((((((((ref_7512 & 0xFFFFFFFF) + (ref_7543 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_7615 & 0xFFFFFFFF)) + (ref_7635 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_7656 & 0xFFFFFFFF)) + (ref_7676 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_7697 & 0xFFFFFFFF)) # MOV operation
ref_7717 = ((ref_7715 & 0xFFFFFFFF) >> (0x6 & 0x1F)) # SHR operation
ref_7736 = ((((((((((((ref_7512 & 0xFFFFFFFF) + (ref_7543 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_7615 & 0xFFFFFFFF)) + (ref_7635 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_7656 & 0xFFFFFFFF)) + (ref_7676 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_7697 & 0xFFFFFFFF)) + (ref_7717 & 0xFFFFFFFF)) & 0xFFFFFFFF) # MOV operation
ref_7749 = (ref_7736 & 0xFFFFFFFF) # MOV operation
ref_8969 = (ref_7749 & 0xFFFFFFFF) # MOV operation
ref_9434 = (ref_8969 & 0xFFFFFFFF) # MOV operation
ref_10863 = (ref_9434 & 0xFFFFFFFF) # MOV operation
ref_11426 = (ref_10863 & 0xFFFFFFFF) # MOV operation
ref_11460 = (ref_11426 & 0xFFFFFFFF) # MOV operation
ref_11472 = ref_11460 # MOV operation
ref_11474 = ref_11472 # MOV operation

print ref_11474 & 0xffffffffffffffff
