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
ref_236419 = ref_665 # MOV operation
ref_236431 = ref_236419 # MOV operation
ref_236459 = ref_236431 # MOV operation
ref_236472 = ref_236459 # MOV operation
ref_236485 = ref_236472 # MOV operation
ref_236487 = ref_236485 # MOV operation
ref_236537 = (((sx(0x40, 0xC2B2AE3D27D4EB4F) * sx(0x40, ref_236487)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_236571 = rol(0x1F, ((((((((((0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) + ref_236537) & 0xFFFFFFFFFFFFFFFF)) # MOV operation
ref_236573 = (((sx(0x40, 0x9E3779B185EBCA87) * sx(0x40, ref_236571)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_236587 = ref_236573 # MOV operation
ref_236604 = ref_236587 # MOV operation
ref_236616 = ref_236604 # MOV operation
ref_236633 = (((((((((0x27) << 8 | 0xD4) << 8 | 0xEB) << 8 | 0x2F) << 8 | 0x16) << 8 | 0x56) << 8 | 0x67) << 8 | 0xCD) ^ ref_236616) # MOV operation
ref_236635 = rol(0x1B, ref_236633) # ROL operation
ref_236639 = ref_236635 # MOV operation
ref_236643 = (((sx(0x40, ref_236639) * sx(0x40, 0x9E3779B185EBCA87)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_236649 = ((0x85EBCA77C2B2AE63 + ref_236643) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_236742 = ref_236649 # MOV operation
ref_236744 = (ref_236742 >> (0x21 & 0x3F)) # SHR operation
ref_236768 = (ref_236649 ^ ref_236744) # MOV operation
ref_236770 = (((sx(0x40, 0xC2B2AE3D27D4EB4F) * sx(0x40, ref_236768)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_236784 = ref_236770 # MOV operation
ref_236786 = (ref_236784 >> (0x1D & 0x3F)) # SHR operation
ref_236810 = (ref_236770 ^ ref_236786) # MOV operation
ref_236812 = (((sx(0x40, 0x165667B19E3779F9) * sx(0x40, ref_236810)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_236826 = ref_236812 # MOV operation
ref_236828 = (ref_236826 >> (0x20 & 0x3F)) # SHR operation
ref_236850 = (ref_236812 ^ ref_236828) # MOV operation
ref_236862 = ref_236850 # MOV operation
ref_294663 = ref_236862 # MOV operation
ref_313870 = ref_294663 # MOV operation
ref_371663 = ref_313870 # MOV operation
ref_390870 = ref_371663 # MOV operation
ref_448663 = ref_390870 # MOV operation
ref_467887 = ref_448663 # MOV operation
ref_487130 = ref_467887 # MOV operation
ref_544834 = ref_487130 # MOV operation
ref_564047 = ref_544834 # MOV operation
ref_564085 = ref_564047 # MOV operation
ref_564097 = ref_564085 # MOV operation
ref_564099 = ref_564097 # MOV operation

print ref_564099 & 0xffffffffffffffff
