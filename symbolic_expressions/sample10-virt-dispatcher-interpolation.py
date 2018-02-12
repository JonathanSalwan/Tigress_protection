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
ref_12372 = ref_665 # MOV operation
ref_12384 = ref_12372 # MOV operation
ref_12412 = ref_12384 # MOV operation
ref_12425 = ref_12412 # MOV operation
ref_12438 = ref_12425 # MOV operation
ref_12440 = ref_12438 # MOV operation
ref_12490 = (((sx(0x40, 0xC2B2AE3D27D4EB4F) * sx(0x40, ref_12440)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_12524 = rol(0x1F, ((((((((((0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) + ref_12490) & 0xFFFFFFFFFFFFFFFF)) # MOV operation
ref_12526 = (((sx(0x40, 0x9E3779B185EBCA87) * sx(0x40, ref_12524)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_12540 = ref_12526 # MOV operation
ref_12557 = ref_12540 # MOV operation
ref_12569 = ref_12557 # MOV operation
ref_12586 = (((((((((0x27) << 8 | 0xD4) << 8 | 0xEB) << 8 | 0x2F) << 8 | 0x16) << 8 | 0x56) << 8 | 0x67) << 8 | 0xCD) ^ ref_12569) # MOV operation
ref_12588 = rol(0x1B, ref_12586) # ROL operation
ref_12592 = ref_12588 # MOV operation
ref_12596 = (((sx(0x40, ref_12592) * sx(0x40, 0x9E3779B185EBCA87)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_12602 = ((0x85EBCA77C2B2AE63 + ref_12596) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_12695 = ref_12602 # MOV operation
ref_12697 = (ref_12695 >> (0x21 & 0x3F)) # SHR operation
ref_12721 = (ref_12602 ^ ref_12697) # MOV operation
ref_12723 = (((sx(0x40, 0xC2B2AE3D27D4EB4F) * sx(0x40, ref_12721)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_12737 = ref_12723 # MOV operation
ref_12739 = (ref_12737 >> (0x1D & 0x3F)) # SHR operation
ref_12763 = (ref_12723 ^ ref_12739) # MOV operation
ref_12765 = (((sx(0x40, 0x165667B19E3779F9) * sx(0x40, ref_12763)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_12779 = ref_12765 # MOV operation
ref_12781 = (ref_12779 >> (0x20 & 0x3F)) # SHR operation
ref_12803 = (ref_12765 ^ ref_12781) # MOV operation
ref_12815 = ref_12803 # MOV operation
ref_14465 = ref_12815 # MOV operation
ref_15094 = ref_14465 # MOV operation
ref_16736 = ref_15094 # MOV operation
ref_17365 = ref_16736 # MOV operation
ref_19007 = ref_17365 # MOV operation
ref_19586 = ref_19007 # MOV operation
ref_20175 = ref_19586 # MOV operation
ref_21548 = ref_20175 # MOV operation
ref_22125 = ref_21548 # MOV operation
ref_22163 = ref_22125 # MOV operation
ref_22175 = ref_22163 # MOV operation
ref_22177 = ref_22175 # MOV operation

print ref_22177 & 0xffffffffffffffff
