#!/usr/bin/env python2
## -*- coding: utf-8 -*-
##
## Triton
##

import sys
import z3

def sx(bits, value):
    sign_bit = 1 << (bits - 1)
    return (value & (sign_bit - 1)) - (value & sign_bit)

ctx = z3.Context()
s   = z3.Solver()

SymVar_0 = z3.BitVec('SymVar_0', 64)
ref_848 = SymVar_0
ref_849 = ((ref_848 >> 56) & 0xFF) # Byte reference - MOV operation
ref_850 = ((ref_848 >> 48) & 0xFF) # Byte reference - MOV operation
ref_851 = ((ref_848 >> 40) & 0xFF) # Byte reference - MOV operation
ref_852 = ((ref_848 >> 32) & 0xFF) # Byte reference - MOV operation
ref_853 = ((ref_848 >> 24) & 0xFF) # Byte reference - MOV operation
ref_854 = ((ref_848 >> 16) & 0xFF) # Byte reference - MOV operation
ref_855 = ((ref_848 >> 8) & 0xFF) # Byte reference - MOV operation
ref_856 = (ref_848 & 0xFF) # Byte reference - MOV operation
ref_857 = ((((((((((ref_848 >> 56) & 0xFF)) << 8 | ((ref_848 >> 48) & 0xFF)) << 8 | ((ref_848 >> 40) & 0xFF)) << 8 | ((ref_848 >> 32) & 0xFF)) << 8 | ((ref_848 >> 24) & 0xFF)) << 8 | ((ref_848 >> 16) & 0xFF)) << 8 | ((ref_848 >> 8) & 0xFF)) << 8 | (ref_848 & 0xFF)) # Temporary concatenation reference - MOV operation
ref_1010 = ref_848 # MOV operation
ref_1012 = ((ref_1010 >> 56) & 0xFF) # Byte reference - MOV operation
ref_1013 = ((ref_1010 >> 48) & 0xFF) # Byte reference - MOV operation
ref_1014 = ((ref_1010 >> 40) & 0xFF) # Byte reference - MOV operation
ref_1015 = ((ref_1010 >> 32) & 0xFF) # Byte reference - MOV operation
ref_1016 = ((ref_1010 >> 24) & 0xFF) # Byte reference - MOV operation
ref_1017 = ((ref_1010 >> 16) & 0xFF) # Byte reference - MOV operation
ref_1018 = ((ref_1010 >> 8) & 0xFF) # Byte reference - MOV operation
ref_1019 = (ref_1010 & 0xFF) # Byte reference - MOV operation
ref_1020 = ((((((((((ref_1010 >> 56) & 0xFF)) << 8 | ((ref_1010 >> 48) & 0xFF)) << 8 | ((ref_1010 >> 40) & 0xFF)) << 8 | ((ref_1010 >> 32) & 0xFF)) << 8 | ((ref_1010 >> 24) & 0xFF)) << 8 | ((ref_1010 >> 16) & 0xFF)) << 8 | ((ref_1010 >> 8) & 0xFF)) << 8 | (ref_1010 & 0xFF)) # Temporary concatenation reference - MOV operation
ref_7847 = ref_1010 # MOV operation
ref_7849 = ((ref_7847 >> 56) & 0xFF) # Byte reference - MOV operation
ref_7850 = ((ref_7847 >> 48) & 0xFF) # Byte reference - MOV operation
ref_7851 = ((ref_7847 >> 40) & 0xFF) # Byte reference - MOV operation
ref_7852 = ((ref_7847 >> 32) & 0xFF) # Byte reference - MOV operation
ref_7853 = ((ref_7847 >> 24) & 0xFF) # Byte reference - MOV operation
ref_7854 = ((ref_7847 >> 16) & 0xFF) # Byte reference - MOV operation
ref_7855 = ((ref_7847 >> 8) & 0xFF) # Byte reference - MOV operation
ref_7856 = (ref_7847 & 0xFF) # Byte reference - MOV operation
ref_7857 = ((((((((((ref_7847 >> 56) & 0xFF)) << 8 | ((ref_7847 >> 48) & 0xFF)) << 8 | ((ref_7847 >> 40) & 0xFF)) << 8 | ((ref_7847 >> 32) & 0xFF)) << 8 | ((ref_7847 >> 24) & 0xFF)) << 8 | ((ref_7847 >> 16) & 0xFF)) << 8 | ((ref_7847 >> 8) & 0xFF)) << 8 | (ref_7847 & 0xFF)) # Temporary concatenation reference - MOV operation
ref_8033 = ref_7847 # MOV operation
ref_8041 = ref_8033 # MOV operation
ref_8043 = (ref_8041 & 0xFFFFFFFFCD5C8BFD) # AND operation
ref_8046 = ((((((((0x1 ^ (((ref_8043 & 0xFF) >> 0x0) & 0x1)) ^ (((ref_8043 & 0xFF) >> 0x1) & 0x1)) ^ (((ref_8043 & 0xFF) >> 0x2) & 0x1)) ^ (((ref_8043 & 0xFF) >> 0x3) & 0x1)) ^ (((ref_8043 & 0xFF) >> 0x4) & 0x1)) ^ (((ref_8043 & 0xFF) >> 0x5) & 0x1)) ^ (((ref_8043 & 0xFF) >> 0x6) & 0x1)) ^ (((ref_8043 & 0xFF) >> 0x7) & 0x1)) # Parity flag
ref_8047 = ((ref_8043 >> 63) & 0x1) # Sign flag
ref_8048 = (0x1 if (ref_8043 == 0x0) else 0x0) # Zero flag
ref_8060 = ref_7847 # MOV operation
ref_8068 = (0xFFFFFFFFCD5C8BFD & ref_8060) # AND operation
ref_8071 = ((((((((0x1 ^ (((ref_8068 & 0xFF) >> 0x0) & 0x1)) ^ (((ref_8068 & 0xFF) >> 0x1) & 0x1)) ^ (((ref_8068 & 0xFF) >> 0x2) & 0x1)) ^ (((ref_8068 & 0xFF) >> 0x3) & 0x1)) ^ (((ref_8068 & 0xFF) >> 0x4) & 0x1)) ^ (((ref_8068 & 0xFF) >> 0x5) & 0x1)) ^ (((ref_8068 & 0xFF) >> 0x6) & 0x1)) ^ (((ref_8068 & 0xFF) >> 0x7) & 0x1)) # Parity flag
ref_8072 = ((ref_8068 >> 63) & 0x1) # Sign flag
ref_8073 = (0x1 if (ref_8068 == 0x0) else 0x0) # Zero flag
ref_8075 = ((ref_8043 + ref_8068) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_8076 = (0x1 if (0x10 == (0x10 & (ref_8075 ^ (ref_8043 ^ ref_8068)))) else 0x0) # Adjust flag
ref_8077 = ((((ref_8043 & ref_8068) ^ (((ref_8043 ^ ref_8068) ^ ref_8075) & (ref_8043 ^ ref_8068))) >> 63) & 0x1) # Carry flag
ref_8078 = ((((ref_8043 ^ ~ref_8068) & (ref_8043 ^ ref_8075)) >> 63) & 0x1) # Overflow flag
ref_8079 = ((((((((0x1 ^ (((ref_8075 & 0xFF) >> 0x0) & 0x1)) ^ (((ref_8075 & 0xFF) >> 0x1) & 0x1)) ^ (((ref_8075 & 0xFF) >> 0x2) & 0x1)) ^ (((ref_8075 & 0xFF) >> 0x3) & 0x1)) ^ (((ref_8075 & 0xFF) >> 0x4) & 0x1)) ^ (((ref_8075 & 0xFF) >> 0x5) & 0x1)) ^ (((ref_8075 & 0xFF) >> 0x6) & 0x1)) ^ (((ref_8075 & 0xFF) >> 0x7) & 0x1)) # Parity flag
ref_8080 = ((ref_8075 >> 63) & 0x1) # Sign flag
ref_8081 = (0x1 if (ref_8075 == 0x0) else 0x0) # Zero flag
ref_8093 = ref_7847 # MOV operation
ref_8099 = (0x32A37402 ^ ref_8093) # XOR operation
ref_8102 = ((((((((0x1 ^ (((ref_8099 & 0xFF) >> 0x0) & 0x1)) ^ (((ref_8099 & 0xFF) >> 0x1) & 0x1)) ^ (((ref_8099 & 0xFF) >> 0x2) & 0x1)) ^ (((ref_8099 & 0xFF) >> 0x3) & 0x1)) ^ (((ref_8099 & 0xFF) >> 0x4) & 0x1)) ^ (((ref_8099 & 0xFF) >> 0x5) & 0x1)) ^ (((ref_8099 & 0xFF) >> 0x6) & 0x1)) ^ (((ref_8099 & 0xFF) >> 0x7) & 0x1)) # Parity flag
ref_8103 = ((ref_8099 >> 63) & 0x1) # Sign flag
ref_8104 = (0x1 if (ref_8099 == 0x0) else 0x0) # Zero flag
ref_8106 = ref_8075 # MOV operation
ref_8108 = ((ref_8106 - ref_8099) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_8109 = (0x1 if (0x10 == (0x10 & (ref_8108 ^ (ref_8106 ^ ref_8099)))) else 0x0) # Adjust flag
ref_8110 = ((((ref_8106 ^ (ref_8099 ^ ref_8108)) ^ ((ref_8106 ^ ref_8108) & (ref_8106 ^ ref_8099))) >> 63) & 0x1) # Carry flag
ref_8111 = ((((ref_8106 ^ ref_8099) & (ref_8106 ^ ref_8108)) >> 63) & 0x1) # Overflow flag
ref_8112 = ((((((((0x1 ^ (((ref_8108 & 0xFF) >> 0x0) & 0x1)) ^ (((ref_8108 & 0xFF) >> 0x1) & 0x1)) ^ (((ref_8108 & 0xFF) >> 0x2) & 0x1)) ^ (((ref_8108 & 0xFF) >> 0x3) & 0x1)) ^ (((ref_8108 & 0xFF) >> 0x4) & 0x1)) ^ (((ref_8108 & 0xFF) >> 0x5) & 0x1)) ^ (((ref_8108 & 0xFF) >> 0x6) & 0x1)) ^ (((ref_8108 & 0xFF) >> 0x7) & 0x1)) # Parity flag
ref_8113 = ((ref_8108 >> 63) & 0x1) # Sign flag
ref_8114 = (0x1 if (ref_8108 == 0x0) else 0x0) # Zero flag
ref_8116 = ref_8108 # MOV operation
ref_8118 = ((ref_8116 >> 56) & 0xFF) # Byte reference - MOV operation
ref_8119 = ((ref_8116 >> 48) & 0xFF) # Byte reference - MOV operation
ref_8120 = ((ref_8116 >> 40) & 0xFF) # Byte reference - MOV operation
ref_8121 = ((ref_8116 >> 32) & 0xFF) # Byte reference - MOV operation
ref_8122 = ((ref_8116 >> 24) & 0xFF) # Byte reference - MOV operation
ref_8123 = ((ref_8116 >> 16) & 0xFF) # Byte reference - MOV operation
ref_8124 = ((ref_8116 >> 8) & 0xFF) # Byte reference - MOV operation
ref_8125 = (ref_8116 & 0xFF) # Byte reference - MOV operation
ref_8126 = ((((((((((ref_8116 >> 56) & 0xFF)) << 8 | ((ref_8116 >> 48) & 0xFF)) << 8 | ((ref_8116 >> 40) & 0xFF)) << 8 | ((ref_8116 >> 32) & 0xFF)) << 8 | ((ref_8116 >> 24) & 0xFF)) << 8 | ((ref_8116 >> 16) & 0xFF)) << 8 | ((ref_8116 >> 8) & 0xFF)) << 8 | (ref_8116 & 0xFF)) # Temporary concatenation reference - MOV operation
ref_13799 = ref_8116 # MOV operation
ref_13801 = ((ref_13799 >> 56) & 0xFF) # Byte reference - MOV operation
ref_13802 = ((ref_13799 >> 48) & 0xFF) # Byte reference - MOV operation
ref_13803 = ((ref_13799 >> 40) & 0xFF) # Byte reference - MOV operation
ref_13804 = ((ref_13799 >> 32) & 0xFF) # Byte reference - MOV operation
ref_13805 = ((ref_13799 >> 24) & 0xFF) # Byte reference - MOV operation
ref_13806 = ((ref_13799 >> 16) & 0xFF) # Byte reference - MOV operation
ref_13807 = ((ref_13799 >> 8) & 0xFF) # Byte reference - MOV operation
ref_13808 = (ref_13799 & 0xFF) # Byte reference - MOV operation
ref_13809 = ((((((((((ref_13799 >> 56) & 0xFF)) << 8 | ((ref_13799 >> 48) & 0xFF)) << 8 | ((ref_13799 >> 40) & 0xFF)) << 8 | ((ref_13799 >> 32) & 0xFF)) << 8 | ((ref_13799 >> 24) & 0xFF)) << 8 | ((ref_13799 >> 16) & 0xFF)) << 8 | ((ref_13799 >> 8) & 0xFF)) << 8 | (ref_13799 & 0xFF)) # Temporary concatenation reference - MOV operation
ref_24123 = ref_13799 # MOV operation
ref_24125 = ((ref_24123 >> 56) & 0xFF) # Byte reference - MOV operation
ref_24126 = ((ref_24123 >> 48) & 0xFF) # Byte reference - MOV operation
ref_24127 = ((ref_24123 >> 40) & 0xFF) # Byte reference - MOV operation
ref_24128 = ((ref_24123 >> 32) & 0xFF) # Byte reference - MOV operation
ref_24129 = ((ref_24123 >> 24) & 0xFF) # Byte reference - MOV operation
ref_24130 = ((ref_24123 >> 16) & 0xFF) # Byte reference - MOV operation
ref_24131 = ((ref_24123 >> 8) & 0xFF) # Byte reference - MOV operation
ref_24132 = (ref_24123 & 0xFF) # Byte reference - MOV operation
ref_24133 = ((((((((((ref_24123 >> 56) & 0xFF)) << 8 | ((ref_24123 >> 48) & 0xFF)) << 8 | ((ref_24123 >> 40) & 0xFF)) << 8 | ((ref_24123 >> 32) & 0xFF)) << 8 | ((ref_24123 >> 24) & 0xFF)) << 8 | ((ref_24123 >> 16) & 0xFF)) << 8 | ((ref_24123 >> 8) & 0xFF)) << 8 | (ref_24123 & 0xFF)) # Temporary concatenation reference - MOV operation
ref_25032 = ref_24123 # MOV operation
ref_25040 = ref_25032 # MOV operation
ref_25044 = (ref_25040 >> (0x3 & 0x3F)) # SHR operation
ref_25045 = (0x0 if ((0x3 & 0x3F) == 0x0) else ((ref_25040 >> (((0x3 & 0x3F) - 0x1) & 0xFFFFFFFFFFFFFFFF)) & 0x1)) # Carry flag
ref_25046 = (((ref_25040 >> ((0x40 - 0x1) & 0xFFFFFFFFFFFFFFFF)) & 0x1) if ((0x3 & 0x3F) == 0x1) else 0x0) # Overflow flag
ref_25047 = (0x1 if ((0x3 & 0x3F) == 0x0) else ((((((((0x1 ^ (((ref_25044 & 0xFF) >> 0x0) & 0x1)) ^ (((ref_25044 & 0xFF) >> 0x1) & 0x1)) ^ (((ref_25044 & 0xFF) >> 0x2) & 0x1)) ^ (((ref_25044 & 0xFF) >> 0x3) & 0x1)) ^ (((ref_25044 & 0xFF) >> 0x4) & 0x1)) ^ (((ref_25044 & 0xFF) >> 0x5) & 0x1)) ^ (((ref_25044 & 0xFF) >> 0x6) & 0x1)) ^ (((ref_25044 & 0xFF) >> 0x7) & 0x1))) # Parity flag
ref_25048 = (0x0 if ((0x3 & 0x3F) == 0x0) else ((ref_25044 >> 63) & 0x1)) # Sign flag
ref_25049 = (0x0 if ((0x3 & 0x3F) == 0x0) else (0x1 if (ref_25044 == 0x0) else 0x0)) # Zero flag
ref_25051 = ref_25044 # MOV operation
ref_25053 = ((ref_25051 >> 56) & 0xFF) # Byte reference - MOV operation
ref_25054 = ((ref_25051 >> 48) & 0xFF) # Byte reference - MOV operation
ref_25055 = ((ref_25051 >> 40) & 0xFF) # Byte reference - MOV operation
ref_25056 = ((ref_25051 >> 32) & 0xFF) # Byte reference - MOV operation
ref_25057 = ((ref_25051 >> 24) & 0xFF) # Byte reference - MOV operation
ref_25058 = ((ref_25051 >> 16) & 0xFF) # Byte reference - MOV operation
ref_25059 = ((ref_25051 >> 8) & 0xFF) # Byte reference - MOV operation
ref_25060 = (ref_25051 & 0xFF) # Byte reference - MOV operation
ref_25061 = ((((((((((ref_25051 >> 56) & 0xFF)) << 8 | ((ref_25051 >> 48) & 0xFF)) << 8 | ((ref_25051 >> 40) & 0xFF)) << 8 | ((ref_25051 >> 32) & 0xFF)) << 8 | ((ref_25051 >> 24) & 0xFF)) << 8 | ((ref_25051 >> 16) & 0xFF)) << 8 | ((ref_25051 >> 8) & 0xFF)) << 8 | (ref_25051 & 0xFF)) # Temporary concatenation reference - MOV operation
ref_25944 = ref_25051 # MOV operation
ref_25946 = ref_25944 # MOV operation
ref_25948 = ~ref_25946 # NOT operation
ref_25954 = (ref_25948 | 0x7) # OR operation
ref_25957 = ((((((((0x1 ^ (((ref_25954 & 0xFF) >> 0x0) & 0x1)) ^ (((ref_25954 & 0xFF) >> 0x1) & 0x1)) ^ (((ref_25954 & 0xFF) >> 0x2) & 0x1)) ^ (((ref_25954 & 0xFF) >> 0x3) & 0x1)) ^ (((ref_25954 & 0xFF) >> 0x4) & 0x1)) ^ (((ref_25954 & 0xFF) >> 0x5) & 0x1)) ^ (((ref_25954 & 0xFF) >> 0x6) & 0x1)) ^ (((ref_25954 & 0xFF) >> 0x7) & 0x1)) # Parity flag
ref_25958 = ((ref_25954 >> 63) & 0x1) # Sign flag
ref_25959 = (0x1 if (ref_25954 == 0x0) else 0x0) # Zero flag
ref_25971 = ref_25051 # MOV operation
ref_25973 = ((ref_25971 + ref_25954) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_25974 = (0x1 if (0x10 == (0x10 & (ref_25973 ^ (ref_25971 ^ ref_25954)))) else 0x0) # Adjust flag
ref_25975 = ((((ref_25971 & ref_25954) ^ (((ref_25971 ^ ref_25954) ^ ref_25973) & (ref_25971 ^ ref_25954))) >> 63) & 0x1) # Carry flag
ref_25976 = ((((ref_25971 ^ ~ref_25954) & (ref_25971 ^ ref_25973)) >> 63) & 0x1) # Overflow flag
ref_25977 = ((((((((0x1 ^ (((ref_25973 & 0xFF) >> 0x0) & 0x1)) ^ (((ref_25973 & 0xFF) >> 0x1) & 0x1)) ^ (((ref_25973 & 0xFF) >> 0x2) & 0x1)) ^ (((ref_25973 & 0xFF) >> 0x3) & 0x1)) ^ (((ref_25973 & 0xFF) >> 0x4) & 0x1)) ^ (((ref_25973 & 0xFF) >> 0x5) & 0x1)) ^ (((ref_25973 & 0xFF) >> 0x6) & 0x1)) ^ (((ref_25973 & 0xFF) >> 0x7) & 0x1)) # Parity flag
ref_25978 = ((ref_25973 >> 63) & 0x1) # Sign flag
ref_25979 = (0x1 if (ref_25973 == 0x0) else 0x0) # Zero flag
ref_25981 = ((ref_25973 + 0x1) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_25982 = (0x1 if (0x10 == (0x10 & (ref_25981 ^ (ref_25973 ^ 0x1)))) else 0x0) # Adjust flag
ref_25983 = ((((ref_25973 & 0x1) ^ (((ref_25973 ^ 0x1) ^ ref_25981) & (ref_25973 ^ 0x1))) >> 63) & 0x1) # Carry flag
ref_25984 = ((((ref_25973 ^ ~0x1) & (ref_25973 ^ ref_25981)) >> 63) & 0x1) # Overflow flag
ref_25985 = ((((((((0x1 ^ (((ref_25981 & 0xFF) >> 0x0) & 0x1)) ^ (((ref_25981 & 0xFF) >> 0x1) & 0x1)) ^ (((ref_25981 & 0xFF) >> 0x2) & 0x1)) ^ (((ref_25981 & 0xFF) >> 0x3) & 0x1)) ^ (((ref_25981 & 0xFF) >> 0x4) & 0x1)) ^ (((ref_25981 & 0xFF) >> 0x5) & 0x1)) ^ (((ref_25981 & 0xFF) >> 0x6) & 0x1)) ^ (((ref_25981 & 0xFF) >> 0x7) & 0x1)) # Parity flag
ref_25986 = ((ref_25981 >> 63) & 0x1) # Sign flag
ref_25987 = (0x1 if (ref_25981 == 0x0) else 0x0) # Zero flag
ref_25989 = ((ref_25981 >> 56) & 0xFF) # Byte reference - MOV operation
ref_25990 = ((ref_25981 >> 48) & 0xFF) # Byte reference - MOV operation
ref_25991 = ((ref_25981 >> 40) & 0xFF) # Byte reference - MOV operation
ref_25992 = ((ref_25981 >> 32) & 0xFF) # Byte reference - MOV operation
ref_25993 = ((ref_25981 >> 24) & 0xFF) # Byte reference - MOV operation
ref_25994 = ((ref_25981 >> 16) & 0xFF) # Byte reference - MOV operation
ref_25995 = ((ref_25981 >> 8) & 0xFF) # Byte reference - MOV operation
ref_25996 = (ref_25981 & 0xFF) # Byte reference - MOV operation
ref_25997 = ((((((((((ref_25981 >> 56) & 0xFF)) << 8 | ((ref_25981 >> 48) & 0xFF)) << 8 | ((ref_25981 >> 40) & 0xFF)) << 8 | ((ref_25981 >> 32) & 0xFF)) << 8 | ((ref_25981 >> 24) & 0xFF)) << 8 | ((ref_25981 >> 16) & 0xFF)) << 8 | ((ref_25981 >> 8) & 0xFF)) << 8 | (ref_25981 & 0xFF)) # Temporary concatenation reference - MOV operation
ref_26248 = ref_25981 # MOV operation
ref_26264 = (0xFFFFFFFFFFFFFFFE & ref_26248) # AND operation
ref_26267 = ((((((((0x1 ^ (((ref_26264 & 0xFF) >> 0x0) & 0x1)) ^ (((ref_26264 & 0xFF) >> 0x1) & 0x1)) ^ (((ref_26264 & 0xFF) >> 0x2) & 0x1)) ^ (((ref_26264 & 0xFF) >> 0x3) & 0x1)) ^ (((ref_26264 & 0xFF) >> 0x4) & 0x1)) ^ (((ref_26264 & 0xFF) >> 0x5) & 0x1)) ^ (((ref_26264 & 0xFF) >> 0x6) & 0x1)) ^ (((ref_26264 & 0xFF) >> 0x7) & 0x1)) # Parity flag
ref_26268 = ((ref_26264 >> 63) & 0x1) # Sign flag
ref_26269 = (0x1 if (ref_26264 == 0x0) else 0x0) # Zero flag
ref_26283 = ((0x1 + ref_26264) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_26284 = (0x1 if (0x10 == (0x10 & (ref_26283 ^ (0x1 ^ ref_26264)))) else 0x0) # Adjust flag
ref_26285 = ((((0x1 & ref_26264) ^ (((0x1 ^ ref_26264) ^ ref_26283) & (0x1 ^ ref_26264))) >> 63) & 0x1) # Carry flag
ref_26286 = ((((0x1 ^ ~ref_26264) & (0x1 ^ ref_26283)) >> 63) & 0x1) # Overflow flag
ref_26287 = ((((((((0x1 ^ (((ref_26283 & 0xFF) >> 0x0) & 0x1)) ^ (((ref_26283 & 0xFF) >> 0x1) & 0x1)) ^ (((ref_26283 & 0xFF) >> 0x2) & 0x1)) ^ (((ref_26283 & 0xFF) >> 0x3) & 0x1)) ^ (((ref_26283 & 0xFF) >> 0x4) & 0x1)) ^ (((ref_26283 & 0xFF) >> 0x5) & 0x1)) ^ (((ref_26283 & 0xFF) >> 0x6) & 0x1)) ^ (((ref_26283 & 0xFF) >> 0x7) & 0x1)) # Parity flag
ref_26288 = ((ref_26283 >> 63) & 0x1) # Sign flag
ref_26289 = (0x1 if (ref_26283 == 0x0) else 0x0) # Zero flag
ref_26291 = ((ref_26283 >> 56) & 0xFF) # Byte reference - MOV operation
ref_26292 = ((ref_26283 >> 48) & 0xFF) # Byte reference - MOV operation
ref_26293 = ((ref_26283 >> 40) & 0xFF) # Byte reference - MOV operation
ref_26294 = ((ref_26283 >> 32) & 0xFF) # Byte reference - MOV operation
ref_26295 = ((ref_26283 >> 24) & 0xFF) # Byte reference - MOV operation
ref_26296 = ((ref_26283 >> 16) & 0xFF) # Byte reference - MOV operation
ref_26297 = ((ref_26283 >> 8) & 0xFF) # Byte reference - MOV operation
ref_26298 = (ref_26283 & 0xFF) # Byte reference - MOV operation
ref_26299 = ((((((((((ref_26283 >> 56) & 0xFF)) << 8 | ((ref_26283 >> 48) & 0xFF)) << 8 | ((ref_26283 >> 40) & 0xFF)) << 8 | ((ref_26283 >> 32) & 0xFF)) << 8 | ((ref_26283 >> 24) & 0xFF)) << 8 | ((ref_26283 >> 16) & 0xFF)) << 8 | ((ref_26283 >> 8) & 0xFF)) << 8 | (ref_26283 & 0xFF)) # Temporary concatenation reference - MOV operation
ref_33031 = ref_1010 # MOV operation
ref_33033 = ((ref_33031 >> 56) & 0xFF) # Byte reference - MOV operation
ref_33034 = ((ref_33031 >> 48) & 0xFF) # Byte reference - MOV operation
ref_33035 = ((ref_33031 >> 40) & 0xFF) # Byte reference - MOV operation
ref_33036 = ((ref_33031 >> 32) & 0xFF) # Byte reference - MOV operation
ref_33037 = ((ref_33031 >> 24) & 0xFF) # Byte reference - MOV operation
ref_33038 = ((ref_33031 >> 16) & 0xFF) # Byte reference - MOV operation
ref_33039 = ((ref_33031 >> 8) & 0xFF) # Byte reference - MOV operation
ref_33040 = (ref_33031 & 0xFF) # Byte reference - MOV operation
ref_33041 = ((((((((((ref_33031 >> 56) & 0xFF)) << 8 | ((ref_33031 >> 48) & 0xFF)) << 8 | ((ref_33031 >> 40) & 0xFF)) << 8 | ((ref_33031 >> 32) & 0xFF)) << 8 | ((ref_33031 >> 24) & 0xFF)) << 8 | ((ref_33031 >> 16) & 0xFF)) << 8 | ((ref_33031 >> 8) & 0xFF)) << 8 | (ref_33031 & 0xFF)) # Temporary concatenation reference - MOV operation
ref_33100 = ref_33031 # MOV operation
ref_33112 = ref_26283 # MOV operation
ref_33114 = ref_33100 # MOV operation
ref_33116 = (ref_33112 & 0xFFFFFFFF) # MOV operation
ref_33118 = ((ref_33114 << ((ref_33116 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_33119 = (0x0 if (((ref_33116 & 0xFF) & 0x3F) == 0x0) else ((ref_33114 >> ((0x40 - ((ref_33116 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF)) & 0x1)) # Carry flag
ref_33120 = ((((ref_33114 >> ((0x40 - 0x1) & 0xFFFFFFFFFFFFFFFF)) ^ (ref_33114 >> ((0x40 - 0x2) & 0xFFFFFFFFFFFFFFFF))) & 0x1) if (((ref_33116 & 0xFF) & 0x3F) == 0x1) else 0x0) # Overflow flag
ref_33121 = (0x0 if (((ref_33116 & 0xFF) & 0x3F) == 0x0) else ((((((((0x1 ^ (((ref_33118 & 0xFF) >> 0x0) & 0x1)) ^ (((ref_33118 & 0xFF) >> 0x1) & 0x1)) ^ (((ref_33118 & 0xFF) >> 0x2) & 0x1)) ^ (((ref_33118 & 0xFF) >> 0x3) & 0x1)) ^ (((ref_33118 & 0xFF) >> 0x4) & 0x1)) ^ (((ref_33118 & 0xFF) >> 0x5) & 0x1)) ^ (((ref_33118 & 0xFF) >> 0x6) & 0x1)) ^ (((ref_33118 & 0xFF) >> 0x7) & 0x1))) # Parity flag
ref_33122 = (0x0 if (((ref_33116 & 0xFF) & 0x3F) == 0x0) else ((ref_33118 >> 63) & 0x1)) # Sign flag
ref_33123 = (0x0 if (((ref_33116 & 0xFF) & 0x3F) == 0x0) else (0x1 if (ref_33118 == 0x0) else 0x0)) # Zero flag
ref_33125 = ref_33118 # MOV operation
ref_33127 = ((ref_33125 >> 56) & 0xFF) # Byte reference - MOV operation
ref_33128 = ((ref_33125 >> 48) & 0xFF) # Byte reference - MOV operation
ref_33129 = ((ref_33125 >> 40) & 0xFF) # Byte reference - MOV operation
ref_33130 = ((ref_33125 >> 32) & 0xFF) # Byte reference - MOV operation
ref_33131 = ((ref_33125 >> 24) & 0xFF) # Byte reference - MOV operation
ref_33132 = ((ref_33125 >> 16) & 0xFF) # Byte reference - MOV operation
ref_33133 = ((ref_33125 >> 8) & 0xFF) # Byte reference - MOV operation
ref_33134 = (ref_33125 & 0xFF) # Byte reference - MOV operation
ref_33135 = ((((((((((ref_33125 >> 56) & 0xFF)) << 8 | ((ref_33125 >> 48) & 0xFF)) << 8 | ((ref_33125 >> 40) & 0xFF)) << 8 | ((ref_33125 >> 32) & 0xFF)) << 8 | ((ref_33125 >> 24) & 0xFF)) << 8 | ((ref_33125 >> 16) & 0xFF)) << 8 | ((ref_33125 >> 8) & 0xFF)) << 8 | (ref_33125 & 0xFF)) # Temporary concatenation reference - MOV operation
ref_33722 = ref_33125 # MOV operation
ref_33724 = ((ref_33722 >> 56) & 0xFF) # Byte reference - MOV operation
ref_33725 = ((ref_33722 >> 48) & 0xFF) # Byte reference - MOV operation
ref_33726 = ((ref_33722 >> 40) & 0xFF) # Byte reference - MOV operation
ref_33727 = ((ref_33722 >> 32) & 0xFF) # Byte reference - MOV operation
ref_33728 = ((ref_33722 >> 24) & 0xFF) # Byte reference - MOV operation
ref_33729 = ((ref_33722 >> 16) & 0xFF) # Byte reference - MOV operation
ref_33730 = ((ref_33722 >> 8) & 0xFF) # Byte reference - MOV operation
ref_33731 = (ref_33722 & 0xFF) # Byte reference - MOV operation
ref_33732 = ((((((((((ref_33722 >> 56) & 0xFF)) << 8 | ((ref_33722 >> 48) & 0xFF)) << 8 | ((ref_33722 >> 40) & 0xFF)) << 8 | ((ref_33722 >> 32) & 0xFF)) << 8 | ((ref_33722 >> 24) & 0xFF)) << 8 | ((ref_33722 >> 16) & 0xFF)) << 8 | ((ref_33722 >> 8) & 0xFF)) << 8 | (ref_33722 & 0xFF)) # Temporary concatenation reference - MOV operation
ref_34847 = ((ref_33118 >> 56) & 0xFF) # Byte reference - PUSH operation
ref_34848 = ((ref_33118 >> 48) & 0xFF) # Byte reference - PUSH operation
ref_34849 = ((ref_33118 >> 40) & 0xFF) # Byte reference - PUSH operation
ref_34850 = ((ref_33118 >> 32) & 0xFF) # Byte reference - PUSH operation
ref_34851 = ((ref_33118 >> 24) & 0xFF) # Byte reference - PUSH operation
ref_34852 = ((ref_33118 >> 16) & 0xFF) # Byte reference - PUSH operation
ref_34853 = ((ref_33118 >> 8) & 0xFF) # Byte reference - PUSH operation
ref_34854 = (ref_33118 & 0xFF) # Byte reference - PUSH operation
ref_34855 = ((((((((((ref_33118 >> 56) & 0xFF)) << 8 | ((ref_33118 >> 48) & 0xFF)) << 8 | ((ref_33118 >> 40) & 0xFF)) << 8 | ((ref_33118 >> 32) & 0xFF)) << 8 | ((ref_33118 >> 24) & 0xFF)) << 8 | ((ref_33118 >> 16) & 0xFF)) << 8 | ((ref_33118 >> 8) & 0xFF)) << 8 | (ref_33118 & 0xFF)) # Temporary concatenation reference - PUSH operation
ref_34991 = ref_33118 # POP operation
ref_35290 = ((ref_34991 >> 56) & 0xFF) # Byte reference - PUSH operation
ref_35291 = ((ref_34991 >> 48) & 0xFF) # Byte reference - PUSH operation
ref_35292 = ((ref_34991 >> 40) & 0xFF) # Byte reference - PUSH operation
ref_35293 = ((ref_34991 >> 32) & 0xFF) # Byte reference - PUSH operation
ref_35294 = ((ref_34991 >> 24) & 0xFF) # Byte reference - PUSH operation
ref_35295 = ((ref_34991 >> 16) & 0xFF) # Byte reference - PUSH operation
ref_35296 = ((ref_34991 >> 8) & 0xFF) # Byte reference - PUSH operation
ref_35297 = (ref_34991 & 0xFF) # Byte reference - PUSH operation
ref_35298 = ((((((((((ref_34991 >> 56) & 0xFF)) << 8 | ((ref_34991 >> 48) & 0xFF)) << 8 | ((ref_34991 >> 40) & 0xFF)) << 8 | ((ref_34991 >> 32) & 0xFF)) << 8 | ((ref_34991 >> 24) & 0xFF)) << 8 | ((ref_34991 >> 16) & 0xFF)) << 8 | ((ref_34991 >> 8) & 0xFF)) << 8 | (ref_34991 & 0xFF)) # Temporary concatenation reference - PUSH operation
ref_35517 = ref_34991 # POP operation
ref_35986 = ((ref_35517 >> 56) & 0xFF) # Byte reference - PUSH operation
ref_35987 = ((ref_35517 >> 48) & 0xFF) # Byte reference - PUSH operation
ref_35988 = ((ref_35517 >> 40) & 0xFF) # Byte reference - PUSH operation
ref_35989 = ((ref_35517 >> 32) & 0xFF) # Byte reference - PUSH operation
ref_35990 = ((ref_35517 >> 24) & 0xFF) # Byte reference - PUSH operation
ref_35991 = ((ref_35517 >> 16) & 0xFF) # Byte reference - PUSH operation
ref_35992 = ((ref_35517 >> 8) & 0xFF) # Byte reference - PUSH operation
ref_35993 = (ref_35517 & 0xFF) # Byte reference - PUSH operation
ref_35994 = ((((((((((ref_35517 >> 56) & 0xFF)) << 8 | ((ref_35517 >> 48) & 0xFF)) << 8 | ((ref_35517 >> 40) & 0xFF)) << 8 | ((ref_35517 >> 32) & 0xFF)) << 8 | ((ref_35517 >> 24) & 0xFF)) << 8 | ((ref_35517 >> 16) & 0xFF)) << 8 | ((ref_35517 >> 8) & 0xFF)) << 8 | (ref_35517 & 0xFF)) # Temporary concatenation reference - PUSH operation
ref_36107 = ref_35517 # POP operation
ref_36414 = ((ref_36107 >> 56) & 0xFF) # Byte reference - PUSH operation
ref_36415 = ((ref_36107 >> 48) & 0xFF) # Byte reference - PUSH operation
ref_36416 = ((ref_36107 >> 40) & 0xFF) # Byte reference - PUSH operation
ref_36417 = ((ref_36107 >> 32) & 0xFF) # Byte reference - PUSH operation
ref_36418 = ((ref_36107 >> 24) & 0xFF) # Byte reference - PUSH operation
ref_36419 = ((ref_36107 >> 16) & 0xFF) # Byte reference - PUSH operation
ref_36420 = ((ref_36107 >> 8) & 0xFF) # Byte reference - PUSH operation
ref_36421 = (ref_36107 & 0xFF) # Byte reference - PUSH operation
ref_36422 = ((((((((((ref_36107 >> 56) & 0xFF)) << 8 | ((ref_36107 >> 48) & 0xFF)) << 8 | ((ref_36107 >> 40) & 0xFF)) << 8 | ((ref_36107 >> 32) & 0xFF)) << 8 | ((ref_36107 >> 24) & 0xFF)) << 8 | ((ref_36107 >> 16) & 0xFF)) << 8 | ((ref_36107 >> 8) & 0xFF)) << 8 | (ref_36107 & 0xFF)) # Temporary concatenation reference - PUSH operation
ref_36796 = ((ref_36107 >> 56) & 0xFF) # Byte reference - PUSH operation
ref_36797 = ((ref_36107 >> 48) & 0xFF) # Byte reference - PUSH operation
ref_36798 = ((ref_36107 >> 40) & 0xFF) # Byte reference - PUSH operation
ref_36799 = ((ref_36107 >> 32) & 0xFF) # Byte reference - PUSH operation
ref_36800 = ((ref_36107 >> 24) & 0xFF) # Byte reference - PUSH operation
ref_36801 = ((ref_36107 >> 16) & 0xFF) # Byte reference - PUSH operation
ref_36802 = ((ref_36107 >> 8) & 0xFF) # Byte reference - PUSH operation
ref_36803 = (ref_36107 & 0xFF) # Byte reference - PUSH operation
ref_36804 = ((((((((((ref_36107 >> 56) & 0xFF)) << 8 | ((ref_36107 >> 48) & 0xFF)) << 8 | ((ref_36107 >> 40) & 0xFF)) << 8 | ((ref_36107 >> 32) & 0xFF)) << 8 | ((ref_36107 >> 24) & 0xFF)) << 8 | ((ref_36107 >> 16) & 0xFF)) << 8 | ((ref_36107 >> 8) & 0xFF)) << 8 | (ref_36107 & 0xFF)) # Temporary concatenation reference - PUSH operation
ref_36962 = ref_36107 # POP operation
ref_36980 = ref_36107 # POP operation
ref_39087 = ((ref_36980 >> 56) & 0xFF) # Byte reference - PUSH operation
ref_39088 = ((ref_36980 >> 48) & 0xFF) # Byte reference - PUSH operation
ref_39089 = ((ref_36980 >> 40) & 0xFF) # Byte reference - PUSH operation
ref_39090 = ((ref_36980 >> 32) & 0xFF) # Byte reference - PUSH operation
ref_39091 = ((ref_36980 >> 24) & 0xFF) # Byte reference - PUSH operation
ref_39092 = ((ref_36980 >> 16) & 0xFF) # Byte reference - PUSH operation
ref_39093 = ((ref_36980 >> 8) & 0xFF) # Byte reference - PUSH operation
ref_39094 = (ref_36980 & 0xFF) # Byte reference - PUSH operation
ref_39095 = ((((((((((ref_36980 >> 56) & 0xFF)) << 8 | ((ref_36980 >> 48) & 0xFF)) << 8 | ((ref_36980 >> 40) & 0xFF)) << 8 | ((ref_36980 >> 32) & 0xFF)) << 8 | ((ref_36980 >> 24) & 0xFF)) << 8 | ((ref_36980 >> 16) & 0xFF)) << 8 | ((ref_36980 >> 8) & 0xFF)) << 8 | (ref_36980 & 0xFF)) # Temporary concatenation reference - PUSH operation
ref_39231 = ref_36980 # POP operation
ref_39530 = ((ref_39231 >> 56) & 0xFF) # Byte reference - PUSH operation
ref_39531 = ((ref_39231 >> 48) & 0xFF) # Byte reference - PUSH operation
ref_39532 = ((ref_39231 >> 40) & 0xFF) # Byte reference - PUSH operation
ref_39533 = ((ref_39231 >> 32) & 0xFF) # Byte reference - PUSH operation
ref_39534 = ((ref_39231 >> 24) & 0xFF) # Byte reference - PUSH operation
ref_39535 = ((ref_39231 >> 16) & 0xFF) # Byte reference - PUSH operation
ref_39536 = ((ref_39231 >> 8) & 0xFF) # Byte reference - PUSH operation
ref_39537 = (ref_39231 & 0xFF) # Byte reference - PUSH operation
ref_39538 = ((((((((((ref_39231 >> 56) & 0xFF)) << 8 | ((ref_39231 >> 48) & 0xFF)) << 8 | ((ref_39231 >> 40) & 0xFF)) << 8 | ((ref_39231 >> 32) & 0xFF)) << 8 | ((ref_39231 >> 24) & 0xFF)) << 8 | ((ref_39231 >> 16) & 0xFF)) << 8 | ((ref_39231 >> 8) & 0xFF)) << 8 | (ref_39231 & 0xFF)) # Temporary concatenation reference - PUSH operation
ref_39757 = ref_39231 # POP operation
ref_42863 = ref_13799 # MOV operation
ref_42865 = ((ref_42863 >> 56) & 0xFF) # Byte reference - MOV operation
ref_42866 = ((ref_42863 >> 48) & 0xFF) # Byte reference - MOV operation
ref_42867 = ((ref_42863 >> 40) & 0xFF) # Byte reference - MOV operation
ref_42868 = ((ref_42863 >> 32) & 0xFF) # Byte reference - MOV operation
ref_42869 = ((ref_42863 >> 24) & 0xFF) # Byte reference - MOV operation
ref_42870 = ((ref_42863 >> 16) & 0xFF) # Byte reference - MOV operation
ref_42871 = ((ref_42863 >> 8) & 0xFF) # Byte reference - MOV operation
ref_42872 = (ref_42863 & 0xFF) # Byte reference - MOV operation
ref_42873 = ((((((((((ref_42863 >> 56) & 0xFF)) << 8 | ((ref_42863 >> 48) & 0xFF)) << 8 | ((ref_42863 >> 40) & 0xFF)) << 8 | ((ref_42863 >> 32) & 0xFF)) << 8 | ((ref_42863 >> 24) & 0xFF)) << 8 | ((ref_42863 >> 16) & 0xFF)) << 8 | ((ref_42863 >> 8) & 0xFF)) << 8 | (ref_42863 & 0xFF)) # Temporary concatenation reference - MOV operation
ref_43314 = ((ref_39757 >> 56) & 0xFF) # Byte reference - PUSH operation
ref_43315 = ((ref_39757 >> 48) & 0xFF) # Byte reference - PUSH operation
ref_43316 = ((ref_39757 >> 40) & 0xFF) # Byte reference - PUSH operation
ref_43317 = ((ref_39757 >> 32) & 0xFF) # Byte reference - PUSH operation
ref_43318 = ((ref_39757 >> 24) & 0xFF) # Byte reference - PUSH operation
ref_43319 = ((ref_39757 >> 16) & 0xFF) # Byte reference - PUSH operation
ref_43320 = ((ref_39757 >> 8) & 0xFF) # Byte reference - PUSH operation
ref_43321 = (ref_39757 & 0xFF) # Byte reference - PUSH operation
ref_43322 = ((((((((((ref_39757 >> 56) & 0xFF)) << 8 | ((ref_39757 >> 48) & 0xFF)) << 8 | ((ref_39757 >> 40) & 0xFF)) << 8 | ((ref_39757 >> 32) & 0xFF)) << 8 | ((ref_39757 >> 24) & 0xFF)) << 8 | ((ref_39757 >> 16) & 0xFF)) << 8 | ((ref_39757 >> 8) & 0xFF)) << 8 | (ref_39757 & 0xFF)) # Temporary concatenation reference - PUSH operation
ref_43435 = ref_39757 # POP operation
ref_43630 = ref_42863 # MOV operation
ref_43640 = (ref_43630 & 0xFFFFFFFFDCDE22A3) # AND operation
ref_43643 = ((((((((0x1 ^ (((ref_43640 & 0xFF) >> 0x0) & 0x1)) ^ (((ref_43640 & 0xFF) >> 0x1) & 0x1)) ^ (((ref_43640 & 0xFF) >> 0x2) & 0x1)) ^ (((ref_43640 & 0xFF) >> 0x3) & 0x1)) ^ (((ref_43640 & 0xFF) >> 0x4) & 0x1)) ^ (((ref_43640 & 0xFF) >> 0x5) & 0x1)) ^ (((ref_43640 & 0xFF) >> 0x6) & 0x1)) ^ (((ref_43640 & 0xFF) >> 0x7) & 0x1)) # Parity flag
ref_43644 = ((ref_43640 >> 63) & 0x1) # Sign flag
ref_43645 = (0x1 if (ref_43640 == 0x0) else 0x0) # Zero flag
ref_43653 = ((0x2321DD5C + ref_43640) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_43654 = (0x1 if (0x10 == (0x10 & (ref_43653 ^ (0x2321DD5C ^ ref_43640)))) else 0x0) # Adjust flag
ref_43655 = ((((0x2321DD5C & ref_43640) ^ (((0x2321DD5C ^ ref_43640) ^ ref_43653) & (0x2321DD5C ^ ref_43640))) >> 63) & 0x1) # Carry flag
ref_43656 = ((((0x2321DD5C ^ ~ref_43640) & (0x2321DD5C ^ ref_43653)) >> 63) & 0x1) # Overflow flag
ref_43657 = ((((((((0x1 ^ (((ref_43653 & 0xFF) >> 0x0) & 0x1)) ^ (((ref_43653 & 0xFF) >> 0x1) & 0x1)) ^ (((ref_43653 & 0xFF) >> 0x2) & 0x1)) ^ (((ref_43653 & 0xFF) >> 0x3) & 0x1)) ^ (((ref_43653 & 0xFF) >> 0x4) & 0x1)) ^ (((ref_43653 & 0xFF) >> 0x5) & 0x1)) ^ (((ref_43653 & 0xFF) >> 0x6) & 0x1)) ^ (((ref_43653 & 0xFF) >> 0x7) & 0x1)) # Parity flag
ref_43658 = ((ref_43653 >> 63) & 0x1) # Sign flag
ref_43659 = (0x1 if (ref_43653 == 0x0) else 0x0) # Zero flag
ref_43661 = ((ref_43653 >> 56) & 0xFF) # Byte reference - MOV operation
ref_43662 = ((ref_43653 >> 48) & 0xFF) # Byte reference - MOV operation
ref_43663 = ((ref_43653 >> 40) & 0xFF) # Byte reference - MOV operation
ref_43664 = ((ref_43653 >> 32) & 0xFF) # Byte reference - MOV operation
ref_43665 = ((ref_43653 >> 24) & 0xFF) # Byte reference - MOV operation
ref_43666 = ((ref_43653 >> 16) & 0xFF) # Byte reference - MOV operation
ref_43667 = ((ref_43653 >> 8) & 0xFF) # Byte reference - MOV operation
ref_43668 = (ref_43653 & 0xFF) # Byte reference - MOV operation
ref_43669 = ((((((((((ref_43653 >> 56) & 0xFF)) << 8 | ((ref_43653 >> 48) & 0xFF)) << 8 | ((ref_43653 >> 40) & 0xFF)) << 8 | ((ref_43653 >> 32) & 0xFF)) << 8 | ((ref_43653 >> 24) & 0xFF)) << 8 | ((ref_43653 >> 16) & 0xFF)) << 8 | ((ref_43653 >> 8) & 0xFF)) << 8 | (ref_43653 & 0xFF)) # Temporary concatenation reference - MOV operation
ref_44611 = ((ref_43435 >> 56) & 0xFF) # Byte reference - PUSH operation
ref_44612 = ((ref_43435 >> 48) & 0xFF) # Byte reference - PUSH operation
ref_44613 = ((ref_43435 >> 40) & 0xFF) # Byte reference - PUSH operation
ref_44614 = ((ref_43435 >> 32) & 0xFF) # Byte reference - PUSH operation
ref_44615 = ((ref_43435 >> 24) & 0xFF) # Byte reference - PUSH operation
ref_44616 = ((ref_43435 >> 16) & 0xFF) # Byte reference - PUSH operation
ref_44617 = ((ref_43435 >> 8) & 0xFF) # Byte reference - PUSH operation
ref_44618 = (ref_43435 & 0xFF) # Byte reference - PUSH operation
ref_44619 = ((((((((((ref_43435 >> 56) & 0xFF)) << 8 | ((ref_43435 >> 48) & 0xFF)) << 8 | ((ref_43435 >> 40) & 0xFF)) << 8 | ((ref_43435 >> 32) & 0xFF)) << 8 | ((ref_43435 >> 24) & 0xFF)) << 8 | ((ref_43435 >> 16) & 0xFF)) << 8 | ((ref_43435 >> 8) & 0xFF)) << 8 | (ref_43435 & 0xFF)) # Temporary concatenation reference - PUSH operation
ref_45865 = ref_43435 # POP operation
ref_46821 = ((ref_45865 >> 56) & 0xFF) # Byte reference - PUSH operation
ref_46822 = ((ref_45865 >> 48) & 0xFF) # Byte reference - PUSH operation
ref_46823 = ((ref_45865 >> 40) & 0xFF) # Byte reference - PUSH operation
ref_46824 = ((ref_45865 >> 32) & 0xFF) # Byte reference - PUSH operation
ref_46825 = ((ref_45865 >> 24) & 0xFF) # Byte reference - PUSH operation
ref_46826 = ((ref_45865 >> 16) & 0xFF) # Byte reference - PUSH operation
ref_46827 = ((ref_45865 >> 8) & 0xFF) # Byte reference - PUSH operation
ref_46828 = (ref_45865 & 0xFF) # Byte reference - PUSH operation
ref_46829 = ((((((((((ref_45865 >> 56) & 0xFF)) << 8 | ((ref_45865 >> 48) & 0xFF)) << 8 | ((ref_45865 >> 40) & 0xFF)) << 8 | ((ref_45865 >> 32) & 0xFF)) << 8 | ((ref_45865 >> 24) & 0xFF)) << 8 | ((ref_45865 >> 16) & 0xFF)) << 8 | ((ref_45865 >> 8) & 0xFF)) << 8 | (ref_45865 & 0xFF)) # Temporary concatenation reference - PUSH operation
ref_46945 = ref_45865 # POP operation
ref_49295 = ((ref_46945 >> 56) & 0xFF) # Byte reference - PUSH operation
ref_49296 = ((ref_46945 >> 48) & 0xFF) # Byte reference - PUSH operation
ref_49297 = ((ref_46945 >> 40) & 0xFF) # Byte reference - PUSH operation
ref_49298 = ((ref_46945 >> 32) & 0xFF) # Byte reference - PUSH operation
ref_49299 = ((ref_46945 >> 24) & 0xFF) # Byte reference - PUSH operation
ref_49300 = ((ref_46945 >> 16) & 0xFF) # Byte reference - PUSH operation
ref_49301 = ((ref_46945 >> 8) & 0xFF) # Byte reference - PUSH operation
ref_49302 = (ref_46945 & 0xFF) # Byte reference - PUSH operation
ref_49303 = ((((((((((ref_46945 >> 56) & 0xFF)) << 8 | ((ref_46945 >> 48) & 0xFF)) << 8 | ((ref_46945 >> 40) & 0xFF)) << 8 | ((ref_46945 >> 32) & 0xFF)) << 8 | ((ref_46945 >> 24) & 0xFF)) << 8 | ((ref_46945 >> 16) & 0xFF)) << 8 | ((ref_46945 >> 8) & 0xFF)) << 8 | (ref_46945 & 0xFF)) # Temporary concatenation reference - PUSH operation
ref_49442 = ref_46945 # POP operation
ref_50404 = ref_1010 # MOV operation
ref_50406 = ((ref_50404 >> 56) & 0xFF) # Byte reference - MOV operation
ref_50407 = ((ref_50404 >> 48) & 0xFF) # Byte reference - MOV operation
ref_50408 = ((ref_50404 >> 40) & 0xFF) # Byte reference - MOV operation
ref_50409 = ((ref_50404 >> 32) & 0xFF) # Byte reference - MOV operation
ref_50410 = ((ref_50404 >> 24) & 0xFF) # Byte reference - MOV operation
ref_50411 = ((ref_50404 >> 16) & 0xFF) # Byte reference - MOV operation
ref_50412 = ((ref_50404 >> 8) & 0xFF) # Byte reference - MOV operation
ref_50413 = (ref_50404 & 0xFF) # Byte reference - MOV operation
ref_50414 = ((((((((((ref_50404 >> 56) & 0xFF)) << 8 | ((ref_50404 >> 48) & 0xFF)) << 8 | ((ref_50404 >> 40) & 0xFF)) << 8 | ((ref_50404 >> 32) & 0xFF)) << 8 | ((ref_50404 >> 24) & 0xFF)) << 8 | ((ref_50404 >> 16) & 0xFF)) << 8 | ((ref_50404 >> 8) & 0xFF)) << 8 | (ref_50404 & 0xFF)) # Temporary concatenation reference - MOV operation
ref_50645 = ref_50404 # MOV operation
ref_50657 = ref_43653 # MOV operation
ref_50659 = ~ref_50657 # NOT operation
ref_50661 = (ref_50659 & ref_50645) # AND operation
ref_50664 = ((((((((0x1 ^ (((ref_50661 & 0xFF) >> 0x0) & 0x1)) ^ (((ref_50661 & 0xFF) >> 0x1) & 0x1)) ^ (((ref_50661 & 0xFF) >> 0x2) & 0x1)) ^ (((ref_50661 & 0xFF) >> 0x3) & 0x1)) ^ (((ref_50661 & 0xFF) >> 0x4) & 0x1)) ^ (((ref_50661 & 0xFF) >> 0x5) & 0x1)) ^ (((ref_50661 & 0xFF) >> 0x6) & 0x1)) ^ (((ref_50661 & 0xFF) >> 0x7) & 0x1)) # Parity flag
ref_50665 = ((ref_50661 >> 63) & 0x1) # Sign flag
ref_50666 = (0x1 if (ref_50661 == 0x0) else 0x0) # Zero flag
ref_50678 = ref_43653 # MOV operation
ref_50680 = ((ref_50678 + ref_50661) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_50681 = (0x1 if (0x10 == (0x10 & (ref_50680 ^ (ref_50678 ^ ref_50661)))) else 0x0) # Adjust flag
ref_50682 = ((((ref_50678 & ref_50661) ^ (((ref_50678 ^ ref_50661) ^ ref_50680) & (ref_50678 ^ ref_50661))) >> 63) & 0x1) # Carry flag
ref_50683 = ((((ref_50678 ^ ~ref_50661) & (ref_50678 ^ ref_50680)) >> 63) & 0x1) # Overflow flag
ref_50684 = ((((((((0x1 ^ (((ref_50680 & 0xFF) >> 0x0) & 0x1)) ^ (((ref_50680 & 0xFF) >> 0x1) & 0x1)) ^ (((ref_50680 & 0xFF) >> 0x2) & 0x1)) ^ (((ref_50680 & 0xFF) >> 0x3) & 0x1)) ^ (((ref_50680 & 0xFF) >> 0x4) & 0x1)) ^ (((ref_50680 & 0xFF) >> 0x5) & 0x1)) ^ (((ref_50680 & 0xFF) >> 0x6) & 0x1)) ^ (((ref_50680 & 0xFF) >> 0x7) & 0x1)) # Parity flag
ref_50685 = ((ref_50680 >> 63) & 0x1) # Sign flag
ref_50686 = (0x1 if (ref_50680 == 0x0) else 0x0) # Zero flag
ref_50688 = ((ref_50680 >> 56) & 0xFF) # Byte reference - MOV operation
ref_50689 = ((ref_50680 >> 48) & 0xFF) # Byte reference - MOV operation
ref_50690 = ((ref_50680 >> 40) & 0xFF) # Byte reference - MOV operation
ref_50691 = ((ref_50680 >> 32) & 0xFF) # Byte reference - MOV operation
ref_50692 = ((ref_50680 >> 24) & 0xFF) # Byte reference - MOV operation
ref_50693 = ((ref_50680 >> 16) & 0xFF) # Byte reference - MOV operation
ref_50694 = ((ref_50680 >> 8) & 0xFF) # Byte reference - MOV operation
ref_50695 = (ref_50680 & 0xFF) # Byte reference - MOV operation
ref_50696 = ((((((((((ref_50680 >> 56) & 0xFF)) << 8 | ((ref_50680 >> 48) & 0xFF)) << 8 | ((ref_50680 >> 40) & 0xFF)) << 8 | ((ref_50680 >> 32) & 0xFF)) << 8 | ((ref_50680 >> 24) & 0xFF)) << 8 | ((ref_50680 >> 16) & 0xFF)) << 8 | ((ref_50680 >> 8) & 0xFF)) << 8 | (ref_50680 & 0xFF)) # Temporary concatenation reference - MOV operation
ref_51283 = ref_50680 # MOV operation
ref_51285 = ((ref_51283 >> 56) & 0xFF) # Byte reference - MOV operation
ref_51286 = ((ref_51283 >> 48) & 0xFF) # Byte reference - MOV operation
ref_51287 = ((ref_51283 >> 40) & 0xFF) # Byte reference - MOV operation
ref_51288 = ((ref_51283 >> 32) & 0xFF) # Byte reference - MOV operation
ref_51289 = ((ref_51283 >> 24) & 0xFF) # Byte reference - MOV operation
ref_51290 = ((ref_51283 >> 16) & 0xFF) # Byte reference - MOV operation
ref_51291 = ((ref_51283 >> 8) & 0xFF) # Byte reference - MOV operation
ref_51292 = (ref_51283 & 0xFF) # Byte reference - MOV operation
ref_51293 = ((((((((((ref_51283 >> 56) & 0xFF)) << 8 | ((ref_51283 >> 48) & 0xFF)) << 8 | ((ref_51283 >> 40) & 0xFF)) << 8 | ((ref_51283 >> 32) & 0xFF)) << 8 | ((ref_51283 >> 24) & 0xFF)) << 8 | ((ref_51283 >> 16) & 0xFF)) << 8 | ((ref_51283 >> 8) & 0xFF)) << 8 | (ref_51283 & 0xFF)) # Temporary concatenation reference - MOV operation
ref_53328 = ((ref_49442 >> 56) & 0xFF) # Byte reference - PUSH operation
ref_53329 = ((ref_49442 >> 48) & 0xFF) # Byte reference - PUSH operation
ref_53330 = ((ref_49442 >> 40) & 0xFF) # Byte reference - PUSH operation
ref_53331 = ((ref_49442 >> 32) & 0xFF) # Byte reference - PUSH operation
ref_53332 = ((ref_49442 >> 24) & 0xFF) # Byte reference - PUSH operation
ref_53333 = ((ref_49442 >> 16) & 0xFF) # Byte reference - PUSH operation
ref_53334 = ((ref_49442 >> 8) & 0xFF) # Byte reference - PUSH operation
ref_53335 = (ref_49442 & 0xFF) # Byte reference - PUSH operation
ref_53336 = ((((((((((ref_49442 >> 56) & 0xFF)) << 8 | ((ref_49442 >> 48) & 0xFF)) << 8 | ((ref_49442 >> 40) & 0xFF)) << 8 | ((ref_49442 >> 32) & 0xFF)) << 8 | ((ref_49442 >> 24) & 0xFF)) << 8 | ((ref_49442 >> 16) & 0xFF)) << 8 | ((ref_49442 >> 8) & 0xFF)) << 8 | (ref_49442 & 0xFF)) # Temporary concatenation reference - PUSH operation
ref_53472 = ref_49442 # POP operation
ref_53771 = ((ref_53472 >> 56) & 0xFF) # Byte reference - PUSH operation
ref_53772 = ((ref_53472 >> 48) & 0xFF) # Byte reference - PUSH operation
ref_53773 = ((ref_53472 >> 40) & 0xFF) # Byte reference - PUSH operation
ref_53774 = ((ref_53472 >> 32) & 0xFF) # Byte reference - PUSH operation
ref_53775 = ((ref_53472 >> 24) & 0xFF) # Byte reference - PUSH operation
ref_53776 = ((ref_53472 >> 16) & 0xFF) # Byte reference - PUSH operation
ref_53777 = ((ref_53472 >> 8) & 0xFF) # Byte reference - PUSH operation
ref_53778 = (ref_53472 & 0xFF) # Byte reference - PUSH operation
ref_53779 = ((((((((((ref_53472 >> 56) & 0xFF)) << 8 | ((ref_53472 >> 48) & 0xFF)) << 8 | ((ref_53472 >> 40) & 0xFF)) << 8 | ((ref_53472 >> 32) & 0xFF)) << 8 | ((ref_53472 >> 24) & 0xFF)) << 8 | ((ref_53472 >> 16) & 0xFF)) << 8 | ((ref_53472 >> 8) & 0xFF)) << 8 | (ref_53472 & 0xFF)) # Temporary concatenation reference - PUSH operation
ref_53998 = ref_53472 # POP operation
ref_54467 = ((ref_53998 >> 56) & 0xFF) # Byte reference - PUSH operation
ref_54468 = ((ref_53998 >> 48) & 0xFF) # Byte reference - PUSH operation
ref_54469 = ((ref_53998 >> 40) & 0xFF) # Byte reference - PUSH operation
ref_54470 = ((ref_53998 >> 32) & 0xFF) # Byte reference - PUSH operation
ref_54471 = ((ref_53998 >> 24) & 0xFF) # Byte reference - PUSH operation
ref_54472 = ((ref_53998 >> 16) & 0xFF) # Byte reference - PUSH operation
ref_54473 = ((ref_53998 >> 8) & 0xFF) # Byte reference - PUSH operation
ref_54474 = (ref_53998 & 0xFF) # Byte reference - PUSH operation
ref_54475 = ((((((((((ref_53998 >> 56) & 0xFF)) << 8 | ((ref_53998 >> 48) & 0xFF)) << 8 | ((ref_53998 >> 40) & 0xFF)) << 8 | ((ref_53998 >> 32) & 0xFF)) << 8 | ((ref_53998 >> 24) & 0xFF)) << 8 | ((ref_53998 >> 16) & 0xFF)) << 8 | ((ref_53998 >> 8) & 0xFF)) << 8 | (ref_53998 & 0xFF)) # Temporary concatenation reference - PUSH operation
ref_54588 = ref_53998 # POP operation
ref_54895 = ((ref_54588 >> 56) & 0xFF) # Byte reference - PUSH operation
ref_54896 = ((ref_54588 >> 48) & 0xFF) # Byte reference - PUSH operation
ref_54897 = ((ref_54588 >> 40) & 0xFF) # Byte reference - PUSH operation
ref_54898 = ((ref_54588 >> 32) & 0xFF) # Byte reference - PUSH operation
ref_54899 = ((ref_54588 >> 24) & 0xFF) # Byte reference - PUSH operation
ref_54900 = ((ref_54588 >> 16) & 0xFF) # Byte reference - PUSH operation
ref_54901 = ((ref_54588 >> 8) & 0xFF) # Byte reference - PUSH operation
ref_54902 = (ref_54588 & 0xFF) # Byte reference - PUSH operation
ref_54903 = ((((((((((ref_54588 >> 56) & 0xFF)) << 8 | ((ref_54588 >> 48) & 0xFF)) << 8 | ((ref_54588 >> 40) & 0xFF)) << 8 | ((ref_54588 >> 32) & 0xFF)) << 8 | ((ref_54588 >> 24) & 0xFF)) << 8 | ((ref_54588 >> 16) & 0xFF)) << 8 | ((ref_54588 >> 8) & 0xFF)) << 8 | (ref_54588 & 0xFF)) # Temporary concatenation reference - PUSH operation
ref_55277 = ((ref_54588 >> 56) & 0xFF) # Byte reference - PUSH operation
ref_55278 = ((ref_54588 >> 48) & 0xFF) # Byte reference - PUSH operation
ref_55279 = ((ref_54588 >> 40) & 0xFF) # Byte reference - PUSH operation
ref_55280 = ((ref_54588 >> 32) & 0xFF) # Byte reference - PUSH operation
ref_55281 = ((ref_54588 >> 24) & 0xFF) # Byte reference - PUSH operation
ref_55282 = ((ref_54588 >> 16) & 0xFF) # Byte reference - PUSH operation
ref_55283 = ((ref_54588 >> 8) & 0xFF) # Byte reference - PUSH operation
ref_55284 = (ref_54588 & 0xFF) # Byte reference - PUSH operation
ref_55285 = ((((((((((ref_54588 >> 56) & 0xFF)) << 8 | ((ref_54588 >> 48) & 0xFF)) << 8 | ((ref_54588 >> 40) & 0xFF)) << 8 | ((ref_54588 >> 32) & 0xFF)) << 8 | ((ref_54588 >> 24) & 0xFF)) << 8 | ((ref_54588 >> 16) & 0xFF)) << 8 | ((ref_54588 >> 8) & 0xFF)) << 8 | (ref_54588 & 0xFF)) # Temporary concatenation reference - PUSH operation
ref_55443 = ref_54588 # POP operation
ref_55461 = ref_54588 # POP operation
ref_57548 = ((ref_55461 >> 56) & 0xFF) # Byte reference - PUSH operation
ref_57549 = ((ref_55461 >> 48) & 0xFF) # Byte reference - PUSH operation
ref_57550 = ((ref_55461 >> 40) & 0xFF) # Byte reference - PUSH operation
ref_57551 = ((ref_55461 >> 32) & 0xFF) # Byte reference - PUSH operation
ref_57552 = ((ref_55461 >> 24) & 0xFF) # Byte reference - PUSH operation
ref_57553 = ((ref_55461 >> 16) & 0xFF) # Byte reference - PUSH operation
ref_57554 = ((ref_55461 >> 8) & 0xFF) # Byte reference - PUSH operation
ref_57555 = (ref_55461 & 0xFF) # Byte reference - PUSH operation
ref_57556 = ((((((((((ref_55461 >> 56) & 0xFF)) << 8 | ((ref_55461 >> 48) & 0xFF)) << 8 | ((ref_55461 >> 40) & 0xFF)) << 8 | ((ref_55461 >> 32) & 0xFF)) << 8 | ((ref_55461 >> 24) & 0xFF)) << 8 | ((ref_55461 >> 16) & 0xFF)) << 8 | ((ref_55461 >> 8) & 0xFF)) << 8 | (ref_55461 & 0xFF)) # Temporary concatenation reference - PUSH operation
ref_57672 = ref_55461 # POP operation
ref_59056 = ((ref_57672 >> 56) & 0xFF) # Byte reference - PUSH operation
ref_59057 = ((ref_57672 >> 48) & 0xFF) # Byte reference - PUSH operation
ref_59058 = ((ref_57672 >> 40) & 0xFF) # Byte reference - PUSH operation
ref_59059 = ((ref_57672 >> 32) & 0xFF) # Byte reference - PUSH operation
ref_59060 = ((ref_57672 >> 24) & 0xFF) # Byte reference - PUSH operation
ref_59061 = ((ref_57672 >> 16) & 0xFF) # Byte reference - PUSH operation
ref_59062 = ((ref_57672 >> 8) & 0xFF) # Byte reference - PUSH operation
ref_59063 = (ref_57672 & 0xFF) # Byte reference - PUSH operation
ref_59064 = ((((((((((ref_57672 >> 56) & 0xFF)) << 8 | ((ref_57672 >> 48) & 0xFF)) << 8 | ((ref_57672 >> 40) & 0xFF)) << 8 | ((ref_57672 >> 32) & 0xFF)) << 8 | ((ref_57672 >> 24) & 0xFF)) << 8 | ((ref_57672 >> 16) & 0xFF)) << 8 | ((ref_57672 >> 8) & 0xFF)) << 8 | (ref_57672 & 0xFF)) # Temporary concatenation reference - PUSH operation
ref_60310 = ref_57672 # POP operation
ref_60717 = ((ref_60310 >> 56) & 0xFF) # Byte reference - PUSH operation
ref_60718 = ((ref_60310 >> 48) & 0xFF) # Byte reference - PUSH operation
ref_60719 = ((ref_60310 >> 40) & 0xFF) # Byte reference - PUSH operation
ref_60720 = ((ref_60310 >> 32) & 0xFF) # Byte reference - PUSH operation
ref_60721 = ((ref_60310 >> 24) & 0xFF) # Byte reference - PUSH operation
ref_60722 = ((ref_60310 >> 16) & 0xFF) # Byte reference - PUSH operation
ref_60723 = ((ref_60310 >> 8) & 0xFF) # Byte reference - PUSH operation
ref_60724 = (ref_60310 & 0xFF) # Byte reference - PUSH operation
ref_60725 = ((((((((((ref_60310 >> 56) & 0xFF)) << 8 | ((ref_60310 >> 48) & 0xFF)) << 8 | ((ref_60310 >> 40) & 0xFF)) << 8 | ((ref_60310 >> 32) & 0xFF)) << 8 | ((ref_60310 >> 24) & 0xFF)) << 8 | ((ref_60310 >> 16) & 0xFF)) << 8 | ((ref_60310 >> 8) & 0xFF)) << 8 | (ref_60310 & 0xFF)) # Temporary concatenation reference - PUSH operation
ref_60944 = ref_60310 # POP operation
ref_61531 = ref_1010 # MOV operation
ref_61533 = ((ref_61531 >> 56) & 0xFF) # Byte reference - MOV operation
ref_61534 = ((ref_61531 >> 48) & 0xFF) # Byte reference - MOV operation
ref_61535 = ((ref_61531 >> 40) & 0xFF) # Byte reference - MOV operation
ref_61536 = ((ref_61531 >> 32) & 0xFF) # Byte reference - MOV operation
ref_61537 = ((ref_61531 >> 24) & 0xFF) # Byte reference - MOV operation
ref_61538 = ((ref_61531 >> 16) & 0xFF) # Byte reference - MOV operation
ref_61539 = ((ref_61531 >> 8) & 0xFF) # Byte reference - MOV operation
ref_61540 = (ref_61531 & 0xFF) # Byte reference - MOV operation
ref_61541 = ((((((((((ref_61531 >> 56) & 0xFF)) << 8 | ((ref_61531 >> 48) & 0xFF)) << 8 | ((ref_61531 >> 40) & 0xFF)) << 8 | ((ref_61531 >> 32) & 0xFF)) << 8 | ((ref_61531 >> 24) & 0xFF)) << 8 | ((ref_61531 >> 16) & 0xFF)) << 8 | ((ref_61531 >> 8) & 0xFF)) << 8 | (ref_61531 & 0xFF)) # Temporary concatenation reference - MOV operation
ref_61982 = ((ref_60944 >> 56) & 0xFF) # Byte reference - PUSH operation
ref_61983 = ((ref_60944 >> 48) & 0xFF) # Byte reference - PUSH operation
ref_61984 = ((ref_60944 >> 40) & 0xFF) # Byte reference - PUSH operation
ref_61985 = ((ref_60944 >> 32) & 0xFF) # Byte reference - PUSH operation
ref_61986 = ((ref_60944 >> 24) & 0xFF) # Byte reference - PUSH operation
ref_61987 = ((ref_60944 >> 16) & 0xFF) # Byte reference - PUSH operation
ref_61988 = ((ref_60944 >> 8) & 0xFF) # Byte reference - PUSH operation
ref_61989 = (ref_60944 & 0xFF) # Byte reference - PUSH operation
ref_61990 = ((((((((((ref_60944 >> 56) & 0xFF)) << 8 | ((ref_60944 >> 48) & 0xFF)) << 8 | ((ref_60944 >> 40) & 0xFF)) << 8 | ((ref_60944 >> 32) & 0xFF)) << 8 | ((ref_60944 >> 24) & 0xFF)) << 8 | ((ref_60944 >> 16) & 0xFF)) << 8 | ((ref_60944 >> 8) & 0xFF)) << 8 | (ref_60944 & 0xFF)) # Temporary concatenation reference - PUSH operation
ref_62103 = ref_60944 # POP operation
ref_62298 = ref_61531 # MOV operation
ref_62308 = (ref_62298 & 0xFFFFFFFFDB7E09B7) # AND operation
ref_62311 = ((((((((0x1 ^ (((ref_62308 & 0xFF) >> 0x0) & 0x1)) ^ (((ref_62308 & 0xFF) >> 0x1) & 0x1)) ^ (((ref_62308 & 0xFF) >> 0x2) & 0x1)) ^ (((ref_62308 & 0xFF) >> 0x3) & 0x1)) ^ (((ref_62308 & 0xFF) >> 0x4) & 0x1)) ^ (((ref_62308 & 0xFF) >> 0x5) & 0x1)) ^ (((ref_62308 & 0xFF) >> 0x6) & 0x1)) ^ (((ref_62308 & 0xFF) >> 0x7) & 0x1)) # Parity flag
ref_62312 = ((ref_62308 >> 63) & 0x1) # Sign flag
ref_62313 = (0x1 if (ref_62308 == 0x0) else 0x0) # Zero flag
ref_62321 = ((0x2481F648 + ref_62308) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_62322 = (0x1 if (0x10 == (0x10 & (ref_62321 ^ (0x2481F648 ^ ref_62308)))) else 0x0) # Adjust flag
ref_62323 = ((((0x2481F648 & ref_62308) ^ (((0x2481F648 ^ ref_62308) ^ ref_62321) & (0x2481F648 ^ ref_62308))) >> 63) & 0x1) # Carry flag
ref_62324 = ((((0x2481F648 ^ ~ref_62308) & (0x2481F648 ^ ref_62321)) >> 63) & 0x1) # Overflow flag
ref_62325 = ((((((((0x1 ^ (((ref_62321 & 0xFF) >> 0x0) & 0x1)) ^ (((ref_62321 & 0xFF) >> 0x1) & 0x1)) ^ (((ref_62321 & 0xFF) >> 0x2) & 0x1)) ^ (((ref_62321 & 0xFF) >> 0x3) & 0x1)) ^ (((ref_62321 & 0xFF) >> 0x4) & 0x1)) ^ (((ref_62321 & 0xFF) >> 0x5) & 0x1)) ^ (((ref_62321 & 0xFF) >> 0x6) & 0x1)) ^ (((ref_62321 & 0xFF) >> 0x7) & 0x1)) # Parity flag
ref_62326 = ((ref_62321 >> 63) & 0x1) # Sign flag
ref_62327 = (0x1 if (ref_62321 == 0x0) else 0x0) # Zero flag
ref_62329 = ((ref_62321 >> 56) & 0xFF) # Byte reference - MOV operation
ref_62330 = ((ref_62321 >> 48) & 0xFF) # Byte reference - MOV operation
ref_62331 = ((ref_62321 >> 40) & 0xFF) # Byte reference - MOV operation
ref_62332 = ((ref_62321 >> 32) & 0xFF) # Byte reference - MOV operation
ref_62333 = ((ref_62321 >> 24) & 0xFF) # Byte reference - MOV operation
ref_62334 = ((ref_62321 >> 16) & 0xFF) # Byte reference - MOV operation
ref_62335 = ((ref_62321 >> 8) & 0xFF) # Byte reference - MOV operation
ref_62336 = (ref_62321 & 0xFF) # Byte reference - MOV operation
ref_62337 = ((((((((((ref_62321 >> 56) & 0xFF)) << 8 | ((ref_62321 >> 48) & 0xFF)) << 8 | ((ref_62321 >> 40) & 0xFF)) << 8 | ((ref_62321 >> 32) & 0xFF)) << 8 | ((ref_62321 >> 24) & 0xFF)) << 8 | ((ref_62321 >> 16) & 0xFF)) << 8 | ((ref_62321 >> 8) & 0xFF)) << 8 | (ref_62321 & 0xFF)) # Temporary concatenation reference - MOV operation
ref_64493 = ((ref_62103 >> 56) & 0xFF) # Byte reference - PUSH operation
ref_64494 = ((ref_62103 >> 48) & 0xFF) # Byte reference - PUSH operation
ref_64495 = ((ref_62103 >> 40) & 0xFF) # Byte reference - PUSH operation
ref_64496 = ((ref_62103 >> 32) & 0xFF) # Byte reference - PUSH operation
ref_64497 = ((ref_62103 >> 24) & 0xFF) # Byte reference - PUSH operation
ref_64498 = ((ref_62103 >> 16) & 0xFF) # Byte reference - PUSH operation
ref_64499 = ((ref_62103 >> 8) & 0xFF) # Byte reference - PUSH operation
ref_64500 = (ref_62103 & 0xFF) # Byte reference - PUSH operation
ref_64501 = ((((((((((ref_62103 >> 56) & 0xFF)) << 8 | ((ref_62103 >> 48) & 0xFF)) << 8 | ((ref_62103 >> 40) & 0xFF)) << 8 | ((ref_62103 >> 32) & 0xFF)) << 8 | ((ref_62103 >> 24) & 0xFF)) << 8 | ((ref_62103 >> 16) & 0xFF)) << 8 | ((ref_62103 >> 8) & 0xFF)) << 8 | (ref_62103 & 0xFF)) # Temporary concatenation reference - PUSH operation
ref_64637 = ref_62103 # POP operation
ref_64936 = ((ref_64637 >> 56) & 0xFF) # Byte reference - PUSH operation
ref_64937 = ((ref_64637 >> 48) & 0xFF) # Byte reference - PUSH operation
ref_64938 = ((ref_64637 >> 40) & 0xFF) # Byte reference - PUSH operation
ref_64939 = ((ref_64637 >> 32) & 0xFF) # Byte reference - PUSH operation
ref_64940 = ((ref_64637 >> 24) & 0xFF) # Byte reference - PUSH operation
ref_64941 = ((ref_64637 >> 16) & 0xFF) # Byte reference - PUSH operation
ref_64942 = ((ref_64637 >> 8) & 0xFF) # Byte reference - PUSH operation
ref_64943 = (ref_64637 & 0xFF) # Byte reference - PUSH operation
ref_64944 = ((((((((((ref_64637 >> 56) & 0xFF)) << 8 | ((ref_64637 >> 48) & 0xFF)) << 8 | ((ref_64637 >> 40) & 0xFF)) << 8 | ((ref_64637 >> 32) & 0xFF)) << 8 | ((ref_64637 >> 24) & 0xFF)) << 8 | ((ref_64637 >> 16) & 0xFF)) << 8 | ((ref_64637 >> 8) & 0xFF)) << 8 | (ref_64637 & 0xFF)) # Temporary concatenation reference - PUSH operation
ref_65163 = ref_64637 # POP operation
ref_65632 = ((ref_65163 >> 56) & 0xFF) # Byte reference - PUSH operation
ref_65633 = ((ref_65163 >> 48) & 0xFF) # Byte reference - PUSH operation
ref_65634 = ((ref_65163 >> 40) & 0xFF) # Byte reference - PUSH operation
ref_65635 = ((ref_65163 >> 32) & 0xFF) # Byte reference - PUSH operation
ref_65636 = ((ref_65163 >> 24) & 0xFF) # Byte reference - PUSH operation
ref_65637 = ((ref_65163 >> 16) & 0xFF) # Byte reference - PUSH operation
ref_65638 = ((ref_65163 >> 8) & 0xFF) # Byte reference - PUSH operation
ref_65639 = (ref_65163 & 0xFF) # Byte reference - PUSH operation
ref_65640 = ((((((((((ref_65163 >> 56) & 0xFF)) << 8 | ((ref_65163 >> 48) & 0xFF)) << 8 | ((ref_65163 >> 40) & 0xFF)) << 8 | ((ref_65163 >> 32) & 0xFF)) << 8 | ((ref_65163 >> 24) & 0xFF)) << 8 | ((ref_65163 >> 16) & 0xFF)) << 8 | ((ref_65163 >> 8) & 0xFF)) << 8 | (ref_65163 & 0xFF)) # Temporary concatenation reference - PUSH operation
ref_65753 = ref_65163 # POP operation
ref_66060 = ((ref_65753 >> 56) & 0xFF) # Byte reference - PUSH operation
ref_66061 = ((ref_65753 >> 48) & 0xFF) # Byte reference - PUSH operation
ref_66062 = ((ref_65753 >> 40) & 0xFF) # Byte reference - PUSH operation
ref_66063 = ((ref_65753 >> 32) & 0xFF) # Byte reference - PUSH operation
ref_66064 = ((ref_65753 >> 24) & 0xFF) # Byte reference - PUSH operation
ref_66065 = ((ref_65753 >> 16) & 0xFF) # Byte reference - PUSH operation
ref_66066 = ((ref_65753 >> 8) & 0xFF) # Byte reference - PUSH operation
ref_66067 = (ref_65753 & 0xFF) # Byte reference - PUSH operation
ref_66068 = ((((((((((ref_65753 >> 56) & 0xFF)) << 8 | ((ref_65753 >> 48) & 0xFF)) << 8 | ((ref_65753 >> 40) & 0xFF)) << 8 | ((ref_65753 >> 32) & 0xFF)) << 8 | ((ref_65753 >> 24) & 0xFF)) << 8 | ((ref_65753 >> 16) & 0xFF)) << 8 | ((ref_65753 >> 8) & 0xFF)) << 8 | (ref_65753 & 0xFF)) # Temporary concatenation reference - PUSH operation
ref_66442 = ((ref_65753 >> 56) & 0xFF) # Byte reference - PUSH operation
ref_66443 = ((ref_65753 >> 48) & 0xFF) # Byte reference - PUSH operation
ref_66444 = ((ref_65753 >> 40) & 0xFF) # Byte reference - PUSH operation
ref_66445 = ((ref_65753 >> 32) & 0xFF) # Byte reference - PUSH operation
ref_66446 = ((ref_65753 >> 24) & 0xFF) # Byte reference - PUSH operation
ref_66447 = ((ref_65753 >> 16) & 0xFF) # Byte reference - PUSH operation
ref_66448 = ((ref_65753 >> 8) & 0xFF) # Byte reference - PUSH operation
ref_66449 = (ref_65753 & 0xFF) # Byte reference - PUSH operation
ref_66450 = ((((((((((ref_65753 >> 56) & 0xFF)) << 8 | ((ref_65753 >> 48) & 0xFF)) << 8 | ((ref_65753 >> 40) & 0xFF)) << 8 | ((ref_65753 >> 32) & 0xFF)) << 8 | ((ref_65753 >> 24) & 0xFF)) << 8 | ((ref_65753 >> 16) & 0xFF)) << 8 | ((ref_65753 >> 8) & 0xFF)) << 8 | (ref_65753 & 0xFF)) # Temporary concatenation reference - PUSH operation
ref_66608 = ref_65753 # POP operation
ref_66626 = ref_65753 # POP operation
ref_66802 = ref_13799 # MOV operation
ref_66804 = ((ref_66802 >> 56) & 0xFF) # Byte reference - MOV operation
ref_66805 = ((ref_66802 >> 48) & 0xFF) # Byte reference - MOV operation
ref_66806 = ((ref_66802 >> 40) & 0xFF) # Byte reference - MOV operation
ref_66807 = ((ref_66802 >> 32) & 0xFF) # Byte reference - MOV operation
ref_66808 = ((ref_66802 >> 24) & 0xFF) # Byte reference - MOV operation
ref_66809 = ((ref_66802 >> 16) & 0xFF) # Byte reference - MOV operation
ref_66810 = ((ref_66802 >> 8) & 0xFF) # Byte reference - MOV operation
ref_66811 = (ref_66802 & 0xFF) # Byte reference - MOV operation
ref_66812 = ((((((((((ref_66802 >> 56) & 0xFF)) << 8 | ((ref_66802 >> 48) & 0xFF)) << 8 | ((ref_66802 >> 40) & 0xFF)) << 8 | ((ref_66802 >> 32) & 0xFF)) << 8 | ((ref_66802 >> 24) & 0xFF)) << 8 | ((ref_66802 >> 16) & 0xFF)) << 8 | ((ref_66802 >> 8) & 0xFF)) << 8 | (ref_66802 & 0xFF)) # Temporary concatenation reference - MOV operation
ref_67445 = ((ref_66626 >> 56) & 0xFF) # Byte reference - PUSH operation
ref_67446 = ((ref_66626 >> 48) & 0xFF) # Byte reference - PUSH operation
ref_67447 = ((ref_66626 >> 40) & 0xFF) # Byte reference - PUSH operation
ref_67448 = ((ref_66626 >> 32) & 0xFF) # Byte reference - PUSH operation
ref_67449 = ((ref_66626 >> 24) & 0xFF) # Byte reference - PUSH operation
ref_67450 = ((ref_66626 >> 16) & 0xFF) # Byte reference - PUSH operation
ref_67451 = ((ref_66626 >> 8) & 0xFF) # Byte reference - PUSH operation
ref_67452 = (ref_66626 & 0xFF) # Byte reference - PUSH operation
ref_67453 = ((((((((((ref_66626 >> 56) & 0xFF)) << 8 | ((ref_66626 >> 48) & 0xFF)) << 8 | ((ref_66626 >> 40) & 0xFF)) << 8 | ((ref_66626 >> 32) & 0xFF)) << 8 | ((ref_66626 >> 24) & 0xFF)) << 8 | ((ref_66626 >> 16) & 0xFF)) << 8 | ((ref_66626 >> 8) & 0xFF)) << 8 | (ref_66626 & 0xFF)) # Temporary concatenation reference - PUSH operation
ref_67528 = ref_66802 # MOV operation
ref_67536 = ref_67528 # MOV operation
ref_67540 = ((ref_67536 << (0x9 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_67541 = (0x0 if ((0x9 & 0x3F) == 0x0) else ((ref_67536 >> ((0x40 - (0x9 & 0x3F)) & 0xFFFFFFFFFFFFFFFF)) & 0x1)) # Carry flag
ref_67542 = ((((ref_67536 >> ((0x40 - 0x1) & 0xFFFFFFFFFFFFFFFF)) ^ (ref_67536 >> ((0x40 - 0x2) & 0xFFFFFFFFFFFFFFFF))) & 0x1) if ((0x9 & 0x3F) == 0x1) else 0x0) # Overflow flag
ref_67543 = (0x1 if ((0x9 & 0x3F) == 0x0) else ((((((((0x1 ^ (((ref_67540 & 0xFF) >> 0x0) & 0x1)) ^ (((ref_67540 & 0xFF) >> 0x1) & 0x1)) ^ (((ref_67540 & 0xFF) >> 0x2) & 0x1)) ^ (((ref_67540 & 0xFF) >> 0x3) & 0x1)) ^ (((ref_67540 & 0xFF) >> 0x4) & 0x1)) ^ (((ref_67540 & 0xFF) >> 0x5) & 0x1)) ^ (((ref_67540 & 0xFF) >> 0x6) & 0x1)) ^ (((ref_67540 & 0xFF) >> 0x7) & 0x1))) # Parity flag
ref_67544 = (0x0 if ((0x9 & 0x3F) == 0x0) else ((ref_67540 >> 63) & 0x1)) # Sign flag
ref_67545 = (0x0 if ((0x9 & 0x3F) == 0x0) else (0x1 if (ref_67540 == 0x0) else 0x0)) # Zero flag
ref_67547 = ref_67540 # MOV operation
ref_67549 = ((ref_67547 >> 56) & 0xFF) # Byte reference - MOV operation
ref_67550 = ((ref_67547 >> 48) & 0xFF) # Byte reference - MOV operation
ref_67551 = ((ref_67547 >> 40) & 0xFF) # Byte reference - MOV operation
ref_67552 = ((ref_67547 >> 32) & 0xFF) # Byte reference - MOV operation
ref_67553 = ((ref_67547 >> 24) & 0xFF) # Byte reference - MOV operation
ref_67554 = ((ref_67547 >> 16) & 0xFF) # Byte reference - MOV operation
ref_67555 = ((ref_67547 >> 8) & 0xFF) # Byte reference - MOV operation
ref_67556 = (ref_67547 & 0xFF) # Byte reference - MOV operation
ref_67557 = ((((((((((ref_67547 >> 56) & 0xFF)) << 8 | ((ref_67547 >> 48) & 0xFF)) << 8 | ((ref_67547 >> 40) & 0xFF)) << 8 | ((ref_67547 >> 32) & 0xFF)) << 8 | ((ref_67547 >> 24) & 0xFF)) << 8 | ((ref_67547 >> 16) & 0xFF)) << 8 | ((ref_67547 >> 8) & 0xFF)) << 8 | (ref_67547 & 0xFF)) # Temporary concatenation reference - MOV operation
ref_67864 = ref_66626 # POP operation
ref_68688 = ((ref_67864 >> 56) & 0xFF) # Byte reference - PUSH operation
ref_68689 = ((ref_67864 >> 48) & 0xFF) # Byte reference - PUSH operation
ref_68690 = ((ref_67864 >> 40) & 0xFF) # Byte reference - PUSH operation
ref_68691 = ((ref_67864 >> 32) & 0xFF) # Byte reference - PUSH operation
ref_68692 = ((ref_67864 >> 24) & 0xFF) # Byte reference - PUSH operation
ref_68693 = ((ref_67864 >> 16) & 0xFF) # Byte reference - PUSH operation
ref_68694 = ((ref_67864 >> 8) & 0xFF) # Byte reference - PUSH operation
ref_68695 = (ref_67864 & 0xFF) # Byte reference - PUSH operation
ref_68696 = ((((((((((ref_67864 >> 56) & 0xFF)) << 8 | ((ref_67864 >> 48) & 0xFF)) << 8 | ((ref_67864 >> 40) & 0xFF)) << 8 | ((ref_67864 >> 32) & 0xFF)) << 8 | ((ref_67864 >> 24) & 0xFF)) << 8 | ((ref_67864 >> 16) & 0xFF)) << 8 | ((ref_67864 >> 8) & 0xFF)) << 8 | (ref_67864 & 0xFF)) # Temporary concatenation reference - PUSH operation
ref_68832 = ref_67864 # POP operation
ref_69131 = ((ref_68832 >> 56) & 0xFF) # Byte reference - PUSH operation
ref_69132 = ((ref_68832 >> 48) & 0xFF) # Byte reference - PUSH operation
ref_69133 = ((ref_68832 >> 40) & 0xFF) # Byte reference - PUSH operation
ref_69134 = ((ref_68832 >> 32) & 0xFF) # Byte reference - PUSH operation
ref_69135 = ((ref_68832 >> 24) & 0xFF) # Byte reference - PUSH operation
ref_69136 = ((ref_68832 >> 16) & 0xFF) # Byte reference - PUSH operation
ref_69137 = ((ref_68832 >> 8) & 0xFF) # Byte reference - PUSH operation
ref_69138 = (ref_68832 & 0xFF) # Byte reference - PUSH operation
ref_69139 = ((((((((((ref_68832 >> 56) & 0xFF)) << 8 | ((ref_68832 >> 48) & 0xFF)) << 8 | ((ref_68832 >> 40) & 0xFF)) << 8 | ((ref_68832 >> 32) & 0xFF)) << 8 | ((ref_68832 >> 24) & 0xFF)) << 8 | ((ref_68832 >> 16) & 0xFF)) << 8 | ((ref_68832 >> 8) & 0xFF)) << 8 | (ref_68832 & 0xFF)) # Temporary concatenation reference - PUSH operation
ref_69358 = ref_68832 # POP operation
ref_72742 = ref_13799 # MOV operation
ref_72744 = ((ref_72742 >> 56) & 0xFF) # Byte reference - MOV operation
ref_72745 = ((ref_72742 >> 48) & 0xFF) # Byte reference - MOV operation
ref_72746 = ((ref_72742 >> 40) & 0xFF) # Byte reference - MOV operation
ref_72747 = ((ref_72742 >> 32) & 0xFF) # Byte reference - MOV operation
ref_72748 = ((ref_72742 >> 24) & 0xFF) # Byte reference - MOV operation
ref_72749 = ((ref_72742 >> 16) & 0xFF) # Byte reference - MOV operation
ref_72750 = ((ref_72742 >> 8) & 0xFF) # Byte reference - MOV operation
ref_72751 = (ref_72742 & 0xFF) # Byte reference - MOV operation
ref_72752 = ((((((((((ref_72742 >> 56) & 0xFF)) << 8 | ((ref_72742 >> 48) & 0xFF)) << 8 | ((ref_72742 >> 40) & 0xFF)) << 8 | ((ref_72742 >> 32) & 0xFF)) << 8 | ((ref_72742 >> 24) & 0xFF)) << 8 | ((ref_72742 >> 16) & 0xFF)) << 8 | ((ref_72742 >> 8) & 0xFF)) << 8 | (ref_72742 & 0xFF)) # Temporary concatenation reference - MOV operation
ref_73540 = ((ref_69358 >> 56) & 0xFF) # Byte reference - PUSH operation
ref_73541 = ((ref_69358 >> 48) & 0xFF) # Byte reference - PUSH operation
ref_73542 = ((ref_69358 >> 40) & 0xFF) # Byte reference - PUSH operation
ref_73543 = ((ref_69358 >> 32) & 0xFF) # Byte reference - PUSH operation
ref_73544 = ((ref_69358 >> 24) & 0xFF) # Byte reference - PUSH operation
ref_73545 = ((ref_69358 >> 16) & 0xFF) # Byte reference - PUSH operation
ref_73546 = ((ref_69358 >> 8) & 0xFF) # Byte reference - PUSH operation
ref_73547 = (ref_69358 & 0xFF) # Byte reference - PUSH operation
ref_73548 = ((((((((((ref_69358 >> 56) & 0xFF)) << 8 | ((ref_69358 >> 48) & 0xFF)) << 8 | ((ref_69358 >> 40) & 0xFF)) << 8 | ((ref_69358 >> 32) & 0xFF)) << 8 | ((ref_69358 >> 24) & 0xFF)) << 8 | ((ref_69358 >> 16) & 0xFF)) << 8 | ((ref_69358 >> 8) & 0xFF)) << 8 | (ref_69358 & 0xFF)) # Temporary concatenation reference - PUSH operation
ref_73651 = ref_72742 # MOV operation
ref_73659 = ref_73651 # MOV operation
ref_73663 = (ref_73659 >> (0x37 & 0x3F)) # SHR operation
ref_73664 = (0x0 if ((0x37 & 0x3F) == 0x0) else ((ref_73659 >> (((0x37 & 0x3F) - 0x1) & 0xFFFFFFFFFFFFFFFF)) & 0x1)) # Carry flag
ref_73665 = (((ref_73659 >> ((0x40 - 0x1) & 0xFFFFFFFFFFFFFFFF)) & 0x1) if ((0x37 & 0x3F) == 0x1) else 0x0) # Overflow flag
ref_73666 = (0x1 if ((0x37 & 0x3F) == 0x0) else ((((((((0x1 ^ (((ref_73663 & 0xFF) >> 0x0) & 0x1)) ^ (((ref_73663 & 0xFF) >> 0x1) & 0x1)) ^ (((ref_73663 & 0xFF) >> 0x2) & 0x1)) ^ (((ref_73663 & 0xFF) >> 0x3) & 0x1)) ^ (((ref_73663 & 0xFF) >> 0x4) & 0x1)) ^ (((ref_73663 & 0xFF) >> 0x5) & 0x1)) ^ (((ref_73663 & 0xFF) >> 0x6) & 0x1)) ^ (((ref_73663 & 0xFF) >> 0x7) & 0x1))) # Parity flag
ref_73667 = (0x0 if ((0x37 & 0x3F) == 0x0) else ((ref_73663 >> 63) & 0x1)) # Sign flag
ref_73668 = (0x0 if ((0x37 & 0x3F) == 0x0) else (0x1 if (ref_73663 == 0x0) else 0x0)) # Zero flag
ref_73670 = ref_73663 # MOV operation
ref_73672 = ((ref_73670 >> 56) & 0xFF) # Byte reference - MOV operation
ref_73673 = ((ref_73670 >> 48) & 0xFF) # Byte reference - MOV operation
ref_73674 = ((ref_73670 >> 40) & 0xFF) # Byte reference - MOV operation
ref_73675 = ((ref_73670 >> 32) & 0xFF) # Byte reference - MOV operation
ref_73676 = ((ref_73670 >> 24) & 0xFF) # Byte reference - MOV operation
ref_73677 = ((ref_73670 >> 16) & 0xFF) # Byte reference - MOV operation
ref_73678 = ((ref_73670 >> 8) & 0xFF) # Byte reference - MOV operation
ref_73679 = (ref_73670 & 0xFF) # Byte reference - MOV operation
ref_73680 = ((((((((((ref_73670 >> 56) & 0xFF)) << 8 | ((ref_73670 >> 48) & 0xFF)) << 8 | ((ref_73670 >> 40) & 0xFF)) << 8 | ((ref_73670 >> 32) & 0xFF)) << 8 | ((ref_73670 >> 24) & 0xFF)) << 8 | ((ref_73670 >> 16) & 0xFF)) << 8 | ((ref_73670 >> 8) & 0xFF)) << 8 | (ref_73670 & 0xFF)) # Temporary concatenation reference - MOV operation
ref_73692 = ref_69358 # POP operation
ref_74146 = ((ref_73692 >> 56) & 0xFF) # Byte reference - PUSH operation
ref_74147 = ((ref_73692 >> 48) & 0xFF) # Byte reference - PUSH operation
ref_74148 = ((ref_73692 >> 40) & 0xFF) # Byte reference - PUSH operation
ref_74149 = ((ref_73692 >> 32) & 0xFF) # Byte reference - PUSH operation
ref_74150 = ((ref_73692 >> 24) & 0xFF) # Byte reference - PUSH operation
ref_74151 = ((ref_73692 >> 16) & 0xFF) # Byte reference - PUSH operation
ref_74152 = ((ref_73692 >> 8) & 0xFF) # Byte reference - PUSH operation
ref_74153 = (ref_73692 & 0xFF) # Byte reference - PUSH operation
ref_74154 = ((((((((((ref_73692 >> 56) & 0xFF)) << 8 | ((ref_73692 >> 48) & 0xFF)) << 8 | ((ref_73692 >> 40) & 0xFF)) << 8 | ((ref_73692 >> 32) & 0xFF)) << 8 | ((ref_73692 >> 24) & 0xFF)) << 8 | ((ref_73692 >> 16) & 0xFF)) << 8 | ((ref_73692 >> 8) & 0xFF)) << 8 | (ref_73692 & 0xFF)) # Temporary concatenation reference - PUSH operation
ref_74381 = ref_73692 # POP operation
ref_74719 = ((ref_74381 >> 56) & 0xFF) # Byte reference - PUSH operation
ref_74720 = ((ref_74381 >> 48) & 0xFF) # Byte reference - PUSH operation
ref_74721 = ((ref_74381 >> 40) & 0xFF) # Byte reference - PUSH operation
ref_74722 = ((ref_74381 >> 32) & 0xFF) # Byte reference - PUSH operation
ref_74723 = ((ref_74381 >> 24) & 0xFF) # Byte reference - PUSH operation
ref_74724 = ((ref_74381 >> 16) & 0xFF) # Byte reference - PUSH operation
ref_74725 = ((ref_74381 >> 8) & 0xFF) # Byte reference - PUSH operation
ref_74726 = (ref_74381 & 0xFF) # Byte reference - PUSH operation
ref_74727 = ((((((((((ref_74381 >> 56) & 0xFF)) << 8 | ((ref_74381 >> 48) & 0xFF)) << 8 | ((ref_74381 >> 40) & 0xFF)) << 8 | ((ref_74381 >> 32) & 0xFF)) << 8 | ((ref_74381 >> 24) & 0xFF)) << 8 | ((ref_74381 >> 16) & 0xFF)) << 8 | ((ref_74381 >> 8) & 0xFF)) << 8 | (ref_74381 & 0xFF)) # Temporary concatenation reference - PUSH operation
ref_74840 = ref_74381 # POP operation
ref_75035 = ref_67547 # MOV operation
ref_75041 = ref_73670 # MOV operation
ref_75043 = ~ref_75041 # NOT operation
ref_75045 = (ref_75035 & ref_75043) # AND operation
ref_75048 = ((((((((0x1 ^ (((ref_75045 & 0xFF) >> 0x0) & 0x1)) ^ (((ref_75045 & 0xFF) >> 0x1) & 0x1)) ^ (((ref_75045 & 0xFF) >> 0x2) & 0x1)) ^ (((ref_75045 & 0xFF) >> 0x3) & 0x1)) ^ (((ref_75045 & 0xFF) >> 0x4) & 0x1)) ^ (((ref_75045 & 0xFF) >> 0x5) & 0x1)) ^ (((ref_75045 & 0xFF) >> 0x6) & 0x1)) ^ (((ref_75045 & 0xFF) >> 0x7) & 0x1)) # Parity flag
ref_75049 = ((ref_75045 >> 63) & 0x1) # Sign flag
ref_75050 = (0x1 if (ref_75045 == 0x0) else 0x0) # Zero flag
ref_75056 = ref_73670 # MOV operation
ref_75058 = ((ref_75056 + ref_75045) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_75059 = (0x1 if (0x10 == (0x10 & (ref_75058 ^ (ref_75056 ^ ref_75045)))) else 0x0) # Adjust flag
ref_75060 = ((((ref_75056 & ref_75045) ^ (((ref_75056 ^ ref_75045) ^ ref_75058) & (ref_75056 ^ ref_75045))) >> 63) & 0x1) # Carry flag
ref_75061 = ((((ref_75056 ^ ~ref_75045) & (ref_75056 ^ ref_75058)) >> 63) & 0x1) # Overflow flag
ref_75062 = ((((((((0x1 ^ (((ref_75058 & 0xFF) >> 0x0) & 0x1)) ^ (((ref_75058 & 0xFF) >> 0x1) & 0x1)) ^ (((ref_75058 & 0xFF) >> 0x2) & 0x1)) ^ (((ref_75058 & 0xFF) >> 0x3) & 0x1)) ^ (((ref_75058 & 0xFF) >> 0x4) & 0x1)) ^ (((ref_75058 & 0xFF) >> 0x5) & 0x1)) ^ (((ref_75058 & 0xFF) >> 0x6) & 0x1)) ^ (((ref_75058 & 0xFF) >> 0x7) & 0x1)) # Parity flag
ref_75063 = ((ref_75058 >> 63) & 0x1) # Sign flag
ref_75064 = (0x1 if (ref_75058 == 0x0) else 0x0) # Zero flag
ref_75066 = ((ref_75058 >> 56) & 0xFF) # Byte reference - MOV operation
ref_75067 = ((ref_75058 >> 48) & 0xFF) # Byte reference - MOV operation
ref_75068 = ((ref_75058 >> 40) & 0xFF) # Byte reference - MOV operation
ref_75069 = ((ref_75058 >> 32) & 0xFF) # Byte reference - MOV operation
ref_75070 = ((ref_75058 >> 24) & 0xFF) # Byte reference - MOV operation
ref_75071 = ((ref_75058 >> 16) & 0xFF) # Byte reference - MOV operation
ref_75072 = ((ref_75058 >> 8) & 0xFF) # Byte reference - MOV operation
ref_75073 = (ref_75058 & 0xFF) # Byte reference - MOV operation
ref_75074 = ((((((((((ref_75058 >> 56) & 0xFF)) << 8 | ((ref_75058 >> 48) & 0xFF)) << 8 | ((ref_75058 >> 40) & 0xFF)) << 8 | ((ref_75058 >> 32) & 0xFF)) << 8 | ((ref_75058 >> 24) & 0xFF)) << 8 | ((ref_75058 >> 16) & 0xFF)) << 8 | ((ref_75058 >> 8) & 0xFF)) << 8 | (ref_75058 & 0xFF)) # Temporary concatenation reference - MOV operation
ref_75538 = ((ref_74840 >> 56) & 0xFF) # Byte reference - PUSH operation
ref_75539 = ((ref_74840 >> 48) & 0xFF) # Byte reference - PUSH operation
ref_75540 = ((ref_74840 >> 40) & 0xFF) # Byte reference - PUSH operation
ref_75541 = ((ref_74840 >> 32) & 0xFF) # Byte reference - PUSH operation
ref_75542 = ((ref_74840 >> 24) & 0xFF) # Byte reference - PUSH operation
ref_75543 = ((ref_74840 >> 16) & 0xFF) # Byte reference - PUSH operation
ref_75544 = ((ref_74840 >> 8) & 0xFF) # Byte reference - PUSH operation
ref_75545 = (ref_74840 & 0xFF) # Byte reference - PUSH operation
ref_75546 = ((((((((((ref_74840 >> 56) & 0xFF)) << 8 | ((ref_74840 >> 48) & 0xFF)) << 8 | ((ref_74840 >> 40) & 0xFF)) << 8 | ((ref_74840 >> 32) & 0xFF)) << 8 | ((ref_74840 >> 24) & 0xFF)) << 8 | ((ref_74840 >> 16) & 0xFF)) << 8 | ((ref_74840 >> 8) & 0xFF)) << 8 | (ref_74840 & 0xFF)) # Temporary concatenation reference - PUSH operation
ref_75659 = ref_74840 # POP operation
ref_76101 = ref_75058 # MOV operation
ref_76103 = (ref_76101 | 0x3B92514D) # OR operation
ref_76106 = ((((((((0x1 ^ (((ref_76103 & 0xFF) >> 0x0) & 0x1)) ^ (((ref_76103 & 0xFF) >> 0x1) & 0x1)) ^ (((ref_76103 & 0xFF) >> 0x2) & 0x1)) ^ (((ref_76103 & 0xFF) >> 0x3) & 0x1)) ^ (((ref_76103 & 0xFF) >> 0x4) & 0x1)) ^ (((ref_76103 & 0xFF) >> 0x5) & 0x1)) ^ (((ref_76103 & 0xFF) >> 0x6) & 0x1)) ^ (((ref_76103 & 0xFF) >> 0x7) & 0x1)) # Parity flag
ref_76107 = ((ref_76103 >> 63) & 0x1) # Sign flag
ref_76108 = (0x1 if (ref_76103 == 0x0) else 0x0) # Zero flag
ref_76110 = ((0x0 + ((ref_76103 + ((ref_76103 * 0x1) & 0xFFFFFFFFFFFFFFFF)) & 0xFFFFFFFFFFFFFFFF)) & 0xFFFFFFFFFFFFFFFF) # LEA operation
ref_76130 = ref_75058 # MOV operation
ref_76132 = (ref_76130 ^ 0x3B92514D) # XOR operation
ref_76135 = ((((((((0x1 ^ (((ref_76132 & 0xFF) >> 0x0) & 0x1)) ^ (((ref_76132 & 0xFF) >> 0x1) & 0x1)) ^ (((ref_76132 & 0xFF) >> 0x2) & 0x1)) ^ (((ref_76132 & 0xFF) >> 0x3) & 0x1)) ^ (((ref_76132 & 0xFF) >> 0x4) & 0x1)) ^ (((ref_76132 & 0xFF) >> 0x5) & 0x1)) ^ (((ref_76132 & 0xFF) >> 0x6) & 0x1)) ^ (((ref_76132 & 0xFF) >> 0x7) & 0x1)) # Parity flag
ref_76136 = ((ref_76132 >> 63) & 0x1) # Sign flag
ref_76137 = (0x1 if (ref_76132 == 0x0) else 0x0) # Zero flag
ref_76139 = ref_76110 # MOV operation
ref_76141 = ((ref_76139 - ref_76132) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_76142 = (0x1 if (0x10 == (0x10 & (ref_76141 ^ (ref_76139 ^ ref_76132)))) else 0x0) # Adjust flag
ref_76143 = ((((ref_76139 ^ (ref_76132 ^ ref_76141)) ^ ((ref_76139 ^ ref_76141) & (ref_76139 ^ ref_76132))) >> 63) & 0x1) # Carry flag
ref_76144 = ((((ref_76139 ^ ref_76132) & (ref_76139 ^ ref_76141)) >> 63) & 0x1) # Overflow flag
ref_76145 = ((((((((0x1 ^ (((ref_76141 & 0xFF) >> 0x0) & 0x1)) ^ (((ref_76141 & 0xFF) >> 0x1) & 0x1)) ^ (((ref_76141 & 0xFF) >> 0x2) & 0x1)) ^ (((ref_76141 & 0xFF) >> 0x3) & 0x1)) ^ (((ref_76141 & 0xFF) >> 0x4) & 0x1)) ^ (((ref_76141 & 0xFF) >> 0x5) & 0x1)) ^ (((ref_76141 & 0xFF) >> 0x6) & 0x1)) ^ (((ref_76141 & 0xFF) >> 0x7) & 0x1)) # Parity flag
ref_76146 = ((ref_76141 >> 63) & 0x1) # Sign flag
ref_76147 = (0x1 if (ref_76141 == 0x0) else 0x0) # Zero flag
ref_76149 = ref_76141 # MOV operation
ref_76151 = ((ref_76149 >> 56) & 0xFF) # Byte reference - MOV operation
ref_76152 = ((ref_76149 >> 48) & 0xFF) # Byte reference - MOV operation
ref_76153 = ((ref_76149 >> 40) & 0xFF) # Byte reference - MOV operation
ref_76154 = ((ref_76149 >> 32) & 0xFF) # Byte reference - MOV operation
ref_76155 = ((ref_76149 >> 24) & 0xFF) # Byte reference - MOV operation
ref_76156 = ((ref_76149 >> 16) & 0xFF) # Byte reference - MOV operation
ref_76157 = ((ref_76149 >> 8) & 0xFF) # Byte reference - MOV operation
ref_76158 = (ref_76149 & 0xFF) # Byte reference - MOV operation
ref_76159 = ((((((((((ref_76149 >> 56) & 0xFF)) << 8 | ((ref_76149 >> 48) & 0xFF)) << 8 | ((ref_76149 >> 40) & 0xFF)) << 8 | ((ref_76149 >> 32) & 0xFF)) << 8 | ((ref_76149 >> 24) & 0xFF)) << 8 | ((ref_76149 >> 16) & 0xFF)) << 8 | ((ref_76149 >> 8) & 0xFF)) << 8 | (ref_76149 & 0xFF)) # Temporary concatenation reference - MOV operation
ref_76596 = ref_62321 # MOV operation
ref_76600 = ref_76149 # MOV operation
ref_76602 = ~ref_76600 # NOT operation
ref_76604 = ref_76596 # MOV operation
ref_76606 = (ref_76604 & ref_76602) # AND operation
ref_76609 = ((((((((0x1 ^ (((ref_76606 & 0xFF) >> 0x0) & 0x1)) ^ (((ref_76606 & 0xFF) >> 0x1) & 0x1)) ^ (((ref_76606 & 0xFF) >> 0x2) & 0x1)) ^ (((ref_76606 & 0xFF) >> 0x3) & 0x1)) ^ (((ref_76606 & 0xFF) >> 0x4) & 0x1)) ^ (((ref_76606 & 0xFF) >> 0x5) & 0x1)) ^ (((ref_76606 & 0xFF) >> 0x6) & 0x1)) ^ (((ref_76606 & 0xFF) >> 0x7) & 0x1)) # Parity flag
ref_76610 = ((ref_76606 >> 63) & 0x1) # Sign flag
ref_76611 = (0x1 if (ref_76606 == 0x0) else 0x0) # Zero flag
ref_76623 = ref_62321 # MOV operation
ref_76627 = ref_76149 # MOV operation
ref_76629 = ~ref_76627 # NOT operation
ref_76631 = (ref_76629 & ref_76623) # AND operation
ref_76634 = ((((((((0x1 ^ (((ref_76631 & 0xFF) >> 0x0) & 0x1)) ^ (((ref_76631 & 0xFF) >> 0x1) & 0x1)) ^ (((ref_76631 & 0xFF) >> 0x2) & 0x1)) ^ (((ref_76631 & 0xFF) >> 0x3) & 0x1)) ^ (((ref_76631 & 0xFF) >> 0x4) & 0x1)) ^ (((ref_76631 & 0xFF) >> 0x5) & 0x1)) ^ (((ref_76631 & 0xFF) >> 0x6) & 0x1)) ^ (((ref_76631 & 0xFF) >> 0x7) & 0x1)) # Parity flag
ref_76635 = ((ref_76631 >> 63) & 0x1) # Sign flag
ref_76636 = (0x1 if (ref_76631 == 0x0) else 0x0) # Zero flag
ref_76638 = ((ref_76606 + ref_76631) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_76639 = (0x1 if (0x10 == (0x10 & (ref_76638 ^ (ref_76606 ^ ref_76631)))) else 0x0) # Adjust flag
ref_76640 = ((((ref_76606 & ref_76631) ^ (((ref_76606 ^ ref_76631) ^ ref_76638) & (ref_76606 ^ ref_76631))) >> 63) & 0x1) # Carry flag
ref_76641 = ((((ref_76606 ^ ~ref_76631) & (ref_76606 ^ ref_76638)) >> 63) & 0x1) # Overflow flag
ref_76642 = ((((((((0x1 ^ (((ref_76638 & 0xFF) >> 0x0) & 0x1)) ^ (((ref_76638 & 0xFF) >> 0x1) & 0x1)) ^ (((ref_76638 & 0xFF) >> 0x2) & 0x1)) ^ (((ref_76638 & 0xFF) >> 0x3) & 0x1)) ^ (((ref_76638 & 0xFF) >> 0x4) & 0x1)) ^ (((ref_76638 & 0xFF) >> 0x5) & 0x1)) ^ (((ref_76638 & 0xFF) >> 0x6) & 0x1)) ^ (((ref_76638 & 0xFF) >> 0x7) & 0x1)) # Parity flag
ref_76643 = ((ref_76638 >> 63) & 0x1) # Sign flag
ref_76644 = (0x1 if (ref_76638 == 0x0) else 0x0) # Zero flag
ref_76656 = ref_62321 # MOV operation
ref_76660 = ref_76149 # MOV operation
ref_76662 = (ref_76660 ^ ref_76656) # XOR operation
ref_76665 = ((((((((0x1 ^ (((ref_76662 & 0xFF) >> 0x0) & 0x1)) ^ (((ref_76662 & 0xFF) >> 0x1) & 0x1)) ^ (((ref_76662 & 0xFF) >> 0x2) & 0x1)) ^ (((ref_76662 & 0xFF) >> 0x3) & 0x1)) ^ (((ref_76662 & 0xFF) >> 0x4) & 0x1)) ^ (((ref_76662 & 0xFF) >> 0x5) & 0x1)) ^ (((ref_76662 & 0xFF) >> 0x6) & 0x1)) ^ (((ref_76662 & 0xFF) >> 0x7) & 0x1)) # Parity flag
ref_76666 = ((ref_76662 >> 63) & 0x1) # Sign flag
ref_76667 = (0x1 if (ref_76662 == 0x0) else 0x0) # Zero flag
ref_76669 = ref_76638 # MOV operation
ref_76671 = ((ref_76669 - ref_76662) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_76672 = (0x1 if (0x10 == (0x10 & (ref_76671 ^ (ref_76669 ^ ref_76662)))) else 0x0) # Adjust flag
ref_76673 = ((((ref_76669 ^ (ref_76662 ^ ref_76671)) ^ ((ref_76669 ^ ref_76671) & (ref_76669 ^ ref_76662))) >> 63) & 0x1) # Carry flag
ref_76674 = ((((ref_76669 ^ ref_76662) & (ref_76669 ^ ref_76671)) >> 63) & 0x1) # Overflow flag
ref_76675 = ((((((((0x1 ^ (((ref_76671 & 0xFF) >> 0x0) & 0x1)) ^ (((ref_76671 & 0xFF) >> 0x1) & 0x1)) ^ (((ref_76671 & 0xFF) >> 0x2) & 0x1)) ^ (((ref_76671 & 0xFF) >> 0x3) & 0x1)) ^ (((ref_76671 & 0xFF) >> 0x4) & 0x1)) ^ (((ref_76671 & 0xFF) >> 0x5) & 0x1)) ^ (((ref_76671 & 0xFF) >> 0x6) & 0x1)) ^ (((ref_76671 & 0xFF) >> 0x7) & 0x1)) # Parity flag
ref_76676 = ((ref_76671 >> 63) & 0x1) # Sign flag
ref_76677 = (0x1 if (ref_76671 == 0x0) else 0x0) # Zero flag
ref_76679 = ref_76671 # MOV operation
ref_76681 = ((ref_76679 >> 56) & 0xFF) # Byte reference - MOV operation
ref_76682 = ((ref_76679 >> 48) & 0xFF) # Byte reference - MOV operation
ref_76683 = ((ref_76679 >> 40) & 0xFF) # Byte reference - MOV operation
ref_76684 = ((ref_76679 >> 32) & 0xFF) # Byte reference - MOV operation
ref_76685 = ((ref_76679 >> 24) & 0xFF) # Byte reference - MOV operation
ref_76686 = ((ref_76679 >> 16) & 0xFF) # Byte reference - MOV operation
ref_76687 = ((ref_76679 >> 8) & 0xFF) # Byte reference - MOV operation
ref_76688 = (ref_76679 & 0xFF) # Byte reference - MOV operation
ref_76689 = ((((((((((ref_76679 >> 56) & 0xFF)) << 8 | ((ref_76679 >> 48) & 0xFF)) << 8 | ((ref_76679 >> 40) & 0xFF)) << 8 | ((ref_76679 >> 32) & 0xFF)) << 8 | ((ref_76679 >> 24) & 0xFF)) << 8 | ((ref_76679 >> 16) & 0xFF)) << 8 | ((ref_76679 >> 8) & 0xFF)) << 8 | (ref_76679 & 0xFF)) # Temporary concatenation reference - MOV operation
ref_77276 = ref_76679 # MOV operation
ref_77278 = ((ref_77276 >> 56) & 0xFF) # Byte reference - MOV operation
ref_77279 = ((ref_77276 >> 48) & 0xFF) # Byte reference - MOV operation
ref_77280 = ((ref_77276 >> 40) & 0xFF) # Byte reference - MOV operation
ref_77281 = ((ref_77276 >> 32) & 0xFF) # Byte reference - MOV operation
ref_77282 = ((ref_77276 >> 24) & 0xFF) # Byte reference - MOV operation
ref_77283 = ((ref_77276 >> 16) & 0xFF) # Byte reference - MOV operation
ref_77284 = ((ref_77276 >> 8) & 0xFF) # Byte reference - MOV operation
ref_77285 = (ref_77276 & 0xFF) # Byte reference - MOV operation
ref_77286 = ((((((((((ref_77276 >> 56) & 0xFF)) << 8 | ((ref_77276 >> 48) & 0xFF)) << 8 | ((ref_77276 >> 40) & 0xFF)) << 8 | ((ref_77276 >> 32) & 0xFF)) << 8 | ((ref_77276 >> 24) & 0xFF)) << 8 | ((ref_77276 >> 16) & 0xFF)) << 8 | ((ref_77276 >> 8) & 0xFF)) << 8 | (ref_77276 & 0xFF)) # Temporary concatenation reference - MOV operation
ref_90047 = (((ref_51291 & 0xFF)) << 8 | (ref_51292 & 0xFF)) # MOVZX operation
ref_90049 = (((ref_90047 & 0xFFFF) >> 8) & 0xFF) # Byte reference - MOV operation
ref_90050 = ((ref_90047 & 0xFFFF) & 0xFF) # Byte reference - MOV operation
ref_90051 = (((((ref_90047 & 0xFFFF) >> 8) & 0xFF)) << 8 | ((ref_90047 & 0xFFFF) & 0xFF)) # Temporary concatenation reference - MOV operation
ref_90448 = (ref_90047 & 0xFFFF) # MOVZX operation
ref_90450 = (((ref_90448 & 0xFFFF) >> 8) & 0xFF) # Byte reference - MOV operation
ref_90451 = ((ref_90448 & 0xFFFF) & 0xFF) # Byte reference - MOV operation
ref_90452 = (((((ref_90448 & 0xFFFF) >> 8) & 0xFF)) << 8 | ((ref_90448 & 0xFFFF) & 0xFF)) # Temporary concatenation reference - MOV operation
ref_108613 = (((ref_51289 & 0xFF)) << 8 | (ref_51290 & 0xFF)) # MOVZX operation
ref_108615 = (((ref_108613 & 0xFFFF) >> 8) & 0xFF) # Byte reference - MOV operation
ref_108616 = ((ref_108613 & 0xFFFF) & 0xFF) # Byte reference - MOV operation
ref_108617 = (((((ref_108613 & 0xFFFF) >> 8) & 0xFF)) << 8 | ((ref_108613 & 0xFFFF) & 0xFF)) # Temporary concatenation reference - MOV operation
ref_109014 = (ref_108613 & 0xFFFF) # MOVZX operation
ref_109016 = (((ref_109014 & 0xFFFF) >> 8) & 0xFF) # Byte reference - MOV operation
ref_109017 = ((ref_109014 & 0xFFFF) & 0xFF) # Byte reference - MOV operation
ref_109018 = (((((ref_109014 & 0xFFFF) >> 8) & 0xFF)) << 8 | ((ref_109014 & 0xFFFF) & 0xFF)) # Temporary concatenation reference - MOV operation
ref_117511 = (ref_90448 & 0xFFFF) # MOVZX operation
ref_117513 = (((ref_117511 & 0xFFFF) >> 8) & 0xFF) # Byte reference - MOV operation
ref_117514 = ((ref_117511 & 0xFFFF) & 0xFF) # Byte reference - MOV operation
ref_117515 = (((((ref_117511 & 0xFFFF) >> 8) & 0xFF)) << 8 | ((ref_117511 & 0xFFFF) & 0xFF)) # Temporary concatenation reference - MOV operation
ref_117912 = (ref_117511 & 0xFFFF) # MOVZX operation
ref_117914 = (((ref_117912 & 0xFFFF) >> 8) & 0xFF) # Byte reference - MOV operation
ref_117915 = ((ref_117912 & 0xFFFF) & 0xFF) # Byte reference - MOV operation
ref_117916 = (((((ref_117912 & 0xFFFF) >> 8) & 0xFF)) << 8 | ((ref_117912 & 0xFFFF) & 0xFF)) # Temporary concatenation reference - MOV operation
ref_122459 = ref_33722 # MOV operation
ref_122461 = ((ref_122459 >> 56) & 0xFF) # Byte reference - MOV operation
ref_122462 = ((ref_122459 >> 48) & 0xFF) # Byte reference - MOV operation
ref_122463 = ((ref_122459 >> 40) & 0xFF) # Byte reference - MOV operation
ref_122464 = ((ref_122459 >> 32) & 0xFF) # Byte reference - MOV operation
ref_122465 = ((ref_122459 >> 24) & 0xFF) # Byte reference - MOV operation
ref_122466 = ((ref_122459 >> 16) & 0xFF) # Byte reference - MOV operation
ref_122467 = ((ref_122459 >> 8) & 0xFF) # Byte reference - MOV operation
ref_122468 = (ref_122459 & 0xFF) # Byte reference - MOV operation
ref_122469 = ((((((((((ref_122459 >> 56) & 0xFF)) << 8 | ((ref_122459 >> 48) & 0xFF)) << 8 | ((ref_122459 >> 40) & 0xFF)) << 8 | ((ref_122459 >> 32) & 0xFF)) << 8 | ((ref_122459 >> 24) & 0xFF)) << 8 | ((ref_122459 >> 16) & 0xFF)) << 8 | ((ref_122459 >> 8) & 0xFF)) << 8 | (ref_122459 & 0xFF)) # Temporary concatenation reference - MOV operation
ref_126198 = ref_33722 # MOV operation
ref_126200 = ((ref_126198 >> 56) & 0xFF) # Byte reference - MOV operation
ref_126201 = ((ref_126198 >> 48) & 0xFF) # Byte reference - MOV operation
ref_126202 = ((ref_126198 >> 40) & 0xFF) # Byte reference - MOV operation
ref_126203 = ((ref_126198 >> 32) & 0xFF) # Byte reference - MOV operation
ref_126204 = ((ref_126198 >> 24) & 0xFF) # Byte reference - MOV operation
ref_126205 = ((ref_126198 >> 16) & 0xFF) # Byte reference - MOV operation
ref_126206 = ((ref_126198 >> 8) & 0xFF) # Byte reference - MOV operation
ref_126207 = (ref_126198 & 0xFF) # Byte reference - MOV operation
ref_126208 = ((((((((((ref_126198 >> 56) & 0xFF)) << 8 | ((ref_126198 >> 48) & 0xFF)) << 8 | ((ref_126198 >> 40) & 0xFF)) << 8 | ((ref_126198 >> 32) & 0xFF)) << 8 | ((ref_126198 >> 24) & 0xFF)) << 8 | ((ref_126198 >> 16) & 0xFF)) << 8 | ((ref_126198 >> 8) & 0xFF)) << 8 | (ref_126198 & 0xFF)) # Temporary concatenation reference - MOV operation
ref_127089 = ref_126198 # MOV operation
ref_127103 = ref_122459 # MOV operation
ref_127105 = (ref_127103 | ref_127089) # OR operation
ref_127108 = ((((((((0x1 ^ (((ref_127105 & 0xFF) >> 0x0) & 0x1)) ^ (((ref_127105 & 0xFF) >> 0x1) & 0x1)) ^ (((ref_127105 & 0xFF) >> 0x2) & 0x1)) ^ (((ref_127105 & 0xFF) >> 0x3) & 0x1)) ^ (((ref_127105 & 0xFF) >> 0x4) & 0x1)) ^ (((ref_127105 & 0xFF) >> 0x5) & 0x1)) ^ (((ref_127105 & 0xFF) >> 0x6) & 0x1)) ^ (((ref_127105 & 0xFF) >> 0x7) & 0x1)) # Parity flag
ref_127109 = ((ref_127105 >> 63) & 0x1) # Sign flag
ref_127110 = (0x1 if (ref_127105 == 0x0) else 0x0) # Zero flag
ref_127112 = ((0x0 + ((ref_127105 + ((ref_127105 * 0x1) & 0xFFFFFFFFFFFFFFFF)) & 0xFFFFFFFFFFFFFFFF)) & 0xFFFFFFFFFFFFFFFF) # LEA operation
ref_127118 = ref_126198 # MOV operation
ref_127132 = ref_122459 # MOV operation
ref_127134 = (ref_127132 ^ ref_127118) # XOR operation
ref_127137 = ((((((((0x1 ^ (((ref_127134 & 0xFF) >> 0x0) & 0x1)) ^ (((ref_127134 & 0xFF) >> 0x1) & 0x1)) ^ (((ref_127134 & 0xFF) >> 0x2) & 0x1)) ^ (((ref_127134 & 0xFF) >> 0x3) & 0x1)) ^ (((ref_127134 & 0xFF) >> 0x4) & 0x1)) ^ (((ref_127134 & 0xFF) >> 0x5) & 0x1)) ^ (((ref_127134 & 0xFF) >> 0x6) & 0x1)) ^ (((ref_127134 & 0xFF) >> 0x7) & 0x1)) # Parity flag
ref_127138 = ((ref_127134 >> 63) & 0x1) # Sign flag
ref_127139 = (0x1 if (ref_127134 == 0x0) else 0x0) # Zero flag
ref_127141 = ref_127112 # MOV operation
ref_127143 = ((ref_127141 - ref_127134) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_127144 = (0x1 if (0x10 == (0x10 & (ref_127143 ^ (ref_127141 ^ ref_127134)))) else 0x0) # Adjust flag
ref_127145 = ((((ref_127141 ^ (ref_127134 ^ ref_127143)) ^ ((ref_127141 ^ ref_127143) & (ref_127141 ^ ref_127134))) >> 63) & 0x1) # Carry flag
ref_127146 = ((((ref_127141 ^ ref_127134) & (ref_127141 ^ ref_127143)) >> 63) & 0x1) # Overflow flag
ref_127147 = ((((((((0x1 ^ (((ref_127143 & 0xFF) >> 0x0) & 0x1)) ^ (((ref_127143 & 0xFF) >> 0x1) & 0x1)) ^ (((ref_127143 & 0xFF) >> 0x2) & 0x1)) ^ (((ref_127143 & 0xFF) >> 0x3) & 0x1)) ^ (((ref_127143 & 0xFF) >> 0x4) & 0x1)) ^ (((ref_127143 & 0xFF) >> 0x5) & 0x1)) ^ (((ref_127143 & 0xFF) >> 0x6) & 0x1)) ^ (((ref_127143 & 0xFF) >> 0x7) & 0x1)) # Parity flag
ref_127148 = ((ref_127143 >> 63) & 0x1) # Sign flag
ref_127149 = (0x1 if (ref_127143 == 0x0) else 0x0) # Zero flag
ref_127151 = ref_127143 # MOV operation
ref_127153 = ((ref_127151 >> 56) & 0xFF) # Byte reference - MOV operation
ref_127154 = ((ref_127151 >> 48) & 0xFF) # Byte reference - MOV operation
ref_127155 = ((ref_127151 >> 40) & 0xFF) # Byte reference - MOV operation
ref_127156 = ((ref_127151 >> 32) & 0xFF) # Byte reference - MOV operation
ref_127157 = ((ref_127151 >> 24) & 0xFF) # Byte reference - MOV operation
ref_127158 = ((ref_127151 >> 16) & 0xFF) # Byte reference - MOV operation
ref_127159 = ((ref_127151 >> 8) & 0xFF) # Byte reference - MOV operation
ref_127160 = (ref_127151 & 0xFF) # Byte reference - MOV operation
ref_127161 = ((((((((((ref_127151 >> 56) & 0xFF)) << 8 | ((ref_127151 >> 48) & 0xFF)) << 8 | ((ref_127151 >> 40) & 0xFF)) << 8 | ((ref_127151 >> 32) & 0xFF)) << 8 | ((ref_127151 >> 24) & 0xFF)) << 8 | ((ref_127151 >> 16) & 0xFF)) << 8 | ((ref_127151 >> 8) & 0xFF)) << 8 | (ref_127151 & 0xFF)) # Temporary concatenation reference - MOV operation
ref_134265 = ref_127151 # MOV operation
ref_134267 = ((ref_134265 >> 56) & 0xFF) # Byte reference - MOV operation
ref_134268 = ((ref_134265 >> 48) & 0xFF) # Byte reference - MOV operation
ref_134269 = ((ref_134265 >> 40) & 0xFF) # Byte reference - MOV operation
ref_134270 = ((ref_134265 >> 32) & 0xFF) # Byte reference - MOV operation
ref_134271 = ((ref_134265 >> 24) & 0xFF) # Byte reference - MOV operation
ref_134272 = ((ref_134265 >> 16) & 0xFF) # Byte reference - MOV operation
ref_134273 = ((ref_134265 >> 8) & 0xFF) # Byte reference - MOV operation
ref_134274 = (ref_134265 & 0xFF) # Byte reference - MOV operation
ref_134275 = ((((((((((ref_134265 >> 56) & 0xFF)) << 8 | ((ref_134265 >> 48) & 0xFF)) << 8 | ((ref_134265 >> 40) & 0xFF)) << 8 | ((ref_134265 >> 32) & 0xFF)) << 8 | ((ref_134265 >> 24) & 0xFF)) << 8 | ((ref_134265 >> 16) & 0xFF)) << 8 | ((ref_134265 >> 8) & 0xFF)) << 8 | (ref_134265 & 0xFF)) # Temporary concatenation reference - MOV operation
ref_147241 = (ref_77284 & 0xFF) # MOVZX operation
ref_147243 = ((ref_147241 & 0xFF) & 0xFF) # Byte reference - MOV operation
ref_148420 = (ref_147241 & 0xFF) # MOVZX operation
ref_148422 = ((ref_148420 & 0xFF) & 0xFF) # Byte reference - MOV operation
ref_157416 = (ref_77285 & 0xFF) # MOVZX operation
ref_157418 = ((ref_157416 & 0xFF) & 0xFF) # Byte reference - MOV operation
ref_164722 = (ref_157416 & 0xFF) # MOVZX operation
ref_164724 = ((ref_164722 & 0xFF) & 0xFF) # Byte reference - MOV operation
ref_165499 = (ref_148420 & 0xFF) # MOVZX operation
ref_165501 = ((ref_165499 & 0xFF) & 0xFF) # Byte reference - MOV operation
ref_173851 = (ref_165499 & 0xFF) # MOVZX operation
ref_173853 = ((ref_173851 & 0xFF) & 0xFF) # Byte reference - MOV operation
ref_182675 = ref_13799 # MOV operation
ref_182677 = ((ref_182675 >> 56) & 0xFF) # Byte reference - MOV operation
ref_182678 = ((ref_182675 >> 48) & 0xFF) # Byte reference - MOV operation
ref_182679 = ((ref_182675 >> 40) & 0xFF) # Byte reference - MOV operation
ref_182680 = ((ref_182675 >> 32) & 0xFF) # Byte reference - MOV operation
ref_182681 = ((ref_182675 >> 24) & 0xFF) # Byte reference - MOV operation
ref_182682 = ((ref_182675 >> 16) & 0xFF) # Byte reference - MOV operation
ref_182683 = ((ref_182675 >> 8) & 0xFF) # Byte reference - MOV operation
ref_182684 = (ref_182675 & 0xFF) # Byte reference - MOV operation
ref_182685 = ((((((((((ref_182675 >> 56) & 0xFF)) << 8 | ((ref_182675 >> 48) & 0xFF)) << 8 | ((ref_182675 >> 40) & 0xFF)) << 8 | ((ref_182675 >> 32) & 0xFF)) << 8 | ((ref_182675 >> 24) & 0xFF)) << 8 | ((ref_182675 >> 16) & 0xFF)) << 8 | ((ref_182675 >> 8) & 0xFF)) << 8 | (ref_182675 & 0xFF)) # Temporary concatenation reference - MOV operation
ref_187393 = ref_33722 # MOV operation
ref_187395 = ((ref_187393 >> 56) & 0xFF) # Byte reference - MOV operation
ref_187396 = ((ref_187393 >> 48) & 0xFF) # Byte reference - MOV operation
ref_187397 = ((ref_187393 >> 40) & 0xFF) # Byte reference - MOV operation
ref_187398 = ((ref_187393 >> 32) & 0xFF) # Byte reference - MOV operation
ref_187399 = ((ref_187393 >> 24) & 0xFF) # Byte reference - MOV operation
ref_187400 = ((ref_187393 >> 16) & 0xFF) # Byte reference - MOV operation
ref_187401 = ((ref_187393 >> 8) & 0xFF) # Byte reference - MOV operation
ref_187402 = (ref_187393 & 0xFF) # Byte reference - MOV operation
ref_187403 = ((((((((((ref_187393 >> 56) & 0xFF)) << 8 | ((ref_187393 >> 48) & 0xFF)) << 8 | ((ref_187393 >> 40) & 0xFF)) << 8 | ((ref_187393 >> 32) & 0xFF)) << 8 | ((ref_187393 >> 24) & 0xFF)) << 8 | ((ref_187393 >> 16) & 0xFF)) << 8 | ((ref_187393 >> 8) & 0xFF)) << 8 | (ref_187393 & 0xFF)) # Temporary concatenation reference - MOV operation
ref_188302 = ref_187393 # MOV operation
ref_188310 = ref_188302 # MOV operation
ref_188314 = (ref_188310 >> (0x2 & 0x3F)) # SHR operation
ref_188315 = (0x0 if ((0x2 & 0x3F) == 0x0) else ((ref_188310 >> (((0x2 & 0x3F) - 0x1) & 0xFFFFFFFFFFFFFFFF)) & 0x1)) # Carry flag
ref_188316 = (((ref_188310 >> ((0x40 - 0x1) & 0xFFFFFFFFFFFFFFFF)) & 0x1) if ((0x2 & 0x3F) == 0x1) else 0x0) # Overflow flag
ref_188317 = (0x1 if ((0x2 & 0x3F) == 0x0) else ((((((((0x1 ^ (((ref_188314 & 0xFF) >> 0x0) & 0x1)) ^ (((ref_188314 & 0xFF) >> 0x1) & 0x1)) ^ (((ref_188314 & 0xFF) >> 0x2) & 0x1)) ^ (((ref_188314 & 0xFF) >> 0x3) & 0x1)) ^ (((ref_188314 & 0xFF) >> 0x4) & 0x1)) ^ (((ref_188314 & 0xFF) >> 0x5) & 0x1)) ^ (((ref_188314 & 0xFF) >> 0x6) & 0x1)) ^ (((ref_188314 & 0xFF) >> 0x7) & 0x1))) # Parity flag
ref_188318 = (0x0 if ((0x2 & 0x3F) == 0x0) else ((ref_188314 >> 63) & 0x1)) # Sign flag
ref_188319 = (0x0 if ((0x2 & 0x3F) == 0x0) else (0x1 if (ref_188314 == 0x0) else 0x0)) # Zero flag
ref_188321 = ref_188314 # MOV operation
ref_188323 = ((ref_188321 >> 56) & 0xFF) # Byte reference - MOV operation
ref_188324 = ((ref_188321 >> 48) & 0xFF) # Byte reference - MOV operation
ref_188325 = ((ref_188321 >> 40) & 0xFF) # Byte reference - MOV operation
ref_188326 = ((ref_188321 >> 32) & 0xFF) # Byte reference - MOV operation
ref_188327 = ((ref_188321 >> 24) & 0xFF) # Byte reference - MOV operation
ref_188328 = ((ref_188321 >> 16) & 0xFF) # Byte reference - MOV operation
ref_188329 = ((ref_188321 >> 8) & 0xFF) # Byte reference - MOV operation
ref_188330 = (ref_188321 & 0xFF) # Byte reference - MOV operation
ref_188331 = ((((((((((ref_188321 >> 56) & 0xFF)) << 8 | ((ref_188321 >> 48) & 0xFF)) << 8 | ((ref_188321 >> 40) & 0xFF)) << 8 | ((ref_188321 >> 32) & 0xFF)) << 8 | ((ref_188321 >> 24) & 0xFF)) << 8 | ((ref_188321 >> 16) & 0xFF)) << 8 | ((ref_188321 >> 8) & 0xFF)) << 8 | (ref_188321 & 0xFF)) # Temporary concatenation reference - MOV operation
ref_189214 = ref_188321 # MOV operation
ref_189216 = ref_189214 # MOV operation
ref_189218 = ~ref_189216 # NOT operation
ref_189224 = (ref_189218 | 0x7) # OR operation
ref_189227 = ((((((((0x1 ^ (((ref_189224 & 0xFF) >> 0x0) & 0x1)) ^ (((ref_189224 & 0xFF) >> 0x1) & 0x1)) ^ (((ref_189224 & 0xFF) >> 0x2) & 0x1)) ^ (((ref_189224 & 0xFF) >> 0x3) & 0x1)) ^ (((ref_189224 & 0xFF) >> 0x4) & 0x1)) ^ (((ref_189224 & 0xFF) >> 0x5) & 0x1)) ^ (((ref_189224 & 0xFF) >> 0x6) & 0x1)) ^ (((ref_189224 & 0xFF) >> 0x7) & 0x1)) # Parity flag
ref_189228 = ((ref_189224 >> 63) & 0x1) # Sign flag
ref_189229 = (0x1 if (ref_189224 == 0x0) else 0x0) # Zero flag
ref_189241 = ref_188321 # MOV operation
ref_189243 = ((ref_189241 + ref_189224) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_189244 = (0x1 if (0x10 == (0x10 & (ref_189243 ^ (ref_189241 ^ ref_189224)))) else 0x0) # Adjust flag
ref_189245 = ((((ref_189241 & ref_189224) ^ (((ref_189241 ^ ref_189224) ^ ref_189243) & (ref_189241 ^ ref_189224))) >> 63) & 0x1) # Carry flag
ref_189246 = ((((ref_189241 ^ ~ref_189224) & (ref_189241 ^ ref_189243)) >> 63) & 0x1) # Overflow flag
ref_189247 = ((((((((0x1 ^ (((ref_189243 & 0xFF) >> 0x0) & 0x1)) ^ (((ref_189243 & 0xFF) >> 0x1) & 0x1)) ^ (((ref_189243 & 0xFF) >> 0x2) & 0x1)) ^ (((ref_189243 & 0xFF) >> 0x3) & 0x1)) ^ (((ref_189243 & 0xFF) >> 0x4) & 0x1)) ^ (((ref_189243 & 0xFF) >> 0x5) & 0x1)) ^ (((ref_189243 & 0xFF) >> 0x6) & 0x1)) ^ (((ref_189243 & 0xFF) >> 0x7) & 0x1)) # Parity flag
ref_189248 = ((ref_189243 >> 63) & 0x1) # Sign flag
ref_189249 = (0x1 if (ref_189243 == 0x0) else 0x0) # Zero flag
ref_189251 = ((ref_189243 + 0x1) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_189252 = (0x1 if (0x10 == (0x10 & (ref_189251 ^ (ref_189243 ^ 0x1)))) else 0x0) # Adjust flag
ref_189253 = ((((ref_189243 & 0x1) ^ (((ref_189243 ^ 0x1) ^ ref_189251) & (ref_189243 ^ 0x1))) >> 63) & 0x1) # Carry flag
ref_189254 = ((((ref_189243 ^ ~0x1) & (ref_189243 ^ ref_189251)) >> 63) & 0x1) # Overflow flag
ref_189255 = ((((((((0x1 ^ (((ref_189251 & 0xFF) >> 0x0) & 0x1)) ^ (((ref_189251 & 0xFF) >> 0x1) & 0x1)) ^ (((ref_189251 & 0xFF) >> 0x2) & 0x1)) ^ (((ref_189251 & 0xFF) >> 0x3) & 0x1)) ^ (((ref_189251 & 0xFF) >> 0x4) & 0x1)) ^ (((ref_189251 & 0xFF) >> 0x5) & 0x1)) ^ (((ref_189251 & 0xFF) >> 0x6) & 0x1)) ^ (((ref_189251 & 0xFF) >> 0x7) & 0x1)) # Parity flag
ref_189256 = ((ref_189251 >> 63) & 0x1) # Sign flag
ref_189257 = (0x1 if (ref_189251 == 0x0) else 0x0) # Zero flag
ref_189259 = ((ref_189251 >> 56) & 0xFF) # Byte reference - MOV operation
ref_189260 = ((ref_189251 >> 48) & 0xFF) # Byte reference - MOV operation
ref_189261 = ((ref_189251 >> 40) & 0xFF) # Byte reference - MOV operation
ref_189262 = ((ref_189251 >> 32) & 0xFF) # Byte reference - MOV operation
ref_189263 = ((ref_189251 >> 24) & 0xFF) # Byte reference - MOV operation
ref_189264 = ((ref_189251 >> 16) & 0xFF) # Byte reference - MOV operation
ref_189265 = ((ref_189251 >> 8) & 0xFF) # Byte reference - MOV operation
ref_189266 = (ref_189251 & 0xFF) # Byte reference - MOV operation
ref_189267 = ((((((((((ref_189251 >> 56) & 0xFF)) << 8 | ((ref_189251 >> 48) & 0xFF)) << 8 | ((ref_189251 >> 40) & 0xFF)) << 8 | ((ref_189251 >> 32) & 0xFF)) << 8 | ((ref_189251 >> 24) & 0xFF)) << 8 | ((ref_189251 >> 16) & 0xFF)) << 8 | ((ref_189251 >> 8) & 0xFF)) << 8 | (ref_189251 & 0xFF)) # Temporary concatenation reference - MOV operation
ref_189518 = ref_189251 # MOV operation
ref_189534 = (0xFFFFFFFFFFFFFFFE & ref_189518) # AND operation
ref_189537 = ((((((((0x1 ^ (((ref_189534 & 0xFF) >> 0x0) & 0x1)) ^ (((ref_189534 & 0xFF) >> 0x1) & 0x1)) ^ (((ref_189534 & 0xFF) >> 0x2) & 0x1)) ^ (((ref_189534 & 0xFF) >> 0x3) & 0x1)) ^ (((ref_189534 & 0xFF) >> 0x4) & 0x1)) ^ (((ref_189534 & 0xFF) >> 0x5) & 0x1)) ^ (((ref_189534 & 0xFF) >> 0x6) & 0x1)) ^ (((ref_189534 & 0xFF) >> 0x7) & 0x1)) # Parity flag
ref_189538 = ((ref_189534 >> 63) & 0x1) # Sign flag
ref_189539 = (0x1 if (ref_189534 == 0x0) else 0x0) # Zero flag
ref_189553 = ((0x1 + ref_189534) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_189554 = (0x1 if (0x10 == (0x10 & (ref_189553 ^ (0x1 ^ ref_189534)))) else 0x0) # Adjust flag
ref_189555 = ((((0x1 & ref_189534) ^ (((0x1 ^ ref_189534) ^ ref_189553) & (0x1 ^ ref_189534))) >> 63) & 0x1) # Carry flag
ref_189556 = ((((0x1 ^ ~ref_189534) & (0x1 ^ ref_189553)) >> 63) & 0x1) # Overflow flag
ref_189557 = ((((((((0x1 ^ (((ref_189553 & 0xFF) >> 0x0) & 0x1)) ^ (((ref_189553 & 0xFF) >> 0x1) & 0x1)) ^ (((ref_189553 & 0xFF) >> 0x2) & 0x1)) ^ (((ref_189553 & 0xFF) >> 0x3) & 0x1)) ^ (((ref_189553 & 0xFF) >> 0x4) & 0x1)) ^ (((ref_189553 & 0xFF) >> 0x5) & 0x1)) ^ (((ref_189553 & 0xFF) >> 0x6) & 0x1)) ^ (((ref_189553 & 0xFF) >> 0x7) & 0x1)) # Parity flag
ref_189558 = ((ref_189553 >> 63) & 0x1) # Sign flag
ref_189559 = (0x1 if (ref_189553 == 0x0) else 0x0) # Zero flag
ref_189561 = ((ref_189553 >> 56) & 0xFF) # Byte reference - MOV operation
ref_189562 = ((ref_189553 >> 48) & 0xFF) # Byte reference - MOV operation
ref_189563 = ((ref_189553 >> 40) & 0xFF) # Byte reference - MOV operation
ref_189564 = ((ref_189553 >> 32) & 0xFF) # Byte reference - MOV operation
ref_189565 = ((ref_189553 >> 24) & 0xFF) # Byte reference - MOV operation
ref_189566 = ((ref_189553 >> 16) & 0xFF) # Byte reference - MOV operation
ref_189567 = ((ref_189553 >> 8) & 0xFF) # Byte reference - MOV operation
ref_189568 = (ref_189553 & 0xFF) # Byte reference - MOV operation
ref_189569 = ((((((((((ref_189553 >> 56) & 0xFF)) << 8 | ((ref_189553 >> 48) & 0xFF)) << 8 | ((ref_189553 >> 40) & 0xFF)) << 8 | ((ref_189553 >> 32) & 0xFF)) << 8 | ((ref_189553 >> 24) & 0xFF)) << 8 | ((ref_189553 >> 16) & 0xFF)) << 8 | ((ref_189553 >> 8) & 0xFF)) << 8 | (ref_189553 & 0xFF)) # Temporary concatenation reference - MOV operation
ref_190196 = ref_182675 # MOV operation
ref_190202 = ref_189553 # MOV operation
ref_190204 = ref_190196 # MOV operation
ref_190206 = (ref_190202 & 0xFFFFFFFF) # MOV operation
ref_190208 = ((ref_190204 << ((ref_190206 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_190209 = (0x0 if (((ref_190206 & 0xFF) & 0x3F) == 0x0) else ((ref_190204 >> ((0x40 - ((ref_190206 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF)) & 0x1)) # Carry flag
ref_190210 = ((((ref_190204 >> ((0x40 - 0x1) & 0xFFFFFFFFFFFFFFFF)) ^ (ref_190204 >> ((0x40 - 0x2) & 0xFFFFFFFFFFFFFFFF))) & 0x1) if (((ref_190206 & 0xFF) & 0x3F) == 0x1) else 0x0) # Overflow flag
ref_190211 = (0x0 if (((ref_190206 & 0xFF) & 0x3F) == 0x0) else ((((((((0x1 ^ (((ref_190208 & 0xFF) >> 0x0) & 0x1)) ^ (((ref_190208 & 0xFF) >> 0x1) & 0x1)) ^ (((ref_190208 & 0xFF) >> 0x2) & 0x1)) ^ (((ref_190208 & 0xFF) >> 0x3) & 0x1)) ^ (((ref_190208 & 0xFF) >> 0x4) & 0x1)) ^ (((ref_190208 & 0xFF) >> 0x5) & 0x1)) ^ (((ref_190208 & 0xFF) >> 0x6) & 0x1)) ^ (((ref_190208 & 0xFF) >> 0x7) & 0x1))) # Parity flag
ref_190212 = (0x0 if (((ref_190206 & 0xFF) & 0x3F) == 0x0) else ((ref_190208 >> 63) & 0x1)) # Sign flag
ref_190213 = (0x0 if (((ref_190206 & 0xFF) & 0x3F) == 0x0) else (0x1 if (ref_190208 == 0x0) else 0x0)) # Zero flag
ref_190215 = ref_190208 # MOV operation
ref_190217 = ((ref_190215 >> 56) & 0xFF) # Byte reference - MOV operation
ref_190218 = ((ref_190215 >> 48) & 0xFF) # Byte reference - MOV operation
ref_190219 = ((ref_190215 >> 40) & 0xFF) # Byte reference - MOV operation
ref_190220 = ((ref_190215 >> 32) & 0xFF) # Byte reference - MOV operation
ref_190221 = ((ref_190215 >> 24) & 0xFF) # Byte reference - MOV operation
ref_190222 = ((ref_190215 >> 16) & 0xFF) # Byte reference - MOV operation
ref_190223 = ((ref_190215 >> 8) & 0xFF) # Byte reference - MOV operation
ref_190224 = (ref_190215 & 0xFF) # Byte reference - MOV operation
ref_190225 = ((((((((((ref_190215 >> 56) & 0xFF)) << 8 | ((ref_190215 >> 48) & 0xFF)) << 8 | ((ref_190215 >> 40) & 0xFF)) << 8 | ((ref_190215 >> 32) & 0xFF)) << 8 | ((ref_190215 >> 24) & 0xFF)) << 8 | ((ref_190215 >> 16) & 0xFF)) << 8 | ((ref_190215 >> 8) & 0xFF)) << 8 | (ref_190215 & 0xFF)) # Temporary concatenation reference - MOV operation
ref_195410 = ref_134265 # MOV operation
ref_195412 = ((ref_195410 >> 56) & 0xFF) # Byte reference - MOV operation
ref_195413 = ((ref_195410 >> 48) & 0xFF) # Byte reference - MOV operation
ref_195414 = ((ref_195410 >> 40) & 0xFF) # Byte reference - MOV operation
ref_195415 = ((ref_195410 >> 32) & 0xFF) # Byte reference - MOV operation
ref_195416 = ((ref_195410 >> 24) & 0xFF) # Byte reference - MOV operation
ref_195417 = ((ref_195410 >> 16) & 0xFF) # Byte reference - MOV operation
ref_195418 = ((ref_195410 >> 8) & 0xFF) # Byte reference - MOV operation
ref_195419 = (ref_195410 & 0xFF) # Byte reference - MOV operation
ref_195420 = ((((((((((ref_195410 >> 56) & 0xFF)) << 8 | ((ref_195410 >> 48) & 0xFF)) << 8 | ((ref_195410 >> 40) & 0xFF)) << 8 | ((ref_195410 >> 32) & 0xFF)) << 8 | ((ref_195410 >> 24) & 0xFF)) << 8 | ((ref_195410 >> 16) & 0xFF)) << 8 | ((ref_195410 >> 8) & 0xFF)) << 8 | (ref_195410 & 0xFF)) # Temporary concatenation reference - MOV operation
ref_200080 = (((((((((ref_77278 & 0xFF)) << 8 | (ref_77279 & 0xFF)) << 8 | (ref_77280 & 0xFF)) << 8 | (ref_77281 & 0xFF)) << 8 | (ref_77282 & 0xFF)) << 8 | (ref_77283 & 0xFF)) << 8 | (ref_164724 & 0xFF)) << 8 | (ref_173853 & 0xFF)) # MOV operation
ref_200082 = ((ref_200080 >> 56) & 0xFF) # Byte reference - MOV operation
ref_200083 = ((ref_200080 >> 48) & 0xFF) # Byte reference - MOV operation
ref_200084 = ((ref_200080 >> 40) & 0xFF) # Byte reference - MOV operation
ref_200085 = ((ref_200080 >> 32) & 0xFF) # Byte reference - MOV operation
ref_200086 = ((ref_200080 >> 24) & 0xFF) # Byte reference - MOV operation
ref_200087 = ((ref_200080 >> 16) & 0xFF) # Byte reference - MOV operation
ref_200088 = ((ref_200080 >> 8) & 0xFF) # Byte reference - MOV operation
ref_200089 = (ref_200080 & 0xFF) # Byte reference - MOV operation
ref_200090 = ((((((((((ref_200080 >> 56) & 0xFF)) << 8 | ((ref_200080 >> 48) & 0xFF)) << 8 | ((ref_200080 >> 40) & 0xFF)) << 8 | ((ref_200080 >> 32) & 0xFF)) << 8 | ((ref_200080 >> 24) & 0xFF)) << 8 | ((ref_200080 >> 16) & 0xFF)) << 8 | ((ref_200080 >> 8) & 0xFF)) << 8 | (ref_200080 & 0xFF)) # Temporary concatenation reference - MOV operation
ref_200989 = ref_200080 # MOV operation
ref_200997 = ref_200989 # MOV operation
ref_201001 = (ref_200997 >> (0x2 & 0x3F)) # SHR operation
ref_201002 = (0x0 if ((0x2 & 0x3F) == 0x0) else ((ref_200997 >> (((0x2 & 0x3F) - 0x1) & 0xFFFFFFFFFFFFFFFF)) & 0x1)) # Carry flag
ref_201003 = (((ref_200997 >> ((0x40 - 0x1) & 0xFFFFFFFFFFFFFFFF)) & 0x1) if ((0x2 & 0x3F) == 0x1) else 0x0) # Overflow flag
ref_201004 = (0x0 if ((0x2 & 0x3F) == 0x0) else ((((((((0x1 ^ (((ref_201001 & 0xFF) >> 0x0) & 0x1)) ^ (((ref_201001 & 0xFF) >> 0x1) & 0x1)) ^ (((ref_201001 & 0xFF) >> 0x2) & 0x1)) ^ (((ref_201001 & 0xFF) >> 0x3) & 0x1)) ^ (((ref_201001 & 0xFF) >> 0x4) & 0x1)) ^ (((ref_201001 & 0xFF) >> 0x5) & 0x1)) ^ (((ref_201001 & 0xFF) >> 0x6) & 0x1)) ^ (((ref_201001 & 0xFF) >> 0x7) & 0x1))) # Parity flag
ref_201005 = (0x0 if ((0x2 & 0x3F) == 0x0) else ((ref_201001 >> 63) & 0x1)) # Sign flag
ref_201006 = (0x0 if ((0x2 & 0x3F) == 0x0) else (0x1 if (ref_201001 == 0x0) else 0x0)) # Zero flag
ref_201008 = ref_201001 # MOV operation
ref_201010 = ((ref_201008 >> 56) & 0xFF) # Byte reference - MOV operation
ref_201011 = ((ref_201008 >> 48) & 0xFF) # Byte reference - MOV operation
ref_201012 = ((ref_201008 >> 40) & 0xFF) # Byte reference - MOV operation
ref_201013 = ((ref_201008 >> 32) & 0xFF) # Byte reference - MOV operation
ref_201014 = ((ref_201008 >> 24) & 0xFF) # Byte reference - MOV operation
ref_201015 = ((ref_201008 >> 16) & 0xFF) # Byte reference - MOV operation
ref_201016 = ((ref_201008 >> 8) & 0xFF) # Byte reference - MOV operation
ref_201017 = (ref_201008 & 0xFF) # Byte reference - MOV operation
ref_201018 = ((((((((((ref_201008 >> 56) & 0xFF)) << 8 | ((ref_201008 >> 48) & 0xFF)) << 8 | ((ref_201008 >> 40) & 0xFF)) << 8 | ((ref_201008 >> 32) & 0xFF)) << 8 | ((ref_201008 >> 24) & 0xFF)) << 8 | ((ref_201008 >> 16) & 0xFF)) << 8 | ((ref_201008 >> 8) & 0xFF)) << 8 | (ref_201008 & 0xFF)) # Temporary concatenation reference - MOV operation
ref_201901 = ref_201008 # MOV operation
ref_201903 = ref_201901 # MOV operation
ref_201905 = ~ref_201903 # NOT operation
ref_201911 = (ref_201905 | 0xF) # OR operation
ref_201914 = ((((((((0x1 ^ (((ref_201911 & 0xFF) >> 0x0) & 0x1)) ^ (((ref_201911 & 0xFF) >> 0x1) & 0x1)) ^ (((ref_201911 & 0xFF) >> 0x2) & 0x1)) ^ (((ref_201911 & 0xFF) >> 0x3) & 0x1)) ^ (((ref_201911 & 0xFF) >> 0x4) & 0x1)) ^ (((ref_201911 & 0xFF) >> 0x5) & 0x1)) ^ (((ref_201911 & 0xFF) >> 0x6) & 0x1)) ^ (((ref_201911 & 0xFF) >> 0x7) & 0x1)) # Parity flag
ref_201915 = ((ref_201911 >> 63) & 0x1) # Sign flag
ref_201916 = (0x1 if (ref_201911 == 0x0) else 0x0) # Zero flag
ref_201928 = ref_201008 # MOV operation
ref_201930 = ((ref_201928 + ref_201911) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_201931 = (0x1 if (0x10 == (0x10 & (ref_201930 ^ (ref_201928 ^ ref_201911)))) else 0x0) # Adjust flag
ref_201932 = ((((ref_201928 & ref_201911) ^ (((ref_201928 ^ ref_201911) ^ ref_201930) & (ref_201928 ^ ref_201911))) >> 63) & 0x1) # Carry flag
ref_201933 = ((((ref_201928 ^ ~ref_201911) & (ref_201928 ^ ref_201930)) >> 63) & 0x1) # Overflow flag
ref_201934 = ((((((((0x1 ^ (((ref_201930 & 0xFF) >> 0x0) & 0x1)) ^ (((ref_201930 & 0xFF) >> 0x1) & 0x1)) ^ (((ref_201930 & 0xFF) >> 0x2) & 0x1)) ^ (((ref_201930 & 0xFF) >> 0x3) & 0x1)) ^ (((ref_201930 & 0xFF) >> 0x4) & 0x1)) ^ (((ref_201930 & 0xFF) >> 0x5) & 0x1)) ^ (((ref_201930 & 0xFF) >> 0x6) & 0x1)) ^ (((ref_201930 & 0xFF) >> 0x7) & 0x1)) # Parity flag
ref_201935 = ((ref_201930 >> 63) & 0x1) # Sign flag
ref_201936 = (0x1 if (ref_201930 == 0x0) else 0x0) # Zero flag
ref_201938 = ((ref_201930 + 0x1) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_201939 = (0x1 if (0x10 == (0x10 & (ref_201938 ^ (ref_201930 ^ 0x1)))) else 0x0) # Adjust flag
ref_201940 = ((((ref_201930 & 0x1) ^ (((ref_201930 ^ 0x1) ^ ref_201938) & (ref_201930 ^ 0x1))) >> 63) & 0x1) # Carry flag
ref_201941 = ((((ref_201930 ^ ~0x1) & (ref_201930 ^ ref_201938)) >> 63) & 0x1) # Overflow flag
ref_201942 = ((((((((0x1 ^ (((ref_201938 & 0xFF) >> 0x0) & 0x1)) ^ (((ref_201938 & 0xFF) >> 0x1) & 0x1)) ^ (((ref_201938 & 0xFF) >> 0x2) & 0x1)) ^ (((ref_201938 & 0xFF) >> 0x3) & 0x1)) ^ (((ref_201938 & 0xFF) >> 0x4) & 0x1)) ^ (((ref_201938 & 0xFF) >> 0x5) & 0x1)) ^ (((ref_201938 & 0xFF) >> 0x6) & 0x1)) ^ (((ref_201938 & 0xFF) >> 0x7) & 0x1)) # Parity flag
ref_201943 = ((ref_201938 >> 63) & 0x1) # Sign flag
ref_201944 = (0x1 if (ref_201938 == 0x0) else 0x0) # Zero flag
ref_201946 = ((ref_201938 >> 56) & 0xFF) # Byte reference - MOV operation
ref_201947 = ((ref_201938 >> 48) & 0xFF) # Byte reference - MOV operation
ref_201948 = ((ref_201938 >> 40) & 0xFF) # Byte reference - MOV operation
ref_201949 = ((ref_201938 >> 32) & 0xFF) # Byte reference - MOV operation
ref_201950 = ((ref_201938 >> 24) & 0xFF) # Byte reference - MOV operation
ref_201951 = ((ref_201938 >> 16) & 0xFF) # Byte reference - MOV operation
ref_201952 = ((ref_201938 >> 8) & 0xFF) # Byte reference - MOV operation
ref_201953 = (ref_201938 & 0xFF) # Byte reference - MOV operation
ref_201954 = ((((((((((ref_201938 >> 56) & 0xFF)) << 8 | ((ref_201938 >> 48) & 0xFF)) << 8 | ((ref_201938 >> 40) & 0xFF)) << 8 | ((ref_201938 >> 32) & 0xFF)) << 8 | ((ref_201938 >> 24) & 0xFF)) << 8 | ((ref_201938 >> 16) & 0xFF)) << 8 | ((ref_201938 >> 8) & 0xFF)) << 8 | (ref_201938 & 0xFF)) # Temporary concatenation reference - MOV operation
ref_202205 = ref_201938 # MOV operation
ref_202221 = (0xFFFFFFFFFFFFFFFE & ref_202205) # AND operation
ref_202224 = ((((((((0x1 ^ (((ref_202221 & 0xFF) >> 0x0) & 0x1)) ^ (((ref_202221 & 0xFF) >> 0x1) & 0x1)) ^ (((ref_202221 & 0xFF) >> 0x2) & 0x1)) ^ (((ref_202221 & 0xFF) >> 0x3) & 0x1)) ^ (((ref_202221 & 0xFF) >> 0x4) & 0x1)) ^ (((ref_202221 & 0xFF) >> 0x5) & 0x1)) ^ (((ref_202221 & 0xFF) >> 0x6) & 0x1)) ^ (((ref_202221 & 0xFF) >> 0x7) & 0x1)) # Parity flag
ref_202225 = ((ref_202221 >> 63) & 0x1) # Sign flag
ref_202226 = (0x1 if (ref_202221 == 0x0) else 0x0) # Zero flag
ref_202240 = ((0x1 + ref_202221) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_202241 = (0x1 if (0x10 == (0x10 & (ref_202240 ^ (0x1 ^ ref_202221)))) else 0x0) # Adjust flag
ref_202242 = ((((0x1 & ref_202221) ^ (((0x1 ^ ref_202221) ^ ref_202240) & (0x1 ^ ref_202221))) >> 63) & 0x1) # Carry flag
ref_202243 = ((((0x1 ^ ~ref_202221) & (0x1 ^ ref_202240)) >> 63) & 0x1) # Overflow flag
ref_202244 = ((((((((0x1 ^ (((ref_202240 & 0xFF) >> 0x0) & 0x1)) ^ (((ref_202240 & 0xFF) >> 0x1) & 0x1)) ^ (((ref_202240 & 0xFF) >> 0x2) & 0x1)) ^ (((ref_202240 & 0xFF) >> 0x3) & 0x1)) ^ (((ref_202240 & 0xFF) >> 0x4) & 0x1)) ^ (((ref_202240 & 0xFF) >> 0x5) & 0x1)) ^ (((ref_202240 & 0xFF) >> 0x6) & 0x1)) ^ (((ref_202240 & 0xFF) >> 0x7) & 0x1)) # Parity flag
ref_202245 = ((ref_202240 >> 63) & 0x1) # Sign flag
ref_202246 = (0x1 if (ref_202240 == 0x0) else 0x0) # Zero flag
ref_202248 = ((ref_202240 >> 56) & 0xFF) # Byte reference - MOV operation
ref_202249 = ((ref_202240 >> 48) & 0xFF) # Byte reference - MOV operation
ref_202250 = ((ref_202240 >> 40) & 0xFF) # Byte reference - MOV operation
ref_202251 = ((ref_202240 >> 32) & 0xFF) # Byte reference - MOV operation
ref_202252 = ((ref_202240 >> 24) & 0xFF) # Byte reference - MOV operation
ref_202253 = ((ref_202240 >> 16) & 0xFF) # Byte reference - MOV operation
ref_202254 = ((ref_202240 >> 8) & 0xFF) # Byte reference - MOV operation
ref_202255 = (ref_202240 & 0xFF) # Byte reference - MOV operation
ref_202256 = ((((((((((ref_202240 >> 56) & 0xFF)) << 8 | ((ref_202240 >> 48) & 0xFF)) << 8 | ((ref_202240 >> 40) & 0xFF)) << 8 | ((ref_202240 >> 32) & 0xFF)) << 8 | ((ref_202240 >> 24) & 0xFF)) << 8 | ((ref_202240 >> 16) & 0xFF)) << 8 | ((ref_202240 >> 8) & 0xFF)) << 8 | (ref_202240 & 0xFF)) # Temporary concatenation reference - MOV operation
ref_202347 = ref_202240 # MOV operation
ref_202349 = ~ref_202347 # NOT operation
ref_202353 = (0x40 & ref_202349) # AND operation
ref_202356 = ((((((((0x1 ^ (((ref_202353 & 0xFF) >> 0x0) & 0x1)) ^ (((ref_202353 & 0xFF) >> 0x1) & 0x1)) ^ (((ref_202353 & 0xFF) >> 0x2) & 0x1)) ^ (((ref_202353 & 0xFF) >> 0x3) & 0x1)) ^ (((ref_202353 & 0xFF) >> 0x4) & 0x1)) ^ (((ref_202353 & 0xFF) >> 0x5) & 0x1)) ^ (((ref_202353 & 0xFF) >> 0x6) & 0x1)) ^ (((ref_202353 & 0xFF) >> 0x7) & 0x1)) # Parity flag
ref_202357 = ((ref_202353 >> 63) & 0x1) # Sign flag
ref_202358 = (0x1 if (ref_202353 == 0x0) else 0x0) # Zero flag
ref_202374 = ref_202240 # MOV operation
ref_202376 = ~ref_202374 # NOT operation
ref_202378 = (ref_202376 & 0x40) # AND operation
ref_202381 = ((((((((0x1 ^ (((ref_202378 & 0xFF) >> 0x0) & 0x1)) ^ (((ref_202378 & 0xFF) >> 0x1) & 0x1)) ^ (((ref_202378 & 0xFF) >> 0x2) & 0x1)) ^ (((ref_202378 & 0xFF) >> 0x3) & 0x1)) ^ (((ref_202378 & 0xFF) >> 0x4) & 0x1)) ^ (((ref_202378 & 0xFF) >> 0x5) & 0x1)) ^ (((ref_202378 & 0xFF) >> 0x6) & 0x1)) ^ (((ref_202378 & 0xFF) >> 0x7) & 0x1)) # Parity flag
ref_202382 = ((ref_202378 >> 63) & 0x1) # Sign flag
ref_202383 = (0x1 if (ref_202378 == 0x0) else 0x0) # Zero flag
ref_202385 = ((ref_202353 + ref_202378) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_202386 = (0x1 if (0x10 == (0x10 & (ref_202385 ^ (ref_202353 ^ ref_202378)))) else 0x0) # Adjust flag
ref_202387 = ((((ref_202353 & ref_202378) ^ (((ref_202353 ^ ref_202378) ^ ref_202385) & (ref_202353 ^ ref_202378))) >> 63) & 0x1) # Carry flag
ref_202388 = ((((ref_202353 ^ ~ref_202378) & (ref_202353 ^ ref_202385)) >> 63) & 0x1) # Overflow flag
ref_202389 = ((((((((0x1 ^ (((ref_202385 & 0xFF) >> 0x0) & 0x1)) ^ (((ref_202385 & 0xFF) >> 0x1) & 0x1)) ^ (((ref_202385 & 0xFF) >> 0x2) & 0x1)) ^ (((ref_202385 & 0xFF) >> 0x3) & 0x1)) ^ (((ref_202385 & 0xFF) >> 0x4) & 0x1)) ^ (((ref_202385 & 0xFF) >> 0x5) & 0x1)) ^ (((ref_202385 & 0xFF) >> 0x6) & 0x1)) ^ (((ref_202385 & 0xFF) >> 0x7) & 0x1)) # Parity flag
ref_202390 = ((ref_202385 >> 63) & 0x1) # Sign flag
ref_202391 = (0x1 if (ref_202385 == 0x0) else 0x0) # Zero flag
ref_202407 = ref_202240 # MOV operation
ref_202409 = (ref_202407 ^ 0x40) # XOR operation
ref_202412 = ((((((((0x1 ^ (((ref_202409 & 0xFF) >> 0x0) & 0x1)) ^ (((ref_202409 & 0xFF) >> 0x1) & 0x1)) ^ (((ref_202409 & 0xFF) >> 0x2) & 0x1)) ^ (((ref_202409 & 0xFF) >> 0x3) & 0x1)) ^ (((ref_202409 & 0xFF) >> 0x4) & 0x1)) ^ (((ref_202409 & 0xFF) >> 0x5) & 0x1)) ^ (((ref_202409 & 0xFF) >> 0x6) & 0x1)) ^ (((ref_202409 & 0xFF) >> 0x7) & 0x1)) # Parity flag
ref_202413 = ((ref_202409 >> 63) & 0x1) # Sign flag
ref_202414 = (0x1 if (ref_202409 == 0x0) else 0x0) # Zero flag
ref_202416 = ref_202385 # MOV operation
ref_202418 = ((ref_202416 - ref_202409) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_202419 = (0x1 if (0x10 == (0x10 & (ref_202418 ^ (ref_202416 ^ ref_202409)))) else 0x0) # Adjust flag
ref_202420 = ((((ref_202416 ^ (ref_202409 ^ ref_202418)) ^ ((ref_202416 ^ ref_202418) & (ref_202416 ^ ref_202409))) >> 63) & 0x1) # Carry flag
ref_202421 = ((((ref_202416 ^ ref_202409) & (ref_202416 ^ ref_202418)) >> 63) & 0x1) # Overflow flag
ref_202422 = ((((((((0x1 ^ (((ref_202418 & 0xFF) >> 0x0) & 0x1)) ^ (((ref_202418 & 0xFF) >> 0x1) & 0x1)) ^ (((ref_202418 & 0xFF) >> 0x2) & 0x1)) ^ (((ref_202418 & 0xFF) >> 0x3) & 0x1)) ^ (((ref_202418 & 0xFF) >> 0x4) & 0x1)) ^ (((ref_202418 & 0xFF) >> 0x5) & 0x1)) ^ (((ref_202418 & 0xFF) >> 0x6) & 0x1)) ^ (((ref_202418 & 0xFF) >> 0x7) & 0x1)) # Parity flag
ref_202423 = ((ref_202418 >> 63) & 0x1) # Sign flag
ref_202424 = (0x1 if (ref_202418 == 0x0) else 0x0) # Zero flag
ref_202426 = ref_202418 # MOV operation
ref_202428 = ((ref_202426 >> 56) & 0xFF) # Byte reference - MOV operation
ref_202429 = ((ref_202426 >> 48) & 0xFF) # Byte reference - MOV operation
ref_202430 = ((ref_202426 >> 40) & 0xFF) # Byte reference - MOV operation
ref_202431 = ((ref_202426 >> 32) & 0xFF) # Byte reference - MOV operation
ref_202432 = ((ref_202426 >> 24) & 0xFF) # Byte reference - MOV operation
ref_202433 = ((ref_202426 >> 16) & 0xFF) # Byte reference - MOV operation
ref_202434 = ((ref_202426 >> 8) & 0xFF) # Byte reference - MOV operation
ref_202435 = (ref_202426 & 0xFF) # Byte reference - MOV operation
ref_202436 = ((((((((((ref_202426 >> 56) & 0xFF)) << 8 | ((ref_202426 >> 48) & 0xFF)) << 8 | ((ref_202426 >> 40) & 0xFF)) << 8 | ((ref_202426 >> 32) & 0xFF)) << 8 | ((ref_202426 >> 24) & 0xFF)) << 8 | ((ref_202426 >> 16) & 0xFF)) << 8 | ((ref_202426 >> 8) & 0xFF)) << 8 | (ref_202426 & 0xFF)) # Temporary concatenation reference - MOV operation
ref_203063 = ref_195410 # MOV operation
ref_203069 = ref_202426 # MOV operation
ref_203071 = ref_203063 # MOV operation
ref_203073 = (ref_203069 & 0xFFFFFFFF) # MOV operation
ref_203075 = ((ref_203071 << ((ref_203073 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_203076 = (0x0 if (((ref_203073 & 0xFF) & 0x3F) == 0x0) else ((ref_203071 >> ((0x40 - ((ref_203073 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF)) & 0x1)) # Carry flag
ref_203077 = ((((ref_203071 >> ((0x40 - 0x1) & 0xFFFFFFFFFFFFFFFF)) ^ (ref_203071 >> ((0x40 - 0x2) & 0xFFFFFFFFFFFFFFFF))) & 0x1) if (((ref_203073 & 0xFF) & 0x3F) == 0x1) else 0x0) # Overflow flag
ref_203078 = (0x1 if (((ref_203073 & 0xFF) & 0x3F) == 0x0) else ((((((((0x1 ^ (((ref_203075 & 0xFF) >> 0x0) & 0x1)) ^ (((ref_203075 & 0xFF) >> 0x1) & 0x1)) ^ (((ref_203075 & 0xFF) >> 0x2) & 0x1)) ^ (((ref_203075 & 0xFF) >> 0x3) & 0x1)) ^ (((ref_203075 & 0xFF) >> 0x4) & 0x1)) ^ (((ref_203075 & 0xFF) >> 0x5) & 0x1)) ^ (((ref_203075 & 0xFF) >> 0x6) & 0x1)) ^ (((ref_203075 & 0xFF) >> 0x7) & 0x1))) # Parity flag
ref_203079 = (0x0 if (((ref_203073 & 0xFF) & 0x3F) == 0x0) else ((ref_203075 >> 63) & 0x1)) # Sign flag
ref_203080 = (0x0 if (((ref_203073 & 0xFF) & 0x3F) == 0x0) else (0x1 if (ref_203075 == 0x0) else 0x0)) # Zero flag
ref_203082 = ref_203075 # MOV operation
ref_203084 = ((ref_203082 >> 56) & 0xFF) # Byte reference - MOV operation
ref_203085 = ((ref_203082 >> 48) & 0xFF) # Byte reference - MOV operation
ref_203086 = ((ref_203082 >> 40) & 0xFF) # Byte reference - MOV operation
ref_203087 = ((ref_203082 >> 32) & 0xFF) # Byte reference - MOV operation
ref_203088 = ((ref_203082 >> 24) & 0xFF) # Byte reference - MOV operation
ref_203089 = ((ref_203082 >> 16) & 0xFF) # Byte reference - MOV operation
ref_203090 = ((ref_203082 >> 8) & 0xFF) # Byte reference - MOV operation
ref_203091 = (ref_203082 & 0xFF) # Byte reference - MOV operation
ref_203092 = ((((((((((ref_203082 >> 56) & 0xFF)) << 8 | ((ref_203082 >> 48) & 0xFF)) << 8 | ((ref_203082 >> 40) & 0xFF)) << 8 | ((ref_203082 >> 32) & 0xFF)) << 8 | ((ref_203082 >> 24) & 0xFF)) << 8 | ((ref_203082 >> 16) & 0xFF)) << 8 | ((ref_203082 >> 8) & 0xFF)) << 8 | (ref_203082 & 0xFF)) # Temporary concatenation reference - MOV operation
ref_208151 = ref_134265 # MOV operation
ref_208153 = ((ref_208151 >> 56) & 0xFF) # Byte reference - MOV operation
ref_208154 = ((ref_208151 >> 48) & 0xFF) # Byte reference - MOV operation
ref_208155 = ((ref_208151 >> 40) & 0xFF) # Byte reference - MOV operation
ref_208156 = ((ref_208151 >> 32) & 0xFF) # Byte reference - MOV operation
ref_208157 = ((ref_208151 >> 24) & 0xFF) # Byte reference - MOV operation
ref_208158 = ((ref_208151 >> 16) & 0xFF) # Byte reference - MOV operation
ref_208159 = ((ref_208151 >> 8) & 0xFF) # Byte reference - MOV operation
ref_208160 = (ref_208151 & 0xFF) # Byte reference - MOV operation
ref_208161 = ((((((((((ref_208151 >> 56) & 0xFF)) << 8 | ((ref_208151 >> 48) & 0xFF)) << 8 | ((ref_208151 >> 40) & 0xFF)) << 8 | ((ref_208151 >> 32) & 0xFF)) << 8 | ((ref_208151 >> 24) & 0xFF)) << 8 | ((ref_208151 >> 16) & 0xFF)) << 8 | ((ref_208151 >> 8) & 0xFF)) << 8 | (ref_208151 & 0xFF)) # Temporary concatenation reference - MOV operation
ref_212603 = (((((((((ref_77278 & 0xFF)) << 8 | (ref_77279 & 0xFF)) << 8 | (ref_77280 & 0xFF)) << 8 | (ref_77281 & 0xFF)) << 8 | (ref_77282 & 0xFF)) << 8 | (ref_77283 & 0xFF)) << 8 | (ref_164724 & 0xFF)) << 8 | (ref_173853 & 0xFF)) # MOV operation
ref_212605 = ((ref_212603 >> 56) & 0xFF) # Byte reference - MOV operation
ref_212606 = ((ref_212603 >> 48) & 0xFF) # Byte reference - MOV operation
ref_212607 = ((ref_212603 >> 40) & 0xFF) # Byte reference - MOV operation
ref_212608 = ((ref_212603 >> 32) & 0xFF) # Byte reference - MOV operation
ref_212609 = ((ref_212603 >> 24) & 0xFF) # Byte reference - MOV operation
ref_212610 = ((ref_212603 >> 16) & 0xFF) # Byte reference - MOV operation
ref_212611 = ((ref_212603 >> 8) & 0xFF) # Byte reference - MOV operation
ref_212612 = (ref_212603 & 0xFF) # Byte reference - MOV operation
ref_212613 = ((((((((((ref_212603 >> 56) & 0xFF)) << 8 | ((ref_212603 >> 48) & 0xFF)) << 8 | ((ref_212603 >> 40) & 0xFF)) << 8 | ((ref_212603 >> 32) & 0xFF)) << 8 | ((ref_212603 >> 24) & 0xFF)) << 8 | ((ref_212603 >> 16) & 0xFF)) << 8 | ((ref_212603 >> 8) & 0xFF)) << 8 | (ref_212603 & 0xFF)) # Temporary concatenation reference - MOV operation
ref_213512 = ref_212603 # MOV operation
ref_213520 = ref_213512 # MOV operation
ref_213524 = (ref_213520 >> (0x2 & 0x3F)) # SHR operation
ref_213525 = (0x0 if ((0x2 & 0x3F) == 0x0) else ((ref_213520 >> (((0x2 & 0x3F) - 0x1) & 0xFFFFFFFFFFFFFFFF)) & 0x1)) # Carry flag
ref_213526 = (((ref_213520 >> ((0x40 - 0x1) & 0xFFFFFFFFFFFFFFFF)) & 0x1) if ((0x2 & 0x3F) == 0x1) else 0x0) # Overflow flag
ref_213527 = (0x0 if ((0x2 & 0x3F) == 0x0) else ((((((((0x1 ^ (((ref_213524 & 0xFF) >> 0x0) & 0x1)) ^ (((ref_213524 & 0xFF) >> 0x1) & 0x1)) ^ (((ref_213524 & 0xFF) >> 0x2) & 0x1)) ^ (((ref_213524 & 0xFF) >> 0x3) & 0x1)) ^ (((ref_213524 & 0xFF) >> 0x4) & 0x1)) ^ (((ref_213524 & 0xFF) >> 0x5) & 0x1)) ^ (((ref_213524 & 0xFF) >> 0x6) & 0x1)) ^ (((ref_213524 & 0xFF) >> 0x7) & 0x1))) # Parity flag
ref_213528 = (0x0 if ((0x2 & 0x3F) == 0x0) else ((ref_213524 >> 63) & 0x1)) # Sign flag
ref_213529 = (0x0 if ((0x2 & 0x3F) == 0x0) else (0x1 if (ref_213524 == 0x0) else 0x0)) # Zero flag
ref_213531 = ref_213524 # MOV operation
ref_213533 = ((ref_213531 >> 56) & 0xFF) # Byte reference - MOV operation
ref_213534 = ((ref_213531 >> 48) & 0xFF) # Byte reference - MOV operation
ref_213535 = ((ref_213531 >> 40) & 0xFF) # Byte reference - MOV operation
ref_213536 = ((ref_213531 >> 32) & 0xFF) # Byte reference - MOV operation
ref_213537 = ((ref_213531 >> 24) & 0xFF) # Byte reference - MOV operation
ref_213538 = ((ref_213531 >> 16) & 0xFF) # Byte reference - MOV operation
ref_213539 = ((ref_213531 >> 8) & 0xFF) # Byte reference - MOV operation
ref_213540 = (ref_213531 & 0xFF) # Byte reference - MOV operation
ref_213541 = ((((((((((ref_213531 >> 56) & 0xFF)) << 8 | ((ref_213531 >> 48) & 0xFF)) << 8 | ((ref_213531 >> 40) & 0xFF)) << 8 | ((ref_213531 >> 32) & 0xFF)) << 8 | ((ref_213531 >> 24) & 0xFF)) << 8 | ((ref_213531 >> 16) & 0xFF)) << 8 | ((ref_213531 >> 8) & 0xFF)) << 8 | (ref_213531 & 0xFF)) # Temporary concatenation reference - MOV operation
ref_214424 = ref_213531 # MOV operation
ref_214426 = ref_214424 # MOV operation
ref_214428 = ~ref_214426 # NOT operation
ref_214434 = (ref_214428 | 0xF) # OR operation
ref_214437 = ((((((((0x1 ^ (((ref_214434 & 0xFF) >> 0x0) & 0x1)) ^ (((ref_214434 & 0xFF) >> 0x1) & 0x1)) ^ (((ref_214434 & 0xFF) >> 0x2) & 0x1)) ^ (((ref_214434 & 0xFF) >> 0x3) & 0x1)) ^ (((ref_214434 & 0xFF) >> 0x4) & 0x1)) ^ (((ref_214434 & 0xFF) >> 0x5) & 0x1)) ^ (((ref_214434 & 0xFF) >> 0x6) & 0x1)) ^ (((ref_214434 & 0xFF) >> 0x7) & 0x1)) # Parity flag
ref_214438 = ((ref_214434 >> 63) & 0x1) # Sign flag
ref_214439 = (0x1 if (ref_214434 == 0x0) else 0x0) # Zero flag
ref_214451 = ref_213531 # MOV operation
ref_214453 = ((ref_214451 + ref_214434) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_214454 = (0x1 if (0x10 == (0x10 & (ref_214453 ^ (ref_214451 ^ ref_214434)))) else 0x0) # Adjust flag
ref_214455 = ((((ref_214451 & ref_214434) ^ (((ref_214451 ^ ref_214434) ^ ref_214453) & (ref_214451 ^ ref_214434))) >> 63) & 0x1) # Carry flag
ref_214456 = ((((ref_214451 ^ ~ref_214434) & (ref_214451 ^ ref_214453)) >> 63) & 0x1) # Overflow flag
ref_214457 = ((((((((0x1 ^ (((ref_214453 & 0xFF) >> 0x0) & 0x1)) ^ (((ref_214453 & 0xFF) >> 0x1) & 0x1)) ^ (((ref_214453 & 0xFF) >> 0x2) & 0x1)) ^ (((ref_214453 & 0xFF) >> 0x3) & 0x1)) ^ (((ref_214453 & 0xFF) >> 0x4) & 0x1)) ^ (((ref_214453 & 0xFF) >> 0x5) & 0x1)) ^ (((ref_214453 & 0xFF) >> 0x6) & 0x1)) ^ (((ref_214453 & 0xFF) >> 0x7) & 0x1)) # Parity flag
ref_214458 = ((ref_214453 >> 63) & 0x1) # Sign flag
ref_214459 = (0x1 if (ref_214453 == 0x0) else 0x0) # Zero flag
ref_214461 = ((ref_214453 + 0x1) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_214462 = (0x1 if (0x10 == (0x10 & (ref_214461 ^ (ref_214453 ^ 0x1)))) else 0x0) # Adjust flag
ref_214463 = ((((ref_214453 & 0x1) ^ (((ref_214453 ^ 0x1) ^ ref_214461) & (ref_214453 ^ 0x1))) >> 63) & 0x1) # Carry flag
ref_214464 = ((((ref_214453 ^ ~0x1) & (ref_214453 ^ ref_214461)) >> 63) & 0x1) # Overflow flag
ref_214465 = ((((((((0x1 ^ (((ref_214461 & 0xFF) >> 0x0) & 0x1)) ^ (((ref_214461 & 0xFF) >> 0x1) & 0x1)) ^ (((ref_214461 & 0xFF) >> 0x2) & 0x1)) ^ (((ref_214461 & 0xFF) >> 0x3) & 0x1)) ^ (((ref_214461 & 0xFF) >> 0x4) & 0x1)) ^ (((ref_214461 & 0xFF) >> 0x5) & 0x1)) ^ (((ref_214461 & 0xFF) >> 0x6) & 0x1)) ^ (((ref_214461 & 0xFF) >> 0x7) & 0x1)) # Parity flag
ref_214466 = ((ref_214461 >> 63) & 0x1) # Sign flag
ref_214467 = (0x1 if (ref_214461 == 0x0) else 0x0) # Zero flag
ref_214469 = ((ref_214461 >> 56) & 0xFF) # Byte reference - MOV operation
ref_214470 = ((ref_214461 >> 48) & 0xFF) # Byte reference - MOV operation
ref_214471 = ((ref_214461 >> 40) & 0xFF) # Byte reference - MOV operation
ref_214472 = ((ref_214461 >> 32) & 0xFF) # Byte reference - MOV operation
ref_214473 = ((ref_214461 >> 24) & 0xFF) # Byte reference - MOV operation
ref_214474 = ((ref_214461 >> 16) & 0xFF) # Byte reference - MOV operation
ref_214475 = ((ref_214461 >> 8) & 0xFF) # Byte reference - MOV operation
ref_214476 = (ref_214461 & 0xFF) # Byte reference - MOV operation
ref_214477 = ((((((((((ref_214461 >> 56) & 0xFF)) << 8 | ((ref_214461 >> 48) & 0xFF)) << 8 | ((ref_214461 >> 40) & 0xFF)) << 8 | ((ref_214461 >> 32) & 0xFF)) << 8 | ((ref_214461 >> 24) & 0xFF)) << 8 | ((ref_214461 >> 16) & 0xFF)) << 8 | ((ref_214461 >> 8) & 0xFF)) << 8 | (ref_214461 & 0xFF)) # Temporary concatenation reference - MOV operation
ref_215254 = ref_214461 # MOV operation
ref_215264 = (ref_215254 & 0xFFFFFFFFFFFFFFFE) # AND operation
ref_215267 = ((((((((0x1 ^ (((ref_215264 & 0xFF) >> 0x0) & 0x1)) ^ (((ref_215264 & 0xFF) >> 0x1) & 0x1)) ^ (((ref_215264 & 0xFF) >> 0x2) & 0x1)) ^ (((ref_215264 & 0xFF) >> 0x3) & 0x1)) ^ (((ref_215264 & 0xFF) >> 0x4) & 0x1)) ^ (((ref_215264 & 0xFF) >> 0x5) & 0x1)) ^ (((ref_215264 & 0xFF) >> 0x6) & 0x1)) ^ (((ref_215264 & 0xFF) >> 0x7) & 0x1)) # Parity flag
ref_215268 = ((ref_215264 >> 63) & 0x1) # Sign flag
ref_215269 = (0x1 if (ref_215264 == 0x0) else 0x0) # Zero flag
ref_215277 = ((0x1 + ref_215264) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_215278 = (0x1 if (0x10 == (0x10 & (ref_215277 ^ (0x1 ^ ref_215264)))) else 0x0) # Adjust flag
ref_215279 = ((((0x1 & ref_215264) ^ (((0x1 ^ ref_215264) ^ ref_215277) & (0x1 ^ ref_215264))) >> 63) & 0x1) # Carry flag
ref_215280 = ((((0x1 ^ ~ref_215264) & (0x1 ^ ref_215277)) >> 63) & 0x1) # Overflow flag
ref_215281 = ((((((((0x1 ^ (((ref_215277 & 0xFF) >> 0x0) & 0x1)) ^ (((ref_215277 & 0xFF) >> 0x1) & 0x1)) ^ (((ref_215277 & 0xFF) >> 0x2) & 0x1)) ^ (((ref_215277 & 0xFF) >> 0x3) & 0x1)) ^ (((ref_215277 & 0xFF) >> 0x4) & 0x1)) ^ (((ref_215277 & 0xFF) >> 0x5) & 0x1)) ^ (((ref_215277 & 0xFF) >> 0x6) & 0x1)) ^ (((ref_215277 & 0xFF) >> 0x7) & 0x1)) # Parity flag
ref_215282 = ((ref_215277 >> 63) & 0x1) # Sign flag
ref_215283 = (0x1 if (ref_215277 == 0x0) else 0x0) # Zero flag
ref_215285 = ((ref_215277 >> 56) & 0xFF) # Byte reference - MOV operation
ref_215286 = ((ref_215277 >> 48) & 0xFF) # Byte reference - MOV operation
ref_215287 = ((ref_215277 >> 40) & 0xFF) # Byte reference - MOV operation
ref_215288 = ((ref_215277 >> 32) & 0xFF) # Byte reference - MOV operation
ref_215289 = ((ref_215277 >> 24) & 0xFF) # Byte reference - MOV operation
ref_215290 = ((ref_215277 >> 16) & 0xFF) # Byte reference - MOV operation
ref_215291 = ((ref_215277 >> 8) & 0xFF) # Byte reference - MOV operation
ref_215292 = (ref_215277 & 0xFF) # Byte reference - MOV operation
ref_215293 = ((((((((((ref_215277 >> 56) & 0xFF)) << 8 | ((ref_215277 >> 48) & 0xFF)) << 8 | ((ref_215277 >> 40) & 0xFF)) << 8 | ((ref_215277 >> 32) & 0xFF)) << 8 | ((ref_215277 >> 24) & 0xFF)) << 8 | ((ref_215277 >> 16) & 0xFF)) << 8 | ((ref_215277 >> 8) & 0xFF)) << 8 | (ref_215277 & 0xFF)) # Temporary concatenation reference - MOV operation
ref_216106 = ref_208151 # MOV operation
ref_216112 = ref_215277 # MOV operation
ref_216114 = ref_216106 # MOV operation
ref_216116 = (ref_216112 & 0xFFFFFFFF) # MOV operation
ref_216118 = (ref_216114 >> ((ref_216116 & 0xFF) & 0x3F)) # SHR operation
ref_216119 = (0x0 if (((ref_216116 & 0xFF) & 0x3F) == 0x0) else ((ref_216114 >> ((((ref_216116 & 0xFF) & 0x3F) - 0x1) & 0xFFFFFFFFFFFFFFFF)) & 0x1)) # Carry flag
ref_216120 = (((ref_216114 >> ((0x40 - 0x1) & 0xFFFFFFFFFFFFFFFF)) & 0x1) if (((ref_216116 & 0xFF) & 0x3F) == 0x1) else 0x0) # Overflow flag
ref_216121 = (0x1 if (((ref_216116 & 0xFF) & 0x3F) == 0x0) else ((((((((0x1 ^ (((ref_216118 & 0xFF) >> 0x0) & 0x1)) ^ (((ref_216118 & 0xFF) >> 0x1) & 0x1)) ^ (((ref_216118 & 0xFF) >> 0x2) & 0x1)) ^ (((ref_216118 & 0xFF) >> 0x3) & 0x1)) ^ (((ref_216118 & 0xFF) >> 0x4) & 0x1)) ^ (((ref_216118 & 0xFF) >> 0x5) & 0x1)) ^ (((ref_216118 & 0xFF) >> 0x6) & 0x1)) ^ (((ref_216118 & 0xFF) >> 0x7) & 0x1))) # Parity flag
ref_216122 = (0x0 if (((ref_216116 & 0xFF) & 0x3F) == 0x0) else ((ref_216118 >> 63) & 0x1)) # Sign flag
ref_216123 = (0x0 if (((ref_216116 & 0xFF) & 0x3F) == 0x0) else (0x1 if (ref_216118 == 0x0) else 0x0)) # Zero flag
ref_216125 = ref_216118 # MOV operation
ref_216127 = ((ref_216125 >> 56) & 0xFF) # Byte reference - MOV operation
ref_216128 = ((ref_216125 >> 48) & 0xFF) # Byte reference - MOV operation
ref_216129 = ((ref_216125 >> 40) & 0xFF) # Byte reference - MOV operation
ref_216130 = ((ref_216125 >> 32) & 0xFF) # Byte reference - MOV operation
ref_216131 = ((ref_216125 >> 24) & 0xFF) # Byte reference - MOV operation
ref_216132 = ((ref_216125 >> 16) & 0xFF) # Byte reference - MOV operation
ref_216133 = ((ref_216125 >> 8) & 0xFF) # Byte reference - MOV operation
ref_216134 = (ref_216125 & 0xFF) # Byte reference - MOV operation
ref_216135 = ((((((((((ref_216125 >> 56) & 0xFF)) << 8 | ((ref_216125 >> 48) & 0xFF)) << 8 | ((ref_216125 >> 40) & 0xFF)) << 8 | ((ref_216125 >> 32) & 0xFF)) << 8 | ((ref_216125 >> 24) & 0xFF)) << 8 | ((ref_216125 >> 16) & 0xFF)) << 8 | ((ref_216125 >> 8) & 0xFF)) << 8 | (ref_216125 & 0xFF)) # Temporary concatenation reference - MOV operation
ref_217073 = ref_216125 # MOV operation
ref_217085 = ref_203082 # MOV operation
ref_217087 = ~ref_217085 # NOT operation
ref_217089 = (ref_217087 & ref_217073) # AND operation
ref_217092 = ((((((((0x1 ^ (((ref_217089 & 0xFF) >> 0x0) & 0x1)) ^ (((ref_217089 & 0xFF) >> 0x1) & 0x1)) ^ (((ref_217089 & 0xFF) >> 0x2) & 0x1)) ^ (((ref_217089 & 0xFF) >> 0x3) & 0x1)) ^ (((ref_217089 & 0xFF) >> 0x4) & 0x1)) ^ (((ref_217089 & 0xFF) >> 0x5) & 0x1)) ^ (((ref_217089 & 0xFF) >> 0x6) & 0x1)) ^ (((ref_217089 & 0xFF) >> 0x7) & 0x1)) # Parity flag
ref_217093 = ((ref_217089 >> 63) & 0x1) # Sign flag
ref_217094 = (0x1 if (ref_217089 == 0x0) else 0x0) # Zero flag
ref_217106 = ref_203082 # MOV operation
ref_217108 = ((ref_217106 + ref_217089) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_217109 = (0x1 if (0x10 == (0x10 & (ref_217108 ^ (ref_217106 ^ ref_217089)))) else 0x0) # Adjust flag
ref_217110 = ((((ref_217106 & ref_217089) ^ (((ref_217106 ^ ref_217089) ^ ref_217108) & (ref_217106 ^ ref_217089))) >> 63) & 0x1) # Carry flag
ref_217111 = ((((ref_217106 ^ ~ref_217089) & (ref_217106 ^ ref_217108)) >> 63) & 0x1) # Overflow flag
ref_217112 = ((((((((0x1 ^ (((ref_217108 & 0xFF) >> 0x0) & 0x1)) ^ (((ref_217108 & 0xFF) >> 0x1) & 0x1)) ^ (((ref_217108 & 0xFF) >> 0x2) & 0x1)) ^ (((ref_217108 & 0xFF) >> 0x3) & 0x1)) ^ (((ref_217108 & 0xFF) >> 0x4) & 0x1)) ^ (((ref_217108 & 0xFF) >> 0x5) & 0x1)) ^ (((ref_217108 & 0xFF) >> 0x6) & 0x1)) ^ (((ref_217108 & 0xFF) >> 0x7) & 0x1)) # Parity flag
ref_217113 = ((ref_217108 >> 63) & 0x1) # Sign flag
ref_217114 = (0x1 if (ref_217108 == 0x0) else 0x0) # Zero flag
ref_217116 = ((ref_217108 >> 56) & 0xFF) # Byte reference - MOV operation
ref_217117 = ((ref_217108 >> 48) & 0xFF) # Byte reference - MOV operation
ref_217118 = ((ref_217108 >> 40) & 0xFF) # Byte reference - MOV operation
ref_217119 = ((ref_217108 >> 32) & 0xFF) # Byte reference - MOV operation
ref_217120 = ((ref_217108 >> 24) & 0xFF) # Byte reference - MOV operation
ref_217121 = ((ref_217108 >> 16) & 0xFF) # Byte reference - MOV operation
ref_217122 = ((ref_217108 >> 8) & 0xFF) # Byte reference - MOV operation
ref_217123 = (ref_217108 & 0xFF) # Byte reference - MOV operation
ref_217124 = ((((((((((ref_217108 >> 56) & 0xFF)) << 8 | ((ref_217108 >> 48) & 0xFF)) << 8 | ((ref_217108 >> 40) & 0xFF)) << 8 | ((ref_217108 >> 32) & 0xFF)) << 8 | ((ref_217108 >> 24) & 0xFF)) << 8 | ((ref_217108 >> 16) & 0xFF)) << 8 | ((ref_217108 >> 8) & 0xFF)) << 8 | (ref_217108 & 0xFF)) # Temporary concatenation reference - MOV operation
ref_217743 = ref_190215 # MOV operation
ref_217749 = ref_217108 # MOV operation
ref_217751 = ref_217743 # MOV operation
ref_217753 = (ref_217751 ^ ref_217749) # XOR operation
ref_217756 = ((((((((0x1 ^ (((ref_217753 & 0xFF) >> 0x0) & 0x1)) ^ (((ref_217753 & 0xFF) >> 0x1) & 0x1)) ^ (((ref_217753 & 0xFF) >> 0x2) & 0x1)) ^ (((ref_217753 & 0xFF) >> 0x3) & 0x1)) ^ (((ref_217753 & 0xFF) >> 0x4) & 0x1)) ^ (((ref_217753 & 0xFF) >> 0x5) & 0x1)) ^ (((ref_217753 & 0xFF) >> 0x6) & 0x1)) ^ (((ref_217753 & 0xFF) >> 0x7) & 0x1)) # Parity flag
ref_217757 = ((ref_217753 >> 63) & 0x1) # Sign flag
ref_217758 = (0x1 if (ref_217753 == 0x0) else 0x0) # Zero flag
ref_217772 = ref_190215 # MOV operation
ref_217778 = ref_217108 # MOV operation
ref_217780 = ref_217772 # MOV operation
ref_217782 = (ref_217780 & ref_217778) # AND operation
ref_217785 = ((((((((0x1 ^ (((ref_217782 & 0xFF) >> 0x0) & 0x1)) ^ (((ref_217782 & 0xFF) >> 0x1) & 0x1)) ^ (((ref_217782 & 0xFF) >> 0x2) & 0x1)) ^ (((ref_217782 & 0xFF) >> 0x3) & 0x1)) ^ (((ref_217782 & 0xFF) >> 0x4) & 0x1)) ^ (((ref_217782 & 0xFF) >> 0x5) & 0x1)) ^ (((ref_217782 & 0xFF) >> 0x6) & 0x1)) ^ (((ref_217782 & 0xFF) >> 0x7) & 0x1)) # Parity flag
ref_217786 = ((ref_217782 >> 63) & 0x1) # Sign flag
ref_217787 = (0x1 if (ref_217782 == 0x0) else 0x0) # Zero flag
ref_217801 = ref_190215 # MOV operation
ref_217807 = ref_217108 # MOV operation
ref_217809 = (ref_217807 & ref_217801) # AND operation
ref_217812 = ((((((((0x1 ^ (((ref_217809 & 0xFF) >> 0x0) & 0x1)) ^ (((ref_217809 & 0xFF) >> 0x1) & 0x1)) ^ (((ref_217809 & 0xFF) >> 0x2) & 0x1)) ^ (((ref_217809 & 0xFF) >> 0x3) & 0x1)) ^ (((ref_217809 & 0xFF) >> 0x4) & 0x1)) ^ (((ref_217809 & 0xFF) >> 0x5) & 0x1)) ^ (((ref_217809 & 0xFF) >> 0x6) & 0x1)) ^ (((ref_217809 & 0xFF) >> 0x7) & 0x1)) # Parity flag
ref_217813 = ((ref_217809 >> 63) & 0x1) # Sign flag
ref_217814 = (0x1 if (ref_217809 == 0x0) else 0x0) # Zero flag
ref_217816 = ((ref_217809 + ref_217782) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_217817 = (0x1 if (0x10 == (0x10 & (ref_217816 ^ (ref_217809 ^ ref_217782)))) else 0x0) # Adjust flag
ref_217818 = ((((ref_217809 & ref_217782) ^ (((ref_217809 ^ ref_217782) ^ ref_217816) & (ref_217809 ^ ref_217782))) >> 63) & 0x1) # Carry flag
ref_217819 = ((((ref_217809 ^ ~ref_217782) & (ref_217809 ^ ref_217816)) >> 63) & 0x1) # Overflow flag
ref_217820 = ((((((((0x1 ^ (((ref_217816 & 0xFF) >> 0x0) & 0x1)) ^ (((ref_217816 & 0xFF) >> 0x1) & 0x1)) ^ (((ref_217816 & 0xFF) >> 0x2) & 0x1)) ^ (((ref_217816 & 0xFF) >> 0x3) & 0x1)) ^ (((ref_217816 & 0xFF) >> 0x4) & 0x1)) ^ (((ref_217816 & 0xFF) >> 0x5) & 0x1)) ^ (((ref_217816 & 0xFF) >> 0x6) & 0x1)) ^ (((ref_217816 & 0xFF) >> 0x7) & 0x1)) # Parity flag
ref_217821 = ((ref_217816 >> 63) & 0x1) # Sign flag
ref_217822 = (0x1 if (ref_217816 == 0x0) else 0x0) # Zero flag
ref_217824 = ((ref_217816 + ref_217753) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_217825 = (0x1 if (0x10 == (0x10 & (ref_217824 ^ (ref_217816 ^ ref_217753)))) else 0x0) # Adjust flag
ref_217826 = ((((ref_217816 & ref_217753) ^ (((ref_217816 ^ ref_217753) ^ ref_217824) & (ref_217816 ^ ref_217753))) >> 63) & 0x1) # Carry flag
ref_217827 = ((((ref_217816 ^ ~ref_217753) & (ref_217816 ^ ref_217824)) >> 63) & 0x1) # Overflow flag
ref_217828 = ((((((((0x1 ^ (((ref_217824 & 0xFF) >> 0x0) & 0x1)) ^ (((ref_217824 & 0xFF) >> 0x1) & 0x1)) ^ (((ref_217824 & 0xFF) >> 0x2) & 0x1)) ^ (((ref_217824 & 0xFF) >> 0x3) & 0x1)) ^ (((ref_217824 & 0xFF) >> 0x4) & 0x1)) ^ (((ref_217824 & 0xFF) >> 0x5) & 0x1)) ^ (((ref_217824 & 0xFF) >> 0x6) & 0x1)) ^ (((ref_217824 & 0xFF) >> 0x7) & 0x1)) # Parity flag
ref_217829 = ((ref_217824 >> 63) & 0x1) # Sign flag
ref_217830 = (0x1 if (ref_217824 == 0x0) else 0x0) # Zero flag
ref_217832 = ((ref_217824 >> 56) & 0xFF) # Byte reference - MOV operation
ref_217833 = ((ref_217824 >> 48) & 0xFF) # Byte reference - MOV operation
ref_217834 = ((ref_217824 >> 40) & 0xFF) # Byte reference - MOV operation
ref_217835 = ((ref_217824 >> 32) & 0xFF) # Byte reference - MOV operation
ref_217836 = ((ref_217824 >> 24) & 0xFF) # Byte reference - MOV operation
ref_217837 = ((ref_217824 >> 16) & 0xFF) # Byte reference - MOV operation
ref_217838 = ((ref_217824 >> 8) & 0xFF) # Byte reference - MOV operation
ref_217839 = (ref_217824 & 0xFF) # Byte reference - MOV operation
ref_217840 = ((((((((((ref_217824 >> 56) & 0xFF)) << 8 | ((ref_217824 >> 48) & 0xFF)) << 8 | ((ref_217824 >> 40) & 0xFF)) << 8 | ((ref_217824 >> 32) & 0xFF)) << 8 | ((ref_217824 >> 24) & 0xFF)) << 8 | ((ref_217824 >> 16) & 0xFF)) << 8 | ((ref_217824 >> 8) & 0xFF)) << 8 | (ref_217824 & 0xFF)) # Temporary concatenation reference - MOV operation
ref_218728 = ref_217824 # MOV operation
ref_218730 = ((ref_218728 >> 56) & 0xFF) # Byte reference - MOV operation
ref_218731 = ((ref_218728 >> 48) & 0xFF) # Byte reference - MOV operation
ref_218732 = ((ref_218728 >> 40) & 0xFF) # Byte reference - MOV operation
ref_218733 = ((ref_218728 >> 32) & 0xFF) # Byte reference - MOV operation
ref_218734 = ((ref_218728 >> 24) & 0xFF) # Byte reference - MOV operation
ref_218735 = ((ref_218728 >> 16) & 0xFF) # Byte reference - MOV operation
ref_218736 = ((ref_218728 >> 8) & 0xFF) # Byte reference - MOV operation
ref_218737 = (ref_218728 & 0xFF) # Byte reference - MOV operation
ref_218738 = ((((((((((ref_218728 >> 56) & 0xFF)) << 8 | ((ref_218728 >> 48) & 0xFF)) << 8 | ((ref_218728 >> 40) & 0xFF)) << 8 | ((ref_218728 >> 32) & 0xFF)) << 8 | ((ref_218728 >> 24) & 0xFF)) << 8 | ((ref_218728 >> 16) & 0xFF)) << 8 | ((ref_218728 >> 8) & 0xFF)) << 8 | (ref_218728 & 0xFF)) # Temporary concatenation reference - MOV operation
ref_219248 = ref_218728 # MOV operation
ref_219250 = ref_219248 # MOV operation


s.add(ref_219250 == int(sys.argv[1]))
collisions = 0
while s.check() == z3.sat and collisions < 10:
    print s.model()
    s.add(SymVar_0 != s.model()[SymVar_0])
    collisions += 1
