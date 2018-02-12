#!/usr/bin/env python2
## -*- coding: utf-8 -*-

import sys

def sx(bits, value):
    sign_bit = 1 << (bits - 1)
    return (value & (sign_bit - 1)) - (value & sign_bit)

SymVar_0 = int(sys.argv[1])
ref_512 = SymVar_0
ref_523 = ref_512 # MOV operation
ref_535 = ref_523 # MOV operation
ref_537 = ref_535 # MOV operation
ref_571 = ((ref_537 >> 56) & 0xFF) # Byte reference - MOV operation
ref_572 = ((ref_537 >> 48) & 0xFF) # Byte reference - MOV operation
ref_573 = ((ref_537 >> 40) & 0xFF) # Byte reference - MOV operation
ref_574 = ((ref_537 >> 32) & 0xFF) # Byte reference - MOV operation
ref_575 = ((ref_537 >> 24) & 0xFF) # Byte reference - MOV operation
ref_576 = ((ref_537 >> 16) & 0xFF) # Byte reference - MOV operation
ref_577 = ((ref_537 >> 8) & 0xFF) # Byte reference - MOV operation
ref_578 = (ref_537 & 0xFF) # Byte reference - MOV operation
ref_6169 = ref_577 # MOVZX operation
ref_6171 = (ref_6169 & 0xFF) # MOVZX operation
ref_6173 = (((ref_6171 & 0xFFFFFFFF) << (0x8 & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_6180 = (ref_6173 & 0xFFFFFFFF) # MOV operation
ref_6184 = ref_578 # MOVZX operation
ref_6186 = (ref_6184 & 0xFF) # MOVZX operation
ref_6188 = (((ref_6186 & 0xFFFFFFFF) + (ref_6180 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_6226 = ref_575 # MOVZX operation
ref_6228 = (ref_6226 & 0xFF) # MOVZX operation
ref_6230 = (((ref_6228 & 0xFFFFFFFF) << (0x8 & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_6237 = (ref_6230 & 0xFFFFFFFF) # MOV operation
ref_6249 = ref_576 # MOVZX operation
ref_6251 = (ref_6249 & 0xFF) # MOVZX operation
ref_6253 = (((ref_6251 & 0xFFFFFFFF) + (ref_6237 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_6261 = (((ref_6253 & 0xFFFFFFFF) << (0xB & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_6268 = ((ref_6261 & 0xFFFFFFFF) ^ ((((((0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x8) + (ref_6188 & 0xFFFFFFFF)) & 0xFFFFFFFF)) # XOR operation
ref_6281 = ((((((0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x8) + (ref_6188 & 0xFFFFFFFF)) & 0xFFFFFFFF) # MOV operation
ref_6283 = (((ref_6281 & 0xFFFFFFFF) << (0x10 & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_6290 = ((ref_6283 & 0xFFFFFFFF) ^ (ref_6268 & 0xFFFFFFFF)) # XOR operation
ref_6319 = (ref_6290 & 0xFFFFFFFF) # MOV operation
ref_6321 = ((ref_6319 & 0xFFFFFFFF) >> (0xB & 0x1F)) # SHR operation
ref_6371 = ref_573 # MOVZX operation
ref_6373 = (ref_6371 & 0xFF) # MOVZX operation
ref_6375 = (((ref_6373 & 0xFFFFFFFF) << (0x8 & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_6382 = (ref_6375 & 0xFFFFFFFF) # MOV operation
ref_6386 = ref_574 # MOVZX operation
ref_6388 = (ref_6386 & 0xFF) # MOVZX operation
ref_6390 = (((ref_6388 & 0xFFFFFFFF) + (ref_6382 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_6428 = ref_571 # MOVZX operation
ref_6430 = (ref_6428 & 0xFF) # MOVZX operation
ref_6432 = (((ref_6430 & 0xFFFFFFFF) << (0x8 & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_6439 = (ref_6432 & 0xFFFFFFFF) # MOV operation
ref_6451 = ref_572 # MOVZX operation
ref_6453 = (ref_6451 & 0xFF) # MOVZX operation
ref_6455 = (((ref_6453 & 0xFFFFFFFF) + (ref_6439 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_6463 = (((ref_6455 & 0xFFFFFFFF) << (0xB & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_6470 = ((ref_6463 & 0xFFFFFFFF) ^ (((((ref_6290 & 0xFFFFFFFF) + (ref_6321 & 0xFFFFFFFF)) & 0xFFFFFFFF) + (ref_6390 & 0xFFFFFFFF)) & 0xFFFFFFFF)) # XOR operation
ref_6483 = (((((ref_6290 & 0xFFFFFFFF) + (ref_6321 & 0xFFFFFFFF)) & 0xFFFFFFFF) + (ref_6390 & 0xFFFFFFFF)) & 0xFFFFFFFF) # MOV operation
ref_6485 = (((ref_6483 & 0xFFFFFFFF) << (0x10 & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_6492 = ((ref_6485 & 0xFFFFFFFF) ^ (ref_6470 & 0xFFFFFFFF)) # XOR operation
ref_6521 = (ref_6492 & 0xFFFFFFFF) # MOV operation
ref_6523 = ((ref_6521 & 0xFFFFFFFF) >> (0xB & 0x1F)) # SHR operation
ref_6593 = (((ref_6492 & 0xFFFFFFFF) + (ref_6523 & 0xFFFFFFFF)) & 0xFFFFFFFF) # MOV operation
ref_6595 = (((ref_6593 & 0xFFFFFFFF) << (0x3 & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_6613 = ((((ref_6492 & 0xFFFFFFFF) + (ref_6523 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_6595 & 0xFFFFFFFF)) # MOV operation
ref_6615 = ((ref_6613 & 0xFFFFFFFF) >> (0x5 & 0x1F)) # SHR operation
ref_6634 = ((((((ref_6492 & 0xFFFFFFFF) + (ref_6523 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_6595 & 0xFFFFFFFF)) + (ref_6615 & 0xFFFFFFFF)) & 0xFFFFFFFF) # MOV operation
ref_6636 = (((ref_6634 & 0xFFFFFFFF) << (0x4 & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_6654 = (((((((ref_6492 & 0xFFFFFFFF) + (ref_6523 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_6595 & 0xFFFFFFFF)) + (ref_6615 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_6636 & 0xFFFFFFFF)) # MOV operation
ref_6656 = ((ref_6654 & 0xFFFFFFFF) >> (0x11 & 0x1F)) # SHR operation
ref_6675 = (((((((((ref_6492 & 0xFFFFFFFF) + (ref_6523 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_6595 & 0xFFFFFFFF)) + (ref_6615 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_6636 & 0xFFFFFFFF)) + (ref_6656 & 0xFFFFFFFF)) & 0xFFFFFFFF) # MOV operation
ref_6677 = (((ref_6675 & 0xFFFFFFFF) << (0x19 & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_6695 = ((((((((((ref_6492 & 0xFFFFFFFF) + (ref_6523 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_6595 & 0xFFFFFFFF)) + (ref_6615 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_6636 & 0xFFFFFFFF)) + (ref_6656 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_6677 & 0xFFFFFFFF)) # MOV operation
ref_6697 = ((ref_6695 & 0xFFFFFFFF) >> (0x6 & 0x1F)) # SHR operation
ref_6716 = ((((((((((((ref_6492 & 0xFFFFFFFF) + (ref_6523 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_6595 & 0xFFFFFFFF)) + (ref_6615 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_6636 & 0xFFFFFFFF)) + (ref_6656 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_6677 & 0xFFFFFFFF)) + (ref_6697 & 0xFFFFFFFF)) & 0xFFFFFFFF) # MOV operation
ref_6729 = (ref_6716 & 0xFFFFFFFF) # MOV operation
ref_7451 = (ref_6729 & 0xFFFFFFFF) # MOV operation
ref_7653 = (ref_7451 & 0xFFFFFFFF) # MOV operation
ref_8326 = (ref_7653 & 0xFFFFFFFF) # MOV operation
ref_8514 = (ref_8326 & 0xFFFFFFFF) # MOV operation
ref_8554 = (ref_8514 & 0xFFFFFFFF) # MOV operation
ref_8578 = (ref_8554 & 0xFFFFFFFF) # MOV operation
ref_8590 = ref_8578 # MOV operation
ref_8592 = ref_8590 # MOV operation

print ref_8592 & 0xffffffffffffffff
