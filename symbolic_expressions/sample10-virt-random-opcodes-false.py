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
ref_6703 = ref_665 # MOV operation
ref_6715 = ref_6703 # MOV operation
ref_6743 = ref_6715 # MOV operation
ref_6756 = ref_6743 # MOV operation
ref_6769 = ref_6756 # MOV operation
ref_6771 = ref_6769 # MOV operation
ref_6821 = (((sx(0x40, 0xC2B2AE3D27D4EB4F) * sx(0x40, ref_6771)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_6855 = rol(0x1F, ((((((((((0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) + ref_6821) & 0xFFFFFFFFFFFFFFFF)) # MOV operation
ref_6857 = (((sx(0x40, 0x9E3779B185EBCA87) * sx(0x40, ref_6855)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_6871 = ref_6857 # MOV operation
ref_6888 = ref_6871 # MOV operation
ref_6900 = ref_6888 # MOV operation
ref_6917 = (((((((((0x27) << 8 | 0xD4) << 8 | 0xEB) << 8 | 0x2F) << 8 | 0x16) << 8 | 0x56) << 8 | 0x67) << 8 | 0xCD) ^ ref_6900) # MOV operation
ref_6919 = rol(0x1B, ref_6917) # ROL operation
ref_6923 = ref_6919 # MOV operation
ref_6927 = (((sx(0x40, ref_6923) * sx(0x40, 0x9E3779B185EBCA87)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_6933 = ((0x85EBCA77C2B2AE63 + ref_6927) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_7026 = ref_6933 # MOV operation
ref_7028 = (ref_7026 >> (0x21 & 0x3F)) # SHR operation
ref_7052 = (ref_6933 ^ ref_7028) # MOV operation
ref_7054 = (((sx(0x40, 0xC2B2AE3D27D4EB4F) * sx(0x40, ref_7052)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_7068 = ref_7054 # MOV operation
ref_7070 = (ref_7068 >> (0x1D & 0x3F)) # SHR operation
ref_7094 = (ref_7054 ^ ref_7070) # MOV operation
ref_7096 = (((sx(0x40, 0x165667B19E3779F9) * sx(0x40, ref_7094)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_7110 = ref_7096 # MOV operation
ref_7112 = (ref_7110 >> (0x20 & 0x3F)) # SHR operation
ref_7134 = (ref_7096 ^ ref_7112) # MOV operation
ref_7146 = ref_7134 # MOV operation
ref_7506 = ref_7146 # MOV operation
ref_7590 = ref_7506 # MOV operation
ref_7942 = ref_7590 # MOV operation
ref_8026 = ref_7942 # MOV operation
ref_8250 = ref_8026 # MOV operation
ref_8324 = ref_8250 # MOV operation
ref_8536 = ref_8324 # MOV operation
ref_8844 = ref_8536 # MOV operation
ref_8916 = ref_8844 # MOV operation
ref_8954 = ref_8916 # MOV operation
ref_8966 = ref_8954 # MOV operation
ref_8968 = ref_8966 # MOV operation

print ref_8968 & 0xffffffffffffffff
