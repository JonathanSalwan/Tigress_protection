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
ref_5088 = ref_311 # MOV operation
ref_5185 = ref_5088 # MOV operation
ref_5261 = (ref_5185 & 0xFFFFFFFF) # MOV operation
ref_5928 = (ref_5261 & 0xFFFFFFFF) # MOV operation
ref_5932 = (ref_5928 & 0xFFFFFFFF) # MOV operation
ref_5966 = (((ref_5932 & 0xFFFFFFFF) >> 24) & 0xFF) # Byte reference - MOV operation
ref_5967 = (((ref_5932 & 0xFFFFFFFF) >> 16) & 0xFF) # Byte reference - MOV operation
ref_5968 = (((ref_5932 & 0xFFFFFFFF) >> 8) & 0xFF) # Byte reference - MOV operation
ref_5969 = ((ref_5932 & 0xFFFFFFFF) & 0xFF) # Byte reference - MOV operation
ref_6020 = ref_5969 # MOVZX operation
ref_6022 = (ref_6020 & 0xFF) # MOVZX operation
ref_6028 = (ref_6022 & 0xFFFFFFFF) # MOV operation
ref_6054 = (ref_6028 & 0xFFFFFFFF) # MOV operation
ref_6064 = (ref_6054 & 0xFF) # MOVZX operation
ref_6066 = ((ref_6064 & 0xFFFFFFFF) ^ ((((0x81) << 8 | 0x1C) << 8 | 0x9D) << 8 | 0xC5)) # XOR operation
ref_6073 = (ref_6066 & 0xFFFFFFFF) # MOV operation
ref_6077 = (((sx(0x20, 0x1000193) * sx(0x20, (ref_6073 & 0xFFFFFFFF))) & 0xFFFFFFFFFFFFFFFF) & 0xFFFFFFFF) # IMUL operation
ref_6122 = ref_5968 # MOVZX operation
ref_6124 = (ref_6122 & 0xFF) # MOVZX operation
ref_6126 = (ref_6077 & 0xFFFFFFFF) # MOV operation
ref_6128 = (ref_6126 & 0xFFFFFFFF) # MOV operation
ref_6130 = (ref_6124 & 0xFFFFFFFF) # MOV operation
ref_6156 = (ref_6130 & 0xFFFFFFFF) # MOV operation
ref_6166 = (ref_6156 & 0xFF) # MOVZX operation
ref_6168 = ((ref_6166 & 0xFFFFFFFF) ^ (ref_6128 & 0xFFFFFFFF)) # XOR operation
ref_6175 = (ref_6168 & 0xFFFFFFFF) # MOV operation
ref_6179 = (((sx(0x20, 0x1000193) * sx(0x20, (ref_6175 & 0xFFFFFFFF))) & 0xFFFFFFFFFFFFFFFF) & 0xFFFFFFFF) # IMUL operation
ref_6224 = ref_5967 # MOVZX operation
ref_6226 = (ref_6224 & 0xFF) # MOVZX operation
ref_6228 = (ref_6179 & 0xFFFFFFFF) # MOV operation
ref_6230 = (ref_6228 & 0xFFFFFFFF) # MOV operation
ref_6232 = (ref_6226 & 0xFFFFFFFF) # MOV operation
ref_6258 = (ref_6232 & 0xFFFFFFFF) # MOV operation
ref_6268 = (ref_6258 & 0xFF) # MOVZX operation
ref_6270 = ((ref_6268 & 0xFFFFFFFF) ^ (ref_6230 & 0xFFFFFFFF)) # XOR operation
ref_6277 = (ref_6270 & 0xFFFFFFFF) # MOV operation
ref_6281 = (((sx(0x20, 0x1000193) * sx(0x20, (ref_6277 & 0xFFFFFFFF))) & 0xFFFFFFFFFFFFFFFF) & 0xFFFFFFFF) # IMUL operation
ref_6298 = ref_5966 # MOVZX operation
ref_6300 = (ref_6298 & 0xFF) # MOVZX operation
ref_6302 = (ref_6281 & 0xFFFFFFFF) # MOV operation
ref_6304 = (ref_6302 & 0xFFFFFFFF) # MOV operation
ref_6306 = (ref_6300 & 0xFFFFFFFF) # MOV operation
ref_6332 = (ref_6306 & 0xFFFFFFFF) # MOV operation
ref_6342 = (ref_6332 & 0xFF) # MOVZX operation
ref_6344 = ((ref_6342 & 0xFFFFFFFF) ^ (ref_6304 & 0xFFFFFFFF)) # XOR operation
ref_6351 = (ref_6344 & 0xFFFFFFFF) # MOV operation
ref_6355 = (((sx(0x20, 0x1000193) * sx(0x20, (ref_6351 & 0xFFFFFFFF))) & 0xFFFFFFFFFFFFFFFF) & 0xFFFFFFFF) # IMUL operation
ref_6370 = (ref_6355 & 0xFFFFFFFF) # MOV operation
ref_6668 = (ref_6370 & 0xFFFFFFFF) # MOV operation
ref_6744 = (ref_6668 & 0xFFFFFFFF) # MOV operation
ref_7045 = (ref_6744 & 0xFFFFFFFF) # MOV operation
ref_7154 = (ref_7045 & 0xFFFFFFFF) # MOV operation
ref_7188 = (ref_7154 & 0xFFFFFFFF) # MOV operation
ref_7200 = ref_7188 # MOV operation
ref_7202 = ref_7200 # MOV operation

print ref_7202 & 0xffffffffffffffff
