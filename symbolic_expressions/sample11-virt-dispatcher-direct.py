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
ref_5411 = ref_290 # MOVZX operation
ref_5413 = (ref_5411 & 0xFF) # MOVZX operation
ref_5415 = (((ref_5413 & 0xFFFFFFFF) << (0x8 & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_5422 = (ref_5415 & 0xFFFFFFFF) # MOV operation
ref_5426 = ref_291 # MOVZX operation
ref_5428 = (ref_5426 & 0xFF) # MOVZX operation
ref_5430 = (((ref_5428 & 0xFFFFFFFF) + (ref_5422 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_5468 = ref_288 # MOVZX operation
ref_5470 = (ref_5468 & 0xFF) # MOVZX operation
ref_5472 = (((ref_5470 & 0xFFFFFFFF) << (0x8 & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_5479 = (ref_5472 & 0xFFFFFFFF) # MOV operation
ref_5491 = ref_289 # MOVZX operation
ref_5493 = (ref_5491 & 0xFF) # MOVZX operation
ref_5495 = (((ref_5493 & 0xFFFFFFFF) + (ref_5479 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_5503 = (((ref_5495 & 0xFFFFFFFF) << (0xB & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_5510 = ((ref_5503 & 0xFFFFFFFF) ^ ((((((0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x8) + (ref_5430 & 0xFFFFFFFF)) & 0xFFFFFFFF)) # XOR operation
ref_5523 = ((((((0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x8) + (ref_5430 & 0xFFFFFFFF)) & 0xFFFFFFFF) # MOV operation
ref_5525 = (((ref_5523 & 0xFFFFFFFF) << (0x10 & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_5532 = ((ref_5525 & 0xFFFFFFFF) ^ (ref_5510 & 0xFFFFFFFF)) # XOR operation
ref_5561 = (ref_5532 & 0xFFFFFFFF) # MOV operation
ref_5563 = ((ref_5561 & 0xFFFFFFFF) >> (0xB & 0x1F)) # SHR operation
ref_5613 = ref_286 # MOVZX operation
ref_5615 = (ref_5613 & 0xFF) # MOVZX operation
ref_5617 = (((ref_5615 & 0xFFFFFFFF) << (0x8 & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_5624 = (ref_5617 & 0xFFFFFFFF) # MOV operation
ref_5628 = ref_287 # MOVZX operation
ref_5630 = (ref_5628 & 0xFF) # MOVZX operation
ref_5632 = (((ref_5630 & 0xFFFFFFFF) + (ref_5624 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_5670 = ref_284 # MOVZX operation
ref_5672 = (ref_5670 & 0xFF) # MOVZX operation
ref_5674 = (((ref_5672 & 0xFFFFFFFF) << (0x8 & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_5681 = (ref_5674 & 0xFFFFFFFF) # MOV operation
ref_5693 = ref_285 # MOVZX operation
ref_5695 = (ref_5693 & 0xFF) # MOVZX operation
ref_5697 = (((ref_5695 & 0xFFFFFFFF) + (ref_5681 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_5705 = (((ref_5697 & 0xFFFFFFFF) << (0xB & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_5712 = ((ref_5705 & 0xFFFFFFFF) ^ (((((ref_5532 & 0xFFFFFFFF) + (ref_5563 & 0xFFFFFFFF)) & 0xFFFFFFFF) + (ref_5632 & 0xFFFFFFFF)) & 0xFFFFFFFF)) # XOR operation
ref_5725 = (((((ref_5532 & 0xFFFFFFFF) + (ref_5563 & 0xFFFFFFFF)) & 0xFFFFFFFF) + (ref_5632 & 0xFFFFFFFF)) & 0xFFFFFFFF) # MOV operation
ref_5727 = (((ref_5725 & 0xFFFFFFFF) << (0x10 & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_5734 = ((ref_5727 & 0xFFFFFFFF) ^ (ref_5712 & 0xFFFFFFFF)) # XOR operation
ref_5763 = (ref_5734 & 0xFFFFFFFF) # MOV operation
ref_5765 = ((ref_5763 & 0xFFFFFFFF) >> (0xB & 0x1F)) # SHR operation
ref_5835 = (((ref_5734 & 0xFFFFFFFF) + (ref_5765 & 0xFFFFFFFF)) & 0xFFFFFFFF) # MOV operation
ref_5837 = (((ref_5835 & 0xFFFFFFFF) << (0x3 & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_5855 = ((((ref_5734 & 0xFFFFFFFF) + (ref_5765 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_5837 & 0xFFFFFFFF)) # MOV operation
ref_5857 = ((ref_5855 & 0xFFFFFFFF) >> (0x5 & 0x1F)) # SHR operation
ref_5876 = ((((((ref_5734 & 0xFFFFFFFF) + (ref_5765 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_5837 & 0xFFFFFFFF)) + (ref_5857 & 0xFFFFFFFF)) & 0xFFFFFFFF) # MOV operation
ref_5878 = (((ref_5876 & 0xFFFFFFFF) << (0x4 & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_5896 = (((((((ref_5734 & 0xFFFFFFFF) + (ref_5765 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_5837 & 0xFFFFFFFF)) + (ref_5857 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_5878 & 0xFFFFFFFF)) # MOV operation
ref_5898 = ((ref_5896 & 0xFFFFFFFF) >> (0x11 & 0x1F)) # SHR operation
ref_5917 = (((((((((ref_5734 & 0xFFFFFFFF) + (ref_5765 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_5837 & 0xFFFFFFFF)) + (ref_5857 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_5878 & 0xFFFFFFFF)) + (ref_5898 & 0xFFFFFFFF)) & 0xFFFFFFFF) # MOV operation
ref_5919 = (((ref_5917 & 0xFFFFFFFF) << (0x19 & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_5937 = ((((((((((ref_5734 & 0xFFFFFFFF) + (ref_5765 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_5837 & 0xFFFFFFFF)) + (ref_5857 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_5878 & 0xFFFFFFFF)) + (ref_5898 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_5919 & 0xFFFFFFFF)) # MOV operation
ref_5939 = ((ref_5937 & 0xFFFFFFFF) >> (0x6 & 0x1F)) # SHR operation
ref_5958 = ((((((((((((ref_5734 & 0xFFFFFFFF) + (ref_5765 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_5837 & 0xFFFFFFFF)) + (ref_5857 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_5878 & 0xFFFFFFFF)) + (ref_5898 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_5919 & 0xFFFFFFFF)) + (ref_5939 & 0xFFFFFFFF)) & 0xFFFFFFFF) # MOV operation
ref_5971 = (ref_5958 & 0xFFFFFFFF) # MOV operation
ref_6230 = (ref_5971 & 0xFFFFFFFF) # MOV operation
ref_6278 = (ref_6230 & 0xFFFFFFFF) # MOV operation
ref_6493 = (ref_6278 & 0xFFFFFFFF) # MOV operation
ref_6529 = (ref_6493 & 0xFFFFFFFF) # MOV operation
ref_6563 = (ref_6529 & 0xFFFFFFFF) # MOV operation
ref_6575 = ref_6563 # MOV operation
ref_6577 = ref_6575 # MOV operation

print ref_6577 & 0xffffffffffffffff
