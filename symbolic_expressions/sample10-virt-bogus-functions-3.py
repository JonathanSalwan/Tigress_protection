#!/usr/bin/env python2
## -*- coding: utf-8 -*-

import sys

def sx(bits, value):
    sign_bit = 1 << (bits - 1)
    return (value & (sign_bit - 1)) - (value & sign_bit)

SymVar_0 = int(sys.argv[1])
ref_640 = SymVar_0
ref_651 = ref_640 # MOV operation
ref_663 = ref_651 # MOV operation
ref_665 = ref_663 # MOV operation
ref_13107 = ref_665 # MOV operation
ref_13119 = ref_13107 # MOV operation
ref_13147 = ref_13119 # MOV operation
ref_13160 = ref_13147 # MOV operation
ref_13173 = ref_13160 # MOV operation
ref_13175 = ref_13173 # MOV operation
ref_13225 = (((sx(0x40, 0xC2B2AE3D27D4EB4F) * sx(0x40, ref_13175)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_13259 = rol(0x1F, ((((((((((0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) + ref_13225) & 0xFFFFFFFFFFFFFFFF)) # MOV operation
ref_13261 = (((sx(0x40, 0x9E3779B185EBCA87) * sx(0x40, ref_13259)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_13275 = ref_13261 # MOV operation
ref_13292 = ref_13275 # MOV operation
ref_13304 = ref_13292 # MOV operation
ref_13321 = (((((((((0x27) << 8 | 0xD4) << 8 | 0xEB) << 8 | 0x2F) << 8 | 0x16) << 8 | 0x56) << 8 | 0x67) << 8 | 0xCD) ^ ref_13304) # MOV operation
ref_13323 = rol(0x1B, ref_13321) # ROL operation
ref_13327 = ref_13323 # MOV operation
ref_13331 = (((sx(0x40, ref_13327) * sx(0x40, 0x9E3779B185EBCA87)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_13337 = ((0x85EBCA77C2B2AE63 + ref_13331) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_13430 = ref_13337 # MOV operation
ref_13432 = (ref_13430 >> (0x21 & 0x3F)) # SHR operation
ref_13456 = (ref_13337 ^ ref_13432) # MOV operation
ref_13458 = (((sx(0x40, 0xC2B2AE3D27D4EB4F) * sx(0x40, ref_13456)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_13472 = ref_13458 # MOV operation
ref_13474 = (ref_13472 >> (0x1D & 0x3F)) # SHR operation
ref_13498 = (ref_13458 ^ ref_13474) # MOV operation
ref_13500 = (((sx(0x40, 0x165667B19E3779F9) * sx(0x40, ref_13498)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_13514 = ref_13500 # MOV operation
ref_13516 = (ref_13514 >> (0x20 & 0x3F)) # SHR operation
ref_13538 = (ref_13500 ^ ref_13516) # MOV operation
ref_13550 = ref_13538 # MOV operation
ref_15766 = ref_13550 # MOV operation
ref_16450 = ref_15766 # MOV operation
ref_18268 = ref_16450 # MOV operation
ref_18904 = ref_18268 # MOV operation
ref_20894 = ref_18904 # MOV operation
ref_21488 = ref_20894 # MOV operation
ref_22165 = ref_21488 # MOV operation
ref_24083 = ref_22165 # MOV operation
ref_24670 = ref_24083 # MOV operation
ref_24711 = ref_24670 # MOV operation
ref_24723 = ref_24711 # MOV operation
ref_24725 = ref_24723 # MOV operation

print ref_24725 & 0xffffffffffffffff
