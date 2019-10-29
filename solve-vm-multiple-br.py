#!/usr/bin/env python2
## -*- coding: utf-8 -*-
##
## This file do the same thing that solve-vm.py but use a worklist for
## cover all paths.
##
## /!\ You have to use the dev-v0.6 of the libTriton.
##

from    functools import wraps
from    triton    import *

from arybo.tools.triton_ import tritonexprs2arybo, tritonast2arybo
from arybo.lib.exprs_asm import to_llvm_function
from arybo.lib.mba_exprs import ExprCond

import  ctypes
import  errno
import  lief
import  os
import  random
import  signal
import  string
import  struct
import  sys
import  threading
import  time
import  argparse


# Used for nested vm
sys.setrecursionlimit(100000)

# Script options
DEBUG    = False
TIMEOUT  = float(120.0)
METRICS  = True
OPAQUE   = False
VM_INPUT = 1234

# Some constants
SYMBOLIZE  = 0
CONCRETIZE = 1


# The debug function
def debug(s):
    if DEBUG:
        sys.stdout.flush()
        print '%s %s\033[0m' %(threading.currentThread().getName(), s)
    return


# This class is used to execute a binary with a seed and get constraints
# along this trace.
class Trace(object):

    def __init__(self, path):
        self.path = path

        # The current seeds during the execution
        self.seeds = [{}]

        # During the trace it's possible that we need to generate new inputs
        # at specific program points.
        self.newInputs = list()

        # Memory mapping
        self.BASE_PLT   = 0x10000000
        self.BASE_ARGV  = 0x20000000
        self.BASE_ALLOC = 0x30000000
        self.BASE_STACK = 0x9fffffff
        self.BASE_LIBC  = 0xa0000000

        # Signal handlers used by raise() and signal()
        self.sigHandlers = dict()

        # File descriptors used by fopen() and fprintf()
        self.fdHandlers = dict()

        # Allocation information used by malloc()
        self.mallocCurrentAllocation = 0
        self.mallocMaxAllocation     = 2048
        self.mallocBase              = self.BASE_ALLOC
        self.mallocChunkSize         = 0x00010000

        # Total of instructions executed
        self.totalInstructions = 0
        self.totalUniqueInstructions = {}

        # Total of functions simulated
        self.totalFunctions = 0

        # Time of execution
        self.startTime = None
        self.endTime   = None

        # Get a Triton context
        self.ctx = TritonContext()

        # Condition summaries
        # When we make function summaries, we define some pre-conditions onto
        # the current path constraint. It's a workaround for this tool. We should
        # add this feature into the libTriton. (pop(), push() constraint (see #350))
        self.preconditions = list()

        # custom PLT
        self.customRelocation = [
            ['__libc_start_main',   self.libcMainHandler,    None], # symbolic
            ['__errno_location',    self.errnoHandler,       None], # concrete
            ['atoi',                self.atoiHandler,        None], # symbolic
            ['calloc',              self.callocHandler,      None], # concrete
            ['fopen',               self.fopenHandler,       None], # concrete
            ['fprintf',             self.fprintfHandler,     None], # concrete
            ['free',                self.freeHandler,        None], # concrete
            ['malloc',              self.mallocHandler,      None], # concrete
            ['printf',              self.printfHandler,      None], # concrete
            ['putchar',             self.putcharHandler,     None], # concrete
            ['puts',                self.putsHandler,        None], # concrete
            ['raise',               self.raiseHandler,       None], # concrete
            ['rand',                self.randHandler,        None], # concrete
            ['signal',              self.signalHandler,      None], # concrete
            ['strcmp',              self.strcmpHandler,      None], # symbolic
            ['strcpy',              self.strcpyHandler,      None], # symbolic
            ['strlen',              self.strlenHandler,      None], # symbolic
            ['strncpy',             self.strncpyHandler,     None], # symbolic
            ['strtoul',             self.strtoulHandler,     None], # concrete
            ['strtoull',            self.strtoulHandler,     None], # concrete
        ]

        return


    def getMemoryString(self, addr):
        s = str()
        index = 0

        while self.ctx.getConcreteMemoryValue(addr+index):
            c = chr(self.ctx.getConcreteMemoryValue(addr+index))
            #if c not in string.printable: c = ""
            s += c
            index  += 1

        return s


    def getFormatString(self, addr):
        return self.getMemoryString(addr)                                               \
               .replace("%s", "{}").replace("%d", "{:d}").replace("%#02x", "{:#02x}")   \
               .replace("%#x", "{:#x}").replace("%x", "{:x}").replace("%02X", "{:02x}") \
               .replace("%c", "{:c}").replace("%02x", "{:02x}").replace("%ld", "{:d}")  \
               .replace("%*s", "").replace("%lX", "{:x}").replace("%08x", "{:08x}")     \
               .replace("%u", "{:d}").replace("%lu", "{:d}")                            \


    # Return true if a memory cell is symbolized
    def isMemoryCellSymbolized(self, ptr, size):
        for index in range(size):
            if self.ctx.isMemorySymbolized(ptr+index) == True:
                return True
        return False


    # Simulate the rand() function
    def randHandler(self):
        debug('[+] rand hooked')
        # Return value
        return (CONCRETIZE, random.randrange(0xffffffff))


    # Simulate the malloc() function
    def mallocHandler(self):
        debug('[+] malloc hooked')

        # Get arguments
        size = self.ctx.getConcreteRegisterValue(self.ctx.registers.rdi)

        if size > self.mallocChunkSize:
            debug('[+] malloc failed: size too big')
            sys.exit(-1)

        if self.mallocCurrentAllocation >= self.mallocMaxAllocation:
            debug('[+] malloc failed: too many allocations done')
            sys.exit(-1)

        area = self.mallocBase + (self.mallocCurrentAllocation * self.mallocChunkSize)
        self.mallocCurrentAllocation += 1

        # Return value
        return (CONCRETIZE, area)


    # Simulate the calloc() function
    def callocHandler(self):
        debug('[+] malloc hooked')

        # Get arguments
        nmemb = self.ctx.getConcreteRegisterValue(self.ctx.registers.rdi)
        size  = self.ctx.getConcreteRegisterValue(self.ctx.registers.rsi)

        # Total size
        size = nmemb * size

        if size > self.mallocChunkSize:
            slef.debug('[+] malloc failed: size too big')
            sys.exit(-1)

        if self.mallocCurrentAllocation >= self.mallocMaxAllocation:
            debug('[+] malloc failed: too many allocations done')
            sys.exit(-1)

        area = self.mallocBase + (self.mallocCurrentAllocation * self.mallocChunkSize)
        self.mallocCurrentAllocation += 1

        # Return value
        return (CONCRETIZE, area)


    # Simulate the signal() function
    def signalHandler(self):
        debug('[+] signal hooked')

        # Get arguments
        signal  = self.ctx.getConcreteRegisterValue(self.ctx.registers.rdi)
        handler = self.ctx.getConcreteRegisterValue(self.ctx.registers.rsi)

        self.sigHandlers.update({signal: handler})

        # Return value (void)
        return (CONCRETIZE, self.ctx.getConcreteRegisterValue(self.ctx.registers.rax))


    # Simulate the raise() function
    def raiseHandler(self):
        debug('[+] raise hooked')

        # Get arguments
        signal  = self.ctx.getConcreteRegisterValue(self.ctx.registers.rdi)
        try:
            # FIXME: Add classical handler (SIGHUP, SIGINT, ...)
            handler = self.sigHandlers[signal]
            self.ctx.processing(Instruction("\x6A\x00")) # push 0
            self.emulate(handler)
        except:
            pass

        # Return value
        return (CONCRETIZE, 0)


    # Simulate the strcmp() function
    def strcmpHandler(self):
        debug('[+] strcmp hooked')

        s1      = self.ctx.getConcreteRegisterValue(self.ctx.registers.rdi)
        s2      = self.ctx.getConcreteRegisterValue(self.ctx.registers.rsi)
        maxlen  = max(len(self.getMemoryString(s1)), len(self.getMemoryString(s2)))

        ast = self.ctx.getAstContext()
        res = ast.bv(0, 64)
        for index in range(maxlen):
            cells1 = self.ctx.buildSymbolicMemory(MemoryAccess(s1+index, 1))
            cells2 = self.ctx.buildSymbolicMemory(MemoryAccess(s2+index, 1))
            res = res + ast.ite(cells1 == cells2, ast.bv(0, 64), ast.bv(1, 64))

        # create a new symbolic expression for this summary
        expr = self.ctx.newSymbolicExpression(res, "strcmp summary")

        return (SYMBOLIZE, expr)


    # Simulate the strcpy() function
    def strcpyHandler(self):
        debug('[+] strcpy hooked')

        dst = self.ctx.getConcreteRegisterValue(self.ctx.registers.rdi)
        src = self.ctx.getConcreteRegisterValue(self.ctx.registers.rsi)
        for index in range(len(self.getMemoryString(src))):
            dmem  = MemoryAccess(dst + index, 1)
            smem  = MemoryAccess(src + index, 1)
            cell = self.ctx.buildSymbolicMemory(smem)
            expr = self.ctx.newSymbolicExpression(cell, "strcpy byte")
            self.ctx.assignSymbolicExpressionToMemory(expr, dmem)
            self.ctx.setConcreteMemoryValue(dmem, cell.evaluate())

        return (CONCRETIZE, dst)


    # Simulate the strncpy() function
    def strncpyHandler(self):
        debug('[+] strncpy hooked')

        dst = self.ctx.getConcreteRegisterValue(self.ctx.registers.rdi)
        src = self.ctx.getConcreteRegisterValue(self.ctx.registers.rsi)
        cnt = self.ctx.getConcreteRegisterValue(self.ctx.registers.rdx)
        for index in range(cnt):
            dmem  = MemoryAccess(dst + index, 1)
            smem  = MemoryAccess(src + index, 1)
            cell = self.ctx.buildSymbolicMemory(smem)
            expr = self.ctx.newSymbolicExpression(cell, "strncpy byte")
            self.ctx.assignSymbolicExpressionToMemory(expr, dmem)
            self.ctx.setConcreteMemoryValue(dmem, cell.evaluate())

        return (CONCRETIZE, dst)


    # Simulate the strtoul() function
    def strtoulHandler(self):
        debug('[+] strtoul hooked')

        # Get arguments
        nptr   = self.getMemoryString(self.ctx.getConcreteRegisterValue(self.ctx.registers.rdi))
        endptr = self.ctx.getConcreteRegisterValue(self.ctx.registers.rsi)
        base   = self.ctx.getConcreteRegisterValue(self.ctx.registers.rdx)

        # Return value
        return (CONCRETIZE, long(nptr, base))


    # Simulate the strlen() function
    def strlenHandler(self):
        debug('[+] strlen hooked')

        # Get arguments
        s = self.ctx.getConcreteRegisterValue(self.ctx.registers.rdi)

        ast = self.ctx.getAstContext()
        def rec(res, s, deep, maxdeep):
            if deep == maxdeep:
                return res
            cell = self.ctx.buildSymbolicMemory(MemoryAccess(s + deep, 1))
            res  = ast.ite(cell == 0x00, ast.bv(deep, 64), rec(res, s, deep+1, maxdeep))
            return res

        sze = len(self.getMemoryString(s))
        res = ast.bv(sze, 64)
        res = rec(res, s, 0, sze)

        # create a new symbolic expression for this summary
        expr = self.ctx.newSymbolicExpression(res, "strlen summary")

        return (SYMBOLIZE, expr)


    # Simulate the atoi() function
    def atoiHandler(self):
        debug('[+] atoi hooked')

        res = self.ctx.getAstContext().bv(0, 32)
        rdi = self.ctx.getConcreteRegisterValue(self.ctx.registers.rdi)
        while self.ctx.getConcreteMemoryValue(rdi):
            # input
            cell = self.ctx.buildSymbolicMemory(MemoryAccess(rdi, 1))
            # pre condition for ascii numbers
            self.preconditions.append(self.ctx.getAstContext().land([cell >= 0x30, cell <= 0x39]))
            # atoi semantics
            cell = self.ctx.getAstContext().zx(24, cell)
            res  = ((res * 10) + cell - 0x30)
            # inc buffer
            rdi += 1
        res = self.ctx.getAstContext().sx(32, res)

        # create a new symbolic expression for this summary
        expr = self.ctx.newSymbolicExpression(res, "atoi summary")

        return (SYMBOLIZE, expr)


    # Simulate the printf() function
    def printfHandler(self):
        debug('[+] printf hooked')

        # Get arguments
        arg1   = self.getFormatString(self.ctx.getConcreteRegisterValue(self.ctx.registers.rdi))
        arg2   = self.ctx.getConcreteRegisterValue(self.ctx.registers.rsi)
        arg3   = self.ctx.getConcreteRegisterValue(self.ctx.registers.rdx)
        arg4   = self.ctx.getConcreteRegisterValue(self.ctx.registers.rcx)
        arg5   = self.ctx.getConcreteRegisterValue(self.ctx.registers.r8)
        arg6   = self.ctx.getConcreteRegisterValue(self.ctx.registers.r9)
        nbArgs = arg1.count("{")
        args   = [arg2, arg3, arg4, arg5, arg6][:nbArgs]
        s      = arg1.format(*args)

        if DEBUG:
            sys.stdout.write(s)
            sys.stdout.flush()

        # Return value
        return (CONCRETIZE, len(s))


    # Simulate the putchar() function
    def putcharHandler(self):
        debug('[+] putchar hooked')

        # Get arguments
        arg1 = self.ctx.getConcreteRegisterValue(self.ctx.registers.rdi)
        sys.stdout.write(chr(arg1) + '\n')
        sys.stdout.flush()

        # Return value
        return (CONCRETIZE, 2)


    # Simulate the puts() function
    def putsHandler(self):
        debug('[+] puts hooked')

        # Get arguments
        arg1 = self.getMemoryString(self.ctx.getConcreteRegisterValue(self.ctx.registers.rdi))
        sys.stdout.write(arg1 + '\n')
        sys.stdout.flush()

        # Return value
        return (CONCRETIZE, len(arg1) + 1)


    # Simulate the printf() function
    def fprintfHandler(self):
        debug('[+] fprintf hooked')

        # Get arguments
        arg1   = self.ctx.getConcreteRegisterValue(self.ctx.registers.rdi)
        arg2   = self.getFormatString(self.ctx.getConcreteRegisterValue(self.ctx.registers.rsi))
        arg3   = self.ctx.getConcreteRegisterValue(self.ctx.registers.rdx)
        arg4   = self.ctx.getConcreteRegisterValue(self.ctx.registers.rcx)
        arg5   = self.ctx.getConcreteRegisterValue(self.ctx.registers.r8)
        arg6   = self.ctx.getConcreteRegisterValue(self.ctx.registers.r9)
        nbArgs = arg2.count("{")
        args   = [arg3, arg4, arg5, arg6][:nbArgs]
        s      = arg2.format(*args)

        self.fdHandlers[arg1].write(s)

        # Return value
        return (CONCRETIZE, len(s))


    # Simulate the free() function (skip this behavior)
    def freeHandler(self):
        debug('[+] free hooked')
        return None


    # Simulate the fopen() function
    def fopenHandler(self):
        debug('[+] fopen hooked')

        # Get arguments
        arg1   = self.getFormatString(self.ctx.getConcreteRegisterValue(self.ctx.registers.rdi))
        arg2   = self.getFormatString(self.ctx.getConcreteRegisterValue(self.ctx.registers.rsi))

        fd = open(arg1, arg2)
        idf = len(self.fdHandlers) + 3 # 3 because 0, 1, 2 are already reserved.
        self.fdHandlers.update({idf : fd})

        # Return value
        return (CONCRETIZE, idf)


    def libcMainHandler(self):
        debug('[+] __libc_start_main hooked')

        # Get arguments
        main = self.ctx.getConcreteRegisterValue(self.ctx.registers.rdi)

        # Push the return value to jump into the main() function
        self.ctx.concretizeRegister(self.ctx.registers.rsp)
        self.ctx.setConcreteRegisterValue(self.ctx.registers.rsp, self.ctx.getConcreteRegisterValue(self.ctx.registers.rsp)-CPUSIZE.QWORD)

        ret2main = MemoryAccess(self.ctx.getConcreteRegisterValue(self.ctx.registers.rsp), CPUSIZE.QWORD)
        self.ctx.concretizeMemory(ret2main)
        self.ctx.setConcreteMemoryValue(ret2main, main)

        # Setup argc / argv
        self.ctx.concretizeRegister(self.ctx.registers.rdi)
        self.ctx.concretizeRegister(self.ctx.registers.rsi)

        argvs = [
            self.path,      # argv[0]
            str(VM_INPUT),  # argv[1]
        ]

        # Define argc / argv
        base  = self.BASE_ARGV
        addrs = list()

        index = 0
        for argv in argvs:
            addrs.append(base)
            self.ctx.setConcreteMemoryAreaValue(base, argv+'\x00')
            base += len(argv)+1
            debug('[+] argv[%d] = %s' %(index, argv))
            index += 1

        argc = len(argvs)
        argv = base
        for addr in addrs:
            self.ctx.setConcreteMemoryValue(MemoryAccess(base, CPUSIZE.QWORD), addr)
            base += CPUSIZE.QWORD

        self.ctx.setConcreteRegisterValue(self.ctx.registers.rdi, argc)
        self.ctx.setConcreteRegisterValue(self.ctx.registers.rsi, argv)

        return (CONCRETIZE, 0)


    def errnoHandler(self):
        debug('[+] __errno_location hooked')

        errno = 0xdeadbeaf
        self.ctx.setConcreteMemoryValue(MemoryAccess(errno, CPUSIZE.QWORD), 0)

        return (CONCRETIZE, errno)


    def hookingHandler(self):
        pc = self.ctx.getConcreteRegisterValue(self.ctx.registers.rip)
        for rel in self.customRelocation:
            if rel[2] == pc:
                # Emulate the routine and the return value
                ret_value = rel[1]()
                if ret_value is not None:
                    if ret_value[0] == CONCRETIZE:
                        self.ctx.concretizeRegister(self.ctx.registers.rax)
                        self.ctx.setConcreteRegisterValue(self.ctx.registers.rax, ret_value[1])
                    elif ret_value[0] == SYMBOLIZE:
                        self.ctx.setConcreteRegisterValue(self.ctx.registers.rax, ret_value[1].getAst().evaluate())
                        self.ctx.assignSymbolicExpressionToRegister(ret_value[1], self.ctx.registers.rax)

                # Used for metric
                self.totalFunctions += 1

                # tigress user input
                if rel[0] == 'strtoul':
                    debug('[+] Symbolizing the strtoul return')
                    var = self.ctx.symbolizeRegister(self.ctx.registers.rax)
                    self.ctx.setConcreteVariableValue(var, VM_INPUT)

                # tigress user input
                if rel[0] == 'printf':
                    debug('[+] Slicing end-point user expression')
                    return False

                # Get the return address
                ret_addr = self.ctx.getConcreteMemoryValue(MemoryAccess(self.ctx.getConcreteRegisterValue(self.ctx.registers.rsp), CPUSIZE.QWORD))

                # Hijack RIP to skip the call
                self.ctx.concretizeRegister(self.ctx.registers.rip)
                self.ctx.setConcreteRegisterValue(self.ctx.registers.rip, ret_addr)

                # Restore RSP (simulate the ret)
                self.ctx.concretizeRegister(self.ctx.registers.rsp)
                self.ctx.setConcreteRegisterValue(self.ctx.registers.rsp, self.ctx.getConcreteRegisterValue(self.ctx.registers.rsp)+CPUSIZE.QWORD)
        return True


    # Generate new models when a LEA is symbolic
    def symbolicLea(self, lea):
        pc     = self.ctx.getPathConstraintsAst()
        ast    = self.ctx.getAstContext()
        crst   = ast.land([pc == pc, lea != lea.evaluate()])
        models = self.ctx.getModels(crst, 255)
        for model in models:
            seed = list()
            argc = self.ctx.getSymbolicVariable(0)
            seed.append({
                'comment':          argc.getComment(),
                'id':               argc.getId(),
                'memory address':   argc.getOrigin(),
                'model result':     self.ctx.getConcreteVariableValue(argc),
                'name':             argc.getName(),
                'src':              None,
                'dst':              None,
            })
            for k,v in model.items():
                # Get the symbolic variable assigned to the model
                symVar = self.ctx.getSymbolicVariable(k)
                # Save the new input as seed.
                seed.append({
                    'comment':          symVar.getComment(),
                    'id':               symVar.getId(),
                    'memory address':   symVar.getOrigin(),
                    'model result':     v.getValue(),
                    'name':             symVar.getName(),
                    'src':              None,
                    'dst':              None,
                })
            self.newInputs.append(seed)
        return


    # Emulate the binary.
    def emulate(self, pc):
        count = 0
        while pc:
            # Fetch opcodes
            opcodes = self.ctx.getConcreteMemoryAreaValue(pc, 16)

            # Create the Triton instruction
            instruction = Instruction()
            instruction.setOpcode(opcodes)
            instruction.setAddress(pc)

            # Process
            if self.ctx.processing(instruction) == False:
                debug('[-] Instruction not supported: %s' %(str(instruction)))
                break

            count += 1
            #print instruction
            for op in instruction.getOperands():
                if op.getType() == OPERAND.MEM:
                    lea = op.getLeaAst()
                    if lea is not None and lea.isSymbolized():
                        self.symbolicLea(lea)

            if pc in self.totalUniqueInstructions:
                self.totalUniqueInstructions[pc] += 1
            else:
                self.totalUniqueInstructions[pc] = 1

            # Simulate routines
            if not self.hookingHandler():
                break

            # Next
            pc = self.ctx.getConcreteRegisterValue(self.ctx.registers.rip)

        # Used for metric
        self.totalInstructions += count
        return


    def loadBinary(self, binary):
        # Map the binary into the memory
        phdrs = binary.segments
        for phdr in phdrs:
            size   = phdr.physical_size
            vaddr  = phdr.virtual_address
            debug('[+] Loading 0x%06x - 0x%06x' %(vaddr, vaddr+size))
            self.ctx.setConcreteMemoryAreaValue(vaddr, phdr.content)
        return


    def makeDynamicRelocation(self, binary):
        # Initialize PLT
        for index in range(len(self.customRelocation)):
            self.customRelocation[index][2] = self.BASE_PLT + index

        # Perform our own relocations
        try:
            for rel in binary.pltgot_relocations:
                symbolName = rel.symbol.name
                symbolRelo = rel.address
                for crel in self.customRelocation:
                    if symbolName == crel[0]:
                        debug('[+] Hooking %s' %(symbolName))
                        self.ctx.setConcreteMemoryValue(MemoryAccess(symbolRelo, CPUSIZE.QWORD), crel[2])
        except:
            pass

        # Perform our own relocations
        try:
            for rel in binary.dynamic_relocations:
                symbolName = rel.symbol.name
                symbolRelo = rel.address
                for crel in self.customRelocation:
                    if symbolName == crel[0]:
                        debug('[+] Hooking %s' %(symbolName))
                        self.ctx.setConcreteMemoryValue(MemoryAccess(symbolRelo, CPUSIZE.QWORD), crel[2])
        except:
            pass

        return


    def makeStaticRelocation(self, binary):
        for rel in self.customRelocation:
            try:
                rel[2] = binary.get_symbol(rel[0]).value
                debug('[+] Hooking %s at %#x' %(rel[0], rel[2]))
            except:
                rel[2] = None
        return


    def injectModels(self, api, mem):
        dst = mem.getAddress()
        sze = mem.getSize()

        if sze > CPUSIZE.BYTE:
            return

        for seed in self.seeds:
            if seed and dst == seed['memory address']:
                self.ctx.setConcreteMemoryValue(mem, seed['model result'])

        return


    def run(self):
        global VM_INPUT

        # Set the architecture
        self.ctx.setArchitecture(ARCH.X86_64)

        # Set optimization
        self.ctx.enableMode(MODE.ALIGNED_MEMORY, True)
        self.ctx.enableMode(MODE.ONLY_ON_SYMBOLIZED, True)

        # Callback to inject symbolic models
        self.ctx.addCallback(self.injectModels, CALLBACK.GET_CONCRETE_MEMORY_VALUE)

        # AST representation as Python syntax
        self.ctx.setAstRepresentationMode(AST_REPRESENTATION.PYTHON)

        # Set seed
        if self.seeds[0]:
            VM_INPUT = self.seeds[0]['model result']
        else:
            VM_INPUT = 1234

        # Parse the binary
        lief.Logger.disable()
        binary = lief.parse(self.path)

        # Load the binary
        self.loadBinary(binary)

        # Perform our own relocations
        #self.makeStaticRelocation(binary)
        self.makeDynamicRelocation(binary)

        # Define a fake stack
        self.ctx.setConcreteRegisterValue(self.ctx.registers.rbp, self.BASE_STACK)
        self.ctx.setConcreteRegisterValue(self.ctx.registers.rsp, self.BASE_STACK)

        # Let's emulate the binary from the entry point
        debug('[+] Starting emulation.')
        self.startTime = time.clock()
        self.emulate(binary.entrypoint)
        self.endTime = time.clock()
        debug('[+] Emulation done.')

        debug('[+] Instructions executed: %d' %(self.totalInstructions))
        debug('[+] Unique instructions executed: %d' %(len(self.totalUniqueInstructions)))
        debug('[+] Symbolic conditions: %d' %(len(self.ctx.getPathConstraints())))
        debug('[+] Time of execution: %f seconds' %(self.endTime - self.startTime))
        debug('[+] Return value: %#x' %(self.ctx.getConcreteRegisterValue(self.ctx.registers.rax)))

        return self.ctx.getConcreteRegisterValue(self.ctx.registers.rax)



# This class is used to represent a node of a tree execution (ite)
class IteTreeNode(object):
    def __init__(self):
        self.src       = None # Address of the condition
        self.dst       = None # Dst of the condition
        self.condition = None # Condition expression
        self.taken     = None # The taken branch
        self.ntaken    = None # The not taken branch

    def __repr__(self):
        return "(ite %s %s %s)" %(self.condition, self.taken, self.ntaken)


# This class is used to represent a node of a tree execution (ret expr)
class ExprTreeNode(object):
    def __init__(self, e):
        self.expr = e

    def __repr__(self):
        return str(self.expr)


# This class execute several Trace to explore the binary.
class PathsExploration(object):

    STRATEGY_FIFO = 0b00000001
    STRATEGY_LIFO = 0b00000010
    STRATEGY_RAND = 0b00000100


    def __init__(self, path):
        self.path       = path             # binary path
        self.wl         = [[{}]]           # work list
        self.dl         = []               # done list
        self.bbcov      = {}               # list of basic block already covered
        self.cstrts     = []               # list of constraints already asked for a model
        self.traces     = []               # list of context for each tarce executed
        self.numExec    = 0                # number of executions
        self.stop       = False
        self.ret        = None
        self.ts         = time.clock()
        self.strategy   = None
        return


    # The worker thread.
    def worker(self, seeds):
        # Inc number of execution
        self.numExec += 1

        if TIMEOUT and (time.clock() - self.ts) >= TIMEOUT:
            debug('[+] Time out.')
            self.stop = True
            return

        # Execute the binary with seeds
        trace = Trace(self.path)
        trace.seeds = seeds
        self.ret = trace.run()

        # Save the context of the trace
        self.traces.append(trace.ctx)

        # Generate new inputs
        debug('[+] Getting models, please wait...')
        inputs = self.getNewInput(trace) + trace.newInputs
        for m in inputs:
            if m not in self.dl:
                self.wl.append(m)

        debug('[+] Time after solving: %f seconds' %(time.clock() - self.ts))
        debug('[+] Work list size: %d' %(len(self.wl)))
        debug('[+] Done list size: %d' %(len(self.dl)))
        return


    # Returns a seed based on a strategy
    def pickSeed(self):
        if self.strategy == PathsExploration.STRATEGY_LIFO:
            return self.wl.pop()

        elif self.strategy == PathsExploration.STRATEGY_FIFO:
            return self.wl.pop(0)

        elif self.strategy == PathsExploration.STRATEGY_RAND:
            return self.wl.pop(random.randrange(0, len(self.wl)))


    def explore(self):
        while self.wl and not self.stop:
            # Take seeds
            seeds = self.pickSeed()
            self.dl.append(seeds)

            # Execution into a thread
            t = threading.Thread(name='\033[0;%dm[exec:%d]' %((31 + (self.numExec % 4)), self.numExec), target=self.worker, args=[seeds])
            t.start()
            t.join()
        return



    def _deepMerge(self, ctx, pcs, node, ret):
        if not len(pcs):
            return

        pc = pcs.pop(0)
        for l in pc.getBranchConstraints():
            if l['isTaken'] == True:
                if not node.src:
                    node.condition = ctx.getAstContext().unrollAst(l['constraint'])
                    node.src = l['srcAddr']
                    node.dst = l['dstAddr']
                    if len(pcs):
                        if not node.taken:
                            node.taken = IteTreeNode()
                        self._deepMerge(ctx, pcs, node.taken, ret)
                    else:
                        if not node.taken:
                            node.taken = ExprTreeNode(ctx.getAstContext().unrollAst(ret))

                elif node.src == l['srcAddr'] and node.dst != l['dstAddr']:
                    if len(pcs):
                        if not node.ntaken:
                            node.ntaken = IteTreeNode()
                        self._deepMerge(ctx, pcs, node.ntaken, ret)
                    else:
                        if not node.ntaken:
                            #node.ntaken = ExprTreeNode(ret)
                            node.ntaken = ExprTreeNode(ctx.getAstContext().unrollAst(ret))

                elif node.src == l['srcAddr'] and node.dst == l['dstAddr']:
                    self._deepMerge(ctx, pcs, node.taken, ret)

                else:
                    raise Exception('???')


    def tracesMerging(self):
        ret = self.traces[0].getSymbolicRegisters()[REG.X86_64.RSI].getAst() # RSI car printf
        pcs = self.traces[0].getPathConstraints()

        if not len(pcs):
            node = ExprTreeNode(self.traces[0].getAstContext().unrollAst(ret))
            return node

        node = IteTreeNode()
        for ctx in self.traces:
            self._deepMerge(ctx, ctx.getPathConstraints(), node, ret)

        return node


    # This function returns a set of new inputs based on the last trace.
    def getNewInput(self, trace):
        # Set of new inputs
        inputs = list()

        # Get path constraints from the last execution
        pco = trace.ctx.getPathConstraints()

        # Get the astContext
        astCtxt = trace.ctx.getAstContext()

        # We start with any input. T (Top)
        previousConstraints = astCtxt.equal(astCtxt.bvtrue(), astCtxt.bvtrue())

        # Apply pre conditions defined during the trace
        for i in trace.preconditions:
            previousConstraints = astCtxt.land([previousConstraints, i])

        # Go through the path constraints
        for pc in pco:
            # If there is a condition
            if pc.isMultipleBranches():
                # Get all branches
                branches = pc.getBranchConstraints()
                for branch in branches:
                    # Get the constraint of the branch which has not been taken.
                    if branch['isTaken'] == False:
                        # Check timeout
                        if TIMEOUT and (time.clock() - self.ts) >= TIMEOUT:
                            return inputs
                        # Create the constraint
                        cstrts = astCtxt.land([previousConstraints, branch['constraint']])
                        # Only ask for a model if the constraints has never been asked
                        if frozenset([str(cstrts), branch['dstAddr']]) not in self.cstrts:
                            models = trace.ctx.getModels(cstrts, 1)
                            for model in models:
                                #model = trace.ctx.getModel(cstrts)
                                seed   = list()
                                for k, v in model.items():
                                    # Get the symbolic variable assigned to the model
                                    symVar = trace.ctx.getSymbolicVariable(k)
                                    # Save the new input as seed.
                                    seed.append({
                                        'comment':          symVar.getComment(),
                                        'id':               symVar.getId(),
                                        'memory address':   symVar.getOrigin(),
                                        'model result':     v.getValue(),
                                        'name':             symVar.getName(),
                                        'src':              branch['srcAddr'],
                                        'dst':              branch['dstAddr'],
                                    })
                                if seed:
                                    self.cstrts.append(frozenset([str(cstrts), branch['dstAddr']]))
                                    self.bbcov.update({branch['dstAddr'] : True})
                                    inputs.append(seed)

            # Update the previous constraints with true branch to keep a good path.
            previousConstraints = astCtxt.land([previousConstraints, pc.getTakenPathConstraintAst()])

        return inputs



def get_all_filepaths(path, ext):
    ret = list()
    for root, dirs, files in os.walk(path):
        for name in files:
            if name.lower().endswith(ext):
                ret.append(os.path.join(root, name))
    return ret


def toTritonAst(ctx, node):
    if isinstance(node, IteTreeNode):
        b1 = toTritonAst(ctx, node.taken)
        b2 = toTritonAst(ctx, node.ntaken)
        sz = (b1.getBitvectorSize() if b1 else (b2.getBitvectorSize() if b2 else 0))
        if not sz:
            raise Exception('Invalid node')
        b1 = (b1 if b1 else ctx.getAstContext().bv(0, sz))
        b2 = (b2 if b2 else ctx.getAstContext().bv(0, sz))
        return ctx.getAstContext().ite(node.condition, b1, b2)
    elif isinstance(node, ExprTreeNode):
        return node.expr


def toLLVMIR(ctx, node):
    # strtoul
    var0 = ctx.newSymbolicVariable(64)

    # Used to get symvar names
    tt_vars = set()
    def deep(node):
        if node.getType() == AST_NODE.VARIABLE:
            tt_vars.add(node.getSymbolicVariable().getName())
        if node.getType() == AST_NODE.REFERENCE:
            deep(node.getSymbolicExpression().getAst())
        for c in node.getChildren():
            deep(c)

    deep(node)
    tt_expr = ctx.newSymbolicExpression(node)
    ar_expr = tritonexprs2arybo(ctx.sliceExpressions(tt_expr))
    ar_var = list()
    for var in tt_vars:
        ar_var.append(tritonast2arybo(ctx.getAstContext().variable(ctx.getSymbolicVariableFromName(var))).v)
    M = to_llvm_function(ar_expr, ar_var, "SECRET")
    M = str(M).replace('unknown-unknown-unknown', 'x86_64-pc-linux-gnu')

    return M


def recompile(M, path):
    name = 'llvm_expressions/%s.ll' %(path.split('/')[-1])
    nameO2 = 'llvm_expressions/%s.O2.ll' %(path.split('/')[-1])
    fd = open(name, 'w')
    M = str(M).replace('__arybo', 'SECRET')
    M = str(M).replace('unknown-unknown-unknown', 'x86_64-pc-linux-gnu')
    fd.write(M)
    fd.close()
    os.system("clang -O2 -S -emit-llvm -o - %s > %s" %(name, nameO2))
    debug('[+] LLVM module wrote in %s' %(name))
    debug('[+] LLVM module wrote in %s' %(nameO2))

    debug('[+] Recompiling deobfuscated binary...')
    dst = 'deobfuscated_binaries/%s' %(path.split('/')[-1] + '.deobfuscated')
    os.system("clang %s -O2 deobfuscated_binaries/run.c -o %s" %(name, dst))
    debug('[+] Deobfuscated binary recompiled: %s' %(dst))
    return


def exploreBinary(path, strategy):
    ts = time.clock()

    if not os.path.exists(path):
        print "[-] Path does not exists"
        sys.exit(-1)

    binary = PathsExploration(path)
    binary.strategy = strategy
    binary.explore()

    ctx  = TritonContext()
    ctx.setArchitecture(ARCH.X86_64)
    node = binary.tracesMerging()
    node = toTritonAst(ctx, node)

    debug('[+] Converting symbolic expressions to an LLVM module...')
    M = toLLVMIR(ctx, node)
    recompile(M, path)

    te = time.clock()
    sys.stdout.flush()
    return binary


def convertStrategy(args):
    strategy = PathsExploration.STRATEGY_LIFO

    if args.strategy == 'fifo':
        strategy = PathsExploration.STRATEGY_FIFO
    elif args.strategy == 'lifo':
        strategy = PathsExploration.STRATEGY_LIFO
    elif args.strategy == 'rand':
        strategy = PathsExploration.STRATEGY_RAND
    else:
        print '[+] Invalid strategy'
        sys.exit(-1)

    return strategy



if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Paths exploration based on top of libTriton.")
    group  = parser.add_mutually_exclusive_group()
    group.add_argument('-b',  '--binary',    help='explore a binary',                           type=str,   metavar='')
    parser.add_argument('-s', '--strategy',  help='define a strategy for path exploration',     type=str,   metavar='', default='lifo')
    parser.add_argument('-t', '--timeout',   help='define a timeout in seconds per execution',  type=float, metavar='', default=300.0) # 5 min
    parser.add_argument('-v', '--verbose',   help='display verbose at runtime',                 action='store_true')
    args = parser.parse_args()

    # Define the timeout
    TIMEOUT = args.timeout

    # Convert strategy
    strategy = convertStrategy(args)

    if args.verbose:
        DEBUG = True

    if args.binary:
        exploreBinary(args.binary, strategy)
    else:
        parser.print_help()
