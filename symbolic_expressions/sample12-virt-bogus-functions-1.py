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
ref_5521 = ref_311 # MOV operation
ref_5841 = ref_5521 # MOV operation
ref_6120 = (ref_5841 & 0xFFFFFFFF) # MOV operation
ref_8037 = (ref_6120 & 0xFFFFFFFF) # MOV operation
ref_8041 = (ref_8037 & 0xFFFFFFFF) # MOV operation
ref_8075 = (((ref_8041 & 0xFFFFFFFF) >> 24) & 0xFF) # Byte reference - MOV operation
ref_8076 = (((ref_8041 & 0xFFFFFFFF) >> 16) & 0xFF) # Byte reference - MOV operation
ref_8077 = (((ref_8041 & 0xFFFFFFFF) >> 8) & 0xFF) # Byte reference - MOV operation
ref_8078 = ((ref_8041 & 0xFFFFFFFF) & 0xFF) # Byte reference - MOV operation
ref_8129 = ref_8078 # MOVZX operation
ref_8131 = (ref_8129 & 0xFF) # MOVZX operation
ref_8137 = (ref_8131 & 0xFFFFFFFF) # MOV operation
ref_8163 = (ref_8137 & 0xFFFFFFFF) # MOV operation
ref_8173 = (ref_8163 & 0xFF) # MOVZX operation
ref_8175 = ((ref_8173 & 0xFFFFFFFF) ^ ((((0x81) << 8 | 0x1C) << 8 | 0x9D) << 8 | 0xC5)) # XOR operation
ref_8182 = (ref_8175 & 0xFFFFFFFF) # MOV operation
ref_8186 = (((sx(0x20, 0x1000193) * sx(0x20, (ref_8182 & 0xFFFFFFFF))) & 0xFFFFFFFFFFFFFFFF) & 0xFFFFFFFF) # IMUL operation
ref_8231 = ref_8077 # MOVZX operation
ref_8233 = (ref_8231 & 0xFF) # MOVZX operation
ref_8235 = (ref_8186 & 0xFFFFFFFF) # MOV operation
ref_8237 = (ref_8235 & 0xFFFFFFFF) # MOV operation
ref_8239 = (ref_8233 & 0xFFFFFFFF) # MOV operation
ref_8265 = (ref_8239 & 0xFFFFFFFF) # MOV operation
ref_8275 = (ref_8265 & 0xFF) # MOVZX operation
ref_8277 = ((ref_8275 & 0xFFFFFFFF) ^ (ref_8237 & 0xFFFFFFFF)) # XOR operation
ref_8284 = (ref_8277 & 0xFFFFFFFF) # MOV operation
ref_8288 = (((sx(0x20, 0x1000193) * sx(0x20, (ref_8284 & 0xFFFFFFFF))) & 0xFFFFFFFFFFFFFFFF) & 0xFFFFFFFF) # IMUL operation
ref_8333 = ref_8076 # MOVZX operation
ref_8335 = (ref_8333 & 0xFF) # MOVZX operation
ref_8337 = (ref_8288 & 0xFFFFFFFF) # MOV operation
ref_8339 = (ref_8337 & 0xFFFFFFFF) # MOV operation
ref_8341 = (ref_8335 & 0xFFFFFFFF) # MOV operation
ref_8367 = (ref_8341 & 0xFFFFFFFF) # MOV operation
ref_8377 = (ref_8367 & 0xFF) # MOVZX operation
ref_8379 = ((ref_8377 & 0xFFFFFFFF) ^ (ref_8339 & 0xFFFFFFFF)) # XOR operation
ref_8386 = (ref_8379 & 0xFFFFFFFF) # MOV operation
ref_8390 = (((sx(0x20, 0x1000193) * sx(0x20, (ref_8386 & 0xFFFFFFFF))) & 0xFFFFFFFFFFFFFFFF) & 0xFFFFFFFF) # IMUL operation
ref_8407 = ref_8075 # MOVZX operation
ref_8409 = (ref_8407 & 0xFF) # MOVZX operation
ref_8411 = (ref_8390 & 0xFFFFFFFF) # MOV operation
ref_8413 = (ref_8411 & 0xFFFFFFFF) # MOV operation
ref_8415 = (ref_8409 & 0xFFFFFFFF) # MOV operation
ref_8441 = (ref_8415 & 0xFFFFFFFF) # MOV operation
ref_8451 = (ref_8441 & 0xFF) # MOVZX operation
ref_8453 = ((ref_8451 & 0xFFFFFFFF) ^ (ref_8413 & 0xFFFFFFFF)) # XOR operation
ref_8460 = (ref_8453 & 0xFFFFFFFF) # MOV operation
ref_8464 = (((sx(0x20, 0x1000193) * sx(0x20, (ref_8460 & 0xFFFFFFFF))) & 0xFFFFFFFFFFFFFFFF) & 0xFFFFFFFF) # IMUL operation
ref_8479 = (ref_8464 & 0xFFFFFFFF) # MOV operation
ref_9540 = (ref_8479 & 0xFFFFFFFF) # MOV operation
ref_9867 = (ref_9540 & 0xFFFFFFFF) # MOV operation
ref_10819 = (ref_9867 & 0xFFFFFFFF) # MOV operation
ref_11075 = (ref_10819 & 0xFFFFFFFF) # MOV operation
ref_11112 = (ref_11075 & 0xFFFFFFFF) # MOV operation
ref_11124 = ref_11112 # MOV operation
ref_11126 = ref_11124 # MOV operation

print ref_11126 & 0xffffffffffffffff
