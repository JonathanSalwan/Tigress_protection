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
ref_9543 = ref_290 # MOVZX operation
ref_9545 = (ref_9543 & 0xFF) # MOVZX operation
ref_9547 = (((ref_9545 & 0xFFFFFFFF) << (0x8 & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_9554 = (ref_9547 & 0xFFFFFFFF) # MOV operation
ref_9558 = ref_291 # MOVZX operation
ref_9560 = (ref_9558 & 0xFF) # MOVZX operation
ref_9562 = (((ref_9560 & 0xFFFFFFFF) + (ref_9554 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_9600 = ref_288 # MOVZX operation
ref_9602 = (ref_9600 & 0xFF) # MOVZX operation
ref_9604 = (((ref_9602 & 0xFFFFFFFF) << (0x8 & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_9611 = (ref_9604 & 0xFFFFFFFF) # MOV operation
ref_9623 = ref_289 # MOVZX operation
ref_9625 = (ref_9623 & 0xFF) # MOVZX operation
ref_9627 = (((ref_9625 & 0xFFFFFFFF) + (ref_9611 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_9635 = (((ref_9627 & 0xFFFFFFFF) << (0xB & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_9642 = ((ref_9635 & 0xFFFFFFFF) ^ ((((((0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x8) + (ref_9562 & 0xFFFFFFFF)) & 0xFFFFFFFF)) # XOR operation
ref_9655 = ((((((0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x8) + (ref_9562 & 0xFFFFFFFF)) & 0xFFFFFFFF) # MOV operation
ref_9657 = (((ref_9655 & 0xFFFFFFFF) << (0x10 & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_9664 = ((ref_9657 & 0xFFFFFFFF) ^ (ref_9642 & 0xFFFFFFFF)) # XOR operation
ref_9693 = (ref_9664 & 0xFFFFFFFF) # MOV operation
ref_9695 = ((ref_9693 & 0xFFFFFFFF) >> (0xB & 0x1F)) # SHR operation
ref_9745 = ref_286 # MOVZX operation
ref_9747 = (ref_9745 & 0xFF) # MOVZX operation
ref_9749 = (((ref_9747 & 0xFFFFFFFF) << (0x8 & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_9756 = (ref_9749 & 0xFFFFFFFF) # MOV operation
ref_9760 = ref_287 # MOVZX operation
ref_9762 = (ref_9760 & 0xFF) # MOVZX operation
ref_9764 = (((ref_9762 & 0xFFFFFFFF) + (ref_9756 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_9802 = ref_284 # MOVZX operation
ref_9804 = (ref_9802 & 0xFF) # MOVZX operation
ref_9806 = (((ref_9804 & 0xFFFFFFFF) << (0x8 & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_9813 = (ref_9806 & 0xFFFFFFFF) # MOV operation
ref_9825 = ref_285 # MOVZX operation
ref_9827 = (ref_9825 & 0xFF) # MOVZX operation
ref_9829 = (((ref_9827 & 0xFFFFFFFF) + (ref_9813 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_9837 = (((ref_9829 & 0xFFFFFFFF) << (0xB & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_9844 = ((ref_9837 & 0xFFFFFFFF) ^ (((((ref_9664 & 0xFFFFFFFF) + (ref_9695 & 0xFFFFFFFF)) & 0xFFFFFFFF) + (ref_9764 & 0xFFFFFFFF)) & 0xFFFFFFFF)) # XOR operation
ref_9857 = (((((ref_9664 & 0xFFFFFFFF) + (ref_9695 & 0xFFFFFFFF)) & 0xFFFFFFFF) + (ref_9764 & 0xFFFFFFFF)) & 0xFFFFFFFF) # MOV operation
ref_9859 = (((ref_9857 & 0xFFFFFFFF) << (0x10 & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_9866 = ((ref_9859 & 0xFFFFFFFF) ^ (ref_9844 & 0xFFFFFFFF)) # XOR operation
ref_9895 = (ref_9866 & 0xFFFFFFFF) # MOV operation
ref_9897 = ((ref_9895 & 0xFFFFFFFF) >> (0xB & 0x1F)) # SHR operation
ref_9967 = (((ref_9866 & 0xFFFFFFFF) + (ref_9897 & 0xFFFFFFFF)) & 0xFFFFFFFF) # MOV operation
ref_9969 = (((ref_9967 & 0xFFFFFFFF) << (0x3 & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_9987 = ((((ref_9866 & 0xFFFFFFFF) + (ref_9897 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_9969 & 0xFFFFFFFF)) # MOV operation
ref_9989 = ((ref_9987 & 0xFFFFFFFF) >> (0x5 & 0x1F)) # SHR operation
ref_10008 = ((((((ref_9866 & 0xFFFFFFFF) + (ref_9897 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_9969 & 0xFFFFFFFF)) + (ref_9989 & 0xFFFFFFFF)) & 0xFFFFFFFF) # MOV operation
ref_10010 = (((ref_10008 & 0xFFFFFFFF) << (0x4 & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_10028 = (((((((ref_9866 & 0xFFFFFFFF) + (ref_9897 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_9969 & 0xFFFFFFFF)) + (ref_9989 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_10010 & 0xFFFFFFFF)) # MOV operation
ref_10030 = ((ref_10028 & 0xFFFFFFFF) >> (0x11 & 0x1F)) # SHR operation
ref_10049 = (((((((((ref_9866 & 0xFFFFFFFF) + (ref_9897 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_9969 & 0xFFFFFFFF)) + (ref_9989 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_10010 & 0xFFFFFFFF)) + (ref_10030 & 0xFFFFFFFF)) & 0xFFFFFFFF) # MOV operation
ref_10051 = (((ref_10049 & 0xFFFFFFFF) << (0x19 & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_10069 = ((((((((((ref_9866 & 0xFFFFFFFF) + (ref_9897 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_9969 & 0xFFFFFFFF)) + (ref_9989 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_10010 & 0xFFFFFFFF)) + (ref_10030 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_10051 & 0xFFFFFFFF)) # MOV operation
ref_10071 = ((ref_10069 & 0xFFFFFFFF) >> (0x6 & 0x1F)) # SHR operation
ref_10090 = ((((((((((((ref_9866 & 0xFFFFFFFF) + (ref_9897 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_9969 & 0xFFFFFFFF)) + (ref_9989 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_10010 & 0xFFFFFFFF)) + (ref_10030 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_10051 & 0xFFFFFFFF)) + (ref_10071 & 0xFFFFFFFF)) & 0xFFFFFFFF) # MOV operation
ref_10103 = (ref_10090 & 0xFFFFFFFF) # MOV operation
ref_10440 = (ref_10103 & 0xFFFFFFFF) # MOV operation
ref_10535 = (ref_10440 & 0xFFFFFFFF) # MOV operation
ref_10857 = (ref_10535 & 0xFFFFFFFF) # MOV operation
ref_10940 = (ref_10857 & 0xFFFFFFFF) # MOV operation
ref_10974 = (ref_10940 & 0xFFFFFFFF) # MOV operation
ref_10986 = ref_10974 # MOV operation
ref_10988 = ref_10986 # MOV operation

print ref_10988 & 0xffffffffffffffff
