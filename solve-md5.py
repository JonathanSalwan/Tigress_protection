#!/usr/bin/env python2
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

from arybo.tools.triton_ import tritonexprs2arybo, tritonast2arybo
from arybo.lib.exprs_asm import to_llvm_function
from arybo.lib.mba_exprs import ExprCond

# Used for nested vm
sys.setrecursionlimit(100000)

# Script options
DEBUG   = True
METRICS = True

# The debug function
def debug(s):
    if DEBUG: print s

# VMs input
VM_INPUT = '1234'

# Multiple-paths
condition = list()
slices = list()

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
           .replace("%u", "{:d}").replace("%lu", "{:d}").replace("%2.2x", "{:02x}") \


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

    debug('[+] calloc hooked')

    # Get arguments
    nmemb = ctx.getConcreteRegisterValue(ctx.registers.rdi)
    size  = ctx.getConcreteRegisterValue(ctx.registers.rsi)

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
    dst  = ctx.getConcreteRegisterValue(ctx.registers.rdi)
    src  = ctx.getConcreteRegisterValue(ctx.registers.rsi)
    size = ctx.getConcreteRegisterValue(ctx.registers.rdx)

    for index in range(size):
        ctx.concretizeMemory(dst + index)
        ctx.setConcreteMemoryValue(dst + index, ctx.getConcreteMemoryValue(src + index))
        expr = ctx.getSymbolicMemory(src + index)
        if expr is not None:
            ctx.assignSymbolicExpressionToMemory(expr, MemoryAccess(dst + index, CPUSIZE.BYTE))

    return dst


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

    ctx.processing(Instruction("\x6A\x00")) # push 0
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
    return long(nptr, base)


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


# Simulate the free() function
def freeHandler(ctx):
    debug('[+] free hooked')
    rax = ctx.getConcreteRegisterValue(ctx.registers.rax)
    return rax


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
        sys.argv[1], # argv[0]
        VM_INPUT,    # argv[1]
    ]

    # Define argc / argv
    base  = BASE_ARGV
    addrs = list()

    index = 0
    for argv in argvs:
        addrs.append(base)
        ctx.setConcreteMemoryAreaValue(base, argv+'\x00')
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


customRelocation = [
    ('__libc_start_main', libcMainHandler, BASE_PLT + 0),
    ('calloc',            callocHandler,   BASE_PLT + 1),
    ('fopen',             fopenHandler,    BASE_PLT + 2),
    ('fprintf',           fprintfHandler,  BASE_PLT + 3),
    ('free',              freeHandler,     BASE_PLT + 4),
    ('malloc',            mallocHandler,   BASE_PLT + 5),
    ('memcpy',            memcpyHandler,   BASE_PLT + 6),
    ('memset',            memsetHandler,   BASE_PLT + 7),
    ('printf',            printfHandler,   BASE_PLT + 8),
    ('raise',             raiseHandler,    BASE_PLT + 9),
    ('rand',              randHandler,     BASE_PLT + 10),
    ('signal',            signalHandler,   BASE_PLT + 11),
    ('strlen',            strlenHandler,   BASE_PLT + 12),
    ('strtoul',           strtoulHandler,  BASE_PLT + 13),
]


def hookingHandler(ctx):
    global condition
    global slices
    global totalFunctions

    pc = ctx.getConcreteRegisterValue(ctx.registers.rip)
    for rel in customRelocation:
        if rel[2] == pc:
            # Emulate the routine and the return value
            ret_value = rel[1](ctx)
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
                slices.append(ctx.sliceExpressions(ctx.getSymbolicRegister(ctx.registers.rsi)))
                slices.append(ctx.sliceExpressions(ctx.getSymbolicRegister(ctx.registers.rdx)))
                slices.append(ctx.sliceExpressions(ctx.getSymbolicRegister(ctx.registers.rcx)))
                slices.append(ctx.sliceExpressions(ctx.getSymbolicRegister(ctx.registers.r8)))

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
        if ctx.processing(instruction) == False:
            debug('[-] Instruction not supported: %s' %(str(instruction)))
            break

        count += 1

        #print instruction
        #if count % 10000 == 0:
        #    print "(%d, %.02f)" %(count, time.clock() - startTime)
        #if count >= 300000:
        #    sys.exit(0)

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
        ctx.setConcreteMemoryAreaValue(vaddr, phdr.content)
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
    os.system("clang %s -O2 deobfuscated_binaries/run_md5.c -o %s" %(name, dst))
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
    #emulate(ctx, binary.entrypoint)
    emulate(ctx, 0x4010C4)
    debug('[+] Emulation done.')
    return


def metrics():
    global METRICS
    if METRICS:
        print '--------------------------------------------------------------------'
        print '->', sys.argv[1].split('/')[-1]
        print '\tInstructions executed:', totalInstructions
        print '\tUnique Instructions executed:', len(totalUniqueInstructions)
        print '\tFunctions simulated:', totalFunctions
        print '\tTime of analysis:', endTime - startTime, "seconds"
    return


def generateSymbolicExpressions(trace, ihash):
    ssa = str()
    for k, v in sorted(trace.items()):
        ssa += str(v) + '\n'

    name = 'symbolic_expressions/%s.py' %(sys.argv[1].split('/')[-1])
    debug('[+] Generating %s' %(name))
    fd = open(name, 'w')
    fd.write(TEMPLATE_GENERATE_HASH_MD5_SSA
              %(ssa,
                ihash[0].getId(),
                ihash[1].getId(),
                ihash[2].getId(),
                ihash[3].getId(),
                ihash[4].getId(),
                ihash[5].getId(),
                ihash[6].getId(),
                ihash[7].getId(),
                ihash[8].getId(),
                ihash[9].getId(),
                ihash[10].getId(),
                ihash[11].getId(),
                ihash[12].getId(),
                ihash[13].getId(),
                ihash[14].getId(),
                ihash[15].getId()
              )
            )
    fd.close()
    return


def generateLLVMExpressions(ctx, trace):
    debug('[+] Converting symbolic expressions to an LLVM module...')
    e = tritonexprs2arybo(trace)
    var = tritonast2arybo(ctx.getAstContext().variable(ctx.getSymbolicVariable(0)))
    M = to_llvm_function(e,[var.v], "SECRET")
    return M


def main():
    global VM_INPUT
    global condition
    global slices

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

    trace = dict()
    index = 0
    ihash = list()
    rhash = dict()
    for s in slices:
        expr = sorted(s.items())[-1][1]
        expr.setComment('md5: h%02d' %(index))
        trace.update(s)
        ihash.append(expr)
        rhash.update({index: expr.getId()})
        index += 1

    # ref_1461340 = (ref_1461336 & 0xFFFFFFFF) # md5: h00
    # ref_1461330 = (ref_1461328 & 0xFF) # md5: h01
    # ref_1461316 = (ref_1461314 & 0xFF) # md5: h02
    # ref_1461338 = (ref_1461302 & 0xFFFFFFFF) # md5: h03
    # ref_1461418 = (ref_1461414 & 0xFFFFFFFF) # md5: h04
    # ref_1461408 = (ref_1461406 & 0xFF) # md5: h05
    # ref_1461394 = (ref_1461392 & 0xFF) # md5: h06
    # ref_1461416 = (ref_1461380 & 0xFFFFFFFF) # md5: h07
    # ref_1461496 = (ref_1461492 & 0xFFFFFFFF) # md5: h08
    # ref_1461486 = (ref_1461484 & 0xFF) # md5: h09
    # ref_1461472 = (ref_1461470 & 0xFF) # md5: h10
    # ref_1461494 = (ref_1461458 & 0xFFFFFFFF) # md5: h11
    # ref_1461574 = (ref_1461570 & 0xFFFFFFFF) # md5: h12
    # ref_1461564 = (ref_1461562 & 0xFF) # md5: h13
    # ref_1461550 = (ref_1461548 & 0xFF) # md5: h14
    # ref_1461572 = (ref_1461536 & 0xFFFFFFFF) # md5: h15

    h0  = ctx.getSymbolicExpression(rhash[0])
    h1  = ctx.getSymbolicExpression(rhash[1])
    h2  = ctx.getSymbolicExpression(rhash[2])
    h3  = ctx.getSymbolicExpression(rhash[3])
    h4  = ctx.getSymbolicExpression(rhash[4])
    h5  = ctx.getSymbolicExpression(rhash[5])
    h6  = ctx.getSymbolicExpression(rhash[6])
    h7  = ctx.getSymbolicExpression(rhash[7])
    h8  = ctx.getSymbolicExpression(rhash[8])
    h9  = ctx.getSymbolicExpression(rhash[9])
    h10 = ctx.getSymbolicExpression(rhash[10])
    h11 = ctx.getSymbolicExpression(rhash[11])
    h12 = ctx.getSymbolicExpression(rhash[12])
    h13 = ctx.getSymbolicExpression(rhash[13])
    h14 = ctx.getSymbolicExpression(rhash[14])
    h15 = ctx.getSymbolicExpression(rhash[15])

    astCtx = ctx.getAstContext()
    finalAst = astCtx.concat([
                astCtx.extract(7, 0, h0.getAst()),
                astCtx.extract(7, 0, h1.getAst()),
                astCtx.extract(7, 0, h2.getAst()),
                astCtx.extract(7, 0, h3.getAst()),
                astCtx.extract(7, 0, h4.getAst()),
                astCtx.extract(7, 0, h5.getAst()),
                astCtx.extract(7, 0, h6.getAst()),
                astCtx.extract(7, 0, h7.getAst()),
                astCtx.extract(7, 0, h8.getAst()),
                astCtx.extract(7, 0, h9.getAst()),
                astCtx.extract(7, 0, h10.getAst()),
                astCtx.extract(7, 0, h11.getAst()),
                astCtx.extract(7, 0, h12.getAst()),
                astCtx.extract(7, 0, h13.getAst()),
                astCtx.extract(7, 0, h14.getAst()),
                astCtx.extract(7, 0, h15.getAst()),
               ])
    finalExpr = ctx.newSymbolicExpression(finalAst, "digest md5")
    trace.update({finalExpr.getId() : finalExpr})

    # Generate symbolic epxressions of the first path
    generateSymbolicExpressions(trace, ihash)

    # Generate llvm of the first path
    M = generateLLVMExpressions(ctx, trace)

    # Recompile the LLVM-IL
    recompile(M)

    return 0


if __name__ == '__main__':
    startTime = time.clock()
    retValue  = main()
    endTime   = time.clock()

    metrics()
    sys.exit(retValue)
