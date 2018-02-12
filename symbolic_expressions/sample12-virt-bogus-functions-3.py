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
ref_6255 = ref_311 # MOV operation
ref_6961 = ref_6255 # MOV operation
ref_7460 = (ref_6961 & 0xFFFFFFFF) # MOV operation
ref_11341 = (ref_7460 & 0xFFFFFFFF) # MOV operation
ref_11345 = (ref_11341 & 0xFFFFFFFF) # MOV operation
ref_11379 = (((ref_11345 & 0xFFFFFFFF) >> 24) & 0xFF) # Byte reference - MOV operation
ref_11380 = (((ref_11345 & 0xFFFFFFFF) >> 16) & 0xFF) # Byte reference - MOV operation
ref_11381 = (((ref_11345 & 0xFFFFFFFF) >> 8) & 0xFF) # Byte reference - MOV operation
ref_11382 = ((ref_11345 & 0xFFFFFFFF) & 0xFF) # Byte reference - MOV operation
ref_11433 = ref_11382 # MOVZX operation
ref_11435 = (ref_11433 & 0xFF) # MOVZX operation
ref_11441 = (ref_11435 & 0xFFFFFFFF) # MOV operation
ref_11467 = (ref_11441 & 0xFFFFFFFF) # MOV operation
ref_11477 = (ref_11467 & 0xFF) # MOVZX operation
ref_11479 = ((ref_11477 & 0xFFFFFFFF) ^ ((((0x81) << 8 | 0x1C) << 8 | 0x9D) << 8 | 0xC5)) # XOR operation
ref_11486 = (ref_11479 & 0xFFFFFFFF) # MOV operation
ref_11490 = (((sx(0x20, 0x1000193) * sx(0x20, (ref_11486 & 0xFFFFFFFF))) & 0xFFFFFFFFFFFFFFFF) & 0xFFFFFFFF) # IMUL operation
ref_11535 = ref_11381 # MOVZX operation
ref_11537 = (ref_11535 & 0xFF) # MOVZX operation
ref_11539 = (ref_11490 & 0xFFFFFFFF) # MOV operation
ref_11541 = (ref_11539 & 0xFFFFFFFF) # MOV operation
ref_11543 = (ref_11537 & 0xFFFFFFFF) # MOV operation
ref_11569 = (ref_11543 & 0xFFFFFFFF) # MOV operation
ref_11579 = (ref_11569 & 0xFF) # MOVZX operation
ref_11581 = ((ref_11579 & 0xFFFFFFFF) ^ (ref_11541 & 0xFFFFFFFF)) # XOR operation
ref_11588 = (ref_11581 & 0xFFFFFFFF) # MOV operation
ref_11592 = (((sx(0x20, 0x1000193) * sx(0x20, (ref_11588 & 0xFFFFFFFF))) & 0xFFFFFFFFFFFFFFFF) & 0xFFFFFFFF) # IMUL operation
ref_11637 = ref_11380 # MOVZX operation
ref_11639 = (ref_11637 & 0xFF) # MOVZX operation
ref_11641 = (ref_11592 & 0xFFFFFFFF) # MOV operation
ref_11643 = (ref_11641 & 0xFFFFFFFF) # MOV operation
ref_11645 = (ref_11639 & 0xFFFFFFFF) # MOV operation
ref_11671 = (ref_11645 & 0xFFFFFFFF) # MOV operation
ref_11681 = (ref_11671 & 0xFF) # MOVZX operation
ref_11683 = ((ref_11681 & 0xFFFFFFFF) ^ (ref_11643 & 0xFFFFFFFF)) # XOR operation
ref_11690 = (ref_11683 & 0xFFFFFFFF) # MOV operation
ref_11694 = (((sx(0x20, 0x1000193) * sx(0x20, (ref_11690 & 0xFFFFFFFF))) & 0xFFFFFFFFFFFFFFFF) & 0xFFFFFFFF) # IMUL operation
ref_11711 = ref_11379 # MOVZX operation
ref_11713 = (ref_11711 & 0xFF) # MOVZX operation
ref_11715 = (ref_11694 & 0xFFFFFFFF) # MOV operation
ref_11717 = (ref_11715 & 0xFFFFFFFF) # MOV operation
ref_11719 = (ref_11713 & 0xFFFFFFFF) # MOV operation
ref_11745 = (ref_11719 & 0xFFFFFFFF) # MOV operation
ref_11755 = (ref_11745 & 0xFF) # MOVZX operation
ref_11757 = ((ref_11755 & 0xFFFFFFFF) ^ (ref_11717 & 0xFFFFFFFF)) # XOR operation
ref_11764 = (ref_11757 & 0xFFFFFFFF) # MOV operation
ref_11768 = (((sx(0x20, 0x1000193) * sx(0x20, (ref_11764 & 0xFFFFFFFF))) & 0xFFFFFFFFFFFFFFFF) & 0xFFFFFFFF) # IMUL operation
ref_11783 = (ref_11768 & 0xFFFFFFFF) # MOV operation
ref_13688 = (ref_11783 & 0xFFFFFFFF) # MOV operation
ref_14331 = (ref_13688 & 0xFFFFFFFF) # MOV operation
ref_16017 = (ref_14331 & 0xFFFFFFFF) # MOV operation
ref_16550 = (ref_16017 & 0xFFFFFFFF) # MOV operation
ref_16587 = (ref_16550 & 0xFFFFFFFF) # MOV operation
ref_16599 = ref_16587 # MOV operation
ref_16601 = ref_16599 # MOV operation

print ref_16601 & 0xffffffffffffffff
