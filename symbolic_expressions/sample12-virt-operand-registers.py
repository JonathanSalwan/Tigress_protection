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
ref_4915 = ref_311 # MOV operation
ref_5040 = ref_4915 # MOV operation
ref_5042 = (ref_5040 & 0xFFFFFFFF) # MOV operation
ref_5291 = (ref_5042 & 0xFFFFFFFF) # MOV operation
ref_6051 = (ref_5291 & 0xFFFFFFFF) # MOV operation
ref_6055 = (ref_6051 & 0xFFFFFFFF) # MOV operation
ref_6089 = (((ref_6055 & 0xFFFFFFFF) >> 24) & 0xFF) # Byte reference - MOV operation
ref_6090 = (((ref_6055 & 0xFFFFFFFF) >> 16) & 0xFF) # Byte reference - MOV operation
ref_6091 = (((ref_6055 & 0xFFFFFFFF) >> 8) & 0xFF) # Byte reference - MOV operation
ref_6092 = ((ref_6055 & 0xFFFFFFFF) & 0xFF) # Byte reference - MOV operation
ref_6143 = ref_6092 # MOVZX operation
ref_6145 = (ref_6143 & 0xFF) # MOVZX operation
ref_6151 = (ref_6145 & 0xFFFFFFFF) # MOV operation
ref_6177 = (ref_6151 & 0xFFFFFFFF) # MOV operation
ref_6187 = (ref_6177 & 0xFF) # MOVZX operation
ref_6189 = ((ref_6187 & 0xFFFFFFFF) ^ ((((0x81) << 8 | 0x1C) << 8 | 0x9D) << 8 | 0xC5)) # XOR operation
ref_6196 = (ref_6189 & 0xFFFFFFFF) # MOV operation
ref_6200 = (((sx(0x20, 0x1000193) * sx(0x20, (ref_6196 & 0xFFFFFFFF))) & 0xFFFFFFFFFFFFFFFF) & 0xFFFFFFFF) # IMUL operation
ref_6245 = ref_6091 # MOVZX operation
ref_6247 = (ref_6245 & 0xFF) # MOVZX operation
ref_6249 = (ref_6200 & 0xFFFFFFFF) # MOV operation
ref_6251 = (ref_6249 & 0xFFFFFFFF) # MOV operation
ref_6253 = (ref_6247 & 0xFFFFFFFF) # MOV operation
ref_6279 = (ref_6253 & 0xFFFFFFFF) # MOV operation
ref_6289 = (ref_6279 & 0xFF) # MOVZX operation
ref_6291 = ((ref_6289 & 0xFFFFFFFF) ^ (ref_6251 & 0xFFFFFFFF)) # XOR operation
ref_6298 = (ref_6291 & 0xFFFFFFFF) # MOV operation
ref_6302 = (((sx(0x20, 0x1000193) * sx(0x20, (ref_6298 & 0xFFFFFFFF))) & 0xFFFFFFFFFFFFFFFF) & 0xFFFFFFFF) # IMUL operation
ref_6347 = ref_6090 # MOVZX operation
ref_6349 = (ref_6347 & 0xFF) # MOVZX operation
ref_6351 = (ref_6302 & 0xFFFFFFFF) # MOV operation
ref_6353 = (ref_6351 & 0xFFFFFFFF) # MOV operation
ref_6355 = (ref_6349 & 0xFFFFFFFF) # MOV operation
ref_6381 = (ref_6355 & 0xFFFFFFFF) # MOV operation
ref_6391 = (ref_6381 & 0xFF) # MOVZX operation
ref_6393 = ((ref_6391 & 0xFFFFFFFF) ^ (ref_6353 & 0xFFFFFFFF)) # XOR operation
ref_6400 = (ref_6393 & 0xFFFFFFFF) # MOV operation
ref_6404 = (((sx(0x20, 0x1000193) * sx(0x20, (ref_6400 & 0xFFFFFFFF))) & 0xFFFFFFFFFFFFFFFF) & 0xFFFFFFFF) # IMUL operation
ref_6421 = ref_6089 # MOVZX operation
ref_6423 = (ref_6421 & 0xFF) # MOVZX operation
ref_6425 = (ref_6404 & 0xFFFFFFFF) # MOV operation
ref_6427 = (ref_6425 & 0xFFFFFFFF) # MOV operation
ref_6429 = (ref_6423 & 0xFFFFFFFF) # MOV operation
ref_6455 = (ref_6429 & 0xFFFFFFFF) # MOV operation
ref_6465 = (ref_6455 & 0xFF) # MOVZX operation
ref_6467 = ((ref_6465 & 0xFFFFFFFF) ^ (ref_6427 & 0xFFFFFFFF)) # XOR operation
ref_6474 = (ref_6467 & 0xFFFFFFFF) # MOV operation
ref_6478 = (((sx(0x20, 0x1000193) * sx(0x20, (ref_6474 & 0xFFFFFFFF))) & 0xFFFFFFFFFFFFFFFF) & 0xFFFFFFFF) # IMUL operation
ref_6493 = (ref_6478 & 0xFFFFFFFF) # MOV operation
ref_6763 = (ref_6493 & 0xFFFFFFFF) # MOV operation
ref_7012 = (ref_6763 & 0xFFFFFFFF) # MOV operation
ref_7338 = (ref_7012 & 0xFFFFFFFF) # MOV operation
ref_7447 = (ref_7338 & 0xFFFFFFFF) # MOV operation
ref_7481 = (ref_7447 & 0xFFFFFFFF) # MOV operation
ref_7493 = ref_7481 # MOV operation
ref_7495 = ref_7493 # MOV operation

print ref_7495 & 0xffffffffffffffff
