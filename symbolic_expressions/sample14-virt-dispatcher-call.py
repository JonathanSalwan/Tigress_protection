#!/usr/bin/env python2
## -*- coding: utf-8 -*-

import sys

def sx(bits, value):
    sign_bit = 1 << (bits - 1)
    return (value & (sign_bit - 1)) - (value & sign_bit)

SymVar_0 = int(sys.argv[1])
ref_680 = SymVar_0
ref_691 = ref_680 # MOV operation
ref_703 = ref_691 # MOV operation
ref_705 = ref_703 # MOV operation
ref_739 = ((ref_705 >> 56) & 0xFF) # Byte reference - MOV operation
ref_740 = ((ref_705 >> 48) & 0xFF) # Byte reference - MOV operation
ref_741 = ((ref_705 >> 40) & 0xFF) # Byte reference - MOV operation
ref_742 = ((ref_705 >> 32) & 0xFF) # Byte reference - MOV operation
ref_743 = ((ref_705 >> 24) & 0xFF) # Byte reference - MOV operation
ref_744 = ((ref_705 >> 16) & 0xFF) # Byte reference - MOV operation
ref_745 = ((ref_705 >> 8) & 0xFF) # Byte reference - MOV operation
ref_746 = (ref_705 & 0xFF) # Byte reference - MOV operation
ref_6429 = ((((ref_743) << 8 | ref_744) << 8 | ref_745) << 8 | ref_746) # MOV operation
ref_6437 = (ref_6429 & 0xFFFFFFFF) # MOV operation
ref_6461 = (ref_6437 & 0xFFFFFFFF) # MOV operation
ref_6475 = (ref_6461 & 0xFFFFFFFF) # MOV operation
ref_6612 = ((((ref_739) << 8 | ref_740) << 8 | ref_741) << 8 | ref_742) # MOV operation
ref_6620 = (ref_6612 & 0xFFFFFFFF) # MOV operation
ref_6644 = (ref_6620 & 0xFFFFFFFF) # MOV operation
ref_6658 = (ref_6644 & 0xFFFFFFFF) # MOV operation
ref_6660 = ref_6475 # MOV operation
ref_6662 = ((0x0 + ((0x0 + ((ref_6660 * 0x8) & 0xFFFFFFFFFFFFFFFF)) & 0xFFFFFFFFFFFFFFFF)) & 0xFFFFFFFFFFFFFFFF) # LEA operation
ref_6666 = ((0x8 + ref_6662) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_6674 = ref_6658 # MOV operation
ref_6676 = ref_6666 # MOV operation
ref_6730 = ref_6676 # MOV operation
ref_6742 = ref_6674 # MOV operation
ref_6754 = ref_6730 # MOV operation
ref_6756 = ref_6742 # MOV operation
ref_6758 = ref_6754 # MOV operation
ref_6760 = ref_6756 # MOV operation
ref_6786 = ref_6758 # MOV operation
ref_6788 = ref_6760 # MOV operation
ref_6790 = ref_6788 # MOV operation
ref_6824 = ref_6786 # MOV operation
ref_6826 = ref_6790 # MOV operation
ref_6828 = (ref_6826 ^ ref_6824) # XOR operation
ref_6835 = (((sx(0x40, ref_6828) * sx(0x40, ((((((((0x9D) << 8 | 0xDF) << 8 | 0xEA) << 8 | 0x8) << 8 | 0xEB) << 8 | 0x38) << 8 | 0x2D) << 8 | 0x69))) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_6849 = ref_6835 # MOV operation
ref_6851 = (ref_6849 >> (0x2F & 0x3F)) # SHR operation
ref_6873 = ref_6790 # MOV operation
ref_6875 = (ref_6873 ^ (ref_6835 ^ ref_6851)) # XOR operation
ref_6882 = (((sx(0x40, ref_6875) * sx(0x40, ((((((((0x9D) << 8 | 0xDF) << 8 | 0xEA) << 8 | 0x8) << 8 | 0xEB) << 8 | 0x38) << 8 | 0x2D) << 8 | 0x69))) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_6896 = ref_6882 # MOV operation
ref_6898 = (ref_6896 >> (0x2F & 0x3F)) # SHR operation
ref_6920 = (ref_6882 ^ ref_6898) # MOV operation
ref_6922 = (((sx(0x40, ref_6920) * sx(0x40, ((((((((0x9D) << 8 | 0xDF) << 8 | 0xEA) << 8 | 0x8) << 8 | 0xEB) << 8 | 0x38) << 8 | 0x2D) << 8 | 0x69))) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_6936 = ref_6922 # MOV operation
ref_6953 = ref_6936 # MOV operation
ref_6971 = ref_6953 # MOV operation
ref_6990 = ref_6971 # MOV operation
ref_7717 = ref_6990 # MOV operation
ref_7923 = ref_7717 # MOV operation
ref_8600 = ref_7923 # MOV operation
ref_8792 = ref_8600 # MOV operation
ref_8836 = ref_8792 # MOV operation
ref_8864 = ref_8836 # MOV operation
ref_8876 = ref_8864 # MOV operation
ref_8878 = ref_8876 # MOV operation

print ref_8878 & 0xffffffffffffffff
