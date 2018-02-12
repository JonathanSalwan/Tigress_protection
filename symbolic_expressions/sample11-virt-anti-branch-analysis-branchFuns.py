#!/usr/bin/env python2
## -*- coding: utf-8 -*-

import sys

def sx(bits, value):
    sign_bit = 1 << (bits - 1)
    return (value & (sign_bit - 1)) - (value & sign_bit)

SymVar_0 = int(sys.argv[1])
ref_220 = SymVar_0
ref_231 = ref_220 # MOV operation
ref_243 = ref_231 # MOV operation
ref_245 = ref_243 # MOV operation
ref_290 = ((ref_245 >> 56) & 0xFF) # Byte reference - MOV operation
ref_291 = ((ref_245 >> 48) & 0xFF) # Byte reference - MOV operation
ref_292 = ((ref_245 >> 40) & 0xFF) # Byte reference - MOV operation
ref_293 = ((ref_245 >> 32) & 0xFF) # Byte reference - MOV operation
ref_294 = ((ref_245 >> 24) & 0xFF) # Byte reference - MOV operation
ref_295 = ((ref_245 >> 16) & 0xFF) # Byte reference - MOV operation
ref_296 = ((ref_245 >> 8) & 0xFF) # Byte reference - MOV operation
ref_297 = (ref_245 & 0xFF) # Byte reference - MOV operation
ref_10387 = ref_296 # MOVZX operation
ref_10389 = (ref_10387 & 0xFF) # MOVZX operation
ref_10391 = (((ref_10389 & 0xFFFFFFFF) << (0x8 & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_10398 = (ref_10391 & 0xFFFFFFFF) # MOV operation
ref_10402 = ref_297 # MOVZX operation
ref_10404 = (ref_10402 & 0xFF) # MOVZX operation
ref_10406 = (((ref_10404 & 0xFFFFFFFF) + (ref_10398 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_10444 = ref_294 # MOVZX operation
ref_10446 = (ref_10444 & 0xFF) # MOVZX operation
ref_10448 = (((ref_10446 & 0xFFFFFFFF) << (0x8 & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_10455 = (ref_10448 & 0xFFFFFFFF) # MOV operation
ref_10467 = ref_295 # MOVZX operation
ref_10469 = (ref_10467 & 0xFF) # MOVZX operation
ref_10471 = (((ref_10469 & 0xFFFFFFFF) + (ref_10455 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_10479 = (((ref_10471 & 0xFFFFFFFF) << (0xB & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_10486 = ((ref_10479 & 0xFFFFFFFF) ^ ((((((0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x8) + (ref_10406 & 0xFFFFFFFF)) & 0xFFFFFFFF)) # XOR operation
ref_10499 = ((((((0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x8) + (ref_10406 & 0xFFFFFFFF)) & 0xFFFFFFFF) # MOV operation
ref_10501 = (((ref_10499 & 0xFFFFFFFF) << (0x10 & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_10508 = ((ref_10501 & 0xFFFFFFFF) ^ (ref_10486 & 0xFFFFFFFF)) # XOR operation
ref_10537 = (ref_10508 & 0xFFFFFFFF) # MOV operation
ref_10539 = ((ref_10537 & 0xFFFFFFFF) >> (0xB & 0x1F)) # SHR operation
ref_10589 = ref_292 # MOVZX operation
ref_10591 = (ref_10589 & 0xFF) # MOVZX operation
ref_10593 = (((ref_10591 & 0xFFFFFFFF) << (0x8 & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_10600 = (ref_10593 & 0xFFFFFFFF) # MOV operation
ref_10604 = ref_293 # MOVZX operation
ref_10606 = (ref_10604 & 0xFF) # MOVZX operation
ref_10608 = (((ref_10606 & 0xFFFFFFFF) + (ref_10600 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_10646 = ref_290 # MOVZX operation
ref_10648 = (ref_10646 & 0xFF) # MOVZX operation
ref_10650 = (((ref_10648 & 0xFFFFFFFF) << (0x8 & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_10657 = (ref_10650 & 0xFFFFFFFF) # MOV operation
ref_10669 = ref_291 # MOVZX operation
ref_10671 = (ref_10669 & 0xFF) # MOVZX operation
ref_10673 = (((ref_10671 & 0xFFFFFFFF) + (ref_10657 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_10681 = (((ref_10673 & 0xFFFFFFFF) << (0xB & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_10688 = ((ref_10681 & 0xFFFFFFFF) ^ (((((ref_10508 & 0xFFFFFFFF) + (ref_10539 & 0xFFFFFFFF)) & 0xFFFFFFFF) + (ref_10608 & 0xFFFFFFFF)) & 0xFFFFFFFF)) # XOR operation
ref_10701 = (((((ref_10508 & 0xFFFFFFFF) + (ref_10539 & 0xFFFFFFFF)) & 0xFFFFFFFF) + (ref_10608 & 0xFFFFFFFF)) & 0xFFFFFFFF) # MOV operation
ref_10703 = (((ref_10701 & 0xFFFFFFFF) << (0x10 & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_10710 = ((ref_10703 & 0xFFFFFFFF) ^ (ref_10688 & 0xFFFFFFFF)) # XOR operation
ref_10739 = (ref_10710 & 0xFFFFFFFF) # MOV operation
ref_10741 = ((ref_10739 & 0xFFFFFFFF) >> (0xB & 0x1F)) # SHR operation
ref_10811 = (((ref_10710 & 0xFFFFFFFF) + (ref_10741 & 0xFFFFFFFF)) & 0xFFFFFFFF) # MOV operation
ref_10813 = (((ref_10811 & 0xFFFFFFFF) << (0x3 & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_10831 = ((((ref_10710 & 0xFFFFFFFF) + (ref_10741 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_10813 & 0xFFFFFFFF)) # MOV operation
ref_10833 = ((ref_10831 & 0xFFFFFFFF) >> (0x5 & 0x1F)) # SHR operation
ref_10852 = ((((((ref_10710 & 0xFFFFFFFF) + (ref_10741 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_10813 & 0xFFFFFFFF)) + (ref_10833 & 0xFFFFFFFF)) & 0xFFFFFFFF) # MOV operation
ref_10854 = (((ref_10852 & 0xFFFFFFFF) << (0x4 & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_10872 = (((((((ref_10710 & 0xFFFFFFFF) + (ref_10741 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_10813 & 0xFFFFFFFF)) + (ref_10833 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_10854 & 0xFFFFFFFF)) # MOV operation
ref_10874 = ((ref_10872 & 0xFFFFFFFF) >> (0x11 & 0x1F)) # SHR operation
ref_10893 = (((((((((ref_10710 & 0xFFFFFFFF) + (ref_10741 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_10813 & 0xFFFFFFFF)) + (ref_10833 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_10854 & 0xFFFFFFFF)) + (ref_10874 & 0xFFFFFFFF)) & 0xFFFFFFFF) # MOV operation
ref_10895 = (((ref_10893 & 0xFFFFFFFF) << (0x19 & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_10913 = ((((((((((ref_10710 & 0xFFFFFFFF) + (ref_10741 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_10813 & 0xFFFFFFFF)) + (ref_10833 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_10854 & 0xFFFFFFFF)) + (ref_10874 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_10895 & 0xFFFFFFFF)) # MOV operation
ref_10915 = ((ref_10913 & 0xFFFFFFFF) >> (0x6 & 0x1F)) # SHR operation
ref_10934 = ((((((((((((ref_10710 & 0xFFFFFFFF) + (ref_10741 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_10813 & 0xFFFFFFFF)) + (ref_10833 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_10854 & 0xFFFFFFFF)) + (ref_10874 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_10895 & 0xFFFFFFFF)) + (ref_10915 & 0xFFFFFFFF)) & 0xFFFFFFFF) # MOV operation
ref_10947 = (ref_10934 & 0xFFFFFFFF) # MOV operation
ref_12191 = (ref_10947 & 0xFFFFFFFF) # MOV operation
ref_12562 = (ref_12191 & 0xFFFFFFFF) # MOV operation
ref_13775 = (ref_12562 & 0xFFFFFFFF) # MOV operation
ref_14198 = (ref_13775 & 0xFFFFFFFF) # MOV operation
ref_14233 = (ref_14198 & 0xFFFFFFFF) # MOV operation
ref_14245 = ref_14233 # MOV operation
ref_14247 = ref_14245 # MOV operation

print ref_14247 & 0xffffffffffffffff
