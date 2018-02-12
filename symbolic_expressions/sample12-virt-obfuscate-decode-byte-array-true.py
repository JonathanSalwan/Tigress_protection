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
ref_9830 = ref_311 # MOV operation
ref_9919 = ref_9830 # MOV operation
ref_10023 = (ref_9919 & 0xFFFFFFFF) # MOV operation
ref_10723 = (ref_10023 & 0xFFFFFFFF) # MOV operation
ref_10727 = (ref_10723 & 0xFFFFFFFF) # MOV operation
ref_10761 = (((ref_10727 & 0xFFFFFFFF) >> 24) & 0xFF) # Byte reference - MOV operation
ref_10762 = (((ref_10727 & 0xFFFFFFFF) >> 16) & 0xFF) # Byte reference - MOV operation
ref_10763 = (((ref_10727 & 0xFFFFFFFF) >> 8) & 0xFF) # Byte reference - MOV operation
ref_10764 = ((ref_10727 & 0xFFFFFFFF) & 0xFF) # Byte reference - MOV operation
ref_10815 = ref_10764 # MOVZX operation
ref_10817 = (ref_10815 & 0xFF) # MOVZX operation
ref_10823 = (ref_10817 & 0xFFFFFFFF) # MOV operation
ref_10849 = (ref_10823 & 0xFFFFFFFF) # MOV operation
ref_10859 = (ref_10849 & 0xFF) # MOVZX operation
ref_10861 = ((ref_10859 & 0xFFFFFFFF) ^ ((((0x81) << 8 | 0x1C) << 8 | 0x9D) << 8 | 0xC5)) # XOR operation
ref_10868 = (ref_10861 & 0xFFFFFFFF) # MOV operation
ref_10872 = (((sx(0x20, 0x1000193) * sx(0x20, (ref_10868 & 0xFFFFFFFF))) & 0xFFFFFFFFFFFFFFFF) & 0xFFFFFFFF) # IMUL operation
ref_10917 = ref_10763 # MOVZX operation
ref_10919 = (ref_10917 & 0xFF) # MOVZX operation
ref_10921 = (ref_10872 & 0xFFFFFFFF) # MOV operation
ref_10923 = (ref_10921 & 0xFFFFFFFF) # MOV operation
ref_10925 = (ref_10919 & 0xFFFFFFFF) # MOV operation
ref_10951 = (ref_10925 & 0xFFFFFFFF) # MOV operation
ref_10961 = (ref_10951 & 0xFF) # MOVZX operation
ref_10963 = ((ref_10961 & 0xFFFFFFFF) ^ (ref_10923 & 0xFFFFFFFF)) # XOR operation
ref_10970 = (ref_10963 & 0xFFFFFFFF) # MOV operation
ref_10974 = (((sx(0x20, 0x1000193) * sx(0x20, (ref_10970 & 0xFFFFFFFF))) & 0xFFFFFFFFFFFFFFFF) & 0xFFFFFFFF) # IMUL operation
ref_11019 = ref_10762 # MOVZX operation
ref_11021 = (ref_11019 & 0xFF) # MOVZX operation
ref_11023 = (ref_10974 & 0xFFFFFFFF) # MOV operation
ref_11025 = (ref_11023 & 0xFFFFFFFF) # MOV operation
ref_11027 = (ref_11021 & 0xFFFFFFFF) # MOV operation
ref_11053 = (ref_11027 & 0xFFFFFFFF) # MOV operation
ref_11063 = (ref_11053 & 0xFF) # MOVZX operation
ref_11065 = ((ref_11063 & 0xFFFFFFFF) ^ (ref_11025 & 0xFFFFFFFF)) # XOR operation
ref_11072 = (ref_11065 & 0xFFFFFFFF) # MOV operation
ref_11076 = (((sx(0x20, 0x1000193) * sx(0x20, (ref_11072 & 0xFFFFFFFF))) & 0xFFFFFFFFFFFFFFFF) & 0xFFFFFFFF) # IMUL operation
ref_11093 = ref_10761 # MOVZX operation
ref_11095 = (ref_11093 & 0xFF) # MOVZX operation
ref_11097 = (ref_11076 & 0xFFFFFFFF) # MOV operation
ref_11099 = (ref_11097 & 0xFFFFFFFF) # MOV operation
ref_11101 = (ref_11095 & 0xFFFFFFFF) # MOV operation
ref_11127 = (ref_11101 & 0xFFFFFFFF) # MOV operation
ref_11137 = (ref_11127 & 0xFF) # MOVZX operation
ref_11139 = ((ref_11137 & 0xFFFFFFFF) ^ (ref_11099 & 0xFFFFFFFF)) # XOR operation
ref_11146 = (ref_11139 & 0xFFFFFFFF) # MOV operation
ref_11150 = (((sx(0x20, 0x1000193) * sx(0x20, (ref_11146 & 0xFFFFFFFF))) & 0xFFFFFFFFFFFFFFFF) & 0xFFFFFFFF) # IMUL operation
ref_11165 = (ref_11150 & 0xFFFFFFFF) # MOV operation
ref_11502 = (ref_11165 & 0xFFFFFFFF) # MOV operation
ref_11606 = (ref_11502 & 0xFFFFFFFF) # MOV operation
ref_11928 = (ref_11606 & 0xFFFFFFFF) # MOV operation
ref_12011 = (ref_11928 & 0xFFFFFFFF) # MOV operation
ref_12045 = (ref_12011 & 0xFFFFFFFF) # MOV operation
ref_12057 = ref_12045 # MOV operation
ref_12059 = ref_12057 # MOV operation

print ref_12059 & 0xffffffffffffffff
