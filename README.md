# Tigress Protections

> [Tigress](http://tigress.cs.arizona.edu/) is a diversifying virtualizer/obfuscator for the C language that supports many novel defenses against both static and dynamic reverse engineering and de-virtualization attacks.

> In particular, Tigress protects against static de-virtualization by generating virtual instruction sets of arbitrary complexity and diversity, by producing interpreters with multiple types of instruction dispatch, and by inserting code for anti alias analysis. Tigress protects against dynamic de-virtualization by merging the real code with bogus functions, by inserting implicit flow, and by creating slowly-executing reenetrant interpreters. Tigress implements its own version of code packing through the use of runtime code generation. Finally, Tigress' dynamic transformation provides a generalized form of continous runtime code modification.

# VMs descriptions

Tigress team has provided some [challenges](http://tigress.cs.arizona.edu/challenges.html#current) where we can find different kind of protections

* **VM-0**: One level of virtualization, random dispatch.
* **VM-1**: One level of virtualization, superoperators, split instruction handlers.
* **VM-2**: One level of virtualization, bogus functions, implicit flow.
* **VM-3**: One level of virtualization, instruction handlers obfuscated with arithmetic encoding, virtualized function is split and the split parts merged.
* **VM-4**: Two levels of virtualization, implicit flow.
* **VM-5**: One level of virtualization, one level of jitting, implicit flow.
* **VM-6**: Two levels of jitting, implicit flow.

# Challenge

All challenges take as input a number and return a hash. Example:

<pre>
$ ./obfuscated_binaries/tigress-2-challenge-2 1234
202180712448

$ ./obfuscated_binaries/tigress-2-challenge-2 823748
50564355584

$ ./obfuscated_binaries/tigress-2-challenge-2 2834723
50714072576
</pre>

The hash computation function is obfuscated. Types of possible attacks:

* In a source recovery attack the task is to identify the algorithm that computes SECRET.
* In a data recovery attack the task is to extract a specific run-time or compile-time data item.
* In a metadata recovery attack the task is to identify the sequence of transformations that resulted in SECRET, along with arguments to those transformations, such as the dispatch method used in a virtualization.
* In a location attack the task is to identify the code bytes of the program that comprise the obfuscated SECRET function.

# Automatic deobfuscation

Our goals were to:

* Symbolically extract the hash algorithm
* Simplify these symbolic expressions
* Provide python scripts where we can get the hash from a given input **and** get input collisions from a given hash
* Provide a new simplified version of the binary

And all of this with only one generic script :). To do so, we made in the following order:

* Symbolically emulate the obfuscated binary with [Triton](https://github.com/JonathanSalwan/Triton)
* Concretize everything which are not related to the user input.
* Extract the hash algorithm and create `input->hash` and `hash->inputs` using [templates](templates.py)
* Convert Triton's expressions to the [Arybo's](https://github.com/quarkslab/arybo) expressions
* Convert Arybo's expressions to the LLVM-IR representation
* Apply LLVM optimizations (O2)
* Rebuild a simplified binary version

If you want more information, you can checkout our [solve-vm.py](solve-vm.py) script.

# solve-vm.py

**Prerequisites**: you must clone the branch `dev-319-bis` of Triton, the branch `feature/exprs` of Arybo and the [llvmlite](https://github.com/numba/llvmlite) project.

However, we already pushed all of our results in this repository but if you want to reproduce by yourself this
analysis, you only have to do execute `solve-vm.py` like this:

<pre>
$ ./solve-vm.py ./obfuscated_binaries/_binary_
</pre>

Example:

<pre>
$ ./solve-vm.py ./obfuscated_binaries/tigress-0-challenge-0
./solve-vm.py:441: SyntaxWarning: name 'VM_INPUT' is assigned to before global declaration
  global VM_INPUT
[+] Loading 0x400040 - 0x400238
[+] Loading 0x400238 - 0x400254
[+] Loading 0x400000 - 0x400f14
[+] Loading 0x601e28 - 0x602550
[+] Loading 0x601e50 - 0x601fe0
[+] Loading 0x400254 - 0x400298
[+] Loading 0x400dc4 - 0x400e08
[+] Loading 0x000000 - 0x000000
[+] Loading 0x601e28 - 0x602000
[+] Hooking printf
[+] Hooking __libc_start_main
[+] Hooking strtoul
[+] Starting emulation.
[+] __libc_start_main hooked
[+] argv[0] = ./obfuscated_binaries/tigress-0-challenge-0
[+] argv[1] = 1234
[+] strtoul hooked
[+] Symbolizing the strtoul return
[+] printf hooked
3035321144166078008
[+] Slicing end-point user expression
[+] Instruction executed: 39817
[+] PC len: 0
[+] Emulation done.
[+] Generating symbolic_expressions/./tigress-0-challenge-0_input_to_hash.py
[+] Generating symbolic_expressions/./tigress-0-challenge-0_hash_to_input.py
[+] Converting symbolic expressions to an LLVM module...
warning: overriding the module target triple with x86_64-pc-linux-gnu [-Woverride-module]
1 warning generated.
[+] LLVM module wrote in llvm_expressions/./tigress-0-challenge-0.ll
[+] Recompiling deobfuscated binary...
warning: overriding the module target triple with x86_64-pc-linux-gnu [-Woverride-module]
1 warning generated.
[+] Deobfuscated binary recompiled: deobfuscated_binaries/./tigress-0-challenge-0.deobfuscated
$
</pre>

Then, symbolic expressions can be found [here](symbolic_expressions), LLVM representations can be found [here](llvm_expressions)
and recompiled binaries can be found [here](deobfuscated_binaries).

# Testing our simplified binaries

As we simplified and recompiled new binaries, we must provide the same behavior of the original binaries. So, to test our binary versions we use this [script](testing_equality.py).

<pre>
$ ./testing_equality.py ./obfuscated_binaries/tigress-0-challenge-0 ./deobfuscated_binaries/tigress-0-challenge-0.deobfuscated
[...]
[+] Success with 272966812638982633
[+] Success with 2304147855662358786
[+] Success with 15697842028176298504
[+] Success with 15273138908025273913
[+] Success with 17329851347176088980
[+] Success with 12160831137213706322
[+] Success with 3489058267725840982
[+] Success with 6474275930952607745
[+] Success with 7363567981237584398
[+] Success with 3685039181436704621
[+] Success: 100.00
</pre>

Basically, this script runs the obfuscated and the deobfuscated binaries with random inputs and checks if they have the same output results.

# Benchmarks

## Results with only one trace

![With one trace](pictures/result_with_one_trace.png)

## Results with the union of two traces

![With two traces](pictures/result_with_two_traces.png)

## Time of extraction per trace

![Time per trace](pictures/time_per_trace.png)

# Credits

* [Adrien Guinet](https://twitter.com/adriengnt) for the Arybo and LLVM parts (Quarkslab)
* [Romain Thomas](https://twitter.com/rh0main) for the Triton part (Quarkslab)
* [Jonathan Salwan](https://twitter.com/JonathanSalwan) for the Triton part (Quarkslab)

