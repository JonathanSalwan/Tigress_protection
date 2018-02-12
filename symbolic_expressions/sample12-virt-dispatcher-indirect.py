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
ref_8253 = ref_311 # MOV operation
ref_8301 = ref_8253 # MOV operation
ref_8355 = (ref_8301 & 0xFFFFFFFF) # MOV operation
ref_8827 = (ref_8355 & 0xFFFFFFFF) # MOV operation
ref_8831 = (ref_8827 & 0xFFFFFFFF) # MOV operation
ref_8865 = (((ref_8831 & 0xFFFFFFFF) >> 24) & 0xFF) # Byte reference - MOV operation
ref_8866 = (((ref_8831 & 0xFFFFFFFF) >> 16) & 0xFF) # Byte reference - MOV operation
ref_8867 = (((ref_8831 & 0xFFFFFFFF) >> 8) & 0xFF) # Byte reference - MOV operation
ref_8868 = ((ref_8831 & 0xFFFFFFFF) & 0xFF) # Byte reference - MOV operation
ref_8919 = ref_8868 # MOVZX operation
ref_8921 = (ref_8919 & 0xFF) # MOVZX operation
ref_8927 = (ref_8921 & 0xFFFFFFFF) # MOV operation
ref_8953 = (ref_8927 & 0xFFFFFFFF) # MOV operation
ref_8963 = (ref_8953 & 0xFF) # MOVZX operation
ref_8965 = ((ref_8963 & 0xFFFFFFFF) ^ ((((0x81) << 8 | 0x1C) << 8 | 0x9D) << 8 | 0xC5)) # XOR operation
ref_8972 = (ref_8965 & 0xFFFFFFFF) # MOV operation
ref_8976 = (((sx(0x20, 0x1000193) * sx(0x20, (ref_8972 & 0xFFFFFFFF))) & 0xFFFFFFFFFFFFFFFF) & 0xFFFFFFFF) # IMUL operation
ref_9021 = ref_8867 # MOVZX operation
ref_9023 = (ref_9021 & 0xFF) # MOVZX operation
ref_9025 = (ref_8976 & 0xFFFFFFFF) # MOV operation
ref_9027 = (ref_9025 & 0xFFFFFFFF) # MOV operation
ref_9029 = (ref_9023 & 0xFFFFFFFF) # MOV operation
ref_9055 = (ref_9029 & 0xFFFFFFFF) # MOV operation
ref_9065 = (ref_9055 & 0xFF) # MOVZX operation
ref_9067 = ((ref_9065 & 0xFFFFFFFF) ^ (ref_9027 & 0xFFFFFFFF)) # XOR operation
ref_9074 = (ref_9067 & 0xFFFFFFFF) # MOV operation
ref_9078 = (((sx(0x20, 0x1000193) * sx(0x20, (ref_9074 & 0xFFFFFFFF))) & 0xFFFFFFFFFFFFFFFF) & 0xFFFFFFFF) # IMUL operation
ref_9123 = ref_8866 # MOVZX operation
ref_9125 = (ref_9123 & 0xFF) # MOVZX operation
ref_9127 = (ref_9078 & 0xFFFFFFFF) # MOV operation
ref_9129 = (ref_9127 & 0xFFFFFFFF) # MOV operation
ref_9131 = (ref_9125 & 0xFFFFFFFF) # MOV operation
ref_9157 = (ref_9131 & 0xFFFFFFFF) # MOV operation
ref_9167 = (ref_9157 & 0xFF) # MOVZX operation
ref_9169 = ((ref_9167 & 0xFFFFFFFF) ^ (ref_9129 & 0xFFFFFFFF)) # XOR operation
ref_9176 = (ref_9169 & 0xFFFFFFFF) # MOV operation
ref_9180 = (((sx(0x20, 0x1000193) * sx(0x20, (ref_9176 & 0xFFFFFFFF))) & 0xFFFFFFFFFFFFFFFF) & 0xFFFFFFFF) # IMUL operation
ref_9197 = ref_8865 # MOVZX operation
ref_9199 = (ref_9197 & 0xFF) # MOVZX operation
ref_9201 = (ref_9180 & 0xFFFFFFFF) # MOV operation
ref_9203 = (ref_9201 & 0xFFFFFFFF) # MOV operation
ref_9205 = (ref_9199 & 0xFFFFFFFF) # MOV operation
ref_9231 = (ref_9205 & 0xFFFFFFFF) # MOV operation
ref_9241 = (ref_9231 & 0xFF) # MOVZX operation
ref_9243 = ((ref_9241 & 0xFFFFFFFF) ^ (ref_9203 & 0xFFFFFFFF)) # XOR operation
ref_9250 = (ref_9243 & 0xFFFFFFFF) # MOV operation
ref_9254 = (((sx(0x20, 0x1000193) * sx(0x20, (ref_9250 & 0xFFFFFFFF))) & 0xFFFFFFFFFFFFFFFF) & 0xFFFFFFFF) # IMUL operation
ref_9269 = (ref_9254 & 0xFFFFFFFF) # MOV operation
ref_9546 = (ref_9269 & 0xFFFFFFFF) # MOV operation
ref_9600 = (ref_9546 & 0xFFFFFFFF) # MOV operation
ref_9826 = (ref_9600 & 0xFFFFFFFF) # MOV operation
ref_9868 = (ref_9826 & 0xFFFFFFFF) # MOV operation
ref_9902 = (ref_9868 & 0xFFFFFFFF) # MOV operation
ref_9914 = ref_9902 # MOV operation
ref_9916 = ref_9914 # MOV operation

print ref_9916 & 0xffffffffffffffff
