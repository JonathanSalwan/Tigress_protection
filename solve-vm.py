#!/usr/bin/env python2
## -*- coding: utf-8 -*-

import os
import sys
import struct
import ctypes
import string
import random

from triton    import *
from templates import *

from arybo.tools.triton_ import tritonexprs2arybo, tritonast2arybo
from arybo.lib.exprs_asm import to_llvm_function
from arybo.lib.mba_exprs import eval_expr, ExprCond

# Script options
DEBUG = False
OPPRE = False # opaque predicates

# VMs input
VM_INPUT = '1234'

# Multiple-branches
condition = list()
branches  = list()

# Memory mapping
BASE_PLT   = 0x10000000
BASE_ARGV  = 0x20000000
BASE_ALLOC = 0x30000000
BASE_STACK = 0x9fffffff

# Signal handlers used by raise() and signal()
sigHandlers = dict()

# Allocation information used by malloc()
mallocCurrentAllocation = 0
mallocMaxAllocation     = 2048
mallocBase              = BASE_ALLOC
mallocChunkSize         = 0x00010000



def getMemoryString(addr):
    s = str()
    index = 0

    while getConcreteMemoryValue(addr+index):
        c = chr(getConcreteMemoryValue(addr+index))
        if c not in string.printable: c = ""
        s += c
        index  += 1

    return s


def getFormatString(addr):
    return getMemoryString(addr)                                                    \
           .replace("%s", "{}").replace("%d", "{:d}").replace("%#02x", "{:#02x}")   \
           .replace("%#x", "{:#x}").replace("%x", "{:x}").replace("%02X", "{:02x}") \
           .replace("%c", "{:c}").replace("%02x", "{:02x}").replace("%ld", "{:d}")  \
           .replace("%*s", "").replace("%lX", "{:x}").replace("%08x", "{:08x}")     \
           .replace("%u", "{:d}").replace("%lu", "{:d}")                            \


# Simulate the rand() function
def randHandler():
    print '[+] rand hooked'
    # Return value
    return random.randrange(0xffffffff)


# Simulate the malloc() function
def mallocHandler():
    global mallocCurrentAllocation
    global mallocMaxAllocation
    global mallocBase
    global mallocChunkSize

    print '[+] malloc hooked'

    # Get arguments
    size = getConcreteRegisterValue(REG.RDI)

    if size > mallocChunkSize:
        print '[+] malloc failed: size too big'
        sys.exit(-1)

    if mallocCurrentAllocation >= mallocMaxAllocation:
        print '[+] malloc failed: too many allocations done'
        sys.exit(-1)

    area = mallocBase + (mallocCurrentAllocation * mallocChunkSize)
    mallocCurrentAllocation += 1

    # Return value
    return area


# Simulate the signal() function
def signalHandler():
    print '[+] signal hooked'

    # Get arguments
    signal  = getConcreteRegisterValue(REG.RDI)
    handler = getConcreteRegisterValue(REG.RSI)

    global sigHandlers
    sigHandlers.update({signal: handler})

    # Return value (void)
    return getConcreteRegisterValue(REG.RAX)


# Simulate the raise() function
def raiseHandler():
    print '[+] raise hooked'

    # Get arguments
    signal  = getConcreteRegisterValue(REG.RDI)
    handler = sigHandlers[signal]

    processing(Instruction("\x6A\x00")) # push 0
    emulate(handler)

    # Return value
    return 0


# Simulate the strlen() function
def strlenHandler():
    print '[+] strlen hooked'

    # Get arguments
    arg1 = getMemoryString(getConcreteRegisterValue(REG.RDI))

    # Return value
    return len(arg1)


# Simulate the strtoul() function
def strtoulHandler():
    print '[+] strtoul hooked'

    # Get arguments
    nptr   = getMemoryString(getConcreteRegisterValue(REG.RDI))
    endptr = getConcreteRegisterValue(REG.RSI)
    base   = getConcreteRegisterValue(REG.RDX)

    # Return value
    return long(nptr, base)


# Simulate the printf() function
def printfHandler():
    print '[+] printf hooked'

    # Get arguments
    arg1   = getFormatString(getConcreteRegisterValue(REG.RDI))
    arg2   = getConcreteRegisterValue(REG.RSI)
    arg3   = getConcreteRegisterValue(REG.RDX)
    arg4   = getConcreteRegisterValue(REG.RCX)
    arg5   = getConcreteRegisterValue(REG.R8)
    arg6   = getConcreteRegisterValue(REG.R9)
    nbArgs = arg1.count("{")
    args   = [arg2, arg3, arg4, arg5, arg6][:nbArgs]
    s      = arg1.format(*args)

    sys.stdout.write(s)

    # Return value
    return len(s)


def libcMainHandler():
    print '[+] __libc_start_main hooked'

    # Get arguments
    main = getConcreteRegisterValue(REG.RDI)

    # Push the return value to jump into the main() function
    concretizeRegister(REG.RSP)
    setConcreteRegisterValue(Register(REG.RSP, getConcreteRegisterValue(REG.RSP)-CPUSIZE.QWORD))

    ret2main = MemoryAccess(getConcreteRegisterValue(REG.RSP), CPUSIZE.QWORD, main)
    concretizeMemory(ret2main)
    setConcreteMemoryValue(ret2main)

    # Setup argc / argv
    concretizeRegister(REG.RDI)
    concretizeRegister(REG.RSI)

    argvs = [
        sys.argv[1], # argv[0]
        VM_INPUT,    # argv[1]
    ]

    # Define argc / argv
    base  = BASE_ARGV
    addrs = list()

    index = 0
    for argv in argvs:
        addrs.append(base)
        setConcreteMemoryAreaValue(base, argv+'\x00')
        base += len(argv)+1
        print '[+] argv[%d] = %s' %(index, argv)
        index += 1

    argc = len(argvs)
    argv = base
    for addr in addrs:
        setConcreteMemoryValue(MemoryAccess(base, CPUSIZE.QWORD, addr))
        base += CPUSIZE.QWORD

    setConcreteRegisterValue(Register(REG.RDI, argc))
    setConcreteRegisterValue(Register(REG.RSI, argv))

    return 0


customRelocation = [
    ('__libc_start_main', libcMainHandler, BASE_PLT + 0),
    ('printf',            printfHandler,   BASE_PLT + 1),
    ('strlen',            strlenHandler,   BASE_PLT + 2),
    ('strtoul',           strtoulHandler,  BASE_PLT + 3),
    ('signal',            signalHandler,   BASE_PLT + 4),
    ('raise',             raiseHandler,    BASE_PLT + 5),
    ('rand',              randHandler,     BASE_PLT + 6),
    ('malloc',            mallocHandler,   BASE_PLT + 7),
]


def hookingHandler():
    global condition
    global branches

    pc = getConcreteRegisterValue(REG.RIP)
    for rel in customRelocation:
        if rel[2] == pc:
            # Emulate the routine and the return value
            ret_value = rel[1]()
            concretizeRegister(REG.RAX)
            setConcreteRegisterValue(Register(REG.RAX, ret_value))

            # tigress user input
            if rel[0] == 'strtoul':
                print '[+] Symbolizing the strtoul return'
                var1 = convertRegisterToSymbolicVariable(REG.RAX)
                var0 = getSymbolicVariableFromId(0)
                var0.setConcreteValue(var1.getConcreteValue())
                rax  = getSymbolicExpressionFromId(getSymbolicRegisterId(REG.RAX))
                rax.setAst(ast.variable(var0))

            # tigress user end-point
            if rel[0] == 'printf':
                print '[+] Slicing end-point user expression'
                exprs = sliceExpressions(getSymbolicExpressionFromId(getSymbolicRegisterId(REG.RSI)))
                branches.append(exprs)

            # Get the return address
            ret_addr = getConcreteMemoryValue(MemoryAccess(getConcreteRegisterValue(REG.RSP), CPUSIZE.QWORD))

            # Hijack RIP to skip the call
            concretizeRegister(REG.RIP)
            setConcreteRegisterValue(Register(REG.RIP, ret_addr))

            # Restore RSP (simulate the ret)
            concretizeRegister(REG.RSP)
            setConcreteRegisterValue(Register(REG.RSP, getConcreteRegisterValue(REG.RSP)+CPUSIZE.QWORD))
    return


# Emulate the binary.
def emulate(pc):
    global condition

    count = 0
    while pc:
        # Fetch opcodes
        opcodes = getConcreteMemoryAreaValue(pc, 16)

        # Create the Triton instruction
        instruction = Instruction()
        instruction.setOpcodes(opcodes)
        instruction.setAddress(pc)

        # Process
        processing(instruction)
        count += 1

        if DEBUG:
            print instruction

        if instruction.getType() == OPCODE.HLT:
            break

        if isRegisterSymbolized(REG.RIP) and len(condition) == 0:
            exprs = sliceExpressions(getSymbolicExpressionFromId(getSymbolicRegisterId(REG.RIP)))
            condition.append((instruction.isConditionTaken(), exprs))

        # Simulate routines
        hookingHandler()

        # Next
        pc = getConcreteRegisterValue(REG.RIP)

    print '[+] Instruction executed: %d' %(count)
    print '[+] PC len: %d' %(len(condition))
    return


def loadBinary(binary):
    # Map the binary into the memory
    raw = binary.getRaw()
    phdrs = binary.getProgramHeaders()
    for phdr in phdrs:
        offset = phdr.getOffset()
        size   = phdr.getFilesz()
        vaddr  = phdr.getVaddr()
        print '[+] Loading 0x%06x - 0x%06x' %(vaddr, vaddr+size)
        setConcreteMemoryAreaValue(vaddr, raw[offset:offset+size])
    return


def makeRelocation(binary):
    # Perform our own relocations
    symbols = binary.getSymbolsTable()
    relocations = binary.getRelocationTable()
    for rel in relocations:
        symbolName = symbols[rel.getSymidx()].getName()
        symbolRelo = rel.getOffset()
        for crel in customRelocation:
            if symbolName == crel[0]:
                print '[+] Hooking %s' %(symbolName)
                setConcreteMemoryValue(MemoryAccess(symbolRelo, CPUSIZE.QWORD, crel[2]))
    return


if __name__ == '__main__':
    # Set the architecture
    setArchitecture(ARCH.X86_64)

    # Set optimization
    enableSymbolicOptimization(OPTIMIZATION.ALIGNED_MEMORY, True)
    #enableSymbolicOptimization(OPTIMIZATION.AST_DICTIONARIES, True)
    enableSymbolicOptimization(OPTIMIZATION.ONLY_ON_SYMBOLIZED, True)

    # AST representation as Python syntax
    setAstRepresentationMode(AST_REPRESENTATION.PYTHON)

    if len(sys.argv) != 2:
        print '[-] Syntax: %s <target vm>' %(sys.argv[0])
        sys.exit(1)

    # Parse the binary
    binary = Elf(sys.argv[1])

    # Load the binary
    loadBinary(binary)

    # Perform our own relocations
    makeRelocation(binary)

    # Define a fake stack
    setConcreteRegisterValue(Register(REG.RBP, BASE_STACK))
    setConcreteRegisterValue(Register(REG.RSP, BASE_STACK))

    # Let's emulate the binary from the entry point
    print '[+] Starting emulation.'
    emulate(binary.getHeader().getEntry())
    print '[+] Emulation done.'

    # we got 100% of the hash algorithm.
    if len(condition) == 0 or OPPRE == True:
        exprs = branches[0]

        ssa = str()
        last = 0
        for k, v in sorted(exprs.items()):
            v = str(v).replace('0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF', '0xFFFFFFFFFFFFFFFF') # tmp fix
            ssa += str(v) + '\n'
            last = k

        name = 'symbolic_expressions/%s_input_to_hash.py' %(sys.argv[1].replace('obfuscated_binaries/', ''))
        print '[+] Generating %s' %(name)
        fd = open(name, 'w')
        fd.write(TEMPLATE_GENERATE_HASH_SSA % (ssa, last))
        fd.close()

        print '[+] Converting symbolic expressions to an LLVM module...'
        e = tritonexprs2arybo(exprs)
        var = tritonast2arybo(ast.variable(getSymbolicVariableFromId(0)))
        M = to_llvm_function(e,[var.v])
        name = 'llvm_expressions/%s.ll' %(sys.argv[1].replace('obfuscated_binaries/', ''))
        nameO2 = 'llvm_expressions/%s.O2.ll' %(sys.argv[1].replace('obfuscated_binaries/', ''))
        fd = open(name, 'w')
        fd.write(str(M))
        fd.close()
        os.system("clang++ -O2 -S -emit-llvm -o - %s > %s" %(name, nameO2))
        print '[+] LLVM module wrote in %s' %(name)

        print '[+] Recompiling deobfuscated binary...'
        dst = 'deobfuscated_binaries/%s' %(sys.argv[1].replace('obfuscated_binaries/', '') + '.deobfuscated')
        os.system("clang++ %s -O2 -std=c++11 deobfuscated_binaries/run.cpp -o %s" %(name, dst))
        print '[+] Deobfuscated binary recompiled: %s' %(dst)

    else:
        ssa_pc = str()
        exprs_pc = condition[0][1]
        last_pc = 0
        for k, v in sorted(exprs_pc.items())[:-1]:
            v = str(v).replace('0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF', '0xFFFFFFFFFFFFFFFF') # tmp fix
            ssa_pc += str(v) + '\n'
            last_pc = k

        ssa_b1 = str()
        exprs_b1 = branches[0]
        last_b1 = 0
        for k, v in sorted(exprs_b1.items()):
            v = str(v).replace('0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF', '0xFFFFFFFFFFFFFFFF') # tmp fix
            ssa_b1 += '    ' + str(v) + '\n'
            last_b1 = k
        ssa_b1 += '    endb = ref_%d\n' %(last_b1)

        pcAst = getPathConstraintsAst()
        newInput = ast.assert_(ast.lnot(pcAst))
        model = getModel(newInput)
        if model:
            global VM_INPUT
            VM_INPUT = str(model[0].getValue())

        # Re-simulate an execution
        # Define a fake stack
        concretizeAllMemory()
        concretizeAllRegister()
        setConcreteRegisterValue(Register(REG.RBP, BASE_STACK))
        setConcreteRegisterValue(Register(REG.RSP, BASE_STACK))

        # Let's emulate the binary from the entry point
        print '[+] Starting emulation.'
        emulate(binary.getHeader().getEntry())
        print '[+] Emulation done.'

        ssa_b2 = str()
        exprs_b2 = branches[1]
        last_b2 = 0
        for k, v in sorted(exprs_b2.items()):
            v = str(v).replace('0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF', '0xFFFFFFFFFFFFFFFF') # tmp fix
            ssa_b2 += '    ' + str(v) + '\n'
            last_b2 = k
        ssa_b2 += '    endb = ref_%d\n' %(last_b2)

        name = 'symbolic_expressions/%s_input_to_hash.py' %(sys.argv[1].replace('obfuscated_binaries/', ''))
        print '[+] Generating %s' %(name)
        fd = open(name, 'w')
        if condition[0][0]:
            fd.write(TEMPLATE_GENERATE_HASH_SSA_PC1 % (ssa_pc, 'ref_%s == 0x1' %(last_pc), ssa_b1, ssa_b2))
        else:
            fd.write(TEMPLATE_GENERATE_HASH_SSA_PC1 % (ssa_pc, 'ref_%s == 0x1' %(last_pc), ssa_b2, ssa_b1))
        fd.close()

        print '[+] Converting symbolic expressions to an LLVM module...'

        last_pc = 0
        exprs_pc = condition[0][1]
        for k, v in sorted(exprs_pc.items()):
            last_pc = k
        del condition[0][1][last_pc]

        c   = tritonexprs2arybo(condition[0][1])
        e1  = tritonexprs2arybo(branches[0])
        e2  = tritonexprs2arybo(branches[1])
        var = tritonast2arybo(ast.variable(getSymbolicVariableFromId(0)))
        if condition[0][0]:
            M = to_llvm_function(ExprCond(c, e1, e2), [var.v])
        else:
            M = to_llvm_function(ExprCond(c, e2, e1), [var.v])
        name = 'llvm_expressions/%s.ll' %(sys.argv[1].replace('obfuscated_binaries/', ''))
        nameO2 = 'llvm_expressions/%s.O2.ll' %(sys.argv[1].replace('obfuscated_binaries/', ''))
        fd = open(name, 'w')
        fd.write(str(M))
        fd.close()
        os.system("clang++ -O2 -S -emit-llvm -o - %s > %s" %(name, nameO2))
        print '[+] LLVM module wrote in %s' %(name)

        print '[+] Recompiling deobfuscated binary...'
        dst = 'deobfuscated_binaries/%s' %(sys.argv[1].replace('obfuscated_binaries/', '') + '.deobfuscated')
        os.system("clang++ %s -O2 -std=c++11 deobfuscated_binaries/run.cpp -o %s" %(name, dst))
        print '[+] Deobfuscated binary recompiled: %s' %(dst)

    sys.exit(0)
