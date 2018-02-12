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
ref_6465 = ref_290 # MOVZX operation
ref_6467 = (ref_6465 & 0xFF) # MOVZX operation
ref_6469 = (((ref_6467 & 0xFFFFFFFF) << (0x8 & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_6476 = (ref_6469 & 0xFFFFFFFF) # MOV operation
ref_6480 = ref_291 # MOVZX operation
ref_6482 = (ref_6480 & 0xFF) # MOVZX operation
ref_6484 = (((ref_6482 & 0xFFFFFFFF) + (ref_6476 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_6522 = ref_288 # MOVZX operation
ref_6524 = (ref_6522 & 0xFF) # MOVZX operation
ref_6526 = (((ref_6524 & 0xFFFFFFFF) << (0x8 & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_6533 = (ref_6526 & 0xFFFFFFFF) # MOV operation
ref_6545 = ref_289 # MOVZX operation
ref_6547 = (ref_6545 & 0xFF) # MOVZX operation
ref_6549 = (((ref_6547 & 0xFFFFFFFF) + (ref_6533 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_6557 = (((ref_6549 & 0xFFFFFFFF) << (0xB & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_6564 = ((ref_6557 & 0xFFFFFFFF) ^ ((((((0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x8) + (ref_6484 & 0xFFFFFFFF)) & 0xFFFFFFFF)) # XOR operation
ref_6577 = ((((((0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x8) + (ref_6484 & 0xFFFFFFFF)) & 0xFFFFFFFF) # MOV operation
ref_6579 = (((ref_6577 & 0xFFFFFFFF) << (0x10 & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_6586 = ((ref_6579 & 0xFFFFFFFF) ^ (ref_6564 & 0xFFFFFFFF)) # XOR operation
ref_6615 = (ref_6586 & 0xFFFFFFFF) # MOV operation
ref_6617 = ((ref_6615 & 0xFFFFFFFF) >> (0xB & 0x1F)) # SHR operation
ref_6667 = ref_286 # MOVZX operation
ref_6669 = (ref_6667 & 0xFF) # MOVZX operation
ref_6671 = (((ref_6669 & 0xFFFFFFFF) << (0x8 & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_6678 = (ref_6671 & 0xFFFFFFFF) # MOV operation
ref_6682 = ref_287 # MOVZX operation
ref_6684 = (ref_6682 & 0xFF) # MOVZX operation
ref_6686 = (((ref_6684 & 0xFFFFFFFF) + (ref_6678 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_6724 = ref_284 # MOVZX operation
ref_6726 = (ref_6724 & 0xFF) # MOVZX operation
ref_6728 = (((ref_6726 & 0xFFFFFFFF) << (0x8 & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_6735 = (ref_6728 & 0xFFFFFFFF) # MOV operation
ref_6747 = ref_285 # MOVZX operation
ref_6749 = (ref_6747 & 0xFF) # MOVZX operation
ref_6751 = (((ref_6749 & 0xFFFFFFFF) + (ref_6735 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_6759 = (((ref_6751 & 0xFFFFFFFF) << (0xB & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_6766 = ((ref_6759 & 0xFFFFFFFF) ^ (((((ref_6586 & 0xFFFFFFFF) + (ref_6617 & 0xFFFFFFFF)) & 0xFFFFFFFF) + (ref_6686 & 0xFFFFFFFF)) & 0xFFFFFFFF)) # XOR operation
ref_6779 = (((((ref_6586 & 0xFFFFFFFF) + (ref_6617 & 0xFFFFFFFF)) & 0xFFFFFFFF) + (ref_6686 & 0xFFFFFFFF)) & 0xFFFFFFFF) # MOV operation
ref_6781 = (((ref_6779 & 0xFFFFFFFF) << (0x10 & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_6788 = ((ref_6781 & 0xFFFFFFFF) ^ (ref_6766 & 0xFFFFFFFF)) # XOR operation
ref_6817 = (ref_6788 & 0xFFFFFFFF) # MOV operation
ref_6819 = ((ref_6817 & 0xFFFFFFFF) >> (0xB & 0x1F)) # SHR operation
ref_6889 = (((ref_6788 & 0xFFFFFFFF) + (ref_6819 & 0xFFFFFFFF)) & 0xFFFFFFFF) # MOV operation
ref_6891 = (((ref_6889 & 0xFFFFFFFF) << (0x3 & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_6909 = ((((ref_6788 & 0xFFFFFFFF) + (ref_6819 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_6891 & 0xFFFFFFFF)) # MOV operation
ref_6911 = ((ref_6909 & 0xFFFFFFFF) >> (0x5 & 0x1F)) # SHR operation
ref_6930 = ((((((ref_6788 & 0xFFFFFFFF) + (ref_6819 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_6891 & 0xFFFFFFFF)) + (ref_6911 & 0xFFFFFFFF)) & 0xFFFFFFFF) # MOV operation
ref_6932 = (((ref_6930 & 0xFFFFFFFF) << (0x4 & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_6950 = (((((((ref_6788 & 0xFFFFFFFF) + (ref_6819 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_6891 & 0xFFFFFFFF)) + (ref_6911 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_6932 & 0xFFFFFFFF)) # MOV operation
ref_6952 = ((ref_6950 & 0xFFFFFFFF) >> (0x11 & 0x1F)) # SHR operation
ref_6971 = (((((((((ref_6788 & 0xFFFFFFFF) + (ref_6819 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_6891 & 0xFFFFFFFF)) + (ref_6911 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_6932 & 0xFFFFFFFF)) + (ref_6952 & 0xFFFFFFFF)) & 0xFFFFFFFF) # MOV operation
ref_6973 = (((ref_6971 & 0xFFFFFFFF) << (0x19 & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_6991 = ((((((((((ref_6788 & 0xFFFFFFFF) + (ref_6819 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_6891 & 0xFFFFFFFF)) + (ref_6911 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_6932 & 0xFFFFFFFF)) + (ref_6952 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_6973 & 0xFFFFFFFF)) # MOV operation
ref_6993 = ((ref_6991 & 0xFFFFFFFF) >> (0x6 & 0x1F)) # SHR operation
ref_7012 = ((((((((((((ref_6788 & 0xFFFFFFFF) + (ref_6819 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_6891 & 0xFFFFFFFF)) + (ref_6911 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_6932 & 0xFFFFFFFF)) + (ref_6952 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_6973 & 0xFFFFFFFF)) + (ref_6993 & 0xFFFFFFFF)) & 0xFFFFFFFF) # MOV operation
ref_7025 = (ref_7012 & 0xFFFFFFFF) # MOV operation
ref_8099 = (ref_7025 & 0xFFFFFFFF) # MOV operation
ref_8592 = (ref_8099 & 0xFFFFFFFF) # MOV operation
ref_9667 = (ref_8592 & 0xFFFFFFFF) # MOV operation
ref_10200 = (ref_9667 & 0xFFFFFFFF) # MOV operation
ref_10234 = (ref_10200 & 0xFFFFFFFF) # MOV operation
ref_10246 = ref_10234 # MOV operation
ref_10248 = ref_10246 # MOV operation

print ref_10248 & 0xffffffffffffffff
