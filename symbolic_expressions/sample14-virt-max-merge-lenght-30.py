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
ref_5459 = ((((ref_456) << 8 | ref_457) << 8 | ref_458) << 8 | ref_459) # MOV operation
ref_5467 = (ref_5459 & 0xFFFFFFFF) # MOV operation
ref_5491 = (ref_5467 & 0xFFFFFFFF) # MOV operation
ref_5505 = (ref_5491 & 0xFFFFFFFF) # MOV operation
ref_5642 = ((((ref_452) << 8 | ref_453) << 8 | ref_454) << 8 | ref_455) # MOV operation
ref_5650 = (ref_5642 & 0xFFFFFFFF) # MOV operation
ref_5674 = (ref_5650 & 0xFFFFFFFF) # MOV operation
ref_5688 = (ref_5674 & 0xFFFFFFFF) # MOV operation
ref_5690 = ref_5505 # MOV operation
ref_5692 = ((0x0 + ((0x0 + ((ref_5690 * 0x8) & 0xFFFFFFFFFFFFFFFF)) & 0xFFFFFFFFFFFFFFFF)) & 0xFFFFFFFFFFFFFFFF) # LEA operation
ref_5696 = ((0x8 + ref_5692) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_5704 = ref_5688 # MOV operation
ref_5706 = ref_5696 # MOV operation
ref_5760 = ref_5706 # MOV operation
ref_5772 = ref_5704 # MOV operation
ref_5784 = ref_5760 # MOV operation
ref_5786 = ref_5772 # MOV operation
ref_5788 = ref_5784 # MOV operation
ref_5790 = ref_5786 # MOV operation
ref_5816 = ref_5788 # MOV operation
ref_5818 = ref_5790 # MOV operation
ref_5820 = ref_5818 # MOV operation
ref_5854 = ref_5816 # MOV operation
ref_5856 = ref_5820 # MOV operation
ref_5858 = (ref_5856 ^ ref_5854) # XOR operation
ref_5865 = (((sx(0x40, ref_5858) * sx(0x40, ((((((((0x9D) << 8 | 0xDF) << 8 | 0xEA) << 8 | 0x8) << 8 | 0xEB) << 8 | 0x38) << 8 | 0x2D) << 8 | 0x69))) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_5879 = ref_5865 # MOV operation
ref_5881 = (ref_5879 >> (0x2F & 0x3F)) # SHR operation
ref_5903 = ref_5820 # MOV operation
ref_5905 = (ref_5903 ^ (ref_5865 ^ ref_5881)) # XOR operation
ref_5912 = (((sx(0x40, ref_5905) * sx(0x40, ((((((((0x9D) << 8 | 0xDF) << 8 | 0xEA) << 8 | 0x8) << 8 | 0xEB) << 8 | 0x38) << 8 | 0x2D) << 8 | 0x69))) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_5926 = ref_5912 # MOV operation
ref_5928 = (ref_5926 >> (0x2F & 0x3F)) # SHR operation
ref_5950 = (ref_5912 ^ ref_5928) # MOV operation
ref_5952 = (((sx(0x40, ref_5950) * sx(0x40, ((((((((0x9D) << 8 | 0xDF) << 8 | 0xEA) << 8 | 0x8) << 8 | 0xEB) << 8 | 0x38) << 8 | 0x2D) << 8 | 0x69))) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_5966 = ref_5952 # MOV operation
ref_5983 = ref_5966 # MOV operation
ref_6001 = ref_5983 # MOV operation
ref_6020 = ref_6001 # MOV operation
ref_6187 = ref_6020 # MOV operation
ref_6221 = ref_6187 # MOV operation
ref_6435 = ref_6221 # MOV operation
ref_6553 = ref_6435 # MOV operation
ref_6591 = ref_6553 # MOV operation
ref_6603 = ref_6591 # MOV operation
ref_6605 = ref_6603 # MOV operation

print ref_6605 & 0xffffffffffffffff
