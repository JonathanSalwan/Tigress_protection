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
ref_6128 = ref_311 # MOV operation
ref_6482 = ref_6128 # MOV operation
ref_6842 = (ref_6482 & 0xFFFFFFFF) # MOV operation
ref_9640 = (ref_6842 & 0xFFFFFFFF) # MOV operation
ref_9644 = (ref_9640 & 0xFFFFFFFF) # MOV operation
ref_9678 = (((ref_9644 & 0xFFFFFFFF) >> 24) & 0xFF) # Byte reference - MOV operation
ref_9679 = (((ref_9644 & 0xFFFFFFFF) >> 16) & 0xFF) # Byte reference - MOV operation
ref_9680 = (((ref_9644 & 0xFFFFFFFF) >> 8) & 0xFF) # Byte reference - MOV operation
ref_9681 = ((ref_9644 & 0xFFFFFFFF) & 0xFF) # Byte reference - MOV operation
ref_9732 = ref_9681 # MOVZX operation
ref_9734 = (ref_9732 & 0xFF) # MOVZX operation
ref_9740 = (ref_9734 & 0xFFFFFFFF) # MOV operation
ref_9766 = (ref_9740 & 0xFFFFFFFF) # MOV operation
ref_9776 = (ref_9766 & 0xFF) # MOVZX operation
ref_9778 = ((ref_9776 & 0xFFFFFFFF) ^ ((((0x81) << 8 | 0x1C) << 8 | 0x9D) << 8 | 0xC5)) # XOR operation
ref_9785 = (ref_9778 & 0xFFFFFFFF) # MOV operation
ref_9789 = (((sx(0x20, 0x1000193) * sx(0x20, (ref_9785 & 0xFFFFFFFF))) & 0xFFFFFFFFFFFFFFFF) & 0xFFFFFFFF) # IMUL operation
ref_9834 = ref_9680 # MOVZX operation
ref_9836 = (ref_9834 & 0xFF) # MOVZX operation
ref_9838 = (ref_9789 & 0xFFFFFFFF) # MOV operation
ref_9840 = (ref_9838 & 0xFFFFFFFF) # MOV operation
ref_9842 = (ref_9836 & 0xFFFFFFFF) # MOV operation
ref_9868 = (ref_9842 & 0xFFFFFFFF) # MOV operation
ref_9878 = (ref_9868 & 0xFF) # MOVZX operation
ref_9880 = ((ref_9878 & 0xFFFFFFFF) ^ (ref_9840 & 0xFFFFFFFF)) # XOR operation
ref_9887 = (ref_9880 & 0xFFFFFFFF) # MOV operation
ref_9891 = (((sx(0x20, 0x1000193) * sx(0x20, (ref_9887 & 0xFFFFFFFF))) & 0xFFFFFFFFFFFFFFFF) & 0xFFFFFFFF) # IMUL operation
ref_9936 = ref_9679 # MOVZX operation
ref_9938 = (ref_9936 & 0xFF) # MOVZX operation
ref_9940 = (ref_9891 & 0xFFFFFFFF) # MOV operation
ref_9942 = (ref_9940 & 0xFFFFFFFF) # MOV operation
ref_9944 = (ref_9938 & 0xFFFFFFFF) # MOV operation
ref_9970 = (ref_9944 & 0xFFFFFFFF) # MOV operation
ref_9980 = (ref_9970 & 0xFF) # MOVZX operation
ref_9982 = ((ref_9980 & 0xFFFFFFFF) ^ (ref_9942 & 0xFFFFFFFF)) # XOR operation
ref_9989 = (ref_9982 & 0xFFFFFFFF) # MOV operation
ref_9993 = (((sx(0x20, 0x1000193) * sx(0x20, (ref_9989 & 0xFFFFFFFF))) & 0xFFFFFFFFFFFFFFFF) & 0xFFFFFFFF) # IMUL operation
ref_10010 = ref_9678 # MOVZX operation
ref_10012 = (ref_10010 & 0xFF) # MOVZX operation
ref_10014 = (ref_9993 & 0xFFFFFFFF) # MOV operation
ref_10016 = (ref_10014 & 0xFFFFFFFF) # MOV operation
ref_10018 = (ref_10012 & 0xFFFFFFFF) # MOV operation
ref_10044 = (ref_10018 & 0xFFFFFFFF) # MOV operation
ref_10054 = (ref_10044 & 0xFF) # MOVZX operation
ref_10056 = ((ref_10054 & 0xFFFFFFFF) ^ (ref_10016 & 0xFFFFFFFF)) # XOR operation
ref_10063 = (ref_10056 & 0xFFFFFFFF) # MOV operation
ref_10067 = (((sx(0x20, 0x1000193) * sx(0x20, (ref_10063 & 0xFFFFFFFF))) & 0xFFFFFFFFFFFFFFFF) & 0xFFFFFFFF) # IMUL operation
ref_10082 = (ref_10067 & 0xFFFFFFFF) # MOV operation
ref_11542 = (ref_10082 & 0xFFFFFFFF) # MOV operation
ref_11902 = (ref_11542 & 0xFFFFFFFF) # MOV operation
ref_13311 = (ref_11902 & 0xFFFFFFFF) # MOV operation
ref_13884 = (ref_13311 & 0xFFFFFFFF) # MOV operation
ref_13918 = (ref_13884 & 0xFFFFFFFF) # MOV operation
ref_13930 = ref_13918 # MOV operation
ref_13932 = ref_13930 # MOV operation

print ref_13932 & 0xffffffffffffffff
