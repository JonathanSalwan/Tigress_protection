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
ref_5550 = ref_290 # MOVZX operation
ref_5552 = (ref_5550 & 0xFF) # MOVZX operation
ref_5554 = (((ref_5552 & 0xFFFFFFFF) << (0x8 & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_5561 = (ref_5554 & 0xFFFFFFFF) # MOV operation
ref_5565 = ref_291 # MOVZX operation
ref_5567 = (ref_5565 & 0xFF) # MOVZX operation
ref_5569 = (((ref_5567 & 0xFFFFFFFF) + (ref_5561 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_5607 = ref_288 # MOVZX operation
ref_5609 = (ref_5607 & 0xFF) # MOVZX operation
ref_5611 = (((ref_5609 & 0xFFFFFFFF) << (0x8 & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_5618 = (ref_5611 & 0xFFFFFFFF) # MOV operation
ref_5630 = ref_289 # MOVZX operation
ref_5632 = (ref_5630 & 0xFF) # MOVZX operation
ref_5634 = (((ref_5632 & 0xFFFFFFFF) + (ref_5618 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_5642 = (((ref_5634 & 0xFFFFFFFF) << (0xB & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_5649 = ((ref_5642 & 0xFFFFFFFF) ^ ((((((0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x8) + (ref_5569 & 0xFFFFFFFF)) & 0xFFFFFFFF)) # XOR operation
ref_5662 = ((((((0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x8) + (ref_5569 & 0xFFFFFFFF)) & 0xFFFFFFFF) # MOV operation
ref_5664 = (((ref_5662 & 0xFFFFFFFF) << (0x10 & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_5671 = ((ref_5664 & 0xFFFFFFFF) ^ (ref_5649 & 0xFFFFFFFF)) # XOR operation
ref_5700 = (ref_5671 & 0xFFFFFFFF) # MOV operation
ref_5702 = ((ref_5700 & 0xFFFFFFFF) >> (0xB & 0x1F)) # SHR operation
ref_5752 = ref_286 # MOVZX operation
ref_5754 = (ref_5752 & 0xFF) # MOVZX operation
ref_5756 = (((ref_5754 & 0xFFFFFFFF) << (0x8 & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_5763 = (ref_5756 & 0xFFFFFFFF) # MOV operation
ref_5767 = ref_287 # MOVZX operation
ref_5769 = (ref_5767 & 0xFF) # MOVZX operation
ref_5771 = (((ref_5769 & 0xFFFFFFFF) + (ref_5763 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_5809 = ref_284 # MOVZX operation
ref_5811 = (ref_5809 & 0xFF) # MOVZX operation
ref_5813 = (((ref_5811 & 0xFFFFFFFF) << (0x8 & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_5820 = (ref_5813 & 0xFFFFFFFF) # MOV operation
ref_5832 = ref_285 # MOVZX operation
ref_5834 = (ref_5832 & 0xFF) # MOVZX operation
ref_5836 = (((ref_5834 & 0xFFFFFFFF) + (ref_5820 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_5844 = (((ref_5836 & 0xFFFFFFFF) << (0xB & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_5851 = ((ref_5844 & 0xFFFFFFFF) ^ (((((ref_5671 & 0xFFFFFFFF) + (ref_5702 & 0xFFFFFFFF)) & 0xFFFFFFFF) + (ref_5771 & 0xFFFFFFFF)) & 0xFFFFFFFF)) # XOR operation
ref_5864 = (((((ref_5671 & 0xFFFFFFFF) + (ref_5702 & 0xFFFFFFFF)) & 0xFFFFFFFF) + (ref_5771 & 0xFFFFFFFF)) & 0xFFFFFFFF) # MOV operation
ref_5866 = (((ref_5864 & 0xFFFFFFFF) << (0x10 & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_5873 = ((ref_5866 & 0xFFFFFFFF) ^ (ref_5851 & 0xFFFFFFFF)) # XOR operation
ref_5902 = (ref_5873 & 0xFFFFFFFF) # MOV operation
ref_5904 = ((ref_5902 & 0xFFFFFFFF) >> (0xB & 0x1F)) # SHR operation
ref_5974 = (((ref_5873 & 0xFFFFFFFF) + (ref_5904 & 0xFFFFFFFF)) & 0xFFFFFFFF) # MOV operation
ref_5976 = (((ref_5974 & 0xFFFFFFFF) << (0x3 & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_5994 = ((((ref_5873 & 0xFFFFFFFF) + (ref_5904 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_5976 & 0xFFFFFFFF)) # MOV operation
ref_5996 = ((ref_5994 & 0xFFFFFFFF) >> (0x5 & 0x1F)) # SHR operation
ref_6015 = ((((((ref_5873 & 0xFFFFFFFF) + (ref_5904 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_5976 & 0xFFFFFFFF)) + (ref_5996 & 0xFFFFFFFF)) & 0xFFFFFFFF) # MOV operation
ref_6017 = (((ref_6015 & 0xFFFFFFFF) << (0x4 & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_6035 = (((((((ref_5873 & 0xFFFFFFFF) + (ref_5904 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_5976 & 0xFFFFFFFF)) + (ref_5996 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_6017 & 0xFFFFFFFF)) # MOV operation
ref_6037 = ((ref_6035 & 0xFFFFFFFF) >> (0x11 & 0x1F)) # SHR operation
ref_6056 = (((((((((ref_5873 & 0xFFFFFFFF) + (ref_5904 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_5976 & 0xFFFFFFFF)) + (ref_5996 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_6017 & 0xFFFFFFFF)) + (ref_6037 & 0xFFFFFFFF)) & 0xFFFFFFFF) # MOV operation
ref_6058 = (((ref_6056 & 0xFFFFFFFF) << (0x19 & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_6076 = ((((((((((ref_5873 & 0xFFFFFFFF) + (ref_5904 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_5976 & 0xFFFFFFFF)) + (ref_5996 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_6017 & 0xFFFFFFFF)) + (ref_6037 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_6058 & 0xFFFFFFFF)) # MOV operation
ref_6078 = ((ref_6076 & 0xFFFFFFFF) >> (0x6 & 0x1F)) # SHR operation
ref_6097 = ((((((((((((ref_5873 & 0xFFFFFFFF) + (ref_5904 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_5976 & 0xFFFFFFFF)) + (ref_5996 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_6017 & 0xFFFFFFFF)) + (ref_6037 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_6058 & 0xFFFFFFFF)) + (ref_6078 & 0xFFFFFFFF)) & 0xFFFFFFFF) # MOV operation
ref_6110 = (ref_6097 & 0xFFFFFFFF) # MOV operation
ref_6574 = (ref_6110 & 0xFFFFFFFF) # MOV operation
ref_6726 = (ref_6574 & 0xFFFFFFFF) # MOV operation
ref_7204 = (ref_6726 & 0xFFFFFFFF) # MOV operation
ref_7361 = (ref_7204 & 0xFFFFFFFF) # MOV operation
ref_7395 = (ref_7361 & 0xFFFFFFFF) # MOV operation
ref_7407 = ref_7395 # MOV operation
ref_7409 = ref_7407 # MOV operation

print ref_7409 & 0xffffffffffffffff
