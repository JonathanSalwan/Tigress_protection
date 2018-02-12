#!/usr/bin/env python2
## -*- coding: utf-8 -*-

import sys

def sx(bits, value):
    sign_bit = 1 << (bits - 1)
    return (value & (sign_bit - 1)) - (value & sign_bit)

SymVar_0 = int(sys.argv[1])
ref_382 = SymVar_0
ref_393 = ref_382 # MOV operation
ref_405 = ref_393 # MOV operation
ref_407 = ref_405 # MOV operation
ref_452 = ((ref_407 >> 56) & 0xFF) # Byte reference - MOV operation
ref_453 = ((ref_407 >> 48) & 0xFF) # Byte reference - MOV operation
ref_454 = ((ref_407 >> 40) & 0xFF) # Byte reference - MOV operation
ref_455 = ((ref_407 >> 32) & 0xFF) # Byte reference - MOV operation
ref_456 = ((ref_407 >> 24) & 0xFF) # Byte reference - MOV operation
ref_457 = ((ref_407 >> 16) & 0xFF) # Byte reference - MOV operation
ref_458 = ((ref_407 >> 8) & 0xFF) # Byte reference - MOV operation
ref_459 = (ref_407 & 0xFF) # Byte reference - MOV operation
ref_5559 = ((((ref_456) << 8 | ref_457) << 8 | ref_458) << 8 | ref_459) # MOV operation
ref_5567 = (ref_5559 & 0xFFFFFFFF) # MOV operation
ref_5591 = (ref_5567 & 0xFFFFFFFF) # MOV operation
ref_5605 = (ref_5591 & 0xFFFFFFFF) # MOV operation
ref_5742 = ((((ref_452) << 8 | ref_453) << 8 | ref_454) << 8 | ref_455) # MOV operation
ref_5750 = (ref_5742 & 0xFFFFFFFF) # MOV operation
ref_5774 = (ref_5750 & 0xFFFFFFFF) # MOV operation
ref_5788 = (ref_5774 & 0xFFFFFFFF) # MOV operation
ref_5790 = ref_5605 # MOV operation
ref_5792 = ((0x0 + ((0x0 + ((ref_5790 * 0x8) & 0xFFFFFFFFFFFFFFFF)) & 0xFFFFFFFFFFFFFFFF)) & 0xFFFFFFFFFFFFFFFF) # LEA operation
ref_5796 = ((0x8 + ref_5792) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_5804 = ref_5788 # MOV operation
ref_5806 = ref_5796 # MOV operation
ref_5860 = ref_5806 # MOV operation
ref_5872 = ref_5804 # MOV operation
ref_5884 = ref_5860 # MOV operation
ref_5886 = ref_5872 # MOV operation
ref_5888 = ref_5884 # MOV operation
ref_5890 = ref_5886 # MOV operation
ref_5916 = ref_5888 # MOV operation
ref_5918 = ref_5890 # MOV operation
ref_5920 = ref_5918 # MOV operation
ref_5954 = ref_5916 # MOV operation
ref_5956 = ref_5920 # MOV operation
ref_5958 = (ref_5956 ^ ref_5954) # XOR operation
ref_5965 = (((sx(0x40, ref_5958) * sx(0x40, ((((((((0x9D) << 8 | 0xDF) << 8 | 0xEA) << 8 | 0x8) << 8 | 0xEB) << 8 | 0x38) << 8 | 0x2D) << 8 | 0x69))) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_5979 = ref_5965 # MOV operation
ref_5981 = (ref_5979 >> (0x2F & 0x3F)) # SHR operation
ref_6003 = ref_5920 # MOV operation
ref_6005 = (ref_6003 ^ (ref_5965 ^ ref_5981)) # XOR operation
ref_6012 = (((sx(0x40, ref_6005) * sx(0x40, ((((((((0x9D) << 8 | 0xDF) << 8 | 0xEA) << 8 | 0x8) << 8 | 0xEB) << 8 | 0x38) << 8 | 0x2D) << 8 | 0x69))) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_6026 = ref_6012 # MOV operation
ref_6028 = (ref_6026 >> (0x2F & 0x3F)) # SHR operation
ref_6050 = (ref_6012 ^ ref_6028) # MOV operation
ref_6052 = (((sx(0x40, ref_6050) * sx(0x40, ((((((((0x9D) << 8 | 0xDF) << 8 | 0xEA) << 8 | 0x8) << 8 | 0xEB) << 8 | 0x38) << 8 | 0x2D) << 8 | 0x69))) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_6066 = ref_6052 # MOV operation
ref_6083 = ref_6066 # MOV operation
ref_6101 = ref_6083 # MOV operation
ref_6120 = ref_6101 # MOV operation
ref_6352 = ref_6120 # MOV operation
ref_6564 = ref_6352 # MOV operation
ref_6872 = ref_6564 # MOV operation
ref_6944 = ref_6872 # MOV operation
ref_6982 = ref_6944 # MOV operation
ref_6994 = ref_6982 # MOV operation
ref_6996 = ref_6994 # MOV operation

print ref_6996 & 0xffffffffffffffff
