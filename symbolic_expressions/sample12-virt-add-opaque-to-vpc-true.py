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
ref_5185 = ref_311 # MOV operation
ref_5322 = ref_5185 # MOV operation
ref_5451 = (ref_5322 & 0xFFFFFFFF) # MOV operation
ref_6449 = (ref_5451 & 0xFFFFFFFF) # MOV operation
ref_6453 = (ref_6449 & 0xFFFFFFFF) # MOV operation
ref_6487 = (((ref_6453 & 0xFFFFFFFF) >> 24) & 0xFF) # Byte reference - MOV operation
ref_6488 = (((ref_6453 & 0xFFFFFFFF) >> 16) & 0xFF) # Byte reference - MOV operation
ref_6489 = (((ref_6453 & 0xFFFFFFFF) >> 8) & 0xFF) # Byte reference - MOV operation
ref_6490 = ((ref_6453 & 0xFFFFFFFF) & 0xFF) # Byte reference - MOV operation
ref_6541 = ref_6490 # MOVZX operation
ref_6543 = (ref_6541 & 0xFF) # MOVZX operation
ref_6549 = (ref_6543 & 0xFFFFFFFF) # MOV operation
ref_6575 = (ref_6549 & 0xFFFFFFFF) # MOV operation
ref_6585 = (ref_6575 & 0xFF) # MOVZX operation
ref_6587 = ((ref_6585 & 0xFFFFFFFF) ^ ((((0x81) << 8 | 0x1C) << 8 | 0x9D) << 8 | 0xC5)) # XOR operation
ref_6594 = (ref_6587 & 0xFFFFFFFF) # MOV operation
ref_6598 = (((sx(0x20, 0x1000193) * sx(0x20, (ref_6594 & 0xFFFFFFFF))) & 0xFFFFFFFFFFFFFFFF) & 0xFFFFFFFF) # IMUL operation
ref_6643 = ref_6489 # MOVZX operation
ref_6645 = (ref_6643 & 0xFF) # MOVZX operation
ref_6647 = (ref_6598 & 0xFFFFFFFF) # MOV operation
ref_6649 = (ref_6647 & 0xFFFFFFFF) # MOV operation
ref_6651 = (ref_6645 & 0xFFFFFFFF) # MOV operation
ref_6677 = (ref_6651 & 0xFFFFFFFF) # MOV operation
ref_6687 = (ref_6677 & 0xFF) # MOVZX operation
ref_6689 = ((ref_6687 & 0xFFFFFFFF) ^ (ref_6649 & 0xFFFFFFFF)) # XOR operation
ref_6696 = (ref_6689 & 0xFFFFFFFF) # MOV operation
ref_6700 = (((sx(0x20, 0x1000193) * sx(0x20, (ref_6696 & 0xFFFFFFFF))) & 0xFFFFFFFFFFFFFFFF) & 0xFFFFFFFF) # IMUL operation
ref_6745 = ref_6488 # MOVZX operation
ref_6747 = (ref_6745 & 0xFF) # MOVZX operation
ref_6749 = (ref_6700 & 0xFFFFFFFF) # MOV operation
ref_6751 = (ref_6749 & 0xFFFFFFFF) # MOV operation
ref_6753 = (ref_6747 & 0xFFFFFFFF) # MOV operation
ref_6779 = (ref_6753 & 0xFFFFFFFF) # MOV operation
ref_6789 = (ref_6779 & 0xFF) # MOVZX operation
ref_6791 = ((ref_6789 & 0xFFFFFFFF) ^ (ref_6751 & 0xFFFFFFFF)) # XOR operation
ref_6798 = (ref_6791 & 0xFFFFFFFF) # MOV operation
ref_6802 = (((sx(0x20, 0x1000193) * sx(0x20, (ref_6798 & 0xFFFFFFFF))) & 0xFFFFFFFFFFFFFFFF) & 0xFFFFFFFF) # IMUL operation
ref_6819 = ref_6487 # MOVZX operation
ref_6821 = (ref_6819 & 0xFF) # MOVZX operation
ref_6823 = (ref_6802 & 0xFFFFFFFF) # MOV operation
ref_6825 = (ref_6823 & 0xFFFFFFFF) # MOV operation
ref_6827 = (ref_6821 & 0xFFFFFFFF) # MOV operation
ref_6853 = (ref_6827 & 0xFFFFFFFF) # MOV operation
ref_6863 = (ref_6853 & 0xFF) # MOVZX operation
ref_6865 = ((ref_6863 & 0xFFFFFFFF) ^ (ref_6825 & 0xFFFFFFFF)) # XOR operation
ref_6872 = (ref_6865 & 0xFFFFFFFF) # MOV operation
ref_6876 = (((sx(0x20, 0x1000193) * sx(0x20, (ref_6872 & 0xFFFFFFFF))) & 0xFFFFFFFFFFFFFFFF) & 0xFFFFFFFF) # IMUL operation
ref_6891 = (ref_6876 & 0xFFFFFFFF) # MOV operation
ref_7454 = (ref_6891 & 0xFFFFFFFF) # MOV operation
ref_7583 = (ref_7454 & 0xFFFFFFFF) # MOV operation
ref_8028 = (ref_7583 & 0xFFFFFFFF) # MOV operation
ref_8134 = (ref_8028 & 0xFFFFFFFF) # MOV operation
ref_8168 = (ref_8134 & 0xFFFFFFFF) # MOV operation
ref_8180 = ref_8168 # MOV operation
ref_8182 = ref_8180 # MOV operation

print ref_8182 & 0xffffffffffffffff
