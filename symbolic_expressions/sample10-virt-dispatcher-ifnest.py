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
ref_7268 = ref_665 # MOV operation
ref_7280 = ref_7268 # MOV operation
ref_7308 = ref_7280 # MOV operation
ref_7321 = ref_7308 # MOV operation
ref_7334 = ref_7321 # MOV operation
ref_7336 = ref_7334 # MOV operation
ref_7386 = (((sx(0x40, 0xC2B2AE3D27D4EB4F) * sx(0x40, ref_7336)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_7420 = rol(0x1F, ((((((((((0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) + ref_7386) & 0xFFFFFFFFFFFFFFFF)) # MOV operation
ref_7422 = (((sx(0x40, 0x9E3779B185EBCA87) * sx(0x40, ref_7420)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_7436 = ref_7422 # MOV operation
ref_7453 = ref_7436 # MOV operation
ref_7465 = ref_7453 # MOV operation
ref_7482 = (((((((((0x27) << 8 | 0xD4) << 8 | 0xEB) << 8 | 0x2F) << 8 | 0x16) << 8 | 0x56) << 8 | 0x67) << 8 | 0xCD) ^ ref_7465) # MOV operation
ref_7484 = rol(0x1B, ref_7482) # ROL operation
ref_7488 = ref_7484 # MOV operation
ref_7492 = (((sx(0x40, ref_7488) * sx(0x40, 0x9E3779B185EBCA87)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_7498 = ((0x85EBCA77C2B2AE63 + ref_7492) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_7591 = ref_7498 # MOV operation
ref_7593 = (ref_7591 >> (0x21 & 0x3F)) # SHR operation
ref_7617 = (ref_7498 ^ ref_7593) # MOV operation
ref_7619 = (((sx(0x40, 0xC2B2AE3D27D4EB4F) * sx(0x40, ref_7617)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_7633 = ref_7619 # MOV operation
ref_7635 = (ref_7633 >> (0x1D & 0x3F)) # SHR operation
ref_7659 = (ref_7619 ^ ref_7635) # MOV operation
ref_7661 = (((sx(0x40, 0x165667B19E3779F9) * sx(0x40, ref_7659)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_7675 = ref_7661 # MOV operation
ref_7677 = (ref_7675 >> (0x20 & 0x3F)) # SHR operation
ref_7699 = (ref_7661 ^ ref_7677) # MOV operation
ref_7711 = ref_7699 # MOV operation
ref_8266 = ref_7711 # MOV operation
ref_8418 = ref_8266 # MOV operation
ref_8965 = ref_8418 # MOV operation
ref_9117 = ref_8965 # MOV operation
ref_9664 = ref_9117 # MOV operation
ref_9824 = ref_9664 # MOV operation
ref_9895 = ref_9824 # MOV operation
ref_10245 = ref_9895 # MOV operation
ref_10358 = ref_10245 # MOV operation
ref_10396 = ref_10358 # MOV operation
ref_10408 = ref_10396 # MOV operation
ref_10410 = ref_10408 # MOV operation

print ref_10410 & 0xffffffffffffffff
