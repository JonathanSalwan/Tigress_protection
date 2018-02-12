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
ref_5063 = ref_311 # MOV operation
ref_5152 = ref_5063 # MOV operation
ref_5229 = (ref_5152 & 0xFFFFFFFF) # MOV operation
ref_5929 = (ref_5229 & 0xFFFFFFFF) # MOV operation
ref_5933 = (ref_5929 & 0xFFFFFFFF) # MOV operation
ref_5967 = (((ref_5933 & 0xFFFFFFFF) >> 24) & 0xFF) # Byte reference - MOV operation
ref_5968 = (((ref_5933 & 0xFFFFFFFF) >> 16) & 0xFF) # Byte reference - MOV operation
ref_5969 = (((ref_5933 & 0xFFFFFFFF) >> 8) & 0xFF) # Byte reference - MOV operation
ref_5970 = ((ref_5933 & 0xFFFFFFFF) & 0xFF) # Byte reference - MOV operation
ref_6021 = ref_5970 # MOVZX operation
ref_6023 = (ref_6021 & 0xFF) # MOVZX operation
ref_6029 = (ref_6023 & 0xFFFFFFFF) # MOV operation
ref_6055 = (ref_6029 & 0xFFFFFFFF) # MOV operation
ref_6065 = (ref_6055 & 0xFF) # MOVZX operation
ref_6067 = ((ref_6065 & 0xFFFFFFFF) ^ ((((0x81) << 8 | 0x1C) << 8 | 0x9D) << 8 | 0xC5)) # XOR operation
ref_6074 = (ref_6067 & 0xFFFFFFFF) # MOV operation
ref_6078 = (((sx(0x20, 0x1000193) * sx(0x20, (ref_6074 & 0xFFFFFFFF))) & 0xFFFFFFFFFFFFFFFF) & 0xFFFFFFFF) # IMUL operation
ref_6123 = ref_5969 # MOVZX operation
ref_6125 = (ref_6123 & 0xFF) # MOVZX operation
ref_6127 = (ref_6078 & 0xFFFFFFFF) # MOV operation
ref_6129 = (ref_6127 & 0xFFFFFFFF) # MOV operation
ref_6131 = (ref_6125 & 0xFFFFFFFF) # MOV operation
ref_6157 = (ref_6131 & 0xFFFFFFFF) # MOV operation
ref_6167 = (ref_6157 & 0xFF) # MOVZX operation
ref_6169 = ((ref_6167 & 0xFFFFFFFF) ^ (ref_6129 & 0xFFFFFFFF)) # XOR operation
ref_6176 = (ref_6169 & 0xFFFFFFFF) # MOV operation
ref_6180 = (((sx(0x20, 0x1000193) * sx(0x20, (ref_6176 & 0xFFFFFFFF))) & 0xFFFFFFFFFFFFFFFF) & 0xFFFFFFFF) # IMUL operation
ref_6225 = ref_5968 # MOVZX operation
ref_6227 = (ref_6225 & 0xFF) # MOVZX operation
ref_6229 = (ref_6180 & 0xFFFFFFFF) # MOV operation
ref_6231 = (ref_6229 & 0xFFFFFFFF) # MOV operation
ref_6233 = (ref_6227 & 0xFFFFFFFF) # MOV operation
ref_6259 = (ref_6233 & 0xFFFFFFFF) # MOV operation
ref_6269 = (ref_6259 & 0xFF) # MOVZX operation
ref_6271 = ((ref_6269 & 0xFFFFFFFF) ^ (ref_6231 & 0xFFFFFFFF)) # XOR operation
ref_6278 = (ref_6271 & 0xFFFFFFFF) # MOV operation
ref_6282 = (((sx(0x20, 0x1000193) * sx(0x20, (ref_6278 & 0xFFFFFFFF))) & 0xFFFFFFFFFFFFFFFF) & 0xFFFFFFFF) # IMUL operation
ref_6299 = ref_5967 # MOVZX operation
ref_6301 = (ref_6299 & 0xFF) # MOVZX operation
ref_6303 = (ref_6282 & 0xFFFFFFFF) # MOV operation
ref_6305 = (ref_6303 & 0xFFFFFFFF) # MOV operation
ref_6307 = (ref_6301 & 0xFFFFFFFF) # MOV operation
ref_6333 = (ref_6307 & 0xFFFFFFFF) # MOV operation
ref_6343 = (ref_6333 & 0xFF) # MOVZX operation
ref_6345 = ((ref_6343 & 0xFFFFFFFF) ^ (ref_6305 & 0xFFFFFFFF)) # XOR operation
ref_6352 = (ref_6345 & 0xFFFFFFFF) # MOV operation
ref_6356 = (((sx(0x20, 0x1000193) * sx(0x20, (ref_6352 & 0xFFFFFFFF))) & 0xFFFFFFFFFFFFFFFF) & 0xFFFFFFFF) # IMUL operation
ref_6371 = (ref_6356 & 0xFFFFFFFF) # MOV operation
ref_6789 = (ref_6371 & 0xFFFFFFFF) # MOV operation
ref_6866 = (ref_6789 & 0xFFFFFFFF) # MOV operation
ref_7188 = (ref_6866 & 0xFFFFFFFF) # MOV operation
ref_7271 = (ref_7188 & 0xFFFFFFFF) # MOV operation
ref_7305 = (ref_7271 & 0xFFFFFFFF) # MOV operation
ref_7317 = ref_7305 # MOV operation
ref_7319 = ref_7317 # MOV operation

print ref_7319 & 0xffffffffffffffff
