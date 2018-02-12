#!/usr/bin/env python2
## -*- coding: utf-8 -*-

import sys

def sx(bits, value):
    sign_bit = 1 << (bits - 1)
    return (value & (sign_bit - 1)) - (value & sign_bit)

SymVar_0 = int(sys.argv[1])
ref_640 = SymVar_0
ref_651 = ref_640 # MOV operation
ref_663 = ref_651 # MOV operation
ref_665 = ref_663 # MOV operation
ref_9731 = ref_665 # MOV operation
ref_9743 = ref_9731 # MOV operation
ref_9771 = ref_9743 # MOV operation
ref_9784 = ref_9771 # MOV operation
ref_9797 = ref_9784 # MOV operation
ref_9799 = ref_9797 # MOV operation
ref_9849 = (((sx(0x40, 0xC2B2AE3D27D4EB4F) * sx(0x40, ref_9799)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_9883 = rol(0x1F, ((((((((((0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) + ref_9849) & 0xFFFFFFFFFFFFFFFF)) # MOV operation
ref_9885 = (((sx(0x40, 0x9E3779B185EBCA87) * sx(0x40, ref_9883)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_9899 = ref_9885 # MOV operation
ref_9916 = ref_9899 # MOV operation
ref_9928 = ref_9916 # MOV operation
ref_9945 = (((((((((0x27) << 8 | 0xD4) << 8 | 0xEB) << 8 | 0x2F) << 8 | 0x16) << 8 | 0x56) << 8 | 0x67) << 8 | 0xCD) ^ ref_9928) # MOV operation
ref_9947 = rol(0x1B, ref_9945) # ROL operation
ref_9951 = ref_9947 # MOV operation
ref_9955 = (((sx(0x40, ref_9951) * sx(0x40, 0x9E3779B185EBCA87)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_9961 = ((0x85EBCA77C2B2AE63 + ref_9955) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_10054 = ref_9961 # MOV operation
ref_10056 = (ref_10054 >> (0x21 & 0x3F)) # SHR operation
ref_10080 = (ref_9961 ^ ref_10056) # MOV operation
ref_10082 = (((sx(0x40, 0xC2B2AE3D27D4EB4F) * sx(0x40, ref_10080)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_10096 = ref_10082 # MOV operation
ref_10098 = (ref_10096 >> (0x1D & 0x3F)) # SHR operation
ref_10122 = (ref_10082 ^ ref_10098) # MOV operation
ref_10124 = (((sx(0x40, 0x165667B19E3779F9) * sx(0x40, ref_10122)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_10138 = ref_10124 # MOV operation
ref_10140 = (ref_10138 >> (0x20 & 0x3F)) # SHR operation
ref_10162 = (ref_10124 ^ ref_10140) # MOV operation
ref_10174 = ref_10162 # MOV operation
ref_10456 = ref_10174 # MOV operation
ref_10514 = ref_10456 # MOV operation
ref_10788 = ref_10514 # MOV operation
ref_10846 = ref_10788 # MOV operation
ref_11120 = ref_10846 # MOV operation
ref_11168 = ref_11120 # MOV operation
ref_11226 = ref_11168 # MOV operation
ref_11456 = ref_11226 # MOV operation
ref_11502 = ref_11456 # MOV operation
ref_11540 = ref_11502 # MOV operation
ref_11552 = ref_11540 # MOV operation
ref_11554 = ref_11552 # MOV operation

print ref_11554 & 0xffffffffffffffff
