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
ref_4991 = ref_311 # MOV operation
ref_5007 = ref_4991 # MOV operation
ref_5029 = (ref_5007 & 0xFFFFFFFF) # MOV operation
ref_5517 = (ref_5029 & 0xFFFFFFFF) # MOV operation
ref_5521 = (ref_5517 & 0xFFFFFFFF) # MOV operation
ref_5555 = (((ref_5521 & 0xFFFFFFFF) >> 24) & 0xFF) # Byte reference - MOV operation
ref_5556 = (((ref_5521 & 0xFFFFFFFF) >> 16) & 0xFF) # Byte reference - MOV operation
ref_5557 = (((ref_5521 & 0xFFFFFFFF) >> 8) & 0xFF) # Byte reference - MOV operation
ref_5558 = ((ref_5521 & 0xFFFFFFFF) & 0xFF) # Byte reference - MOV operation
ref_5609 = ref_5558 # MOVZX operation
ref_5611 = (ref_5609 & 0xFF) # MOVZX operation
ref_5617 = (ref_5611 & 0xFFFFFFFF) # MOV operation
ref_5643 = (ref_5617 & 0xFFFFFFFF) # MOV operation
ref_5653 = (ref_5643 & 0xFF) # MOVZX operation
ref_5655 = ((ref_5653 & 0xFFFFFFFF) ^ ((((0x81) << 8 | 0x1C) << 8 | 0x9D) << 8 | 0xC5)) # XOR operation
ref_5662 = (ref_5655 & 0xFFFFFFFF) # MOV operation
ref_5666 = (((sx(0x20, 0x1000193) * sx(0x20, (ref_5662 & 0xFFFFFFFF))) & 0xFFFFFFFFFFFFFFFF) & 0xFFFFFFFF) # IMUL operation
ref_5711 = ref_5557 # MOVZX operation
ref_5713 = (ref_5711 & 0xFF) # MOVZX operation
ref_5715 = (ref_5666 & 0xFFFFFFFF) # MOV operation
ref_5717 = (ref_5715 & 0xFFFFFFFF) # MOV operation
ref_5719 = (ref_5713 & 0xFFFFFFFF) # MOV operation
ref_5745 = (ref_5719 & 0xFFFFFFFF) # MOV operation
ref_5755 = (ref_5745 & 0xFF) # MOVZX operation
ref_5757 = ((ref_5755 & 0xFFFFFFFF) ^ (ref_5717 & 0xFFFFFFFF)) # XOR operation
ref_5764 = (ref_5757 & 0xFFFFFFFF) # MOV operation
ref_5768 = (((sx(0x20, 0x1000193) * sx(0x20, (ref_5764 & 0xFFFFFFFF))) & 0xFFFFFFFFFFFFFFFF) & 0xFFFFFFFF) # IMUL operation
ref_5813 = ref_5556 # MOVZX operation
ref_5815 = (ref_5813 & 0xFF) # MOVZX operation
ref_5817 = (ref_5768 & 0xFFFFFFFF) # MOV operation
ref_5819 = (ref_5817 & 0xFFFFFFFF) # MOV operation
ref_5821 = (ref_5815 & 0xFFFFFFFF) # MOV operation
ref_5847 = (ref_5821 & 0xFFFFFFFF) # MOV operation
ref_5857 = (ref_5847 & 0xFF) # MOVZX operation
ref_5859 = ((ref_5857 & 0xFFFFFFFF) ^ (ref_5819 & 0xFFFFFFFF)) # XOR operation
ref_5866 = (ref_5859 & 0xFFFFFFFF) # MOV operation
ref_5870 = (((sx(0x20, 0x1000193) * sx(0x20, (ref_5866 & 0xFFFFFFFF))) & 0xFFFFFFFFFFFFFFFF) & 0xFFFFFFFF) # IMUL operation
ref_5887 = ref_5555 # MOVZX operation
ref_5889 = (ref_5887 & 0xFF) # MOVZX operation
ref_5891 = (ref_5870 & 0xFFFFFFFF) # MOV operation
ref_5893 = (ref_5891 & 0xFFFFFFFF) # MOV operation
ref_5895 = (ref_5889 & 0xFFFFFFFF) # MOV operation
ref_5921 = (ref_5895 & 0xFFFFFFFF) # MOV operation
ref_5931 = (ref_5921 & 0xFF) # MOVZX operation
ref_5933 = ((ref_5931 & 0xFFFFFFFF) ^ (ref_5893 & 0xFFFFFFFF)) # XOR operation
ref_5940 = (ref_5933 & 0xFFFFFFFF) # MOV operation
ref_5944 = (((sx(0x20, 0x1000193) * sx(0x20, (ref_5940 & 0xFFFFFFFF))) & 0xFFFFFFFFFFFFFFFF) & 0xFFFFFFFF) # IMUL operation
ref_5959 = (ref_5944 & 0xFFFFFFFF) # MOV operation
ref_6166 = (ref_5959 & 0xFFFFFFFF) # MOV operation
ref_6196 = (ref_6166 & 0xFFFFFFFF) # MOV operation
ref_6424 = (ref_6196 & 0xFFFFFFFF) # MOV operation
ref_6547 = (ref_6424 & 0xFFFFFFFF) # MOV operation
ref_6581 = (ref_6547 & 0xFFFFFFFF) # MOV operation
ref_6593 = ref_6581 # MOV operation
ref_6595 = ref_6593 # MOV operation

print ref_6595 & 0xffffffffffffffff
