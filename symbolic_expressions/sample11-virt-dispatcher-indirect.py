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
ref_8509 = ref_290 # MOVZX operation
ref_8511 = (ref_8509 & 0xFF) # MOVZX operation
ref_8513 = (((ref_8511 & 0xFFFFFFFF) << (0x8 & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_8520 = (ref_8513 & 0xFFFFFFFF) # MOV operation
ref_8524 = ref_291 # MOVZX operation
ref_8526 = (ref_8524 & 0xFF) # MOVZX operation
ref_8528 = (((ref_8526 & 0xFFFFFFFF) + (ref_8520 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_8566 = ref_288 # MOVZX operation
ref_8568 = (ref_8566 & 0xFF) # MOVZX operation
ref_8570 = (((ref_8568 & 0xFFFFFFFF) << (0x8 & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_8577 = (ref_8570 & 0xFFFFFFFF) # MOV operation
ref_8589 = ref_289 # MOVZX operation
ref_8591 = (ref_8589 & 0xFF) # MOVZX operation
ref_8593 = (((ref_8591 & 0xFFFFFFFF) + (ref_8577 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_8601 = (((ref_8593 & 0xFFFFFFFF) << (0xB & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_8608 = ((ref_8601 & 0xFFFFFFFF) ^ ((((((0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x8) + (ref_8528 & 0xFFFFFFFF)) & 0xFFFFFFFF)) # XOR operation
ref_8621 = ((((((0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x8) + (ref_8528 & 0xFFFFFFFF)) & 0xFFFFFFFF) # MOV operation
ref_8623 = (((ref_8621 & 0xFFFFFFFF) << (0x10 & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_8630 = ((ref_8623 & 0xFFFFFFFF) ^ (ref_8608 & 0xFFFFFFFF)) # XOR operation
ref_8659 = (ref_8630 & 0xFFFFFFFF) # MOV operation
ref_8661 = ((ref_8659 & 0xFFFFFFFF) >> (0xB & 0x1F)) # SHR operation
ref_8711 = ref_286 # MOVZX operation
ref_8713 = (ref_8711 & 0xFF) # MOVZX operation
ref_8715 = (((ref_8713 & 0xFFFFFFFF) << (0x8 & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_8722 = (ref_8715 & 0xFFFFFFFF) # MOV operation
ref_8726 = ref_287 # MOVZX operation
ref_8728 = (ref_8726 & 0xFF) # MOVZX operation
ref_8730 = (((ref_8728 & 0xFFFFFFFF) + (ref_8722 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_8768 = ref_284 # MOVZX operation
ref_8770 = (ref_8768 & 0xFF) # MOVZX operation
ref_8772 = (((ref_8770 & 0xFFFFFFFF) << (0x8 & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_8779 = (ref_8772 & 0xFFFFFFFF) # MOV operation
ref_8791 = ref_285 # MOVZX operation
ref_8793 = (ref_8791 & 0xFF) # MOVZX operation
ref_8795 = (((ref_8793 & 0xFFFFFFFF) + (ref_8779 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_8803 = (((ref_8795 & 0xFFFFFFFF) << (0xB & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_8810 = ((ref_8803 & 0xFFFFFFFF) ^ (((((ref_8630 & 0xFFFFFFFF) + (ref_8661 & 0xFFFFFFFF)) & 0xFFFFFFFF) + (ref_8730 & 0xFFFFFFFF)) & 0xFFFFFFFF)) # XOR operation
ref_8823 = (((((ref_8630 & 0xFFFFFFFF) + (ref_8661 & 0xFFFFFFFF)) & 0xFFFFFFFF) + (ref_8730 & 0xFFFFFFFF)) & 0xFFFFFFFF) # MOV operation
ref_8825 = (((ref_8823 & 0xFFFFFFFF) << (0x10 & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_8832 = ((ref_8825 & 0xFFFFFFFF) ^ (ref_8810 & 0xFFFFFFFF)) # XOR operation
ref_8861 = (ref_8832 & 0xFFFFFFFF) # MOV operation
ref_8863 = ((ref_8861 & 0xFFFFFFFF) >> (0xB & 0x1F)) # SHR operation
ref_8933 = (((ref_8832 & 0xFFFFFFFF) + (ref_8863 & 0xFFFFFFFF)) & 0xFFFFFFFF) # MOV operation
ref_8935 = (((ref_8933 & 0xFFFFFFFF) << (0x3 & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_8953 = ((((ref_8832 & 0xFFFFFFFF) + (ref_8863 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_8935 & 0xFFFFFFFF)) # MOV operation
ref_8955 = ((ref_8953 & 0xFFFFFFFF) >> (0x5 & 0x1F)) # SHR operation
ref_8974 = ((((((ref_8832 & 0xFFFFFFFF) + (ref_8863 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_8935 & 0xFFFFFFFF)) + (ref_8955 & 0xFFFFFFFF)) & 0xFFFFFFFF) # MOV operation
ref_8976 = (((ref_8974 & 0xFFFFFFFF) << (0x4 & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_8994 = (((((((ref_8832 & 0xFFFFFFFF) + (ref_8863 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_8935 & 0xFFFFFFFF)) + (ref_8955 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_8976 & 0xFFFFFFFF)) # MOV operation
ref_8996 = ((ref_8994 & 0xFFFFFFFF) >> (0x11 & 0x1F)) # SHR operation
ref_9015 = (((((((((ref_8832 & 0xFFFFFFFF) + (ref_8863 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_8935 & 0xFFFFFFFF)) + (ref_8955 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_8976 & 0xFFFFFFFF)) + (ref_8996 & 0xFFFFFFFF)) & 0xFFFFFFFF) # MOV operation
ref_9017 = (((ref_9015 & 0xFFFFFFFF) << (0x19 & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_9035 = ((((((((((ref_8832 & 0xFFFFFFFF) + (ref_8863 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_8935 & 0xFFFFFFFF)) + (ref_8955 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_8976 & 0xFFFFFFFF)) + (ref_8996 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_9017 & 0xFFFFFFFF)) # MOV operation
ref_9037 = ((ref_9035 & 0xFFFFFFFF) >> (0x6 & 0x1F)) # SHR operation
ref_9056 = ((((((((((((ref_8832 & 0xFFFFFFFF) + (ref_8863 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_8935 & 0xFFFFFFFF)) + (ref_8955 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_8976 & 0xFFFFFFFF)) + (ref_8996 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_9017 & 0xFFFFFFFF)) + (ref_9037 & 0xFFFFFFFF)) & 0xFFFFFFFF) # MOV operation
ref_9069 = (ref_9056 & 0xFFFFFFFF) # MOV operation
ref_9346 = (ref_9069 & 0xFFFFFFFF) # MOV operation
ref_9400 = (ref_9346 & 0xFFFFFFFF) # MOV operation
ref_9626 = (ref_9400 & 0xFFFFFFFF) # MOV operation
ref_9668 = (ref_9626 & 0xFFFFFFFF) # MOV operation
ref_9702 = (ref_9668 & 0xFFFFFFFF) # MOV operation
ref_9714 = ref_9702 # MOV operation
ref_9716 = ref_9714 # MOV operation

print ref_9716 & 0xffffffffffffffff
