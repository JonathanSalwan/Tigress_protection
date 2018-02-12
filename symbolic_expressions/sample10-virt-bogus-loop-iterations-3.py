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
ref_351055 = ref_665 # MOV operation
ref_351067 = ref_351055 # MOV operation
ref_351095 = ref_351067 # MOV operation
ref_351108 = ref_351095 # MOV operation
ref_351121 = ref_351108 # MOV operation
ref_351123 = ref_351121 # MOV operation
ref_351173 = (((sx(0x40, 0xC2B2AE3D27D4EB4F) * sx(0x40, ref_351123)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_351207 = rol(0x1F, ((((((((((0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) + ref_351173) & 0xFFFFFFFFFFFFFFFF)) # MOV operation
ref_351209 = (((sx(0x40, 0x9E3779B185EBCA87) * sx(0x40, ref_351207)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_351223 = ref_351209 # MOV operation
ref_351240 = ref_351223 # MOV operation
ref_351252 = ref_351240 # MOV operation
ref_351269 = (((((((((0x27) << 8 | 0xD4) << 8 | 0xEB) << 8 | 0x2F) << 8 | 0x16) << 8 | 0x56) << 8 | 0x67) << 8 | 0xCD) ^ ref_351252) # MOV operation
ref_351271 = rol(0x1B, ref_351269) # ROL operation
ref_351275 = ref_351271 # MOV operation
ref_351279 = (((sx(0x40, ref_351275) * sx(0x40, 0x9E3779B185EBCA87)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_351285 = ((0x85EBCA77C2B2AE63 + ref_351279) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_351378 = ref_351285 # MOV operation
ref_351380 = (ref_351378 >> (0x21 & 0x3F)) # SHR operation
ref_351404 = (ref_351285 ^ ref_351380) # MOV operation
ref_351406 = (((sx(0x40, 0xC2B2AE3D27D4EB4F) * sx(0x40, ref_351404)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_351420 = ref_351406 # MOV operation
ref_351422 = (ref_351420 >> (0x1D & 0x3F)) # SHR operation
ref_351446 = (ref_351406 ^ ref_351422) # MOV operation
ref_351448 = (((sx(0x40, 0x165667B19E3779F9) * sx(0x40, ref_351446)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_351462 = ref_351448 # MOV operation
ref_351464 = (ref_351462 >> (0x20 & 0x3F)) # SHR operation
ref_351486 = (ref_351448 ^ ref_351464) # MOV operation
ref_351498 = ref_351486 # MOV operation
ref_437958 = ref_351498 # MOV operation
ref_466718 = ref_437958 # MOV operation
ref_553170 = ref_466718 # MOV operation
ref_581930 = ref_553170 # MOV operation
ref_668382 = ref_581930 # MOV operation
ref_697159 = ref_668382 # MOV operation
ref_725955 = ref_697159 # MOV operation
ref_812318 = ref_725955 # MOV operation
ref_841084 = ref_812318 # MOV operation
ref_841122 = ref_841084 # MOV operation
ref_841134 = ref_841122 # MOV operation
ref_841136 = ref_841134 # MOV operation

print ref_841136 & 0xffffffffffffffff
