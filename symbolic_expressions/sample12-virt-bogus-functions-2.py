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
ref_5865 = ref_311 # MOV operation
ref_6293 = ref_5865 # MOV operation
ref_6615 = (ref_6293 & 0xFFFFFFFF) # MOV operation
ref_9565 = (ref_6615 & 0xFFFFFFFF) # MOV operation
ref_9569 = (ref_9565 & 0xFFFFFFFF) # MOV operation
ref_9603 = (((ref_9569 & 0xFFFFFFFF) >> 24) & 0xFF) # Byte reference - MOV operation
ref_9604 = (((ref_9569 & 0xFFFFFFFF) >> 16) & 0xFF) # Byte reference - MOV operation
ref_9605 = (((ref_9569 & 0xFFFFFFFF) >> 8) & 0xFF) # Byte reference - MOV operation
ref_9606 = ((ref_9569 & 0xFFFFFFFF) & 0xFF) # Byte reference - MOV operation
ref_9657 = ref_9606 # MOVZX operation
ref_9659 = (ref_9657 & 0xFF) # MOVZX operation
ref_9665 = (ref_9659 & 0xFFFFFFFF) # MOV operation
ref_9691 = (ref_9665 & 0xFFFFFFFF) # MOV operation
ref_9701 = (ref_9691 & 0xFF) # MOVZX operation
ref_9703 = ((ref_9701 & 0xFFFFFFFF) ^ ((((0x81) << 8 | 0x1C) << 8 | 0x9D) << 8 | 0xC5)) # XOR operation
ref_9710 = (ref_9703 & 0xFFFFFFFF) # MOV operation
ref_9714 = (((sx(0x20, 0x1000193) * sx(0x20, (ref_9710 & 0xFFFFFFFF))) & 0xFFFFFFFFFFFFFFFF) & 0xFFFFFFFF) # IMUL operation
ref_9759 = ref_9605 # MOVZX operation
ref_9761 = (ref_9759 & 0xFF) # MOVZX operation
ref_9763 = (ref_9714 & 0xFFFFFFFF) # MOV operation
ref_9765 = (ref_9763 & 0xFFFFFFFF) # MOV operation
ref_9767 = (ref_9761 & 0xFFFFFFFF) # MOV operation
ref_9793 = (ref_9767 & 0xFFFFFFFF) # MOV operation
ref_9803 = (ref_9793 & 0xFF) # MOVZX operation
ref_9805 = ((ref_9803 & 0xFFFFFFFF) ^ (ref_9765 & 0xFFFFFFFF)) # XOR operation
ref_9812 = (ref_9805 & 0xFFFFFFFF) # MOV operation
ref_9816 = (((sx(0x20, 0x1000193) * sx(0x20, (ref_9812 & 0xFFFFFFFF))) & 0xFFFFFFFFFFFFFFFF) & 0xFFFFFFFF) # IMUL operation
ref_9861 = ref_9604 # MOVZX operation
ref_9863 = (ref_9861 & 0xFF) # MOVZX operation
ref_9865 = (ref_9816 & 0xFFFFFFFF) # MOV operation
ref_9867 = (ref_9865 & 0xFFFFFFFF) # MOV operation
ref_9869 = (ref_9863 & 0xFFFFFFFF) # MOV operation
ref_9895 = (ref_9869 & 0xFFFFFFFF) # MOV operation
ref_9905 = (ref_9895 & 0xFF) # MOVZX operation
ref_9907 = ((ref_9905 & 0xFFFFFFFF) ^ (ref_9867 & 0xFFFFFFFF)) # XOR operation
ref_9914 = (ref_9907 & 0xFFFFFFFF) # MOV operation
ref_9918 = (((sx(0x20, 0x1000193) * sx(0x20, (ref_9914 & 0xFFFFFFFF))) & 0xFFFFFFFFFFFFFFFF) & 0xFFFFFFFF) # IMUL operation
ref_9935 = ref_9603 # MOVZX operation
ref_9937 = (ref_9935 & 0xFF) # MOVZX operation
ref_9939 = (ref_9918 & 0xFFFFFFFF) # MOV operation
ref_9941 = (ref_9939 & 0xFFFFFFFF) # MOV operation
ref_9943 = (ref_9937 & 0xFFFFFFFF) # MOV operation
ref_9969 = (ref_9943 & 0xFFFFFFFF) # MOV operation
ref_9979 = (ref_9969 & 0xFF) # MOVZX operation
ref_9981 = ((ref_9979 & 0xFFFFFFFF) ^ (ref_9941 & 0xFFFFFFFF)) # XOR operation
ref_9988 = (ref_9981 & 0xFFFFFFFF) # MOV operation
ref_9992 = (((sx(0x20, 0x1000193) * sx(0x20, (ref_9988 & 0xFFFFFFFF))) & 0xFFFFFFFFFFFFFFFF) & 0xFFFFFFFF) # IMUL operation
ref_10007 = (ref_9992 & 0xFFFFFFFF) # MOV operation
ref_11613 = (ref_10007 & 0xFFFFFFFF) # MOV operation
ref_12051 = (ref_11613 & 0xFFFFFFFF) # MOV operation
ref_13408 = (ref_12051 & 0xFFFFFFFF) # MOV operation
ref_13812 = (ref_13408 & 0xFFFFFFFF) # MOV operation
ref_13849 = (ref_13812 & 0xFFFFFFFF) # MOV operation
ref_13861 = ref_13849 # MOV operation
ref_13863 = ref_13861 # MOV operation

print ref_13863 & 0xffffffffffffffff
