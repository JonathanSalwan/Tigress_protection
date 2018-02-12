#!/usr/bin/env python2
## -*- coding: utf-8 -*-

import sys
import random
import subprocess

bad  = 0.0
test = 0.0

if len(sys.argv) != 3:
    print 'Syntax: %s <tigress binary> <clean binary>'
    sys.exit(-1)

tigress = sys.argv[1]
triton  = sys.argv[2]

for x in range(1000):
    ret1 = subprocess.check_output([tigress, str(x)])
    ret2 = subprocess.check_output([triton, str(x)])
    if ret1 != ret2:
        print '[-] Invalid with %d' %(x)
        bad += 1
    else:
        print '[+] Success with %d' %(x)
    test += 1

for i in range(1000):
    x = random.randrange(0, 0xffff)
    ret1 = subprocess.check_output([tigress, str(x)])
    ret2 = subprocess.check_output([triton, str(x)])
    if ret1 != ret2:
        print '[-] Invalid with %d' %(x)
        bad += 1
    else:
        print '[+] Success with %d' %(x)
    test += 1

for i in range(1000):
    x = random.randrange(0xffff, 0xffffffff)
    ret1 = subprocess.check_output([tigress, str(x)])
    ret2 = subprocess.check_output([triton, str(x)])
    if ret1 != ret2:
        print '[-] Invalid with %d' %(x)
        bad += 1
    else:
        print '[+] Success with %d' %(x)
    test += 1

for i in range(1000):
    x = random.randrange(0xffffffff, 0xffffffffffffffff)
    ret1 = subprocess.check_output([tigress, str(x)])
    ret2 = subprocess.check_output([triton, str(x)])
    if ret1 != ret2:
        print '[-] Invalid with %d' %(x)
        bad += 1
    else:
        print '[+] Success with %d' %(x)
    test += 1

print '[+] Success: %.02f' %(100 - (bad * 100.0 / test))
