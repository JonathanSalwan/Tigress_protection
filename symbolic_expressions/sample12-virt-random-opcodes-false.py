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
ref_4863 = ref_311 # MOV operation
ref_4937 = ref_4863 # MOV operation
ref_5145 = (ref_4937 & 0xFFFFFFFF) # MOV operation
ref_5773 = (ref_5145 & 0xFFFFFFFF) # MOV operation
ref_5777 = (ref_5773 & 0xFFFFFFFF) # MOV operation
ref_5811 = (((ref_5777 & 0xFFFFFFFF) >> 24) & 0xFF) # Byte reference - MOV operation
ref_5812 = (((ref_5777 & 0xFFFFFFFF) >> 16) & 0xFF) # Byte reference - MOV operation
ref_5813 = (((ref_5777 & 0xFFFFFFFF) >> 8) & 0xFF) # Byte reference - MOV operation
ref_5814 = ((ref_5777 & 0xFFFFFFFF) & 0xFF) # Byte reference - MOV operation
ref_5865 = ref_5814 # MOVZX operation
ref_5867 = (ref_5865 & 0xFF) # MOVZX operation
ref_5873 = (ref_5867 & 0xFFFFFFFF) # MOV operation
ref_5899 = (ref_5873 & 0xFFFFFFFF) # MOV operation
ref_5909 = (ref_5899 & 0xFF) # MOVZX operation
ref_5911 = ((ref_5909 & 0xFFFFFFFF) ^ ((((0x81) << 8 | 0x1C) << 8 | 0x9D) << 8 | 0xC5)) # XOR operation
ref_5918 = (ref_5911 & 0xFFFFFFFF) # MOV operation
ref_5922 = (((sx(0x20, 0x1000193) * sx(0x20, (ref_5918 & 0xFFFFFFFF))) & 0xFFFFFFFFFFFFFFFF) & 0xFFFFFFFF) # IMUL operation
ref_5967 = ref_5813 # MOVZX operation
ref_5969 = (ref_5967 & 0xFF) # MOVZX operation
ref_5971 = (ref_5922 & 0xFFFFFFFF) # MOV operation
ref_5973 = (ref_5971 & 0xFFFFFFFF) # MOV operation
ref_5975 = (ref_5969 & 0xFFFFFFFF) # MOV operation
ref_6001 = (ref_5975 & 0xFFFFFFFF) # MOV operation
ref_6011 = (ref_6001 & 0xFF) # MOVZX operation
ref_6013 = ((ref_6011 & 0xFFFFFFFF) ^ (ref_5973 & 0xFFFFFFFF)) # XOR operation
ref_6020 = (ref_6013 & 0xFFFFFFFF) # MOV operation
ref_6024 = (((sx(0x20, 0x1000193) * sx(0x20, (ref_6020 & 0xFFFFFFFF))) & 0xFFFFFFFFFFFFFFFF) & 0xFFFFFFFF) # IMUL operation
ref_6069 = ref_5812 # MOVZX operation
ref_6071 = (ref_6069 & 0xFF) # MOVZX operation
ref_6073 = (ref_6024 & 0xFFFFFFFF) # MOV operation
ref_6075 = (ref_6073 & 0xFFFFFFFF) # MOV operation
ref_6077 = (ref_6071 & 0xFFFFFFFF) # MOV operation
ref_6103 = (ref_6077 & 0xFFFFFFFF) # MOV operation
ref_6113 = (ref_6103 & 0xFF) # MOVZX operation
ref_6115 = ((ref_6113 & 0xFFFFFFFF) ^ (ref_6075 & 0xFFFFFFFF)) # XOR operation
ref_6122 = (ref_6115 & 0xFFFFFFFF) # MOV operation
ref_6126 = (((sx(0x20, 0x1000193) * sx(0x20, (ref_6122 & 0xFFFFFFFF))) & 0xFFFFFFFFFFFFFFFF) & 0xFFFFFFFF) # IMUL operation
ref_6143 = ref_5811 # MOVZX operation
ref_6145 = (ref_6143 & 0xFF) # MOVZX operation
ref_6147 = (ref_6126 & 0xFFFFFFFF) # MOV operation
ref_6149 = (ref_6147 & 0xFFFFFFFF) # MOV operation
ref_6151 = (ref_6145 & 0xFFFFFFFF) # MOV operation
ref_6177 = (ref_6151 & 0xFFFFFFFF) # MOV operation
ref_6187 = (ref_6177 & 0xFF) # MOVZX operation
ref_6189 = ((ref_6187 & 0xFFFFFFFF) ^ (ref_6149 & 0xFFFFFFFF)) # XOR operation
ref_6196 = (ref_6189 & 0xFFFFFFFF) # MOV operation
ref_6200 = (((sx(0x20, 0x1000193) * sx(0x20, (ref_6196 & 0xFFFFFFFF))) & 0xFFFFFFFFFFFFFFFF) & 0xFFFFFFFF) # IMUL operation
ref_6215 = (ref_6200 & 0xFFFFFFFF) # MOV operation
ref_6442 = (ref_6215 & 0xFFFFFFFF) # MOV operation
ref_6650 = (ref_6442 & 0xFFFFFFFF) # MOV operation
ref_6954 = (ref_6650 & 0xFFFFFFFF) # MOV operation
ref_7022 = (ref_6954 & 0xFFFFFFFF) # MOV operation
ref_7056 = (ref_7022 & 0xFFFFFFFF) # MOV operation
ref_7068 = ref_7056 # MOV operation
ref_7070 = ref_7068 # MOV operation

print ref_7070 & 0xffffffffffffffff
