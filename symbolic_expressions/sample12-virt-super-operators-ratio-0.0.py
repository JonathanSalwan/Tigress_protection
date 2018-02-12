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
ref_5983 = (ref_5247 & 0xFFFFFFFF) # MOV operation
ref_5987 = (ref_5983 & 0xFFFFFFFF) # MOV operation
ref_6021 = (((ref_5987 & 0xFFFFFFFF) >> 24) & 0xFF) # Byte reference - MOV operation
ref_6022 = (((ref_5987 & 0xFFFFFFFF) >> 16) & 0xFF) # Byte reference - MOV operation
ref_6023 = (((ref_5987 & 0xFFFFFFFF) >> 8) & 0xFF) # Byte reference - MOV operation
ref_6024 = ((ref_5987 & 0xFFFFFFFF) & 0xFF) # Byte reference - MOV operation
ref_6075 = ref_6024 # MOVZX operation
ref_6077 = (ref_6075 & 0xFF) # MOVZX operation
ref_6083 = (ref_6077 & 0xFFFFFFFF) # MOV operation
ref_6109 = (ref_6083 & 0xFFFFFFFF) # MOV operation
ref_6119 = (ref_6109 & 0xFF) # MOVZX operation
ref_6121 = ((ref_6119 & 0xFFFFFFFF) ^ ((((0x81) << 8 | 0x1C) << 8 | 0x9D) << 8 | 0xC5)) # XOR operation
ref_6128 = (ref_6121 & 0xFFFFFFFF) # MOV operation
ref_6132 = (((sx(0x20, 0x1000193) * sx(0x20, (ref_6128 & 0xFFFFFFFF))) & 0xFFFFFFFFFFFFFFFF) & 0xFFFFFFFF) # IMUL operation
ref_6177 = ref_6023 # MOVZX operation
ref_6179 = (ref_6177 & 0xFF) # MOVZX operation
ref_6181 = (ref_6132 & 0xFFFFFFFF) # MOV operation
ref_6183 = (ref_6181 & 0xFFFFFFFF) # MOV operation
ref_6185 = (ref_6179 & 0xFFFFFFFF) # MOV operation
ref_6211 = (ref_6185 & 0xFFFFFFFF) # MOV operation
ref_6221 = (ref_6211 & 0xFF) # MOVZX operation
ref_6223 = ((ref_6221 & 0xFFFFFFFF) ^ (ref_6183 & 0xFFFFFFFF)) # XOR operation
ref_6230 = (ref_6223 & 0xFFFFFFFF) # MOV operation
ref_6234 = (((sx(0x20, 0x1000193) * sx(0x20, (ref_6230 & 0xFFFFFFFF))) & 0xFFFFFFFFFFFFFFFF) & 0xFFFFFFFF) # IMUL operation
ref_6279 = ref_6022 # MOVZX operation
ref_6281 = (ref_6279 & 0xFF) # MOVZX operation
ref_6283 = (ref_6234 & 0xFFFFFFFF) # MOV operation
ref_6285 = (ref_6283 & 0xFFFFFFFF) # MOV operation
ref_6287 = (ref_6281 & 0xFFFFFFFF) # MOV operation
ref_6313 = (ref_6287 & 0xFFFFFFFF) # MOV operation
ref_6323 = (ref_6313 & 0xFF) # MOVZX operation
ref_6325 = ((ref_6323 & 0xFFFFFFFF) ^ (ref_6285 & 0xFFFFFFFF)) # XOR operation
ref_6332 = (ref_6325 & 0xFFFFFFFF) # MOV operation
ref_6336 = (((sx(0x20, 0x1000193) * sx(0x20, (ref_6332 & 0xFFFFFFFF))) & 0xFFFFFFFFFFFFFFFF) & 0xFFFFFFFF) # IMUL operation
ref_6353 = ref_6021 # MOVZX operation
ref_6355 = (ref_6353 & 0xFF) # MOVZX operation
ref_6357 = (ref_6336 & 0xFFFFFFFF) # MOV operation
ref_6359 = (ref_6357 & 0xFFFFFFFF) # MOV operation
ref_6361 = (ref_6355 & 0xFFFFFFFF) # MOV operation
ref_6387 = (ref_6361 & 0xFFFFFFFF) # MOV operation
ref_6397 = (ref_6387 & 0xFF) # MOVZX operation
ref_6399 = ((ref_6397 & 0xFFFFFFFF) ^ (ref_6359 & 0xFFFFFFFF)) # XOR operation
ref_6406 = (ref_6399 & 0xFFFFFFFF) # MOV operation
ref_6410 = (((sx(0x20, 0x1000193) * sx(0x20, (ref_6406 & 0xFFFFFFFF))) & 0xFFFFFFFFFFFFFFFF) & 0xFFFFFFFF) # IMUL operation
ref_6425 = (ref_6410 & 0xFFFFFFFF) # MOV operation
ref_6843 = (ref_6425 & 0xFFFFFFFF) # MOV operation
ref_6956 = (ref_6843 & 0xFFFFFFFF) # MOV operation
ref_7314 = (ref_6956 & 0xFFFFFFFF) # MOV operation
ref_7397 = (ref_7314 & 0xFFFFFFFF) # MOV operation
ref_7431 = (ref_7397 & 0xFFFFFFFF) # MOV operation
ref_7443 = ref_7431 # MOV operation
ref_7445 = ref_7443 # MOV operation

print ref_7445 & 0xffffffffffffffff
