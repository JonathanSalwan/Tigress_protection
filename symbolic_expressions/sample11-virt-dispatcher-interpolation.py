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
ref_7619 = ref_290 # MOVZX operation
ref_7621 = (ref_7619 & 0xFF) # MOVZX operation
ref_7623 = (((ref_7621 & 0xFFFFFFFF) << (0x8 & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_7630 = (ref_7623 & 0xFFFFFFFF) # MOV operation
ref_7634 = ref_291 # MOVZX operation
ref_7636 = (ref_7634 & 0xFF) # MOVZX operation
ref_7638 = (((ref_7636 & 0xFFFFFFFF) + (ref_7630 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_7676 = ref_288 # MOVZX operation
ref_7678 = (ref_7676 & 0xFF) # MOVZX operation
ref_7680 = (((ref_7678 & 0xFFFFFFFF) << (0x8 & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_7687 = (ref_7680 & 0xFFFFFFFF) # MOV operation
ref_7699 = ref_289 # MOVZX operation
ref_7701 = (ref_7699 & 0xFF) # MOVZX operation
ref_7703 = (((ref_7701 & 0xFFFFFFFF) + (ref_7687 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_7711 = (((ref_7703 & 0xFFFFFFFF) << (0xB & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_7718 = ((ref_7711 & 0xFFFFFFFF) ^ ((((((0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x8) + (ref_7638 & 0xFFFFFFFF)) & 0xFFFFFFFF)) # XOR operation
ref_7731 = ((((((0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x8) + (ref_7638 & 0xFFFFFFFF)) & 0xFFFFFFFF) # MOV operation
ref_7733 = (((ref_7731 & 0xFFFFFFFF) << (0x10 & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_7740 = ((ref_7733 & 0xFFFFFFFF) ^ (ref_7718 & 0xFFFFFFFF)) # XOR operation
ref_7769 = (ref_7740 & 0xFFFFFFFF) # MOV operation
ref_7771 = ((ref_7769 & 0xFFFFFFFF) >> (0xB & 0x1F)) # SHR operation
ref_7821 = ref_286 # MOVZX operation
ref_7823 = (ref_7821 & 0xFF) # MOVZX operation
ref_7825 = (((ref_7823 & 0xFFFFFFFF) << (0x8 & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_7832 = (ref_7825 & 0xFFFFFFFF) # MOV operation
ref_7836 = ref_287 # MOVZX operation
ref_7838 = (ref_7836 & 0xFF) # MOVZX operation
ref_7840 = (((ref_7838 & 0xFFFFFFFF) + (ref_7832 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_7878 = ref_284 # MOVZX operation
ref_7880 = (ref_7878 & 0xFF) # MOVZX operation
ref_7882 = (((ref_7880 & 0xFFFFFFFF) << (0x8 & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_7889 = (ref_7882 & 0xFFFFFFFF) # MOV operation
ref_7901 = ref_285 # MOVZX operation
ref_7903 = (ref_7901 & 0xFF) # MOVZX operation
ref_7905 = (((ref_7903 & 0xFFFFFFFF) + (ref_7889 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_7913 = (((ref_7905 & 0xFFFFFFFF) << (0xB & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_7920 = ((ref_7913 & 0xFFFFFFFF) ^ (((((ref_7740 & 0xFFFFFFFF) + (ref_7771 & 0xFFFFFFFF)) & 0xFFFFFFFF) + (ref_7840 & 0xFFFFFFFF)) & 0xFFFFFFFF)) # XOR operation
ref_7933 = (((((ref_7740 & 0xFFFFFFFF) + (ref_7771 & 0xFFFFFFFF)) & 0xFFFFFFFF) + (ref_7840 & 0xFFFFFFFF)) & 0xFFFFFFFF) # MOV operation
ref_7935 = (((ref_7933 & 0xFFFFFFFF) << (0x10 & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_7942 = ((ref_7935 & 0xFFFFFFFF) ^ (ref_7920 & 0xFFFFFFFF)) # XOR operation
ref_7971 = (ref_7942 & 0xFFFFFFFF) # MOV operation
ref_7973 = ((ref_7971 & 0xFFFFFFFF) >> (0xB & 0x1F)) # SHR operation
ref_8043 = (((ref_7942 & 0xFFFFFFFF) + (ref_7973 & 0xFFFFFFFF)) & 0xFFFFFFFF) # MOV operation
ref_8045 = (((ref_8043 & 0xFFFFFFFF) << (0x3 & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_8063 = ((((ref_7942 & 0xFFFFFFFF) + (ref_7973 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_8045 & 0xFFFFFFFF)) # MOV operation
ref_8065 = ((ref_8063 & 0xFFFFFFFF) >> (0x5 & 0x1F)) # SHR operation
ref_8084 = ((((((ref_7942 & 0xFFFFFFFF) + (ref_7973 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_8045 & 0xFFFFFFFF)) + (ref_8065 & 0xFFFFFFFF)) & 0xFFFFFFFF) # MOV operation
ref_8086 = (((ref_8084 & 0xFFFFFFFF) << (0x4 & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_8104 = (((((((ref_7942 & 0xFFFFFFFF) + (ref_7973 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_8045 & 0xFFFFFFFF)) + (ref_8065 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_8086 & 0xFFFFFFFF)) # MOV operation
ref_8106 = ((ref_8104 & 0xFFFFFFFF) >> (0x11 & 0x1F)) # SHR operation
ref_8125 = (((((((((ref_7942 & 0xFFFFFFFF) + (ref_7973 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_8045 & 0xFFFFFFFF)) + (ref_8065 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_8086 & 0xFFFFFFFF)) + (ref_8106 & 0xFFFFFFFF)) & 0xFFFFFFFF) # MOV operation
ref_8127 = (((ref_8125 & 0xFFFFFFFF) << (0x19 & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_8145 = ((((((((((ref_7942 & 0xFFFFFFFF) + (ref_7973 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_8045 & 0xFFFFFFFF)) + (ref_8065 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_8086 & 0xFFFFFFFF)) + (ref_8106 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_8127 & 0xFFFFFFFF)) # MOV operation
ref_8147 = ((ref_8145 & 0xFFFFFFFF) >> (0x6 & 0x1F)) # SHR operation
ref_8166 = ((((((((((((ref_7942 & 0xFFFFFFFF) + (ref_7973 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_8045 & 0xFFFFFFFF)) + (ref_8065 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_8086 & 0xFFFFFFFF)) + (ref_8106 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_8127 & 0xFFFFFFFF)) + (ref_8147 & 0xFFFFFFFF)) & 0xFFFFFFFF) # MOV operation
ref_8179 = (ref_8166 & 0xFFFFFFFF) # MOV operation
ref_9824 = (ref_8179 & 0xFFFFFFFF) # MOV operation
ref_10184 = (ref_9824 & 0xFFFFFFFF) # MOV operation
ref_11553 = (ref_10184 & 0xFFFFFFFF) # MOV operation
ref_11901 = (ref_11553 & 0xFFFFFFFF) # MOV operation
ref_11935 = (ref_11901 & 0xFFFFFFFF) # MOV operation
ref_11947 = ref_11935 # MOV operation
ref_11949 = ref_11947 # MOV operation

print ref_11949 & 0xffffffffffffffff
