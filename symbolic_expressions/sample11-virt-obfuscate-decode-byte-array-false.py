#!/usr/bin/env python2
## -*- coding: utf-8 -*-

import sys

def sx(bits, value):
    sign_bit = 1 << (bits - 1)
    return (value & (sign_bit - 1)) - (value & sign_bit)

SymVar_0 = int(sys.argv[1])
ref_214 = SymVar_0
ref_225 = ref_214 # MOV operation
ref_237 = ref_225 # MOV operation
ref_239 = ref_237 # MOV operation
ref_284 = ((ref_239 >> 56) & 0xFF) # Byte reference - MOV operation
ref_285 = ((ref_239 >> 48) & 0xFF) # Byte reference - MOV operation
ref_286 = ((ref_239 >> 40) & 0xFF) # Byte reference - MOV operation
ref_287 = ((ref_239 >> 32) & 0xFF) # Byte reference - MOV operation
ref_288 = ((ref_239 >> 24) & 0xFF) # Byte reference - MOV operation
ref_289 = ((ref_239 >> 16) & 0xFF) # Byte reference - MOV operation
ref_290 = ((ref_239 >> 8) & 0xFF) # Byte reference - MOV operation
ref_291 = (ref_239 & 0xFF) # Byte reference - MOV operation
ref_9531 = ref_290 # MOVZX operation
ref_9533 = (ref_9531 & 0xFF) # MOVZX operation
ref_9535 = (((ref_9533 & 0xFFFFFFFF) << (0x8 & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_9542 = (ref_9535 & 0xFFFFFFFF) # MOV operation
ref_9546 = ref_291 # MOVZX operation
ref_9548 = (ref_9546 & 0xFF) # MOVZX operation
ref_9550 = (((ref_9548 & 0xFFFFFFFF) + (ref_9542 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_9588 = ref_288 # MOVZX operation
ref_9590 = (ref_9588 & 0xFF) # MOVZX operation
ref_9592 = (((ref_9590 & 0xFFFFFFFF) << (0x8 & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_9599 = (ref_9592 & 0xFFFFFFFF) # MOV operation
ref_9611 = ref_289 # MOVZX operation
ref_9613 = (ref_9611 & 0xFF) # MOVZX operation
ref_9615 = (((ref_9613 & 0xFFFFFFFF) + (ref_9599 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_9623 = (((ref_9615 & 0xFFFFFFFF) << (0xB & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_9630 = ((ref_9623 & 0xFFFFFFFF) ^ ((((((0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x8) + (ref_9550 & 0xFFFFFFFF)) & 0xFFFFFFFF)) # XOR operation
ref_9643 = ((((((0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x8) + (ref_9550 & 0xFFFFFFFF)) & 0xFFFFFFFF) # MOV operation
ref_9645 = (((ref_9643 & 0xFFFFFFFF) << (0x10 & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_9652 = ((ref_9645 & 0xFFFFFFFF) ^ (ref_9630 & 0xFFFFFFFF)) # XOR operation
ref_9681 = (ref_9652 & 0xFFFFFFFF) # MOV operation
ref_9683 = ((ref_9681 & 0xFFFFFFFF) >> (0xB & 0x1F)) # SHR operation
ref_9733 = ref_286 # MOVZX operation
ref_9735 = (ref_9733 & 0xFF) # MOVZX operation
ref_9737 = (((ref_9735 & 0xFFFFFFFF) << (0x8 & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_9744 = (ref_9737 & 0xFFFFFFFF) # MOV operation
ref_9748 = ref_287 # MOVZX operation
ref_9750 = (ref_9748 & 0xFF) # MOVZX operation
ref_9752 = (((ref_9750 & 0xFFFFFFFF) + (ref_9744 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_9790 = ref_284 # MOVZX operation
ref_9792 = (ref_9790 & 0xFF) # MOVZX operation
ref_9794 = (((ref_9792 & 0xFFFFFFFF) << (0x8 & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_9801 = (ref_9794 & 0xFFFFFFFF) # MOV operation
ref_9813 = ref_285 # MOVZX operation
ref_9815 = (ref_9813 & 0xFF) # MOVZX operation
ref_9817 = (((ref_9815 & 0xFFFFFFFF) + (ref_9801 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_9825 = (((ref_9817 & 0xFFFFFFFF) << (0xB & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_9832 = ((ref_9825 & 0xFFFFFFFF) ^ (((((ref_9652 & 0xFFFFFFFF) + (ref_9683 & 0xFFFFFFFF)) & 0xFFFFFFFF) + (ref_9752 & 0xFFFFFFFF)) & 0xFFFFFFFF)) # XOR operation
ref_9845 = (((((ref_9652 & 0xFFFFFFFF) + (ref_9683 & 0xFFFFFFFF)) & 0xFFFFFFFF) + (ref_9752 & 0xFFFFFFFF)) & 0xFFFFFFFF) # MOV operation
ref_9847 = (((ref_9845 & 0xFFFFFFFF) << (0x10 & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_9854 = ((ref_9847 & 0xFFFFFFFF) ^ (ref_9832 & 0xFFFFFFFF)) # XOR operation
ref_9883 = (ref_9854 & 0xFFFFFFFF) # MOV operation
ref_9885 = ((ref_9883 & 0xFFFFFFFF) >> (0xB & 0x1F)) # SHR operation
ref_9955 = (((ref_9854 & 0xFFFFFFFF) + (ref_9885 & 0xFFFFFFFF)) & 0xFFFFFFFF) # MOV operation
ref_9957 = (((ref_9955 & 0xFFFFFFFF) << (0x3 & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_9975 = ((((ref_9854 & 0xFFFFFFFF) + (ref_9885 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_9957 & 0xFFFFFFFF)) # MOV operation
ref_9977 = ((ref_9975 & 0xFFFFFFFF) >> (0x5 & 0x1F)) # SHR operation
ref_9996 = ((((((ref_9854 & 0xFFFFFFFF) + (ref_9885 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_9957 & 0xFFFFFFFF)) + (ref_9977 & 0xFFFFFFFF)) & 0xFFFFFFFF) # MOV operation
ref_9998 = (((ref_9996 & 0xFFFFFFFF) << (0x4 & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_10016 = (((((((ref_9854 & 0xFFFFFFFF) + (ref_9885 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_9957 & 0xFFFFFFFF)) + (ref_9977 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_9998 & 0xFFFFFFFF)) # MOV operation
ref_10018 = ((ref_10016 & 0xFFFFFFFF) >> (0x11 & 0x1F)) # SHR operation
ref_10037 = (((((((((ref_9854 & 0xFFFFFFFF) + (ref_9885 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_9957 & 0xFFFFFFFF)) + (ref_9977 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_9998 & 0xFFFFFFFF)) + (ref_10018 & 0xFFFFFFFF)) & 0xFFFFFFFF) # MOV operation
ref_10039 = (((ref_10037 & 0xFFFFFFFF) << (0x19 & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_10057 = ((((((((((ref_9854 & 0xFFFFFFFF) + (ref_9885 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_9957 & 0xFFFFFFFF)) + (ref_9977 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_9998 & 0xFFFFFFFF)) + (ref_10018 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_10039 & 0xFFFFFFFF)) # MOV operation
ref_10059 = ((ref_10057 & 0xFFFFFFFF) >> (0x6 & 0x1F)) # SHR operation
ref_10078 = ((((((((((((ref_9854 & 0xFFFFFFFF) + (ref_9885 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_9957 & 0xFFFFFFFF)) + (ref_9977 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_9998 & 0xFFFFFFFF)) + (ref_10018 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_10039 & 0xFFFFFFFF)) + (ref_10059 & 0xFFFFFFFF)) & 0xFFFFFFFF) # MOV operation
ref_10091 = (ref_10078 & 0xFFFFFFFF) # MOV operation
ref_10428 = (ref_10091 & 0xFFFFFFFF) # MOV operation
ref_10523 = (ref_10428 & 0xFFFFFFFF) # MOV operation
ref_10845 = (ref_10523 & 0xFFFFFFFF) # MOV operation
ref_10928 = (ref_10845 & 0xFFFFFFFF) # MOV operation
ref_10962 = (ref_10928 & 0xFFFFFFFF) # MOV operation
ref_10974 = ref_10962 # MOV operation
ref_10976 = ref_10974 # MOV operation

print ref_10976 & 0xffffffffffffffff
