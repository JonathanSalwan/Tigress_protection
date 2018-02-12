#!/usr/bin/env python2
## -*- coding: utf-8 -*-

import sys

def sx(bits, value):
    sign_bit = 1 << (bits - 1)
    return (value & (sign_bit - 1)) - (value & sign_bit)

SymVar_0 = int(sys.argv[1])
ref_296 = SymVar_0
ref_307 = ref_296 # MOV operation
ref_319 = ref_307 # MOV operation
ref_321 = ref_319 # MOV operation
ref_9489 = ref_321 # MOV operation
ref_9854 = ref_9489 # MOV operation
ref_10240 = (ref_9854 & 0xFFFFFFFF) # MOV operation
ref_13029 = (ref_10240 & 0xFFFFFFFF) # MOV operation
ref_13033 = (ref_13029 & 0xFFFFFFFF) # MOV operation
ref_13067 = (((ref_13033 & 0xFFFFFFFF) >> 24) & 0xFF) # Byte reference - MOV operation
ref_13068 = (((ref_13033 & 0xFFFFFFFF) >> 16) & 0xFF) # Byte reference - MOV operation
ref_13069 = (((ref_13033 & 0xFFFFFFFF) >> 8) & 0xFF) # Byte reference - MOV operation
ref_13070 = ((ref_13033 & 0xFFFFFFFF) & 0xFF) # Byte reference - MOV operation
ref_13121 = ref_13070 # MOVZX operation
ref_13123 = (ref_13121 & 0xFF) # MOVZX operation
ref_13129 = (ref_13123 & 0xFFFFFFFF) # MOV operation
ref_13155 = (ref_13129 & 0xFFFFFFFF) # MOV operation
ref_13165 = (ref_13155 & 0xFF) # MOVZX operation
ref_13167 = ((ref_13165 & 0xFFFFFFFF) ^ ((((0x81) << 8 | 0x1C) << 8 | 0x9D) << 8 | 0xC5)) # XOR operation
ref_13174 = (ref_13167 & 0xFFFFFFFF) # MOV operation
ref_13180 = (((sx(0x20, 0x1000193) * sx(0x20, (ref_13174 & 0xFFFFFFFF))) & 0xFFFFFFFFFFFFFFFF) & 0xFFFFFFFF) # IMUL operation
ref_13225 = ref_13069 # MOVZX operation
ref_13227 = (ref_13225 & 0xFF) # MOVZX operation
ref_13229 = (ref_13180 & 0xFFFFFFFF) # MOV operation
ref_13231 = (ref_13229 & 0xFFFFFFFF) # MOV operation
ref_13233 = (ref_13227 & 0xFFFFFFFF) # MOV operation
ref_13259 = (ref_13233 & 0xFFFFFFFF) # MOV operation
ref_13269 = (ref_13259 & 0xFF) # MOVZX operation
ref_13271 = ((ref_13269 & 0xFFFFFFFF) ^ (ref_13231 & 0xFFFFFFFF)) # XOR operation
ref_13278 = (ref_13271 & 0xFFFFFFFF) # MOV operation
ref_13284 = (((sx(0x20, 0x1000193) * sx(0x20, (ref_13278 & 0xFFFFFFFF))) & 0xFFFFFFFFFFFFFFFF) & 0xFFFFFFFF) # IMUL operation
ref_13329 = ref_13068 # MOVZX operation
ref_13331 = (ref_13329 & 0xFF) # MOVZX operation
ref_13333 = (ref_13284 & 0xFFFFFFFF) # MOV operation
ref_13335 = (ref_13333 & 0xFFFFFFFF) # MOV operation
ref_13337 = (ref_13331 & 0xFFFFFFFF) # MOV operation
ref_13363 = (ref_13337 & 0xFFFFFFFF) # MOV operation
ref_13373 = (ref_13363 & 0xFF) # MOVZX operation
ref_13375 = ((ref_13373 & 0xFFFFFFFF) ^ (ref_13335 & 0xFFFFFFFF)) # XOR operation
ref_13382 = (ref_13375 & 0xFFFFFFFF) # MOV operation
ref_13388 = (((sx(0x20, 0x1000193) * sx(0x20, (ref_13382 & 0xFFFFFFFF))) & 0xFFFFFFFFFFFFFFFF) & 0xFFFFFFFF) # IMUL operation
ref_13405 = ref_13067 # MOVZX operation
ref_13407 = (ref_13405 & 0xFF) # MOVZX operation
ref_13409 = (ref_13388 & 0xFFFFFFFF) # MOV operation
ref_13411 = (ref_13409 & 0xFFFFFFFF) # MOV operation
ref_13413 = (ref_13407 & 0xFFFFFFFF) # MOV operation
ref_13439 = (ref_13413 & 0xFFFFFFFF) # MOV operation
ref_13449 = (ref_13439 & 0xFF) # MOVZX operation
ref_13451 = ((ref_13449 & 0xFFFFFFFF) ^ (ref_13411 & 0xFFFFFFFF)) # XOR operation
ref_13458 = (ref_13451 & 0xFFFFFFFF) # MOV operation
ref_13464 = (((sx(0x20, 0x1000193) * sx(0x20, (ref_13458 & 0xFFFFFFFF))) & 0xFFFFFFFFFFFFFFFF) & 0xFFFFFFFF) # IMUL operation
ref_13479 = (ref_13464 & 0xFFFFFFFF) # MOV operation
ref_14879 = (ref_13479 & 0xFFFFFFFF) # MOV operation
ref_15269 = (ref_14879 & 0xFFFFFFFF) # MOV operation
ref_16585 = (ref_15269 & 0xFFFFFFFF) # MOV operation
ref_16967 = (ref_16585 & 0xFFFFFFFF) # MOV operation
ref_17002 = (ref_16967 & 0xFFFFFFFF) # MOV operation
ref_17014 = ref_17002 # MOV operation
ref_17016 = ref_17014 # MOV operation

print ref_17016 & 0xffffffffffffffff
