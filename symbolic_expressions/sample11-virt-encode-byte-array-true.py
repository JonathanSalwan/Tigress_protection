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
ref_7124 = ref_290 # MOVZX operation
ref_7126 = (ref_7124 & 0xFF) # MOVZX operation
ref_7128 = (((ref_7126 & 0xFFFFFFFF) << (0x8 & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_7135 = (ref_7128 & 0xFFFFFFFF) # MOV operation
ref_7139 = ref_291 # MOVZX operation
ref_7141 = (ref_7139 & 0xFF) # MOVZX operation
ref_7143 = (((ref_7141 & 0xFFFFFFFF) + (ref_7135 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_7181 = ref_288 # MOVZX operation
ref_7183 = (ref_7181 & 0xFF) # MOVZX operation
ref_7185 = (((ref_7183 & 0xFFFFFFFF) << (0x8 & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_7192 = (ref_7185 & 0xFFFFFFFF) # MOV operation
ref_7204 = ref_289 # MOVZX operation
ref_7206 = (ref_7204 & 0xFF) # MOVZX operation
ref_7208 = (((ref_7206 & 0xFFFFFFFF) + (ref_7192 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_7216 = (((ref_7208 & 0xFFFFFFFF) << (0xB & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_7223 = ((ref_7216 & 0xFFFFFFFF) ^ ((((((0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x8) + (ref_7143 & 0xFFFFFFFF)) & 0xFFFFFFFF)) # XOR operation
ref_7236 = ((((((0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x8) + (ref_7143 & 0xFFFFFFFF)) & 0xFFFFFFFF) # MOV operation
ref_7238 = (((ref_7236 & 0xFFFFFFFF) << (0x10 & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_7245 = ((ref_7238 & 0xFFFFFFFF) ^ (ref_7223 & 0xFFFFFFFF)) # XOR operation
ref_7274 = (ref_7245 & 0xFFFFFFFF) # MOV operation
ref_7276 = ((ref_7274 & 0xFFFFFFFF) >> (0xB & 0x1F)) # SHR operation
ref_7326 = ref_286 # MOVZX operation
ref_7328 = (ref_7326 & 0xFF) # MOVZX operation
ref_7330 = (((ref_7328 & 0xFFFFFFFF) << (0x8 & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_7337 = (ref_7330 & 0xFFFFFFFF) # MOV operation
ref_7341 = ref_287 # MOVZX operation
ref_7343 = (ref_7341 & 0xFF) # MOVZX operation
ref_7345 = (((ref_7343 & 0xFFFFFFFF) + (ref_7337 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_7383 = ref_284 # MOVZX operation
ref_7385 = (ref_7383 & 0xFF) # MOVZX operation
ref_7387 = (((ref_7385 & 0xFFFFFFFF) << (0x8 & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_7394 = (ref_7387 & 0xFFFFFFFF) # MOV operation
ref_7406 = ref_285 # MOVZX operation
ref_7408 = (ref_7406 & 0xFF) # MOVZX operation
ref_7410 = (((ref_7408 & 0xFFFFFFFF) + (ref_7394 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_7418 = (((ref_7410 & 0xFFFFFFFF) << (0xB & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_7425 = ((ref_7418 & 0xFFFFFFFF) ^ (((((ref_7245 & 0xFFFFFFFF) + (ref_7276 & 0xFFFFFFFF)) & 0xFFFFFFFF) + (ref_7345 & 0xFFFFFFFF)) & 0xFFFFFFFF)) # XOR operation
ref_7438 = (((((ref_7245 & 0xFFFFFFFF) + (ref_7276 & 0xFFFFFFFF)) & 0xFFFFFFFF) + (ref_7345 & 0xFFFFFFFF)) & 0xFFFFFFFF) # MOV operation
ref_7440 = (((ref_7438 & 0xFFFFFFFF) << (0x10 & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_7447 = ((ref_7440 & 0xFFFFFFFF) ^ (ref_7425 & 0xFFFFFFFF)) # XOR operation
ref_7476 = (ref_7447 & 0xFFFFFFFF) # MOV operation
ref_7478 = ((ref_7476 & 0xFFFFFFFF) >> (0xB & 0x1F)) # SHR operation
ref_7548 = (((ref_7447 & 0xFFFFFFFF) + (ref_7478 & 0xFFFFFFFF)) & 0xFFFFFFFF) # MOV operation
ref_7550 = (((ref_7548 & 0xFFFFFFFF) << (0x3 & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_7568 = ((((ref_7447 & 0xFFFFFFFF) + (ref_7478 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_7550 & 0xFFFFFFFF)) # MOV operation
ref_7570 = ((ref_7568 & 0xFFFFFFFF) >> (0x5 & 0x1F)) # SHR operation
ref_7589 = ((((((ref_7447 & 0xFFFFFFFF) + (ref_7478 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_7550 & 0xFFFFFFFF)) + (ref_7570 & 0xFFFFFFFF)) & 0xFFFFFFFF) # MOV operation
ref_7591 = (((ref_7589 & 0xFFFFFFFF) << (0x4 & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_7609 = (((((((ref_7447 & 0xFFFFFFFF) + (ref_7478 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_7550 & 0xFFFFFFFF)) + (ref_7570 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_7591 & 0xFFFFFFFF)) # MOV operation
ref_7611 = ((ref_7609 & 0xFFFFFFFF) >> (0x11 & 0x1F)) # SHR operation
ref_7630 = (((((((((ref_7447 & 0xFFFFFFFF) + (ref_7478 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_7550 & 0xFFFFFFFF)) + (ref_7570 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_7591 & 0xFFFFFFFF)) + (ref_7611 & 0xFFFFFFFF)) & 0xFFFFFFFF) # MOV operation
ref_7632 = (((ref_7630 & 0xFFFFFFFF) << (0x19 & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_7650 = ((((((((((ref_7447 & 0xFFFFFFFF) + (ref_7478 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_7550 & 0xFFFFFFFF)) + (ref_7570 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_7591 & 0xFFFFFFFF)) + (ref_7611 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_7632 & 0xFFFFFFFF)) # MOV operation
ref_7652 = ((ref_7650 & 0xFFFFFFFF) >> (0x6 & 0x1F)) # SHR operation
ref_7671 = ((((((((((((ref_7447 & 0xFFFFFFFF) + (ref_7478 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_7550 & 0xFFFFFFFF)) + (ref_7570 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_7591 & 0xFFFFFFFF)) + (ref_7611 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_7632 & 0xFFFFFFFF)) + (ref_7652 & 0xFFFFFFFF)) & 0xFFFFFFFF) # MOV operation
ref_7684 = (ref_7671 & 0xFFFFFFFF) # MOV operation
ref_8021 = (ref_7684 & 0xFFFFFFFF) # MOV operation
ref_8116 = (ref_8021 & 0xFFFFFFFF) # MOV operation
ref_8438 = (ref_8116 & 0xFFFFFFFF) # MOV operation
ref_8530 = (ref_8438 & 0xFFFFFFFF) # MOV operation
ref_8564 = (ref_8530 & 0xFFFFFFFF) # MOV operation
ref_8576 = ref_8564 # MOV operation
ref_8578 = ref_8576 # MOV operation

print ref_8578 & 0xffffffffffffffff
