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
ref_5271 = ref_311 # MOV operation
ref_5313 = ref_5271 # MOV operation
ref_5361 = (ref_5313 & 0xFFFFFFFF) # MOV operation
ref_5797 = (ref_5361 & 0xFFFFFFFF) # MOV operation
ref_5801 = (ref_5797 & 0xFFFFFFFF) # MOV operation
ref_5835 = (((ref_5801 & 0xFFFFFFFF) >> 24) & 0xFF) # Byte reference - MOV operation
ref_5836 = (((ref_5801 & 0xFFFFFFFF) >> 16) & 0xFF) # Byte reference - MOV operation
ref_5837 = (((ref_5801 & 0xFFFFFFFF) >> 8) & 0xFF) # Byte reference - MOV operation
ref_5838 = ((ref_5801 & 0xFFFFFFFF) & 0xFF) # Byte reference - MOV operation
ref_5889 = ref_5838 # MOVZX operation
ref_5891 = (ref_5889 & 0xFF) # MOVZX operation
ref_5897 = (ref_5891 & 0xFFFFFFFF) # MOV operation
ref_5923 = (ref_5897 & 0xFFFFFFFF) # MOV operation
ref_5933 = (ref_5923 & 0xFF) # MOVZX operation
ref_5935 = ((ref_5933 & 0xFFFFFFFF) ^ ((((0x81) << 8 | 0x1C) << 8 | 0x9D) << 8 | 0xC5)) # XOR operation
ref_5942 = (ref_5935 & 0xFFFFFFFF) # MOV operation
ref_5946 = (((sx(0x20, 0x1000193) * sx(0x20, (ref_5942 & 0xFFFFFFFF))) & 0xFFFFFFFFFFFFFFFF) & 0xFFFFFFFF) # IMUL operation
ref_5991 = ref_5837 # MOVZX operation
ref_5993 = (ref_5991 & 0xFF) # MOVZX operation
ref_5995 = (ref_5946 & 0xFFFFFFFF) # MOV operation
ref_5997 = (ref_5995 & 0xFFFFFFFF) # MOV operation
ref_5999 = (ref_5993 & 0xFFFFFFFF) # MOV operation
ref_6025 = (ref_5999 & 0xFFFFFFFF) # MOV operation
ref_6035 = (ref_6025 & 0xFF) # MOVZX operation
ref_6037 = ((ref_6035 & 0xFFFFFFFF) ^ (ref_5997 & 0xFFFFFFFF)) # XOR operation
ref_6044 = (ref_6037 & 0xFFFFFFFF) # MOV operation
ref_6048 = (((sx(0x20, 0x1000193) * sx(0x20, (ref_6044 & 0xFFFFFFFF))) & 0xFFFFFFFFFFFFFFFF) & 0xFFFFFFFF) # IMUL operation
ref_6093 = ref_5836 # MOVZX operation
ref_6095 = (ref_6093 & 0xFF) # MOVZX operation
ref_6097 = (ref_6048 & 0xFFFFFFFF) # MOV operation
ref_6099 = (ref_6097 & 0xFFFFFFFF) # MOV operation
ref_6101 = (ref_6095 & 0xFFFFFFFF) # MOV operation
ref_6127 = (ref_6101 & 0xFFFFFFFF) # MOV operation
ref_6137 = (ref_6127 & 0xFF) # MOVZX operation
ref_6139 = ((ref_6137 & 0xFFFFFFFF) ^ (ref_6099 & 0xFFFFFFFF)) # XOR operation
ref_6146 = (ref_6139 & 0xFFFFFFFF) # MOV operation
ref_6150 = (((sx(0x20, 0x1000193) * sx(0x20, (ref_6146 & 0xFFFFFFFF))) & 0xFFFFFFFFFFFFFFFF) & 0xFFFFFFFF) # IMUL operation
ref_6167 = ref_5835 # MOVZX operation
ref_6169 = (ref_6167 & 0xFF) # MOVZX operation
ref_6171 = (ref_6150 & 0xFFFFFFFF) # MOV operation
ref_6173 = (ref_6171 & 0xFFFFFFFF) # MOV operation
ref_6175 = (ref_6169 & 0xFFFFFFFF) # MOV operation
ref_6201 = (ref_6175 & 0xFFFFFFFF) # MOV operation
ref_6211 = (ref_6201 & 0xFF) # MOVZX operation
ref_6213 = ((ref_6211 & 0xFFFFFFFF) ^ (ref_6173 & 0xFFFFFFFF)) # XOR operation
ref_6220 = (ref_6213 & 0xFFFFFFFF) # MOV operation
ref_6224 = (((sx(0x20, 0x1000193) * sx(0x20, (ref_6220 & 0xFFFFFFFF))) & 0xFFFFFFFFFFFFFFFF) & 0xFFFFFFFF) # IMUL operation
ref_6239 = (ref_6224 & 0xFFFFFFFF) # MOV operation
ref_6498 = (ref_6239 & 0xFFFFFFFF) # MOV operation
ref_6546 = (ref_6498 & 0xFFFFFFFF) # MOV operation
ref_6761 = (ref_6546 & 0xFFFFFFFF) # MOV operation
ref_6797 = (ref_6761 & 0xFFFFFFFF) # MOV operation
ref_6831 = (ref_6797 & 0xFFFFFFFF) # MOV operation
ref_6843 = ref_6831 # MOV operation
ref_6845 = ref_6843 # MOV operation

print ref_6845 & 0xffffffffffffffff
