#!/usr/bin/env python2
## -*- coding: utf-8 -*-

import sys

def sx(bits, value):
    sign_bit = 1 << (bits - 1)
    return (value & (sign_bit - 1)) - (value & sign_bit)

SymVar_0 = int(sys.argv[1])
ref_382 = SymVar_0
ref_393 = ref_382 # MOV operation
ref_405 = ref_393 # MOV operation
ref_407 = ref_405 # MOV operation
ref_452 = ((ref_407 >> 56) & 0xFF) # Byte reference - MOV operation
ref_453 = ((ref_407 >> 48) & 0xFF) # Byte reference - MOV operation
ref_454 = ((ref_407 >> 40) & 0xFF) # Byte reference - MOV operation
ref_455 = ((ref_407 >> 32) & 0xFF) # Byte reference - MOV operation
ref_456 = ((ref_407 >> 24) & 0xFF) # Byte reference - MOV operation
ref_457 = ((ref_407 >> 16) & 0xFF) # Byte reference - MOV operation
ref_458 = ((ref_407 >> 8) & 0xFF) # Byte reference - MOV operation
ref_459 = (ref_407 & 0xFF) # Byte reference - MOV operation
ref_9791 = ((((ref_456) << 8 | ref_457) << 8 | ref_458) << 8 | ref_459) # MOV operation
ref_9799 = (ref_9791 & 0xFFFFFFFF) # MOV operation
ref_9823 = (ref_9799 & 0xFFFFFFFF) # MOV operation
ref_9837 = (ref_9823 & 0xFFFFFFFF) # MOV operation
ref_9974 = ((((ref_452) << 8 | ref_453) << 8 | ref_454) << 8 | ref_455) # MOV operation
ref_9982 = (ref_9974 & 0xFFFFFFFF) # MOV operation
ref_10006 = (ref_9982 & 0xFFFFFFFF) # MOV operation
ref_10020 = (ref_10006 & 0xFFFFFFFF) # MOV operation
ref_10022 = ref_9837 # MOV operation
ref_10024 = ((0x0 + ((0x0 + ((ref_10022 * 0x8) & 0xFFFFFFFFFFFFFFFF)) & 0xFFFFFFFFFFFFFFFF)) & 0xFFFFFFFFFFFFFFFF) # LEA operation
ref_10028 = ((0x8 + ref_10024) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_10036 = ref_10020 # MOV operation
ref_10038 = ref_10028 # MOV operation
ref_10092 = ref_10038 # MOV operation
ref_10104 = ref_10036 # MOV operation
ref_10116 = ref_10092 # MOV operation
ref_10118 = ref_10104 # MOV operation
ref_10120 = ref_10116 # MOV operation
ref_10122 = ref_10118 # MOV operation
ref_10148 = ref_10120 # MOV operation
ref_10150 = ref_10122 # MOV operation
ref_10152 = ref_10150 # MOV operation
ref_10186 = ref_10148 # MOV operation
ref_10188 = ref_10152 # MOV operation
ref_10190 = (ref_10188 ^ ref_10186) # XOR operation
ref_10197 = (((sx(0x40, ref_10190) * sx(0x40, ((((((((0x9D) << 8 | 0xDF) << 8 | 0xEA) << 8 | 0x8) << 8 | 0xEB) << 8 | 0x38) << 8 | 0x2D) << 8 | 0x69))) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_10211 = ref_10197 # MOV operation
ref_10213 = (ref_10211 >> (0x2F & 0x3F)) # SHR operation
ref_10235 = ref_10152 # MOV operation
ref_10237 = (ref_10235 ^ (ref_10197 ^ ref_10213)) # XOR operation
ref_10244 = (((sx(0x40, ref_10237) * sx(0x40, ((((((((0x9D) << 8 | 0xDF) << 8 | 0xEA) << 8 | 0x8) << 8 | 0xEB) << 8 | 0x38) << 8 | 0x2D) << 8 | 0x69))) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_10258 = ref_10244 # MOV operation
ref_10260 = (ref_10258 >> (0x2F & 0x3F)) # SHR operation
ref_10282 = (ref_10244 ^ ref_10260) # MOV operation
ref_10284 = (((sx(0x40, ref_10282) * sx(0x40, ((((((((0x9D) << 8 | 0xDF) << 8 | 0xEA) << 8 | 0x8) << 8 | 0xEB) << 8 | 0x38) << 8 | 0x2D) << 8 | 0x69))) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_10298 = ref_10284 # MOV operation
ref_10315 = ref_10298 # MOV operation
ref_10333 = ref_10315 # MOV operation
ref_10352 = ref_10333 # MOV operation
ref_10694 = ref_10352 # MOV operation
ref_10793 = ref_10694 # MOV operation
ref_11119 = ref_10793 # MOV operation
ref_11206 = ref_11119 # MOV operation
ref_11244 = ref_11206 # MOV operation
ref_11256 = ref_11244 # MOV operation
ref_11258 = ref_11256 # MOV operation

print ref_11258 & 0xffffffffffffffff
