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
ref_121783 = ref_665 # MOV operation
ref_121795 = ref_121783 # MOV operation
ref_121823 = ref_121795 # MOV operation
ref_121836 = ref_121823 # MOV operation
ref_121849 = ref_121836 # MOV operation
ref_121851 = ref_121849 # MOV operation
ref_121901 = (((sx(0x40, 0xC2B2AE3D27D4EB4F) * sx(0x40, ref_121851)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_121935 = rol(0x1F, ((((((((((0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) + ref_121901) & 0xFFFFFFFFFFFFFFFF)) # MOV operation
ref_121937 = (((sx(0x40, 0x9E3779B185EBCA87) * sx(0x40, ref_121935)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_121951 = ref_121937 # MOV operation
ref_121968 = ref_121951 # MOV operation
ref_121980 = ref_121968 # MOV operation
ref_121997 = (((((((((0x27) << 8 | 0xD4) << 8 | 0xEB) << 8 | 0x2F) << 8 | 0x16) << 8 | 0x56) << 8 | 0x67) << 8 | 0xCD) ^ ref_121980) # MOV operation
ref_121999 = rol(0x1B, ref_121997) # ROL operation
ref_122003 = ref_121999 # MOV operation
ref_122007 = (((sx(0x40, ref_122003) * sx(0x40, 0x9E3779B185EBCA87)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_122013 = ((0x85EBCA77C2B2AE63 + ref_122007) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_122106 = ref_122013 # MOV operation
ref_122108 = (ref_122106 >> (0x21 & 0x3F)) # SHR operation
ref_122132 = (ref_122013 ^ ref_122108) # MOV operation
ref_122134 = (((sx(0x40, 0xC2B2AE3D27D4EB4F) * sx(0x40, ref_122132)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_122148 = ref_122134 # MOV operation
ref_122150 = (ref_122148 >> (0x1D & 0x3F)) # SHR operation
ref_122174 = (ref_122134 ^ ref_122150) # MOV operation
ref_122176 = (((sx(0x40, 0x165667B19E3779F9) * sx(0x40, ref_122174)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_122190 = ref_122176 # MOV operation
ref_122192 = (ref_122190 >> (0x20 & 0x3F)) # SHR operation
ref_122214 = (ref_122176 ^ ref_122192) # MOV operation
ref_122226 = ref_122214 # MOV operation
ref_151368 = ref_122226 # MOV operation
ref_161022 = ref_151368 # MOV operation
ref_190156 = ref_161022 # MOV operation
ref_199810 = ref_190156 # MOV operation
ref_228944 = ref_199810 # MOV operation
ref_238615 = ref_228944 # MOV operation
ref_248305 = ref_238615 # MOV operation
ref_277350 = ref_248305 # MOV operation
ref_287010 = ref_277350 # MOV operation
ref_287048 = ref_287010 # MOV operation
ref_287060 = ref_287048 # MOV operation
ref_287062 = ref_287060 # MOV operation

print ref_287062 & 0xffffffffffffffff
