#!/usr/bin/env python2
## -*- coding: utf-8 -*-

import os
import random
import subprocess
import sys

binaries = list()

for (dirpath, dirnames, filenames) in os.walk('./build'):
    for filename in filenames:
        if filename.find('sample1-virt-') != -1:
            binaries.append(dirpath + '/' + filename)
        if filename.find('sample2-virt-') != -1:
            binaries.append(dirpath + '/' + filename)
        #if filename.find('sample4-virt-') != -1:
        #    binaries.append(dirpath + '/' + filename)

for origin in binaries:
    tigress = origin
    triton  = './deobfuscated_binaries/' + origin.split('/')[-1] + '.deobfuscated'
    bad     = False

    if not os.path.exists(triton):
        print '[+] Not found \t : %s' %(triton)
        continue

    for x in range(1000):
        ret1 = subprocess.check_output([tigress, str(x)])
        ret2 = subprocess.check_output([triton, str(x)])
        if ret1 != ret2:
            bad = True
            break


    for i in range(1000):
        x = random.randrange(0, 0xffff)
        ret1 = subprocess.check_output([tigress, str(x)])
        ret2 = subprocess.check_output([triton, str(x)])
        if ret1 != ret2:
            bad = True
            break

    for i in range(1000):
        x = random.randrange(0xffff, 0xffffffff)
        ret1 = subprocess.check_output([tigress, str(x)])
        ret2 = subprocess.check_output([triton, str(x)])
        if ret1 != ret2:
            bad = True
            break

    for i in range(1000):
        x = random.randrange(0xffffffff, 0xffffffffffffffff)
        ret1 = subprocess.check_output([tigress, str(x)])
        ret2 = subprocess.check_output([triton, str(x)])
        if ret1 != ret2:
            bad = True
            break

    if bad:
        print '[-] Invalid \t : %s' %(triton)
    else:
        print '[+] Valid \t : %s' %(triton)


