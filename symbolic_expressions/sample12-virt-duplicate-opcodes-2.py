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
ref_4884 = ref_311 # MOV operation
ref_4982 = ref_4884 # MOV operation
ref_5229 = (ref_4982 & 0xFFFFFFFF) # MOV operation
ref_5947 = (ref_5229 & 0xFFFFFFFF) # MOV operation
ref_5951 = (ref_5947 & 0xFFFFFFFF) # MOV operation
ref_5985 = (((ref_5951 & 0xFFFFFFFF) >> 24) & 0xFF) # Byte reference - MOV operation
ref_5986 = (((ref_5951 & 0xFFFFFFFF) >> 16) & 0xFF) # Byte reference - MOV operation
ref_5987 = (((ref_5951 & 0xFFFFFFFF) >> 8) & 0xFF) # Byte reference - MOV operation
ref_5988 = ((ref_5951 & 0xFFFFFFFF) & 0xFF) # Byte reference - MOV operation
ref_6039 = ref_5988 # MOVZX operation
ref_6041 = (ref_6039 & 0xFF) # MOVZX operation
ref_6047 = (ref_6041 & 0xFFFFFFFF) # MOV operation
ref_6073 = (ref_6047 & 0xFFFFFFFF) # MOV operation
ref_6083 = (ref_6073 & 0xFF) # MOVZX operation
ref_6085 = ((ref_6083 & 0xFFFFFFFF) ^ ((((0x81) << 8 | 0x1C) << 8 | 0x9D) << 8 | 0xC5)) # XOR operation
ref_6092 = (ref_6085 & 0xFFFFFFFF) # MOV operation
ref_6096 = (((sx(0x20, 0x1000193) * sx(0x20, (ref_6092 & 0xFFFFFFFF))) & 0xFFFFFFFFFFFFFFFF) & 0xFFFFFFFF) # IMUL operation
ref_6141 = ref_5987 # MOVZX operation
ref_6143 = (ref_6141 & 0xFF) # MOVZX operation
ref_6145 = (ref_6096 & 0xFFFFFFFF) # MOV operation
ref_6147 = (ref_6145 & 0xFFFFFFFF) # MOV operation
ref_6149 = (ref_6143 & 0xFFFFFFFF) # MOV operation
ref_6175 = (ref_6149 & 0xFFFFFFFF) # MOV operation
ref_6185 = (ref_6175 & 0xFF) # MOVZX operation
ref_6187 = ((ref_6185 & 0xFFFFFFFF) ^ (ref_6147 & 0xFFFFFFFF)) # XOR operation
ref_6194 = (ref_6187 & 0xFFFFFFFF) # MOV operation
ref_6198 = (((sx(0x20, 0x1000193) * sx(0x20, (ref_6194 & 0xFFFFFFFF))) & 0xFFFFFFFFFFFFFFFF) & 0xFFFFFFFF) # IMUL operation
ref_6243 = ref_5986 # MOVZX operation
ref_6245 = (ref_6243 & 0xFF) # MOVZX operation
ref_6247 = (ref_6198 & 0xFFFFFFFF) # MOV operation
ref_6249 = (ref_6247 & 0xFFFFFFFF) # MOV operation
ref_6251 = (ref_6245 & 0xFFFFFFFF) # MOV operation
ref_6277 = (ref_6251 & 0xFFFFFFFF) # MOV operation
ref_6287 = (ref_6277 & 0xFF) # MOVZX operation
ref_6289 = ((ref_6287 & 0xFFFFFFFF) ^ (ref_6249 & 0xFFFFFFFF)) # XOR operation
ref_6296 = (ref_6289 & 0xFFFFFFFF) # MOV operation
ref_6300 = (((sx(0x20, 0x1000193) * sx(0x20, (ref_6296 & 0xFFFFFFFF))) & 0xFFFFFFFFFFFFFFFF) & 0xFFFFFFFF) # IMUL operation
ref_6317 = ref_5985 # MOVZX operation
ref_6319 = (ref_6317 & 0xFF) # MOVZX operation
ref_6321 = (ref_6300 & 0xFFFFFFFF) # MOV operation
ref_6323 = (ref_6321 & 0xFFFFFFFF) # MOV operation
ref_6325 = (ref_6319 & 0xFFFFFFFF) # MOV operation
ref_6351 = (ref_6325 & 0xFFFFFFFF) # MOV operation
ref_6361 = (ref_6351 & 0xFF) # MOVZX operation
ref_6363 = ((ref_6361 & 0xFFFFFFFF) ^ (ref_6323 & 0xFFFFFFFF)) # XOR operation
ref_6370 = (ref_6363 & 0xFFFFFFFF) # MOV operation
ref_6374 = (((sx(0x20, 0x1000193) * sx(0x20, (ref_6370 & 0xFFFFFFFF))) & 0xFFFFFFFFFFFFFFFF) & 0xFFFFFFFF) # IMUL operation
ref_6389 = (ref_6374 & 0xFFFFFFFF) # MOV operation
ref_6807 = (ref_6389 & 0xFFFFFFFF) # MOV operation
ref_6920 = (ref_6807 & 0xFFFFFFFF) # MOV operation
ref_7242 = (ref_6920 & 0xFFFFFFFF) # MOV operation
ref_7325 = (ref_7242 & 0xFFFFFFFF) # MOV operation
ref_7359 = (ref_7325 & 0xFFFFFFFF) # MOV operation
ref_7371 = ref_7359 # MOV operation
ref_7373 = ref_7371 # MOV operation

print ref_7373 & 0xffffffffffffffff
