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
ref_9977 = ref_311 # MOV operation
ref_11702 = ref_9977 # MOV operation
ref_13415 = (ref_11702 & 0xFFFFFFFF) # MOV operation
ref_23931 = (ref_13415 & 0xFFFFFFFF) # MOV operation
ref_23935 = (ref_23931 & 0xFFFFFFFF) # MOV operation
ref_23969 = (((ref_23935 & 0xFFFFFFFF) >> 24) & 0xFF) # Byte reference - MOV operation
ref_23970 = (((ref_23935 & 0xFFFFFFFF) >> 16) & 0xFF) # Byte reference - MOV operation
ref_23971 = (((ref_23935 & 0xFFFFFFFF) >> 8) & 0xFF) # Byte reference - MOV operation
ref_23972 = ((ref_23935 & 0xFFFFFFFF) & 0xFF) # Byte reference - MOV operation
ref_24023 = ref_23972 # MOVZX operation
ref_24025 = (ref_24023 & 0xFF) # MOVZX operation
ref_24031 = (ref_24025 & 0xFFFFFFFF) # MOV operation
ref_24057 = (ref_24031 & 0xFFFFFFFF) # MOV operation
ref_24067 = (ref_24057 & 0xFF) # MOVZX operation
ref_24069 = ((ref_24067 & 0xFFFFFFFF) ^ ((((0x81) << 8 | 0x1C) << 8 | 0x9D) << 8 | 0xC5)) # XOR operation
ref_24076 = (ref_24069 & 0xFFFFFFFF) # MOV operation
ref_24080 = (((sx(0x20, 0x1000193) * sx(0x20, (ref_24076 & 0xFFFFFFFF))) & 0xFFFFFFFFFFFFFFFF) & 0xFFFFFFFF) # IMUL operation
ref_24125 = ref_23971 # MOVZX operation
ref_24127 = (ref_24125 & 0xFF) # MOVZX operation
ref_24129 = (ref_24080 & 0xFFFFFFFF) # MOV operation
ref_24131 = (ref_24129 & 0xFFFFFFFF) # MOV operation
ref_24133 = (ref_24127 & 0xFFFFFFFF) # MOV operation
ref_24159 = (ref_24133 & 0xFFFFFFFF) # MOV operation
ref_24169 = (ref_24159 & 0xFF) # MOVZX operation
ref_24171 = ((ref_24169 & 0xFFFFFFFF) ^ (ref_24131 & 0xFFFFFFFF)) # XOR operation
ref_24178 = (ref_24171 & 0xFFFFFFFF) # MOV operation
ref_24182 = (((sx(0x20, 0x1000193) * sx(0x20, (ref_24178 & 0xFFFFFFFF))) & 0xFFFFFFFFFFFFFFFF) & 0xFFFFFFFF) # IMUL operation
ref_24227 = ref_23970 # MOVZX operation
ref_24229 = (ref_24227 & 0xFF) # MOVZX operation
ref_24231 = (ref_24182 & 0xFFFFFFFF) # MOV operation
ref_24233 = (ref_24231 & 0xFFFFFFFF) # MOV operation
ref_24235 = (ref_24229 & 0xFFFFFFFF) # MOV operation
ref_24261 = (ref_24235 & 0xFFFFFFFF) # MOV operation
ref_24271 = (ref_24261 & 0xFF) # MOVZX operation
ref_24273 = ((ref_24271 & 0xFFFFFFFF) ^ (ref_24233 & 0xFFFFFFFF)) # XOR operation
ref_24280 = (ref_24273 & 0xFFFFFFFF) # MOV operation
ref_24284 = (((sx(0x20, 0x1000193) * sx(0x20, (ref_24280 & 0xFFFFFFFF))) & 0xFFFFFFFFFFFFFFFF) & 0xFFFFFFFF) # IMUL operation
ref_24301 = ref_23969 # MOVZX operation
ref_24303 = (ref_24301 & 0xFF) # MOVZX operation
ref_24305 = (ref_24284 & 0xFFFFFFFF) # MOV operation
ref_24307 = (ref_24305 & 0xFFFFFFFF) # MOV operation
ref_24309 = (ref_24303 & 0xFFFFFFFF) # MOV operation
ref_24335 = (ref_24309 & 0xFFFFFFFF) # MOV operation
ref_24345 = (ref_24335 & 0xFF) # MOVZX operation
ref_24347 = ((ref_24345 & 0xFFFFFFFF) ^ (ref_24307 & 0xFFFFFFFF)) # XOR operation
ref_24354 = (ref_24347 & 0xFFFFFFFF) # MOV operation
ref_24358 = (((sx(0x20, 0x1000193) * sx(0x20, (ref_24354 & 0xFFFFFFFF))) & 0xFFFFFFFFFFFFFFFF) & 0xFFFFFFFF) # IMUL operation
ref_24373 = (ref_24358 & 0xFFFFFFFF) # MOV operation
ref_29699 = (ref_24373 & 0xFFFFFFFF) # MOV operation
ref_31412 = (ref_29699 & 0xFFFFFFFF) # MOV operation
ref_36642 = (ref_31412 & 0xFFFFFFFF) # MOV operation
ref_38361 = (ref_36642 & 0xFFFFFFFF) # MOV operation
ref_38395 = (ref_38361 & 0xFFFFFFFF) # MOV operation
ref_38407 = ref_38395 # MOV operation
ref_38409 = ref_38407 # MOV operation

print ref_38409 & 0xffffffffffffffff
