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
ref_5036 = ref_311 # MOV operation
ref_5134 = ref_5036 # MOV operation
ref_5247 = (ref_5134 & 0xFFFFFFFF) # MOV operation
ref_5965 = (ref_5247 & 0xFFFFFFFF) # MOV operation
ref_5969 = (ref_5965 & 0xFFFFFFFF) # MOV operation
ref_6003 = (((ref_5969 & 0xFFFFFFFF) >> 24) & 0xFF) # Byte reference - MOV operation
ref_6004 = (((ref_5969 & 0xFFFFFFFF) >> 16) & 0xFF) # Byte reference - MOV operation
ref_6005 = (((ref_5969 & 0xFFFFFFFF) >> 8) & 0xFF) # Byte reference - MOV operation
ref_6006 = ((ref_5969 & 0xFFFFFFFF) & 0xFF) # Byte reference - MOV operation
ref_6057 = ref_6006 # MOVZX operation
ref_6059 = (ref_6057 & 0xFF) # MOVZX operation
ref_6065 = (ref_6059 & 0xFFFFFFFF) # MOV operation
ref_6091 = (ref_6065 & 0xFFFFFFFF) # MOV operation
ref_6101 = (ref_6091 & 0xFF) # MOVZX operation
ref_6103 = ((ref_6101 & 0xFFFFFFFF) ^ ((((0x81) << 8 | 0x1C) << 8 | 0x9D) << 8 | 0xC5)) # XOR operation
ref_6110 = (ref_6103 & 0xFFFFFFFF) # MOV operation
ref_6114 = (((sx(0x20, 0x1000193) * sx(0x20, (ref_6110 & 0xFFFFFFFF))) & 0xFFFFFFFFFFFFFFFF) & 0xFFFFFFFF) # IMUL operation
ref_6159 = ref_6005 # MOVZX operation
ref_6161 = (ref_6159 & 0xFF) # MOVZX operation
ref_6163 = (ref_6114 & 0xFFFFFFFF) # MOV operation
ref_6165 = (ref_6163 & 0xFFFFFFFF) # MOV operation
ref_6167 = (ref_6161 & 0xFFFFFFFF) # MOV operation
ref_6193 = (ref_6167 & 0xFFFFFFFF) # MOV operation
ref_6203 = (ref_6193 & 0xFF) # MOVZX operation
ref_6205 = ((ref_6203 & 0xFFFFFFFF) ^ (ref_6165 & 0xFFFFFFFF)) # XOR operation
ref_6212 = (ref_6205 & 0xFFFFFFFF) # MOV operation
ref_6216 = (((sx(0x20, 0x1000193) * sx(0x20, (ref_6212 & 0xFFFFFFFF))) & 0xFFFFFFFFFFFFFFFF) & 0xFFFFFFFF) # IMUL operation
ref_6261 = ref_6004 # MOVZX operation
ref_6263 = (ref_6261 & 0xFF) # MOVZX operation
ref_6265 = (ref_6216 & 0xFFFFFFFF) # MOV operation
ref_6267 = (ref_6265 & 0xFFFFFFFF) # MOV operation
ref_6269 = (ref_6263 & 0xFFFFFFFF) # MOV operation
ref_6295 = (ref_6269 & 0xFFFFFFFF) # MOV operation
ref_6305 = (ref_6295 & 0xFF) # MOVZX operation
ref_6307 = ((ref_6305 & 0xFFFFFFFF) ^ (ref_6267 & 0xFFFFFFFF)) # XOR operation
ref_6314 = (ref_6307 & 0xFFFFFFFF) # MOV operation
ref_6318 = (((sx(0x20, 0x1000193) * sx(0x20, (ref_6314 & 0xFFFFFFFF))) & 0xFFFFFFFFFFFFFFFF) & 0xFFFFFFFF) # IMUL operation
ref_6335 = ref_6003 # MOVZX operation
ref_6337 = (ref_6335 & 0xFF) # MOVZX operation
ref_6339 = (ref_6318 & 0xFFFFFFFF) # MOV operation
ref_6341 = (ref_6339 & 0xFFFFFFFF) # MOV operation
ref_6343 = (ref_6337 & 0xFFFFFFFF) # MOV operation
ref_6369 = (ref_6343 & 0xFFFFFFFF) # MOV operation
ref_6379 = (ref_6369 & 0xFF) # MOVZX operation
ref_6381 = ((ref_6379 & 0xFFFFFFFF) ^ (ref_6341 & 0xFFFFFFFF)) # XOR operation
ref_6388 = (ref_6381 & 0xFFFFFFFF) # MOV operation
ref_6392 = (((sx(0x20, 0x1000193) * sx(0x20, (ref_6388 & 0xFFFFFFFF))) & 0xFFFFFFFFFFFFFFFF) & 0xFFFFFFFF) # IMUL operation
ref_6407 = (ref_6392 & 0xFFFFFFFF) # MOV operation
ref_6825 = (ref_6407 & 0xFFFFFFFF) # MOV operation
ref_6938 = (ref_6825 & 0xFFFFFFFF) # MOV operation
ref_7260 = (ref_6938 & 0xFFFFFFFF) # MOV operation
ref_7343 = (ref_7260 & 0xFFFFFFFF) # MOV operation
ref_7377 = (ref_7343 & 0xFFFFFFFF) # MOV operation
ref_7389 = ref_7377 # MOV operation
ref_7391 = ref_7389 # MOV operation

print ref_7391 & 0xffffffffffffffff
