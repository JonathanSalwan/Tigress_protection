#!/usr/bin/env python2
## -*- coding: utf-8 -*-

import sys

def sx(bits, value):
    sign_bit = 1 << (bits - 1)
    return (value & (sign_bit - 1)) - (value & sign_bit)

SymVar_0 = int(sys.argv[1])
ref_286 = SymVar_0
ref_297 = ref_286 # MOV operation
ref_309 = ref_297 # MOV operation
ref_311 = ref_309 # MOV operation
ref_12401 = ref_311 # MOV operation
ref_14934 = ref_12401 # MOV operation
ref_17455 = (ref_14934 & 0xFFFFFFFF) # MOV operation
ref_32819 = (ref_17455 & 0xFFFFFFFF) # MOV operation
ref_32823 = (ref_32819 & 0xFFFFFFFF) # MOV operation
ref_32857 = (((ref_32823 & 0xFFFFFFFF) >> 24) & 0xFF) # Byte reference - MOV operation
ref_32858 = (((ref_32823 & 0xFFFFFFFF) >> 16) & 0xFF) # Byte reference - MOV operation
ref_32859 = (((ref_32823 & 0xFFFFFFFF) >> 8) & 0xFF) # Byte reference - MOV operation
ref_32860 = ((ref_32823 & 0xFFFFFFFF) & 0xFF) # Byte reference - MOV operation
ref_32911 = ref_32860 # MOVZX operation
ref_32913 = (ref_32911 & 0xFF) # MOVZX operation
ref_32919 = (ref_32913 & 0xFFFFFFFF) # MOV operation
ref_32945 = (ref_32919 & 0xFFFFFFFF) # MOV operation
ref_32955 = (ref_32945 & 0xFF) # MOVZX operation
ref_32957 = ((ref_32955 & 0xFFFFFFFF) ^ ((((0x81) << 8 | 0x1C) << 8 | 0x9D) << 8 | 0xC5)) # XOR operation
ref_32964 = (ref_32957 & 0xFFFFFFFF) # MOV operation
ref_32968 = (((sx(0x20, 0x1000193) * sx(0x20, (ref_32964 & 0xFFFFFFFF))) & 0xFFFFFFFFFFFFFFFF) & 0xFFFFFFFF) # IMUL operation
ref_33013 = ref_32859 # MOVZX operation
ref_33015 = (ref_33013 & 0xFF) # MOVZX operation
ref_33017 = (ref_32968 & 0xFFFFFFFF) # MOV operation
ref_33019 = (ref_33017 & 0xFFFFFFFF) # MOV operation
ref_33021 = (ref_33015 & 0xFFFFFFFF) # MOV operation
ref_33047 = (ref_33021 & 0xFFFFFFFF) # MOV operation
ref_33057 = (ref_33047 & 0xFF) # MOVZX operation
ref_33059 = ((ref_33057 & 0xFFFFFFFF) ^ (ref_33019 & 0xFFFFFFFF)) # XOR operation
ref_33066 = (ref_33059 & 0xFFFFFFFF) # MOV operation
ref_33070 = (((sx(0x20, 0x1000193) * sx(0x20, (ref_33066 & 0xFFFFFFFF))) & 0xFFFFFFFFFFFFFFFF) & 0xFFFFFFFF) # IMUL operation
ref_33115 = ref_32858 # MOVZX operation
ref_33117 = (ref_33115 & 0xFF) # MOVZX operation
ref_33119 = (ref_33070 & 0xFFFFFFFF) # MOV operation
ref_33121 = (ref_33119 & 0xFFFFFFFF) # MOV operation
ref_33123 = (ref_33117 & 0xFFFFFFFF) # MOV operation
ref_33149 = (ref_33123 & 0xFFFFFFFF) # MOV operation
ref_33159 = (ref_33149 & 0xFF) # MOVZX operation
ref_33161 = ((ref_33159 & 0xFFFFFFFF) ^ (ref_33121 & 0xFFFFFFFF)) # XOR operation
ref_33168 = (ref_33161 & 0xFFFFFFFF) # MOV operation
ref_33172 = (((sx(0x20, 0x1000193) * sx(0x20, (ref_33168 & 0xFFFFFFFF))) & 0xFFFFFFFFFFFFFFFF) & 0xFFFFFFFF) # IMUL operation
ref_33189 = ref_32857 # MOVZX operation
ref_33191 = (ref_33189 & 0xFF) # MOVZX operation
ref_33193 = (ref_33172 & 0xFFFFFFFF) # MOV operation
ref_33195 = (ref_33193 & 0xFFFFFFFF) # MOV operation
ref_33197 = (ref_33191 & 0xFFFFFFFF) # MOV operation
ref_33223 = (ref_33197 & 0xFFFFFFFF) # MOV operation
ref_33233 = (ref_33223 & 0xFF) # MOVZX operation
ref_33235 = ((ref_33233 & 0xFFFFFFFF) ^ (ref_33195 & 0xFFFFFFFF)) # XOR operation
ref_33242 = (ref_33235 & 0xFFFFFFFF) # MOV operation
ref_33246 = (((sx(0x20, 0x1000193) * sx(0x20, (ref_33242 & 0xFFFFFFFF))) & 0xFFFFFFFFFFFFFFFF) & 0xFFFFFFFF) # IMUL operation
ref_33261 = (ref_33246 & 0xFFFFFFFF) # MOV operation
ref_41011 = (ref_33261 & 0xFFFFFFFF) # MOV operation
ref_43532 = (ref_41011 & 0xFFFFFFFF) # MOV operation
ref_51186 = (ref_43532 & 0xFFFFFFFF) # MOV operation
ref_53713 = (ref_51186 & 0xFFFFFFFF) # MOV operation
ref_53747 = (ref_53713 & 0xFFFFFFFF) # MOV operation
ref_53759 = ref_53747 # MOV operation
ref_53761 = ref_53759 # MOV operation

print ref_53761 & 0xffffffffffffffff
