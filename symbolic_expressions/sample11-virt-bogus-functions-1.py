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
ref_295 = ((ref_239 >> 56) & 0xFF) # Byte reference - MOV operation
ref_296 = ((ref_239 >> 48) & 0xFF) # Byte reference - MOV operation
ref_297 = ((ref_239 >> 40) & 0xFF) # Byte reference - MOV operation
ref_298 = ((ref_239 >> 32) & 0xFF) # Byte reference - MOV operation
ref_299 = ((ref_239 >> 24) & 0xFF) # Byte reference - MOV operation
ref_300 = ((ref_239 >> 16) & 0xFF) # Byte reference - MOV operation
ref_301 = ((ref_239 >> 8) & 0xFF) # Byte reference - MOV operation
ref_302 = (ref_239 & 0xFF) # Byte reference - MOV operation
ref_6199 = ref_301 # MOVZX operation
ref_6201 = (ref_6199 & 0xFF) # MOVZX operation
ref_6203 = (((ref_6201 & 0xFFFFFFFF) << (0x8 & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_6210 = (ref_6203 & 0xFFFFFFFF) # MOV operation
ref_6214 = ref_302 # MOVZX operation
ref_6216 = (ref_6214 & 0xFF) # MOVZX operation
ref_6218 = (((ref_6216 & 0xFFFFFFFF) + (ref_6210 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_6256 = ref_299 # MOVZX operation
ref_6258 = (ref_6256 & 0xFF) # MOVZX operation
ref_6260 = (((ref_6258 & 0xFFFFFFFF) << (0x8 & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_6267 = (ref_6260 & 0xFFFFFFFF) # MOV operation
ref_6279 = ref_300 # MOVZX operation
ref_6281 = (ref_6279 & 0xFF) # MOVZX operation
ref_6283 = (((ref_6281 & 0xFFFFFFFF) + (ref_6267 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_6291 = (((ref_6283 & 0xFFFFFFFF) << (0xB & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_6298 = ((ref_6291 & 0xFFFFFFFF) ^ ((((((0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x8) + (ref_6218 & 0xFFFFFFFF)) & 0xFFFFFFFF)) # XOR operation
ref_6311 = ((((((0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x8) + (ref_6218 & 0xFFFFFFFF)) & 0xFFFFFFFF) # MOV operation
ref_6313 = (((ref_6311 & 0xFFFFFFFF) << (0x10 & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_6320 = ((ref_6313 & 0xFFFFFFFF) ^ (ref_6298 & 0xFFFFFFFF)) # XOR operation
ref_6349 = (ref_6320 & 0xFFFFFFFF) # MOV operation
ref_6351 = ((ref_6349 & 0xFFFFFFFF) >> (0xB & 0x1F)) # SHR operation
ref_6401 = ref_297 # MOVZX operation
ref_6403 = (ref_6401 & 0xFF) # MOVZX operation
ref_6405 = (((ref_6403 & 0xFFFFFFFF) << (0x8 & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_6412 = (ref_6405 & 0xFFFFFFFF) # MOV operation
ref_6416 = ref_298 # MOVZX operation
ref_6418 = (ref_6416 & 0xFF) # MOVZX operation
ref_6420 = (((ref_6418 & 0xFFFFFFFF) + (ref_6412 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_6458 = ref_295 # MOVZX operation
ref_6460 = (ref_6458 & 0xFF) # MOVZX operation
ref_6462 = (((ref_6460 & 0xFFFFFFFF) << (0x8 & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_6469 = (ref_6462 & 0xFFFFFFFF) # MOV operation
ref_6481 = ref_296 # MOVZX operation
ref_6483 = (ref_6481 & 0xFF) # MOVZX operation
ref_6485 = (((ref_6483 & 0xFFFFFFFF) + (ref_6469 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_6493 = (((ref_6485 & 0xFFFFFFFF) << (0xB & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_6500 = ((ref_6493 & 0xFFFFFFFF) ^ (((((ref_6320 & 0xFFFFFFFF) + (ref_6351 & 0xFFFFFFFF)) & 0xFFFFFFFF) + (ref_6420 & 0xFFFFFFFF)) & 0xFFFFFFFF)) # XOR operation
ref_6513 = (((((ref_6320 & 0xFFFFFFFF) + (ref_6351 & 0xFFFFFFFF)) & 0xFFFFFFFF) + (ref_6420 & 0xFFFFFFFF)) & 0xFFFFFFFF) # MOV operation
ref_6515 = (((ref_6513 & 0xFFFFFFFF) << (0x10 & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_6522 = ((ref_6515 & 0xFFFFFFFF) ^ (ref_6500 & 0xFFFFFFFF)) # XOR operation
ref_6551 = (ref_6522 & 0xFFFFFFFF) # MOV operation
ref_6553 = ((ref_6551 & 0xFFFFFFFF) >> (0xB & 0x1F)) # SHR operation
ref_6623 = (((ref_6522 & 0xFFFFFFFF) + (ref_6553 & 0xFFFFFFFF)) & 0xFFFFFFFF) # MOV operation
ref_6625 = (((ref_6623 & 0xFFFFFFFF) << (0x3 & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_6643 = ((((ref_6522 & 0xFFFFFFFF) + (ref_6553 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_6625 & 0xFFFFFFFF)) # MOV operation
ref_6645 = ((ref_6643 & 0xFFFFFFFF) >> (0x5 & 0x1F)) # SHR operation
ref_6664 = ((((((ref_6522 & 0xFFFFFFFF) + (ref_6553 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_6625 & 0xFFFFFFFF)) + (ref_6645 & 0xFFFFFFFF)) & 0xFFFFFFFF) # MOV operation
ref_6666 = (((ref_6664 & 0xFFFFFFFF) << (0x4 & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_6684 = (((((((ref_6522 & 0xFFFFFFFF) + (ref_6553 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_6625 & 0xFFFFFFFF)) + (ref_6645 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_6666 & 0xFFFFFFFF)) # MOV operation
ref_6686 = ((ref_6684 & 0xFFFFFFFF) >> (0x11 & 0x1F)) # SHR operation
ref_6705 = (((((((((ref_6522 & 0xFFFFFFFF) + (ref_6553 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_6625 & 0xFFFFFFFF)) + (ref_6645 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_6666 & 0xFFFFFFFF)) + (ref_6686 & 0xFFFFFFFF)) & 0xFFFFFFFF) # MOV operation
ref_6707 = (((ref_6705 & 0xFFFFFFFF) << (0x19 & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_6725 = ((((((((((ref_6522 & 0xFFFFFFFF) + (ref_6553 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_6625 & 0xFFFFFFFF)) + (ref_6645 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_6666 & 0xFFFFFFFF)) + (ref_6686 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_6707 & 0xFFFFFFFF)) # MOV operation
ref_6727 = ((ref_6725 & 0xFFFFFFFF) >> (0x6 & 0x1F)) # SHR operation
ref_6746 = ((((((((((((ref_6522 & 0xFFFFFFFF) + (ref_6553 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_6625 & 0xFFFFFFFF)) + (ref_6645 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_6666 & 0xFFFFFFFF)) + (ref_6686 & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (ref_6707 & 0xFFFFFFFF)) + (ref_6727 & 0xFFFFFFFF)) & 0xFFFFFFFF) # MOV operation
ref_6759 = (ref_6746 & 0xFFFFFFFF) # MOV operation
ref_7706 = (ref_6759 & 0xFFFFFFFF) # MOV operation
ref_8006 = (ref_7706 & 0xFFFFFFFF) # MOV operation
ref_8899 = (ref_8006 & 0xFFFFFFFF) # MOV operation
ref_9135 = (ref_8899 & 0xFFFFFFFF) # MOV operation
ref_9172 = (ref_9135 & 0xFFFFFFFF) # MOV operation
ref_9184 = ref_9172 # MOV operation
ref_9186 = ref_9184 # MOV operation

print ref_9186 & 0xffffffffffffffff
