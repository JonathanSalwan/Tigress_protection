#!/usr/bin/env python2
## -*- coding: utf-8 -*-


TEMPLATE_GENERATE_HASH = '''\
#!/usr/bin/env python2
## -*- coding: utf-8 -*-

import sys

def sx(bits, value):
    sign_bit = 1 << (bits - 1)
    return (value & (sign_bit - 1)) - (value & sign_bit)

SymVar_0 = int(sys.argv[1])
a = %s
print a & 0xffffffffffffffff
'''


TEMPLATE_GENERATE_HASH_SSA = '''\
#!/usr/bin/env python2
## -*- coding: utf-8 -*-

import sys

def sx(bits, value):
    sign_bit = 1 << (bits - 1)
    return (value & (sign_bit - 1)) - (value & sign_bit)

SymVar_0 = int(sys.argv[1])
%s
print ref_%s & 0xffffffffffffffff
'''


TEMPLATE_GENERATE_HASH_MD5_SSA = '''\
#!/usr/bin/env python2
## -*- coding: utf-8 -*-

import sys

def sx(bits, value):
    sign_bit = 1 << (bits - 1)
    return (value & (sign_bit - 1)) - (value & sign_bit)

SymVar_0 = int(sys.argv[1])
%s

sys.stdout.write("%%2.2x" %%(ref_%d))
sys.stdout.write("%%2.2x" %%(ref_%d))
sys.stdout.write("%%2.2x" %%(ref_%d))
sys.stdout.write("%%2.2x" %%(ref_%d))
sys.stdout.write("%%2.2x" %%(ref_%d))
sys.stdout.write("%%2.2x" %%(ref_%d))
sys.stdout.write("%%2.2x" %%(ref_%d))
sys.stdout.write("%%2.2x" %%(ref_%d))
sys.stdout.write("%%2.2x" %%(ref_%d))
sys.stdout.write("%%2.2x" %%(ref_%d))
sys.stdout.write("%%2.2x" %%(ref_%d))
sys.stdout.write("%%2.2x" %%(ref_%d))
sys.stdout.write("%%2.2x" %%(ref_%d))
sys.stdout.write("%%2.2x" %%(ref_%d))
sys.stdout.write("%%2.2x" %%(ref_%d))
sys.stdout.write("%%2.2x" %%(ref_%d))
print
'''


TEMPLATE_GENERATE_HASH_SSA_PC1 = '''\
#!/usr/bin/env python2
## -*- coding: utf-8 -*-

import sys

def sx(bits, value):
    sign_bit = 1 << (bits - 1)
    return (value & (sign_bit - 1)) - (value & sign_bit)

SymVar_0 = int(sys.argv[1])

%s

if %s:
%s

else:
%s

print endb & 0xffffffffffffffff
'''


TEMPLATE_GENERATE_INPUT_Z3 = '''\
#!/usr/bin/env python2
## -*- coding: utf-8 -*-

import sys
import z3

def sx(bits, value):
    sign_bit = 1 << (bits - 1)
    return (value & (sign_bit - 1)) - (value & sign_bit)

ctx = z3.Context()
s   = z3.Solver()

SymVar_0 = z3.BitVec('SymVar_0', 64)
a = %s

s.add(a == int(sys.argv[1]))
collisions = 0
while s.check() == z3.sat and collisions < 10:
    print s.model()
    s.add(SymVar_0 != s.model()[SymVar_0])
    collisions += 1
'''


TEMPLATE_GENERATE_INPUT_Z3_SSA = '''\
#!/usr/bin/env python2
## -*- coding: utf-8 -*-

import sys
import z3

def sx(bits, value):
    sign_bit = 1 << (bits - 1)
    return (value & (sign_bit - 1)) - (value & sign_bit)

ctx = z3.Context()
s   = z3.Solver()

SymVar_0 = z3.BitVec('SymVar_0', 64)
%s

s.add(ref_%s == int(sys.argv[1]))
collisions = 0
while s.check() == z3.sat and collisions < 10:
    print s.model()
    s.add(SymVar_0 != s.model()[SymVar_0])
    collisions += 1
'''


TEMPLATE_GENERATE_INPUT_TRITON = '''\
#!/usr/bin/env python2
## -*- coding: utf-8 -*-

import sys
from triton import *

def sx(bits, value):
    sign_bit = 1 << (bits - 1)
    return (value & (sign_bit - 1)) - (value & sign_bit)


setArchitecture(ARCH.X86_64)
SymVar_0 = ast.variable(newSymbolicVariable(64))

a = ast.assert_(
        ast.equal(
            %s,
            ast.bv(int(sys.argv[1]), 64))
    )

models = getModels(a, 5)
for k, m in models.items():
    print m.getName(), m.getValue()
'''
