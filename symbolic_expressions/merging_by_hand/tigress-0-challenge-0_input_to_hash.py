#!/usr/bin/env python2
## -*- coding: utf-8 -*-
##
## Triton
##

import sys

def sx(bits, value):
    sign_bit = 1 << (bits - 1)
    return (value & (sign_bit - 1)) - (value & sign_bit)

SymVar_0 = int(sys.argv[1])
a = ((sx(0x40, ((sx(0x40, ((sx(0x40, 0x2C7C60B7) * sx(0x40, ((((0x3F & (((0x46BC480 | SymVar_0) << ((((0x1 | (0x7 & ((0x34D870D1 + SymVar_0) & 0xFFFFFFFFFFFFFFFF))) & 0xFFFFFFFF) & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF)) << (0x4 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) | (((((0x1DD9C3C5 + SymVar_0) & 0xFFFFFFFFFFFFFFFF) << (((((0x40 - (0x1 | (0xF & ((sx(0x40, 0x38BCA01F) * sx(0x40, ((0x34D870D1 + SymVar_0) & 0xFFFFFFFFFFFFFFFF))) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF)))) & 0xFFFFFFFFFFFFFFFF) & 0xFFFFFFFF) & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) | (((0x1DD9C3C5 + SymVar_0) & 0xFFFFFFFFFFFFFFFF) >> ((((0x1 | (0xF & ((sx(0x40, 0x38BCA01F) * sx(0x40, ((0x34D870D1 + SymVar_0) & 0xFFFFFFFFFFFFFFFF))) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF))) & 0xFFFFFFFF) & 0xFF) & 0x3F)))))) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF)) * sx(0x40, (0x46BC480 | SymVar_0))) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF)) * sx(0x40, (((0xFFFFFFFFD9FCA98B | (((0x34D870D1 + SymVar_0) & 0xFFFFFFFFFFFFFFFF) | SymVar_0)) + ((0x34D870D1 + SymVar_0) & 0xFFFFFFFFFFFFFFFF)) & 0xFFFFFFFFFFFFFFFF))) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF)
print a & 0xffffffffffffffff
