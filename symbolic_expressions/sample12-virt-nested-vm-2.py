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
ref_43826 = ref_311 # MOV operation
ref_45948 = ref_43826 # MOV operation
ref_54163 = ref_45948 # MOV operation
ref_54245 = ref_54163 # MOV operation
ref_54333 = (ref_54245 & 0xFFFFFFFF) # MOV operation
ref_62710 = (ref_54333 & 0xFFFFFFFF) # MOV operation
ref_62798 = (ref_62710 & 0xFFFFFFFF) # MOV operation
ref_127004 = (ref_62798 & 0xFFFFFFFF) # MOV operation
ref_127092 = (ref_127004 & 0xFFFFFFFF) # MOV operation
ref_129087 = (ref_127092 & 0xFFFFFFFF) # MOV operation
ref_129091 = (ref_129087 & 0xFFFFFFFF) # MOV operation
ref_129125 = (((ref_129091 & 0xFFFFFFFF) >> 24) & 0xFF) # Byte reference - MOV operation
ref_129126 = (((ref_129091 & 0xFFFFFFFF) >> 16) & 0xFF) # Byte reference - MOV operation
ref_129127 = (((ref_129091 & 0xFFFFFFFF) >> 8) & 0xFF) # Byte reference - MOV operation
ref_129128 = ((ref_129091 & 0xFFFFFFFF) & 0xFF) # Byte reference - MOV operation
ref_129179 = ref_129128 # MOVZX operation
ref_129181 = (ref_129179 & 0xFF) # MOVZX operation
ref_129187 = (ref_129181 & 0xFFFFFFFF) # MOV operation
ref_129213 = (ref_129187 & 0xFFFFFFFF) # MOV operation
ref_129223 = (ref_129213 & 0xFF) # MOVZX operation
ref_129225 = ((ref_129223 & 0xFFFFFFFF) ^ ((((0x81) << 8 | 0x1C) << 8 | 0x9D) << 8 | 0xC5)) # XOR operation
ref_129232 = (ref_129225 & 0xFFFFFFFF) # MOV operation
ref_129236 = (((sx(0x20, 0x1000193) * sx(0x20, (ref_129232 & 0xFFFFFFFF))) & 0xFFFFFFFFFFFFFFFF) & 0xFFFFFFFF) # IMUL operation
ref_129281 = ref_129127 # MOVZX operation
ref_129283 = (ref_129281 & 0xFF) # MOVZX operation
ref_129285 = (ref_129236 & 0xFFFFFFFF) # MOV operation
ref_129287 = (ref_129285 & 0xFFFFFFFF) # MOV operation
ref_129289 = (ref_129283 & 0xFFFFFFFF) # MOV operation
ref_129315 = (ref_129289 & 0xFFFFFFFF) # MOV operation
ref_129325 = (ref_129315 & 0xFF) # MOVZX operation
ref_129327 = ((ref_129325 & 0xFFFFFFFF) ^ (ref_129287 & 0xFFFFFFFF)) # XOR operation
ref_129334 = (ref_129327 & 0xFFFFFFFF) # MOV operation
ref_129338 = (((sx(0x20, 0x1000193) * sx(0x20, (ref_129334 & 0xFFFFFFFF))) & 0xFFFFFFFFFFFFFFFF) & 0xFFFFFFFF) # IMUL operation
ref_129383 = ref_129126 # MOVZX operation
ref_129385 = (ref_129383 & 0xFF) # MOVZX operation
ref_129387 = (ref_129338 & 0xFFFFFFFF) # MOV operation
ref_129389 = (ref_129387 & 0xFFFFFFFF) # MOV operation
ref_129391 = (ref_129385 & 0xFFFFFFFF) # MOV operation
ref_129417 = (ref_129391 & 0xFFFFFFFF) # MOV operation
ref_129427 = (ref_129417 & 0xFF) # MOVZX operation
ref_129429 = ((ref_129427 & 0xFFFFFFFF) ^ (ref_129389 & 0xFFFFFFFF)) # XOR operation
ref_129436 = (ref_129429 & 0xFFFFFFFF) # MOV operation
ref_129440 = (((sx(0x20, 0x1000193) * sx(0x20, (ref_129436 & 0xFFFFFFFF))) & 0xFFFFFFFFFFFFFFFF) & 0xFFFFFFFF) # IMUL operation
ref_129457 = ref_129125 # MOVZX operation
ref_129459 = (ref_129457 & 0xFF) # MOVZX operation
ref_129461 = (ref_129440 & 0xFFFFFFFF) # MOV operation
ref_129463 = (ref_129461 & 0xFFFFFFFF) # MOV operation
ref_129465 = (ref_129459 & 0xFFFFFFFF) # MOV operation
ref_129491 = (ref_129465 & 0xFFFFFFFF) # MOV operation
ref_129501 = (ref_129491 & 0xFF) # MOVZX operation
ref_129503 = ((ref_129501 & 0xFFFFFFFF) ^ (ref_129463 & 0xFFFFFFFF)) # XOR operation
ref_129510 = (ref_129503 & 0xFFFFFFFF) # MOV operation
ref_129514 = (((sx(0x20, 0x1000193) * sx(0x20, (ref_129510 & 0xFFFFFFFF))) & 0xFFFFFFFFFFFFFFFF) & 0xFFFFFFFF) # IMUL operation
ref_129529 = (ref_129514 & 0xFFFFFFFF) # MOV operation
ref_131304 = (ref_129529 & 0xFFFFFFFF) # MOV operation
ref_131392 = (ref_131304 & 0xFFFFFFFF) # MOV operation
ref_170031 = (ref_131392 & 0xFFFFFFFF) # MOV operation
ref_170119 = (ref_170031 & 0xFFFFFFFF) # MOV operation
ref_178496 = (ref_170119 & 0xFFFFFFFF) # MOV operation
ref_178584 = (ref_178496 & 0xFFFFFFFF) # MOV operation
ref_210841 = (ref_178584 & 0xFFFFFFFF) # MOV operation
ref_210929 = (ref_210841 & 0xFFFFFFFF) # MOV operation
ref_217246 = (ref_210929 & 0xFFFFFFFF) # MOV operation
ref_217334 = (ref_217246 & 0xFFFFFFFF) # MOV operation
ref_217754 = (ref_217334 & 0xFFFFFFFF) # MOV operation
ref_217830 = (ref_217754 & 0xFFFFFFFF) # MOV operation
ref_217864 = (ref_217830 & 0xFFFFFFFF) # MOV operation
ref_217876 = ref_217864 # MOV operation
ref_217878 = ref_217876 # MOV operation

print ref_217878 & 0xffffffffffffffff
