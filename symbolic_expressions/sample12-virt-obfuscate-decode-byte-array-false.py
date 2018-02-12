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
ref_9818 = ref_311 # MOV operation
ref_9907 = ref_9818 # MOV operation
ref_10011 = (ref_9907 & 0xFFFFFFFF) # MOV operation
ref_10711 = (ref_10011 & 0xFFFFFFFF) # MOV operation
ref_10715 = (ref_10711 & 0xFFFFFFFF) # MOV operation
ref_10749 = (((ref_10715 & 0xFFFFFFFF) >> 24) & 0xFF) # Byte reference - MOV operation
ref_10750 = (((ref_10715 & 0xFFFFFFFF) >> 16) & 0xFF) # Byte reference - MOV operation
ref_10751 = (((ref_10715 & 0xFFFFFFFF) >> 8) & 0xFF) # Byte reference - MOV operation
ref_10752 = ((ref_10715 & 0xFFFFFFFF) & 0xFF) # Byte reference - MOV operation
ref_10803 = ref_10752 # MOVZX operation
ref_10805 = (ref_10803 & 0xFF) # MOVZX operation
ref_10811 = (ref_10805 & 0xFFFFFFFF) # MOV operation
ref_10837 = (ref_10811 & 0xFFFFFFFF) # MOV operation
ref_10847 = (ref_10837 & 0xFF) # MOVZX operation
ref_10849 = ((ref_10847 & 0xFFFFFFFF) ^ ((((0x81) << 8 | 0x1C) << 8 | 0x9D) << 8 | 0xC5)) # XOR operation
ref_10856 = (ref_10849 & 0xFFFFFFFF) # MOV operation
ref_10860 = (((sx(0x20, 0x1000193) * sx(0x20, (ref_10856 & 0xFFFFFFFF))) & 0xFFFFFFFFFFFFFFFF) & 0xFFFFFFFF) # IMUL operation
ref_10905 = ref_10751 # MOVZX operation
ref_10907 = (ref_10905 & 0xFF) # MOVZX operation
ref_10909 = (ref_10860 & 0xFFFFFFFF) # MOV operation
ref_10911 = (ref_10909 & 0xFFFFFFFF) # MOV operation
ref_10913 = (ref_10907 & 0xFFFFFFFF) # MOV operation
ref_10939 = (ref_10913 & 0xFFFFFFFF) # MOV operation
ref_10949 = (ref_10939 & 0xFF) # MOVZX operation
ref_10951 = ((ref_10949 & 0xFFFFFFFF) ^ (ref_10911 & 0xFFFFFFFF)) # XOR operation
ref_10958 = (ref_10951 & 0xFFFFFFFF) # MOV operation
ref_10962 = (((sx(0x20, 0x1000193) * sx(0x20, (ref_10958 & 0xFFFFFFFF))) & 0xFFFFFFFFFFFFFFFF) & 0xFFFFFFFF) # IMUL operation
ref_11007 = ref_10750 # MOVZX operation
ref_11009 = (ref_11007 & 0xFF) # MOVZX operation
ref_11011 = (ref_10962 & 0xFFFFFFFF) # MOV operation
ref_11013 = (ref_11011 & 0xFFFFFFFF) # MOV operation
ref_11015 = (ref_11009 & 0xFFFFFFFF) # MOV operation
ref_11041 = (ref_11015 & 0xFFFFFFFF) # MOV operation
ref_11051 = (ref_11041 & 0xFF) # MOVZX operation
ref_11053 = ((ref_11051 & 0xFFFFFFFF) ^ (ref_11013 & 0xFFFFFFFF)) # XOR operation
ref_11060 = (ref_11053 & 0xFFFFFFFF) # MOV operation
ref_11064 = (((sx(0x20, 0x1000193) * sx(0x20, (ref_11060 & 0xFFFFFFFF))) & 0xFFFFFFFFFFFFFFFF) & 0xFFFFFFFF) # IMUL operation
ref_11081 = ref_10749 # MOVZX operation
ref_11083 = (ref_11081 & 0xFF) # MOVZX operation
ref_11085 = (ref_11064 & 0xFFFFFFFF) # MOV operation
ref_11087 = (ref_11085 & 0xFFFFFFFF) # MOV operation
ref_11089 = (ref_11083 & 0xFFFFFFFF) # MOV operation
ref_11115 = (ref_11089 & 0xFFFFFFFF) # MOV operation
ref_11125 = (ref_11115 & 0xFF) # MOVZX operation
ref_11127 = ((ref_11125 & 0xFFFFFFFF) ^ (ref_11087 & 0xFFFFFFFF)) # XOR operation
ref_11134 = (ref_11127 & 0xFFFFFFFF) # MOV operation
ref_11138 = (((sx(0x20, 0x1000193) * sx(0x20, (ref_11134 & 0xFFFFFFFF))) & 0xFFFFFFFFFFFFFFFF) & 0xFFFFFFFF) # IMUL operation
ref_11153 = (ref_11138 & 0xFFFFFFFF) # MOV operation
ref_11490 = (ref_11153 & 0xFFFFFFFF) # MOV operation
ref_11594 = (ref_11490 & 0xFFFFFFFF) # MOV operation
ref_11916 = (ref_11594 & 0xFFFFFFFF) # MOV operation
ref_11999 = (ref_11916 & 0xFFFFFFFF) # MOV operation
ref_12033 = (ref_11999 & 0xFFFFFFFF) # MOV operation
ref_12045 = ref_12033 # MOV operation
ref_12047 = ref_12045 # MOV operation

print ref_12047 & 0xffffffffffffffff
