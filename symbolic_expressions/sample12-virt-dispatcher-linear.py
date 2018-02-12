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
ref_6527 = ref_311 # MOV operation
ref_6962 = ref_6527 # MOV operation
ref_7507 = (ref_6962 & 0xFFFFFFFF) # MOV operation
ref_9365 = (ref_7507 & 0xFFFFFFFF) # MOV operation
ref_9369 = (ref_9365 & 0xFFFFFFFF) # MOV operation
ref_9403 = (((ref_9369 & 0xFFFFFFFF) >> 24) & 0xFF) # Byte reference - MOV operation
ref_9404 = (((ref_9369 & 0xFFFFFFFF) >> 16) & 0xFF) # Byte reference - MOV operation
ref_9405 = (((ref_9369 & 0xFFFFFFFF) >> 8) & 0xFF) # Byte reference - MOV operation
ref_9406 = ((ref_9369 & 0xFFFFFFFF) & 0xFF) # Byte reference - MOV operation
ref_9457 = ref_9406 # MOVZX operation
ref_9459 = (ref_9457 & 0xFF) # MOVZX operation
ref_9465 = (ref_9459 & 0xFFFFFFFF) # MOV operation
ref_9491 = (ref_9465 & 0xFFFFFFFF) # MOV operation
ref_9501 = (ref_9491 & 0xFF) # MOVZX operation
ref_9503 = ((ref_9501 & 0xFFFFFFFF) ^ ((((0x81) << 8 | 0x1C) << 8 | 0x9D) << 8 | 0xC5)) # XOR operation
ref_9510 = (ref_9503 & 0xFFFFFFFF) # MOV operation
ref_9514 = (((sx(0x20, 0x1000193) * sx(0x20, (ref_9510 & 0xFFFFFFFF))) & 0xFFFFFFFFFFFFFFFF) & 0xFFFFFFFF) # IMUL operation
ref_9559 = ref_9405 # MOVZX operation
ref_9561 = (ref_9559 & 0xFF) # MOVZX operation
ref_9563 = (ref_9514 & 0xFFFFFFFF) # MOV operation
ref_9565 = (ref_9563 & 0xFFFFFFFF) # MOV operation
ref_9567 = (ref_9561 & 0xFFFFFFFF) # MOV operation
ref_9593 = (ref_9567 & 0xFFFFFFFF) # MOV operation
ref_9603 = (ref_9593 & 0xFF) # MOVZX operation
ref_9605 = ((ref_9603 & 0xFFFFFFFF) ^ (ref_9565 & 0xFFFFFFFF)) # XOR operation
ref_9612 = (ref_9605 & 0xFFFFFFFF) # MOV operation
ref_9616 = (((sx(0x20, 0x1000193) * sx(0x20, (ref_9612 & 0xFFFFFFFF))) & 0xFFFFFFFFFFFFFFFF) & 0xFFFFFFFF) # IMUL operation
ref_9661 = ref_9404 # MOVZX operation
ref_9663 = (ref_9661 & 0xFF) # MOVZX operation
ref_9665 = (ref_9616 & 0xFFFFFFFF) # MOV operation
ref_9667 = (ref_9665 & 0xFFFFFFFF) # MOV operation
ref_9669 = (ref_9663 & 0xFFFFFFFF) # MOV operation
ref_9695 = (ref_9669 & 0xFFFFFFFF) # MOV operation
ref_9705 = (ref_9695 & 0xFF) # MOVZX operation
ref_9707 = ((ref_9705 & 0xFFFFFFFF) ^ (ref_9667 & 0xFFFFFFFF)) # XOR operation
ref_9714 = (ref_9707 & 0xFFFFFFFF) # MOV operation
ref_9718 = (((sx(0x20, 0x1000193) * sx(0x20, (ref_9714 & 0xFFFFFFFF))) & 0xFFFFFFFFFFFFFFFF) & 0xFFFFFFFF) # IMUL operation
ref_9735 = ref_9403 # MOVZX operation
ref_9737 = (ref_9735 & 0xFF) # MOVZX operation
ref_9739 = (ref_9718 & 0xFFFFFFFF) # MOV operation
ref_9741 = (ref_9739 & 0xFFFFFFFF) # MOV operation
ref_9743 = (ref_9737 & 0xFFFFFFFF) # MOV operation
ref_9769 = (ref_9743 & 0xFFFFFFFF) # MOV operation
ref_9779 = (ref_9769 & 0xFF) # MOVZX operation
ref_9781 = ((ref_9779 & 0xFFFFFFFF) ^ (ref_9741 & 0xFFFFFFFF)) # XOR operation
ref_9788 = (ref_9781 & 0xFFFFFFFF) # MOV operation
ref_9792 = (((sx(0x20, 0x1000193) * sx(0x20, (ref_9788 & 0xFFFFFFFF))) & 0xFFFFFFFFFFFFFFFF) & 0xFFFFFFFF) # IMUL operation
ref_9807 = (ref_9792 & 0xFFFFFFFF) # MOV operation
ref_10881 = (ref_9807 & 0xFFFFFFFF) # MOV operation
ref_11426 = (ref_10881 & 0xFFFFFFFF) # MOV operation
ref_12501 = (ref_11426 & 0xFFFFFFFF) # MOV operation
ref_13086 = (ref_12501 & 0xFFFFFFFF) # MOV operation
ref_13120 = (ref_13086 & 0xFFFFFFFF) # MOV operation
ref_13132 = ref_13120 # MOV operation
ref_13134 = ref_13132 # MOV operation

print ref_13134 & 0xffffffffffffffff
