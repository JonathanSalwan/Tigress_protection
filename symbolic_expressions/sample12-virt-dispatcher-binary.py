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
ref_6853 = ref_311 # MOV operation
ref_7352 = ref_6853 # MOV operation
ref_7707 = (ref_7352 & 0xFFFFFFFF) # MOV operation
ref_10925 = (ref_7707 & 0xFFFFFFFF) # MOV operation
ref_10929 = (ref_10925 & 0xFFFFFFFF) # MOV operation
ref_10963 = (((ref_10929 & 0xFFFFFFFF) >> 24) & 0xFF) # Byte reference - MOV operation
ref_10964 = (((ref_10929 & 0xFFFFFFFF) >> 16) & 0xFF) # Byte reference - MOV operation
ref_10965 = (((ref_10929 & 0xFFFFFFFF) >> 8) & 0xFF) # Byte reference - MOV operation
ref_10966 = ((ref_10929 & 0xFFFFFFFF) & 0xFF) # Byte reference - MOV operation
ref_11017 = ref_10966 # MOVZX operation
ref_11019 = (ref_11017 & 0xFF) # MOVZX operation
ref_11025 = (ref_11019 & 0xFFFFFFFF) # MOV operation
ref_11051 = (ref_11025 & 0xFFFFFFFF) # MOV operation
ref_11061 = (ref_11051 & 0xFF) # MOVZX operation
ref_11063 = ((ref_11061 & 0xFFFFFFFF) ^ ((((0x81) << 8 | 0x1C) << 8 | 0x9D) << 8 | 0xC5)) # XOR operation
ref_11070 = (ref_11063 & 0xFFFFFFFF) # MOV operation
ref_11074 = (((sx(0x20, 0x1000193) * sx(0x20, (ref_11070 & 0xFFFFFFFF))) & 0xFFFFFFFFFFFFFFFF) & 0xFFFFFFFF) # IMUL operation
ref_11119 = ref_10965 # MOVZX operation
ref_11121 = (ref_11119 & 0xFF) # MOVZX operation
ref_11123 = (ref_11074 & 0xFFFFFFFF) # MOV operation
ref_11125 = (ref_11123 & 0xFFFFFFFF) # MOV operation
ref_11127 = (ref_11121 & 0xFFFFFFFF) # MOV operation
ref_11153 = (ref_11127 & 0xFFFFFFFF) # MOV operation
ref_11163 = (ref_11153 & 0xFF) # MOVZX operation
ref_11165 = ((ref_11163 & 0xFFFFFFFF) ^ (ref_11125 & 0xFFFFFFFF)) # XOR operation
ref_11172 = (ref_11165 & 0xFFFFFFFF) # MOV operation
ref_11176 = (((sx(0x20, 0x1000193) * sx(0x20, (ref_11172 & 0xFFFFFFFF))) & 0xFFFFFFFFFFFFFFFF) & 0xFFFFFFFF) # IMUL operation
ref_11221 = ref_10964 # MOVZX operation
ref_11223 = (ref_11221 & 0xFF) # MOVZX operation
ref_11225 = (ref_11176 & 0xFFFFFFFF) # MOV operation
ref_11227 = (ref_11225 & 0xFFFFFFFF) # MOV operation
ref_11229 = (ref_11223 & 0xFFFFFFFF) # MOV operation
ref_11255 = (ref_11229 & 0xFFFFFFFF) # MOV operation
ref_11265 = (ref_11255 & 0xFF) # MOVZX operation
ref_11267 = ((ref_11265 & 0xFFFFFFFF) ^ (ref_11227 & 0xFFFFFFFF)) # XOR operation
ref_11274 = (ref_11267 & 0xFFFFFFFF) # MOV operation
ref_11278 = (((sx(0x20, 0x1000193) * sx(0x20, (ref_11274 & 0xFFFFFFFF))) & 0xFFFFFFFFFFFFFFFF) & 0xFFFFFFFF) # IMUL operation
ref_11295 = ref_10963 # MOVZX operation
ref_11297 = (ref_11295 & 0xFF) # MOVZX operation
ref_11299 = (ref_11278 & 0xFFFFFFFF) # MOV operation
ref_11301 = (ref_11299 & 0xFFFFFFFF) # MOV operation
ref_11303 = (ref_11297 & 0xFFFFFFFF) # MOV operation
ref_11329 = (ref_11303 & 0xFFFFFFFF) # MOV operation
ref_11339 = (ref_11329 & 0xFF) # MOVZX operation
ref_11341 = ((ref_11339 & 0xFFFFFFFF) ^ (ref_11301 & 0xFFFFFFFF)) # XOR operation
ref_11348 = (ref_11341 & 0xFFFFFFFF) # MOV operation
ref_11352 = (((sx(0x20, 0x1000193) * sx(0x20, (ref_11348 & 0xFFFFFFFF))) & 0xFFFFFFFFFFFFFFFF) & 0xFFFFFFFF) # IMUL operation
ref_11367 = (ref_11352 & 0xFFFFFFFF) # MOV operation
ref_13217 = (ref_11367 & 0xFFFFFFFF) # MOV operation
ref_13572 = (ref_13217 & 0xFFFFFFFF) # MOV operation
ref_15001 = (ref_13572 & 0xFFFFFFFF) # MOV operation
ref_15454 = (ref_15001 & 0xFFFFFFFF) # MOV operation
ref_15488 = (ref_15454 & 0xFFFFFFFF) # MOV operation
ref_15500 = ref_15488 # MOV operation
ref_15502 = ref_15500 # MOV operation

print ref_15502 & 0xffffffffffffffff
