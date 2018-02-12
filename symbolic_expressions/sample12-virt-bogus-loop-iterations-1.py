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
ref_7553 = ref_311 # MOV operation
ref_8470 = ref_7553 # MOV operation
ref_9375 = (ref_8470 & 0xFFFFFFFF) # MOV operation
ref_15043 = (ref_9375 & 0xFFFFFFFF) # MOV operation
ref_15047 = (ref_15043 & 0xFFFFFFFF) # MOV operation
ref_15081 = (((ref_15047 & 0xFFFFFFFF) >> 24) & 0xFF) # Byte reference - MOV operation
ref_15082 = (((ref_15047 & 0xFFFFFFFF) >> 16) & 0xFF) # Byte reference - MOV operation
ref_15083 = (((ref_15047 & 0xFFFFFFFF) >> 8) & 0xFF) # Byte reference - MOV operation
ref_15084 = ((ref_15047 & 0xFFFFFFFF) & 0xFF) # Byte reference - MOV operation
ref_15135 = ref_15084 # MOVZX operation
ref_15137 = (ref_15135 & 0xFF) # MOVZX operation
ref_15143 = (ref_15137 & 0xFFFFFFFF) # MOV operation
ref_15169 = (ref_15143 & 0xFFFFFFFF) # MOV operation
ref_15179 = (ref_15169 & 0xFF) # MOVZX operation
ref_15181 = ((ref_15179 & 0xFFFFFFFF) ^ ((((0x81) << 8 | 0x1C) << 8 | 0x9D) << 8 | 0xC5)) # XOR operation
ref_15188 = (ref_15181 & 0xFFFFFFFF) # MOV operation
ref_15192 = (((sx(0x20, 0x1000193) * sx(0x20, (ref_15188 & 0xFFFFFFFF))) & 0xFFFFFFFFFFFFFFFF) & 0xFFFFFFFF) # IMUL operation
ref_15237 = ref_15083 # MOVZX operation
ref_15239 = (ref_15237 & 0xFF) # MOVZX operation
ref_15241 = (ref_15192 & 0xFFFFFFFF) # MOV operation
ref_15243 = (ref_15241 & 0xFFFFFFFF) # MOV operation
ref_15245 = (ref_15239 & 0xFFFFFFFF) # MOV operation
ref_15271 = (ref_15245 & 0xFFFFFFFF) # MOV operation
ref_15281 = (ref_15271 & 0xFF) # MOVZX operation
ref_15283 = ((ref_15281 & 0xFFFFFFFF) ^ (ref_15243 & 0xFFFFFFFF)) # XOR operation
ref_15290 = (ref_15283 & 0xFFFFFFFF) # MOV operation
ref_15294 = (((sx(0x20, 0x1000193) * sx(0x20, (ref_15290 & 0xFFFFFFFF))) & 0xFFFFFFFFFFFFFFFF) & 0xFFFFFFFF) # IMUL operation
ref_15339 = ref_15082 # MOVZX operation
ref_15341 = (ref_15339 & 0xFF) # MOVZX operation
ref_15343 = (ref_15294 & 0xFFFFFFFF) # MOV operation
ref_15345 = (ref_15343 & 0xFFFFFFFF) # MOV operation
ref_15347 = (ref_15341 & 0xFFFFFFFF) # MOV operation
ref_15373 = (ref_15347 & 0xFFFFFFFF) # MOV operation
ref_15383 = (ref_15373 & 0xFF) # MOVZX operation
ref_15385 = ((ref_15383 & 0xFFFFFFFF) ^ (ref_15345 & 0xFFFFFFFF)) # XOR operation
ref_15392 = (ref_15385 & 0xFFFFFFFF) # MOV operation
ref_15396 = (((sx(0x20, 0x1000193) * sx(0x20, (ref_15392 & 0xFFFFFFFF))) & 0xFFFFFFFFFFFFFFFF) & 0xFFFFFFFF) # IMUL operation
ref_15413 = ref_15081 # MOVZX operation
ref_15415 = (ref_15413 & 0xFF) # MOVZX operation
ref_15417 = (ref_15396 & 0xFFFFFFFF) # MOV operation
ref_15419 = (ref_15417 & 0xFFFFFFFF) # MOV operation
ref_15421 = (ref_15415 & 0xFFFFFFFF) # MOV operation
ref_15447 = (ref_15421 & 0xFFFFFFFF) # MOV operation
ref_15457 = (ref_15447 & 0xFF) # MOVZX operation
ref_15459 = ((ref_15457 & 0xFFFFFFFF) ^ (ref_15419 & 0xFFFFFFFF)) # XOR operation
ref_15466 = (ref_15459 & 0xFFFFFFFF) # MOV operation
ref_15470 = (((sx(0x20, 0x1000193) * sx(0x20, (ref_15466 & 0xFFFFFFFF))) & 0xFFFFFFFFFFFFFFFF) & 0xFFFFFFFF) # IMUL operation
ref_15485 = (ref_15470 & 0xFFFFFFFF) # MOV operation
ref_18387 = (ref_15485 & 0xFFFFFFFF) # MOV operation
ref_19292 = (ref_18387 & 0xFFFFFFFF) # MOV operation
ref_22098 = (ref_19292 & 0xFFFFFFFF) # MOV operation
ref_23009 = (ref_22098 & 0xFFFFFFFF) # MOV operation
ref_23043 = (ref_23009 & 0xFFFFFFFF) # MOV operation
ref_23055 = ref_23043 # MOV operation
ref_23057 = ref_23055 # MOV operation

print ref_23057 & 0xffffffffffffffff
