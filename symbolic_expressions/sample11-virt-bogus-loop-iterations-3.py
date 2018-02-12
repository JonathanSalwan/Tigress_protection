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
ref_36593 = ref_290 # MOVZX operation
ref_36595 = (ref_36593 & 0xFF) # MOVZX operation
ref_36597 = (((ref_36595 & 0xFFFFFFFF) << (0x8 & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_36604 = (ref_36597 & 0xFFFFFFFF) # MOV operation
ref_36608 = ref_291 # MOVZX operation
ref_36610 = (ref_36608 & 0xFF) # MOVZX operation
ref_36612 = (((ref_36610 & 0xFFFFFFFF) + (ref_36604 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_36650 = ref_288 # MOVZX operation
ref_36652 = (ref_36650 & 0xFF) # MOVZX operation
ref_36654 = (((ref_36652 & 0xFFFFFFFF) << (0x8 & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_36661 = (ref_36654 & 0xFFFFFFFF) # MOV operation
ref_36673 = ref_289 # MOVZX operation
ref_36675 = (ref_36673 & 0xFF) # MOVZX operation
ref_36677 = (((ref_36675 & 0xFFFFFFFF) + (ref_36661 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_36685 = (((ref_36677 & 0xFFFFFFFF) << (0xB & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_36692 = ((ref_36685 & 0xFFFFFFFF) ^ ((((((0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x8) + (ref_36612 & 0xFFFFFFFF)) & 0xFFFFFFFF)) # XOR operation
ref_36705 = ((((((0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x8) + (ref_36612 & 0xFFFFFFFF)) & 0xFFFFFFFF) # MOV operation
ref_36707 = (((ref_36705 & 0xFFFFFFFF) << (0x10 & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_36714 = ((ref_36707 & 0xFFFFFFFF) ^ (ref_36692 & 0xFFFFFFFF)) # XOR operation
ref_36743 = (ref_36714 & 0xFFFFFFFF) # MOV operation
ref_36745 = ((ref_36743 & 0xFFFFFFFF) >> (0xB & 0x1F)) # SHR operation
ref_36795 = ref_286 # MOVZX operation
ref_36797 = (ref_36795 & 0xFF) # MOVZX operation
ref_36799 = (((ref_36797 & 0xFFFFFFFF) << (0x8 & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_36806 = (ref_36799 & 0xFFFFFFFF) # MOV operation
ref_36810 = ref_287 # MOVZX operation
ref_36812 = (ref_36810 & 0xFF) # MOVZX operation
ref_36814 = (((ref_36812 & 0xFFFFFFFF) + (ref_36806 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_36852 = ref_284 # MOVZX operation
ref_36854 = (ref_36852 & 0xFF) # MOVZX operation
ref_36856 = (((ref_36854 & 0xFFFFFFFF) << (0x8 & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_36863 = (ref_36856 & 0xFFFFFFFF) # MOV operation
ref_36875 = ref_285 # MOVZX operation
ref_36877 = (ref_36875 & 0xFF) # MOVZX operation
ref_36879 = (((ref_36877 & 0xFFFFFFFF) + (ref_36863 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_36887 = (((ref_36879 & 0xFFFFFFFF) << (0xB & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_36894 = ((ref_36887 & 0xFFFFFFFF) ^ (((((ref_36714 & 0xFFFFFFFF) + (ref_36745 & 0xFFFFFFFF)) & 0xFFFFFFFF) + (ref_36814 & 0xFFFFFFFF)) & 0xFFFFFFFF)) # XOR operation
ref_36907 = (((((ref_36714 & 0xFFFFFFFF) + (ref_36745 & 0xFFFFFFFF)) & 0xFFFFFFFF) + (ref_36814 & 0xFFFFFFFF)) & 0xFFFFFFFF) # MOV operation
ref_36909 = (((ref_36907 & 0xFFFFFFFF) << (0x10 & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_36916 = ((ref_36909 & 0xFFFFFFFF) ^ (ref_36894 & 0xFFFFFFFF)) # XOR operation
ref_36945 = (ref_36916 & 0xFFFFFFFF) # MOV operation
ref_36947 = ((ref_36945 & 0xFFFFFFFF) >> (0xB & 0x1F)) # SHR operation
ref_37017 = (((ref_36916 & 0xFFFFFFFF) + (ref_36947 & 0xFFFFFFFF)) & 0xFFFFFFFF) # MOV operation
ref_37019 = (((ref_37017 & 0xFFFFFFFF) << (0x3 & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_37037 = ((((ref_36916 & 0xFFFFFFFF) + (ref_36947 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_37019 & 0xFFFFFFFF)) # MOV operation
ref_37039 = ((ref_37037 & 0xFFFFFFFF) >> (0x5 & 0x1F)) # SHR operation
ref_37058 = ((((((ref_36916 & 0xFFFFFFFF) + (ref_36947 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_37019 & 0xFFFFFFFF)) + (ref_37039 & 0xFFFFFFFF)) & 0xFFFFFFFF) # MOV operation
ref_37060 = (((ref_37058 & 0xFFFFFFFF) << (0x4 & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_37078 = (((((((ref_36916 & 0xFFFFFFFF) + (ref_36947 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_37019 & 0xFFFFFFFF)) + (ref_37039 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_37060 & 0xFFFFFFFF)) # MOV operation
ref_37080 = ((ref_37078 & 0xFFFFFFFF) >> (0x11 & 0x1F)) # SHR operation
ref_37099 = (((((((((ref_36916 & 0xFFFFFFFF) + (ref_36947 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_37019 & 0xFFFFFFFF)) + (ref_37039 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_37060 & 0xFFFFFFFF)) + (ref_37080 & 0xFFFFFFFF)) & 0xFFFFFFFF) # MOV operation
ref_37101 = (((ref_37099 & 0xFFFFFFFF) << (0x19 & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_37119 = ((((((((((ref_36916 & 0xFFFFFFFF) + (ref_36947 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_37019 & 0xFFFFFFFF)) + (ref_37039 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_37060 & 0xFFFFFFFF)) + (ref_37080 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_37101 & 0xFFFFFFFF)) # MOV operation
ref_37121 = ((ref_37119 & 0xFFFFFFFF) >> (0x6 & 0x1F)) # SHR operation
ref_37140 = ((((((((((((ref_36916 & 0xFFFFFFFF) + (ref_36947 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_37019 & 0xFFFFFFFF)) + (ref_37039 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_37060 & 0xFFFFFFFF)) + (ref_37080 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_37101 & 0xFFFFFFFF)) + (ref_37121 & 0xFFFFFFFF)) & 0xFFFFFFFF) # MOV operation
ref_37153 = (ref_37140 & 0xFFFFFFFF) # MOV operation
ref_56261 = (ref_37153 & 0xFFFFFFFF) # MOV operation
ref_62613 = (ref_56261 & 0xFFFFFFFF) # MOV operation
ref_81706 = (ref_62613 & 0xFFFFFFFF) # MOV operation
ref_88055 = (ref_81706 & 0xFFFFFFFF) # MOV operation
ref_88089 = (ref_88055 & 0xFFFFFFFF) # MOV operation
ref_88101 = ref_88089 # MOV operation
ref_88103 = ref_88101 # MOV operation

print ref_88103 & 0xffffffffffffffff
