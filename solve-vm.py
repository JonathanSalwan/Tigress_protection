#!/usr/bin/env python
## -*- coding: utf-8 -*-
##
## Jonathan Salwan
##

import ctypes
import os
import random
import string
import struct
import sys
import time
import lief

from triton             import *
from scripts.templates  import *

# Used for nested vm
sys.setrecursionlimit(100000)

# Script options
DEBUG   = True
METRICS = True
OPAQUE  = False

# The debug function
def debug(s):
    if DEBUG: print(s)

# VMs input
VM_INPUT = b'1234'

# Multiple-paths
condition = list()
paths = list()

# Memory mapping
BASE_PLT   = 0x10000000
BASE_ARGV  = 0x20000000
BASE_ALLOC = 0x30000000
BASE_STACK = 0x9fffffff

# Signal handlers used by raise() and signal()
sigHandlers = dict()

# File descriptors used by fopen() and fprintf()
fdHandlers = dict()

# Allocation information used by malloc()
mallocCurrentAllocation = 0
mallocMaxAllocation     = 2048
mallocBase              = BASE_ALLOC
mallocChunkSize         = 0x00010000

# Total of instructions executed
totalInstructions = 0
totalUniqueInstructions = {}

# Total of functions simulated
totalFunctions = 0

# Time of execution
startTime = None
endTime   = None



def getMemoryString(ctx, addr):
    s = str()
    index = 0

    while ctx.getConcreteMemoryValue(addr+index):
        c = chr(ctx.getConcreteMemoryValue(addr+index))
        if c not in string.printable: c = ""
        s += c
        index  += 1

    return s


def getFormatString(ctx, addr):
    return getMemoryString(ctx, addr)                                               \
           .replace("%s", "{}").replace("%d", "{:d}").replace("%#02x", "{:#02x}")   \
           .replace("%#x", "{:#x}").replace("%x", "{:x}").replace("%02X", "{:02x}") \
           .replace("%c", "{:c}").replace("%02x", "{:02x}").replace("%ld", "{:d}")  \
           .replace("%*s", "").replace("%lX", "{:x}").replace("%08x", "{:08x}")     \
           .replace("%u", "{:d}").replace("%lu", "{:d}")                            \


# Simulate the rand() function
def randHandler(ctx):
    debug('[+] rand hooked')
    # Return value
    return random.randrange(0xffffffff)


# Simulate the malloc() function
def mallocHandler(ctx):
    global mallocCurrentAllocation
    global mallocMaxAllocation
    global mallocBase
    global mallocChunkSize

    debug('[+] malloc hooked')

    # Get arguments
    size = ctx.getConcreteRegisterValue(ctx.registers.rdi)

    if size > mallocChunkSize:
        debug('[+] malloc failed: size too big')
        sys.exit(-1)

    if mallocCurrentAllocation >= mallocMaxAllocation:
        debug('[+] malloc failed: too many allocations done')
        sys.exit(-1)

    area = mallocBase + (mallocCurrentAllocation * mallocChunkSize)
    mallocCurrentAllocation += 1

    # Return value
    return area


# Simulate the calloc() function
def callocHandler(ctx):
    global mallocCurrentAllocation
    global mallocMaxAllocation
    global mallocBase
    global mallocChunkSize

    debug('[+] malloc hooked')

    # Get arguments
    nmemb = ctx.getConcreteRegisterValue(ctx.registers.rdi)
    size  = ctx.getConcreteRegisterValue(ctx.registers.rsi)

    # Total size
    size = nmemb * size

    if size > mallocChunkSize:
        debug('[+] malloc failed: size too big')
        sys.exit(-1)

    if mallocCurrentAllocation >= mallocMaxAllocation:
        debug('[+] malloc failed: too many allocations done')
        sys.exit(-1)

    area = mallocBase + (mallocCurrentAllocation * mallocChunkSize)
    mallocCurrentAllocation += 1

    # Return value
    return area


# Simulate the memcpy() function
def memcpyHandler(ctx):
    debug('[+] memcpy hooked')

    # Get arguments
    arg1 = ctx.getConcreteRegisterValue(ctx.registers.rdi)
    arg2 = ctx.getConcreteRegisterValue(ctx.registers.rsi)
    arg3 = ctx.getConcreteRegisterValue(ctx.registers.rdx)
    mems = ctx.getSymbolicMemory()

    for index in range(arg3):
        ctx.concretizeMemory(arg1 + index)
        ctx.setConcreteMemoryValue(arg1 + index, ctx.getConcreteMemoryValue(arg2 + index))
        try:
            ctx.assignSymbolicExpressionToMemory(mems[arg2 + index], MemoryAccess(arg1 + index, CPUSIZE.BYTE))
        except:
            pass

    return arg1


# Simulate the memset() function
def memsetHandler(ctx):
    debug('[+] memset hooked')

    dst = ctx.getConcreteRegisterValue(ctx.registers.rdi)
    src = ctx.getConcreteRegisterValue(ctx.registers.rsi)
    size = ctx.getConcreteRegisterValue(ctx.registers.rdx)

    for index in range(size):
        dmem = MemoryAccess(dst + index, CPUSIZE.BYTE)
        cell = ctx.getAstContext().extract(7, 0, ctx.getRegisterAst(ctx.registers.rsi))
        expr = ctx.newSymbolicExpression(cell, "memset byte")
        ctx.setConcreteMemoryValue(dmem, cell.evaluate())
        ctx.assignSymbolicExpressionToMemory(expr, dmem)

    return dst


# Simulate the signal() function
def signalHandler(ctx):
    debug('[+] signal hooked')

    # Get arguments
    signal  = ctx.getConcreteRegisterValue(ctx.registers.rdi)
    handler = ctx.getConcreteRegisterValue(ctx.registers.rsi)

    global sigHandlers
    sigHandlers.update({signal: handler})

    # Return value (void)
    return ctx.getConcreteRegisterValue(ctx.registers.rax)


# Simulate the raise() function
def raiseHandler(ctx):
    debug('[+] raise hooked')

    # Get arguments
    signal  = ctx.getConcreteRegisterValue(ctx.registers.rdi)
    handler = sigHandlers[signal]

    ctx.processing(Instruction(b"\x6A\x00")) # push 0
    emulate(ctx, handler)

    # Return value
    return 0


# Simulate the strlen() function
def strlenHandler(ctx):
    debug('[+] strlen hooked')

    # Get arguments
    arg1 = getMemoryString(ctx, ctx.getConcreteRegisterValue(ctx.registers.rdi))

    # Return value
    return len(arg1)


# Simulate the strtoul() function
def strtoulHandler(ctx):
    debug('[+] strtoul hooked')

    # Get arguments
    nptr   = getMemoryString(ctx, ctx.getConcreteRegisterValue(ctx.registers.rdi))
    endptr = ctx.getConcreteRegisterValue(ctx.registers.rsi)
    base   = ctx.getConcreteRegisterValue(ctx.registers.rdx)

    # Return value
    return int(nptr, base)


# Simulate the printf() function
def printfHandler(ctx):
    debug('[+] printf hooked')

    # Get arguments
    arg1   = getFormatString(ctx, ctx.getConcreteRegisterValue(ctx.registers.rdi))
    arg2   = ctx.getConcreteRegisterValue(ctx.registers.rsi)
    arg3   = ctx.getConcreteRegisterValue(ctx.registers.rdx)
    arg4   = ctx.getConcreteRegisterValue(ctx.registers.rcx)
    arg5   = ctx.getConcreteRegisterValue(ctx.registers.r8)
    arg6   = ctx.getConcreteRegisterValue(ctx.registers.r9)
    nbArgs = arg1.count("{")
    args   = [arg2, arg3, arg4, arg5, arg6][:nbArgs]
    s      = arg1.format(*args)

    if DEBUG:
        sys.stdout.write(s)

    # Return value
    return len(s)


# Simulate the putchar() function
def putcharHandler(ctx):
    debug('[+] putchar hooked')

    # Get arguments
    arg1 = ctx.getConcreteRegisterValue(ctx.registers.rdi)
    sys.stdout.write(chr(arg1) + '\n')

    # Return value
    return 2


# Simulate the puts() function
def putsHandler(ctx):
    debug('[+] puts hooked')

    # Get arguments
    arg1 = getMemoryString(ctx, ctx.getConcreteRegisterValue(ctx.registers.rdi))
    sys.stdout.write(arg1 + '\n')

    # Return value
    return len(arg1) + 1


# Simulate the printf() function
def fprintfHandler(ctx):
    global fdHandlers
    debug('[+] fprintf hooked')

    # Get arguments
    arg1   = ctx.getConcreteRegisterValue(ctx.registers.rdi)
    arg2   = getFormatString(ctx, ctx.getConcreteRegisterValue(ctx.registers.rsi))
    arg3   = ctx.getConcreteRegisterValue(ctx.registers.rdx)
    arg4   = ctx.getConcreteRegisterValue(ctx.registers.rcx)
    arg5   = ctx.getConcreteRegisterValue(ctx.registers.r8)
    arg6   = ctx.getConcreteRegisterValue(ctx.registers.r9)
    nbArgs = arg2.count("{")
    args   = [arg3, arg4, arg5, arg6][:nbArgs]
    s      = arg2.format(*args)

    fdHandlers[arg1].write(s)

    # Return value
    return len(s)


# Simulate the free() function (skip this behavior)
def freeHandler(ctx):
    debug('[+] free hooked')
    return None


# Simulate the fopen() function
def fopenHandler(ctx):
    global fdHandlers
    debug('[+] fopen hooked')

    # Get arguments
    arg1   = getFormatString(ctx, ctx.getConcreteRegisterValue(ctx.registers.rdi))
    arg2   = getFormatString(ctx, ctx.getConcreteRegisterValue(ctx.registers.rsi))

    fd = open(arg1, arg2)
    idf = len(fdHandlers) + 3 # 3 because 0, 1, 3 are already reserved.
    fdHandlers.update({idf : fd})

    # Return value
    return idf


def libcMainHandler(ctx):
    debug('[+] __libc_start_main hooked')

    # Get arguments
    main = ctx.getConcreteRegisterValue(ctx.registers.rdi)

    # Push the return value to jump into the main() function
    ctx.concretizeRegister(ctx.registers.rsp)
    ctx.setConcreteRegisterValue(ctx.registers.rsp, ctx.getConcreteRegisterValue(ctx.registers.rsp)-CPUSIZE.QWORD)

    ret2main = MemoryAccess(ctx.getConcreteRegisterValue(ctx.registers.rsp), CPUSIZE.QWORD)
    ctx.concretizeMemory(ret2main)
    ctx.setConcreteMemoryValue(ret2main, main)

    # Setup argc / argv
    ctx.concretizeRegister(ctx.registers.rdi)
    ctx.concretizeRegister(ctx.registers.rsi)

    argvs = [
        bytes(sys.argv[1].encode('utf-8')), # argv[0]
        bytes(VM_INPUT),                    # argv[1]
    ]

    # Define argc / argv
    base  = BASE_ARGV
    addrs = list()

    index = 0
    for argv in argvs:
        addrs.append(base)
        ctx.setConcreteMemoryAreaValue(base, list(argv+b'\x00'))
        base += len(argv)+1
        debug('[+] argv[%d] = %s' %(index, argv))
        index += 1

    argc = len(argvs)
    argv = base
    for addr in addrs:
        ctx.setConcreteMemoryValue(MemoryAccess(base, CPUSIZE.QWORD), addr)
        base += CPUSIZE.QWORD

    ctx.setConcreteRegisterValue(ctx.registers.rdi, argc)
    ctx.setConcreteRegisterValue(ctx.registers.rsi, argv)

    return 0


def errnoHandler(ctx):
    debug('[+] __errno_location hooked')

    errno = 0xdeadbeaf
    ctx.setConcreteMemoryValue(MemoryAccess(errno, CPUSIZE.QWORD), 0)

    return errno


customRelocation = [
    ('__libc_start_main', libcMainHandler, BASE_PLT + 0),
    ('__errno_location',  errnoHandler,    BASE_PLT + 1),
    ('calloc',            callocHandler,   BASE_PLT + 2),
    ('fopen',             fopenHandler,    BASE_PLT + 3),
    ('fprintf',           fprintfHandler,  BASE_PLT + 4),
    ('free',              freeHandler,     BASE_PLT + 5),
    ('malloc',            mallocHandler,   BASE_PLT + 6),
    ('memcpy',            memcpyHandler,   BASE_PLT + 7),
    ('memset',            memsetHandler,   BASE_PLT + 8),
    ('printf',            printfHandler,   BASE_PLT + 9),
    ('putchar',           putcharHandler,  BASE_PLT + 10),
    ('puts',              putsHandler,     BASE_PLT + 11),
    ('raise',             raiseHandler,    BASE_PLT + 12),
    ('rand',              randHandler,     BASE_PLT + 13),
    ('signal',            signalHandler,   BASE_PLT + 14),
    ('strlen',            strlenHandler,   BASE_PLT + 15),
    ('strtoul',           strtoulHandler,  BASE_PLT + 16),
    ('strtoull',          strtoulHandler,  BASE_PLT + 17),
]


def hookingHandler(ctx):
    global condition
    global paths
    global totalFunctions

    pc = ctx.getConcreteRegisterValue(ctx.registers.rip)
    for rel in customRelocation:
        if rel[2] == pc:
            # Emulate the routine and the return value
            ret_value = rel[1](ctx)
            if ret_value is not None:
                ctx.concretizeRegister(ctx.registers.rax)
                ctx.setConcreteRegisterValue(ctx.registers.rax, ret_value)

            # Used for metric
            totalFunctions += 1

            # tigress user input
            if rel[0] == 'strtoul':
                debug('[+] Symbolizing the strtoul return')
                var1 = ctx.symbolizeRegister(ctx.registers.rax)
                var0 = ctx.getSymbolicVariable(0)
                ctx.setConcreteVariableValue(var0, ctx.getConcreteVariableValue(var1))
                rax = ctx.getSymbolicRegister(ctx.registers.rax)
                ast = ctx.getAstContext()
                rax.setAst(ast.variable(var0))

            # tigress user end-point
            if rel[0] == 'printf':
                debug('[+] Slicing end-point user expression')
                if ctx.getSymbolicRegister(ctx.registers.rsi):
                    exprs = ctx.sliceExpressions(ctx.getSymbolicRegister(ctx.registers.rsi))
                    paths.append(exprs)
                #else:
                #    ast = ctx.getAstContext()
                #    n = ctx.newSymbolicExpression(ast.bv(ctx.getConcreteRegisterValue(ctx.registers.rsi), 64))
                #    exprs = {n.getId() : n}
                #    paths.append(exprs)
                else:
                    debug('[+] -------------------------------------------------------------- ')
                    debug('[+] /!\ /!\ /!\ /!\ /!\ /!\ Symbolic lost! /!\ /!\ /!\ /!\ /!\ /!\ ')
                    debug('[+] -------------------------------------------------------------- ')
                    sys.exit(-1)

            # Get the return address
            ret_addr = ctx.getConcreteMemoryValue(MemoryAccess(ctx.getConcreteRegisterValue(ctx.registers.rsp), CPUSIZE.QWORD))

            # Hijack RIP to skip the call
            ctx.concretizeRegister(ctx.registers.rip)
            ctx.setConcreteRegisterValue(ctx.registers.rip, ret_addr)

            # Restore RSP (simulate the ret)
            ctx.concretizeRegister(ctx.registers.rsp)
            ctx.setConcreteRegisterValue(ctx.registers.rsp, ctx.getConcreteRegisterValue(ctx.registers.rsp)+CPUSIZE.QWORD)
    return


# Emulate the binary.
def emulate(ctx, pc):
    global condition
    global totalInstructions
    global totalUniqueInstructions

    count = 0
    while pc:
        # Fetch opcodes
        opcodes = ctx.getConcreteMemoryAreaValue(pc, 16)

        # Create the Triton instruction
        instruction = Instruction()
        instruction.setOpcode(opcodes)
        instruction.setAddress(pc)

        # Process
        if ctx.processing(instruction) != EXCEPTION.NO_FAULT:
            debug('[-] Instruction not supported: %s' %(str(instruction)))
            break

        #print(instruction)

        count += 1

        if pc in totalUniqueInstructions:
            totalUniqueInstructions[pc] += 1
        else:
            totalUniqueInstructions[pc] = 1

        if instruction.getType() == OPCODE.X86.HLT:
            break

        if ctx.isRegisterSymbolized(ctx.registers.rip) and len(condition) == 0:
            exprs = ctx.sliceExpressions(ctx.getSymbolicRegister(ctx.registers.rip))
            condition.append((instruction.isConditionTaken(), exprs))

        # Simulate routines
        hookingHandler(ctx)

        # Next
        pc = ctx.getConcreteRegisterValue(ctx.registers.rip)

    debug('[+] Instruction executed: %d' %(count))
    debug('[+] Unique instruction executed: %d' %(len(totalUniqueInstructions)))
    debug('[+] PC len: %d' %(len(condition)))

    # Used for metric
    totalInstructions += count
    return


def loadBinary(ctx, binary):
    # Map the binary into the memory
    phdrs = binary.segments
    for phdr in phdrs:
        size   = phdr.physical_size
        vaddr  = phdr.virtual_address
        debug('[+] Loading 0x%06x - 0x%06x' %(vaddr, vaddr+size))
        ctx.setConcreteMemoryAreaValue(vaddr, list(phdr.content))
    return


def makeRelocation(ctx, binary):
    # Perform our own relocations
    try:
        for rel in binary.pltgot_relocations:
            symbolName = rel.symbol.name
            symbolRelo = rel.address
            for crel in customRelocation:
                if symbolName == crel[0]:
                    debug('[+] Hooking %s' %(symbolName))
                    ctx.setConcreteMemoryValue(MemoryAccess(symbolRelo, CPUSIZE.QWORD), crel[2])
    except:
        pass

    # Perform our own relocations
    try:
        for rel in binary.dynamic_relocations:
            symbolName = rel.symbol.name
            symbolRelo = rel.address
            for crel in customRelocation:
                if symbolName == crel[0]:
                    debug('[+] Hooking %s' %(symbolName))
                    ctx.setConcreteMemoryValue(MemoryAccess(symbolRelo, CPUSIZE.QWORD), crel[2])
    except:
        pass
    return


def recompile(M):
    name = 'llvm_expressions/%s.ll' %(sys.argv[1].split('/')[-1])
    nameO2 = 'llvm_expressions/%s.O2.ll' %(sys.argv[1].split('/')[-1])
    fd = open(name, 'w')
    M = str(M).replace('unknown-unknown-unknown', 'x86_64-pc-linux-gnu')
    fd.write(M)
    fd.close()
    os.system("clang -O2 -S -emit-llvm -o - %s > %s" %(name, nameO2))
    debug('[+] LLVM module wrote in %s' %(name))

    debug('[+] Recompiling deobfuscated binary...')
    dst = 'deobfuscated_binaries/%s' %(sys.argv[1].split('/')[-1] + '.deobfuscated')
    os.system("clang %s -O2 deobfuscated_binaries/run.c -o %s" %(name, dst))
    debug('[+] Deobfuscated binary recompiled: %s' %(dst))
    return


def run(ctx, binary):
    # Concretize previous context
    ctx.concretizeAllMemory()
    ctx.concretizeAllRegister()

    # Define a fake stack
    ctx.setConcreteRegisterValue(ctx.registers.rbp, BASE_STACK)
    ctx.setConcreteRegisterValue(ctx.registers.rsp, BASE_STACK)

    # Let's emulate the binary from the entry point
    debug('[+] Starting emulation.')
    emulate(ctx, binary.entrypoint)
    debug('[+] Emulation done.')
    return


def metrics():
    global METRICS
    if METRICS:
        print('--------------------------------------------------------------------')
        print('->', sys.argv[1].split('/')[-1])
        print('   Instructions executed:', totalInstructions)
        print('   Unique Instructions executed:', len(totalUniqueInstructions))
        print('   Functions simulated:', totalFunctions)
        print('   Time of analysis:', endTime - startTime, "seconds")
    return


def generateSymbolicExpressions(pathNumber):
    global paths
    exprs = paths[pathNumber]

    ssa = str()
    last = 0
    for k, v in sorted(exprs.items()):
        ssa += str(v) + '\n'
        last = k

    name = 'symbolic_expressions/%s.py' %(sys.argv[1].split('/')[-1])
    debug('[+] Generating %s' %(name))
    fd = open(name, 'w')
    fd.write(TEMPLATE_GENERATE_HASH_SSA % (ssa, last))
    fd.close()
    return last


def generateLLVMExpressions(ctx, pathNumber, last):
    global paths
    exprs = paths[pathNumber]

    debug('[+] Converting symbolic expressions to an LLVM module...')
    M = ctx.liftToLLVM(exprs[last], fname="SECRET", optimize=True)

    return M


def main():
    global VM_INPUT
    global condition
    global paths

    # Get a Triton context
    ctx = TritonContext()

    # Set the architecture
    ctx.setArchitecture(ARCH.X86_64)

    # Set optimization
    ctx.setMode(MODE.ALIGNED_MEMORY, True)
    ctx.setMode(MODE.ONLY_ON_SYMBOLIZED, True)

    # AST representation as Python syntax
    ctx.setAstRepresentationMode(AST_REPRESENTATION.PYTHON)

    if len(sys.argv) != 2:
        debug('[-] Syntax: %s <target vm>' %(sys.argv[0]))
        return -1

    # Parse the binary
    binary = lief.parse(sys.argv[1])

    # Load the binary
    loadBinary(ctx, binary)

    # Perform our own relocations
    makeRelocation(ctx, binary)

    # Init and emulate
    run(ctx, binary)

    # we got 100% of code coverage (there is only one path).
    if len(condition) == 0 or OPAQUE == True:
        # Generate symbolic epxressions of the first path
        last = generateSymbolicExpressions(0)

        # Generate llvm of the first path
        M = generateLLVMExpressions(ctx, 0, last)

        # Recompile the LLVM-IL
        recompile(M)
    else:
        ssa_pc   = str()
        exprs_pc = condition[0][1]
        last_pc  = None
        for k, v in sorted(exprs_pc.items()):
            ssa_pc += str(v) + '\n'
            last_pc = v

        ssa_b1   = str()
        exprs_b1 = paths[0]
        last_b1 = 0
        for k, v in sorted(exprs_b1.items()):
            ssa_b1 += '    ' + str(v) + '\n'
            last_b1 = k
        ssa_b1 += '    endb = ref_%d\n' %(last_b1)

        debug('[+] Asking for a new input...')
        pcAst = ctx.getPathPredicate()
        ast   = ctx.getAstContext()
        model = ctx.getModel(ast.lnot(pcAst))
        if model:
            VM_INPUT = str(model[0].getValue())
        else:
            debug('[+] No model found! Opaque predicate?')
            # Generate symbolic epxressions of the first path
            last = generateSymbolicExpressions(0)

            # Generate llvm of the first path
            M = generateLLVMExpressions(ctx, 0, last)

            # Recompile the LLVM-IL
            recompile(M)
            return 0

        # Re-simulate an execution to take another path
        run(ctx, binary)

        ssa_b2 = str()
        exprs_b2 = paths[1]
        last_b2 = 0
        for k, v in sorted(exprs_b2.items()):
            ssa_b2 += '    ' + str(v) + '\n'
            last_b2 = k
        ssa_b2 += '    endb = ref_%d\n' %(last_b2)

        name = 'symbolic_expressions/%s.py' %(sys.argv[1].split('/')[-1])
        debug('[+] Generating %s' %(name))
        fd = open(name, 'w')
        if condition[0][0]:
            fd.write(TEMPLATE_GENERATE_HASH_SSA_PC1 % (ssa_pc, '%s' %(str(last_pc.getAst().getChildren()[0])), ssa_b1, ssa_b2))
        else:
            fd.write(TEMPLATE_GENERATE_HASH_SSA_PC1 % (ssa_pc, '%s' %(str(last_pc.getAst().getChildren()[0])), ssa_b2, ssa_b1))
        fd.close()

        debug('[+] Converting symbolic expressions to an LLVM module...')
        last_pc_expr = None
        last_pc_id   = 0
        exprs_pc = condition[0][1]
        for k, v in sorted(exprs_pc.items()):
            last_pc_expr = v
            last_pc_id = k
        del condition[0][1][last_pc_id]

        ast  = ctx.getAstContext()
        nc   = ast.ite(last_pc_expr.getAst().getChildren()[0], ast.bvtrue(), ast.bvfalse())
        expr = ctx.newSymbolicExpression(nc)
        condition[0][1][expr.getId()] = expr

        c   = tritonexprs2arybo(condition[0][1])
        e1  = tritonexprs2arybo(paths[0])
        e2  = tritonexprs2arybo(paths[1])
        ast = ctx.getAstContext()
        var = tritonast2arybo(ast.variable(ctx.getSymbolicVariable(0)))
        if condition[0][0]:
            M = to_llvm_function(ExprCond(c, e1, e2), [var.v])
        else:
            M = to_llvm_function(ExprCond(c, e2, e1), [var.v])

        # Recompile the LLVM-IL
        recompile(M)

    return 0


if __name__ == '__main__':
    startTime = time.time()
    retValue  = main()
    endTime   = time.time()

    metrics()
    sys.exit(retValue)
