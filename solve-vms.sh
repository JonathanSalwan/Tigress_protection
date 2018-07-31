#!/bin/sh

#echo "1 sur 20"
#for i in $(find build | grep sample4  | grep -v CMakeFiles); do echo $i; /usr/bin/time -v ./solve-vm.py $i &>> metrics/adler32.data; done
#
#echo "2 sur 20"
#for i in $(find build | grep sample5  | grep -v CMakeFiles); do echo $i; /usr/bin/time -v ./solve-vm.py $i &>> metrics/jenkins.data; done
#
#echo "3 sur 20"
#for i in $(find build | grep sample8  | grep -v CMakeFiles); do echo $i; /usr/bin/time -v ./solve-vm.py $i &>> metrics/spiHash.data; done
#
#echo "4 sur 20"
#for i in $(find build | grep sample10 | grep -v CMakeFiles); do echo $i; /usr/bin/time -v ./solve-vm.py $i &>> metrics/xxhash.data; done
#
#echo "5 sur 20"
#for i in $(find build | grep sample11 | grep -v CMakeFiles); do echo $i; /usr/bin/time -v ./solve-vm.py $i &>> metrics/superFastHash.data; done
#
#echo "6 sur 20"
#for i in $(find build | grep sample12 | grep -v CMakeFiles); do echo $i; /usr/bin/time -v ./solve-vm.py $i &>> metrics/FNV1a.data; done
#
#echo "7 sur 20"
#for i in $(find build | grep sample13 | grep -v CMakeFiles); do echo $i; /usr/bin/time -v ./solve-vm.py $i &>> metrics/spookyHash.data; done
#
#echo "8 sur 20"
#for i in $(find build | grep sample14 | grep -v CMakeFiles); do echo $i; /usr/bin/time -v ./solve-vm.py $i &>> metrics/cityHash.data; done
#
#echo "9 sur 20"
#for i in $(find build | grep sample15 | grep -v CMakeFiles); do echo $i; /usr/bin/time -v ./solve-vm.py $i &>> metrics/jodyHash.data; done
#
#echo "10 sur 20"
#for i in $(find build | grep sample17 | grep -v CMakeFiles); do echo $i; /usr/bin/time -v ./solve-vm.py $i &>> metrics/collberg-0001-0.data; done
#
#echo "11 sur 20"
#for i in $(find build | grep sample18 | grep -v CMakeFiles); do echo $i; /usr/bin/time -v ./solve-vm.py $i &>> metrics/collberg-0001-1.data; done
#
#echo "12 sur 20"
#for i in $(find build | grep sample19 | grep -v CMakeFiles); do echo $i; /usr/bin/time -v ./solve-vm.py $i &>> metrics/collberg-0001-2.data; done
#
#echo "13 sur 20"
#for i in $(find build | grep sample20 | grep -v CMakeFiles); do echo $i; /usr/bin/time -v ./solve-vm.py $i &>> metrics/collberg-0001-3.data; done
#
#echo "14 sur 20"
#for i in $(find build | grep sample21 | grep -v CMakeFiles); do echo $i; /usr/bin/time -v ./solve-vm.py $i &>> metrics/collberg-0001-4.data; done
#
#echo "15 sur 20"
#for i in $(find build | grep sample22 | grep -v CMakeFiles); do echo $i; /usr/bin/time -v ./solve-vm.py $i &>> metrics/collberg-0004-0.data; done
#
#echo "16 sur 20"
#for i in $(find build | grep sample23 | grep -v CMakeFiles); do echo $i; /usr/bin/time -v ./solve-vm.py $i &>> metrics/collberg-0004-1.data; done
#
#echo "17 sur 20"
#for i in $(find build | grep sample24 | grep -v CMakeFiles); do echo $i; /usr/bin/time -v ./solve-vm.py $i &>> metrics/collberg-0004-2.data; done
#
#echo "18 sur 20"
#for i in $(find build | grep sample25 | grep -v CMakeFiles); do echo $i; /usr/bin/time -v ./solve-vm.py $i &>> metrics/collberg-0004-3.data; done
#
#echo "19 sur 20"
#for i in $(find build | grep sample26 | grep -v CMakeFiles); do echo $i; /usr/bin/time -v ./solve-vm.py $i &>> metrics/collberg-0004-4.data; done
#
#echo "19 sur 20"
#for i in $(find build | grep sample3 | grep -v CMakeFiles); do echo $i; /usr/bin/time -v ./solve-md5.py $i &>> metrics/md5.data; done
#
##----------------------------------------------------------------------------
#
#echo "1 sur 20"
#/usr/bin/time -v ./solve-vm.py ./samples/sample4-unprotected.bin
#
#echo "2 sur 20"
#/usr/bin/time -v ./solve-vm.py ./samples/sample5-unprotected.bin
#
#echo "3 sur 20"
#/usr/bin/time -v ./solve-vm.py ./samples/sample8-unprotected.bin
#
#echo "4 sur 20"
#/usr/bin/time -v ./solve-vm.py ./samples/sample10-unprotected.bin
#
#echo "5 sur 20"
#/usr/bin/time -v ./solve-vm.py ./samples/sample11-unprotected.bin
#
#echo "6 sur 20"
#/usr/bin/time -v ./solve-vm.py ./samples/sample12-unprotected.bin
#
#echo "7 sur 20"
#/usr/bin/time -v ./solve-vm.py ./samples/sample13-unprotected.bin
#
#echo "8 sur 20"
#/usr/bin/time -v ./solve-vm.py ./samples/sample14-unprotected.bin
#
#echo "9 sur 20"
#/usr/bin/time -v ./solve-vm.py ./samples/sample15-unprotected.bin
#
#echo "10 sur 20"
#/usr/bin/time -v ./solve-vm.py ./samples/sample17-unprotected.bin
#
#echo "11 sur 20"
#/usr/bin/time -v ./solve-vm.py ./samples/sample18-unprotected.bin
#
#echo "12 sur 20"
#/usr/bin/time -v ./solve-vm.py ./samples/sample19-unprotected.bin
#
#echo "13 sur 20"
#/usr/bin/time -v ./solve-vm.py ./samples/sample20-unprotected.bin
#
#echo "14 sur 20"
#/usr/bin/time -v ./solve-vm.py ./samples/sample21-unprotected.bin
#
#echo "15 sur 20"
#/usr/bin/time -v ./solve-vm.py ./samples/sample22-unprotected.bin
#
#echo "16 sur 20"
#/usr/bin/time -v ./solve-vm.py ./samples/sample23-unprotected.bin
#
#echo "17 sur 20"
#/usr/bin/time -v ./solve-vm.py ./samples/sample24-unprotected.bin
#
#echo "18 sur 20"
#/usr/bin/time -v ./solve-vm.py ./samples/sample25-unprotected.bin
#
#echo "19 sur 20"
#/usr/bin/time -v ./solve-vm.py ./samples/sample26-unprotected.bin
#
#echo "19 sur 20"
#/usr/bin/time -v ./solve-vm.py ./samples/sample3-unprotected.bin
#
##----------------------------------------------------------------------------
#
#echo "1 sur 20"
#/usr/bin/time -v ./solve-vm.py ./deobfuscated_binaries/sample4-virt-dispatcher-switch.deobfuscated
#
#echo "2 sur 20"
#/usr/bin/time -v ./solve-vm.py ./deobfuscated_binaries/sample5-virt-dispatcher-switch.deobfuscated
#
#echo "3 sur 20"
#/usr/bin/time -v ./solve-vm.py ./deobfuscated_binaries/sample8-virt-dispatcher-switch.deobfuscated
#
#echo "4 sur 20"
#/usr/bin/time -v ./solve-vm.py ./deobfuscated_binaries/sample10-virt-dispatcher-switch.deobfuscated
#
#echo "5 sur 20"
#/usr/bin/time -v ./solve-vm.py ./deobfuscated_binaries/sample11-virt-dispatcher-switch.deobfuscated
#
#echo "6 sur 20"
#/usr/bin/time -v ./solve-vm.py ./deobfuscated_binaries/sample12-virt-dispatcher-switch.deobfuscated
#
#echo "7 sur 20"
#/usr/bin/time -v ./solve-vm.py ./deobfuscated_binaries/sample13-virt-dispatcher-switch.deobfuscated
#
#echo "8 sur 20"
#/usr/bin/time -v ./solve-vm.py ./deobfuscated_binaries/sample14-virt-dispatcher-switch.deobfuscated
#
#echo "9 sur 20"
#/usr/bin/time -v ./solve-vm.py ./deobfuscated_binaries/sample15-virt-dispatcher-switch.deobfuscated
#
#echo "10 sur 20"
#/usr/bin/time -v ./solve-vm.py ./deobfuscated_binaries/sample17-virt-dispatcher-switch.deobfuscated
#
#echo "11 sur 20"
#/usr/bin/time -v ./solve-vm.py ./deobfuscated_binaries/sample18-virt-dispatcher-switch.deobfuscated
#
#echo "12 sur 20"
#/usr/bin/time -v ./solve-vm.py ./deobfuscated_binaries/sample19-virt-dispatcher-switch.deobfuscated
#
#echo "13 sur 20"
#/usr/bin/time -v ./solve-vm.py ./deobfuscated_binaries/sample20-virt-dispatcher-switch.deobfuscated
#
#echo "14 sur 20"
#/usr/bin/time -v ./solve-vm.py ./deobfuscated_binaries/sample21-virt-dispatcher-switch.deobfuscated
#
#echo "15 sur 20"
#/usr/bin/time -v ./solve-vm.py ./deobfuscated_binaries/sample22-virt-dispatcher-switch.deobfuscated
#
#echo "16 sur 20"
#/usr/bin/time -v ./solve-vm.py ./deobfuscated_binaries/sample23-virt-dispatcher-switch.deobfuscated
#
#echo "17 sur 20"
#/usr/bin/time -v ./solve-vm.py ./deobfuscated_binaries/sample24-virt-dispatcher-switch.deobfuscated
#
#echo "18 sur 20"
#/usr/bin/time -v ./solve-vm.py ./deobfuscated_binaries/sample25-virt-dispatcher-switch.deobfuscated
#
#echo "19 sur 20"
#/usr/bin/time -v ./solve-vm.py ./deobfuscated_binaries/sample26-virt-dispatcher-switch.deobfuscated
#
#echo "19 sur 20"
#/usr/bin/time -v ./solve-vm.py ./deobfuscated_binaries/sample3-virt-dispatcher-switch.deobfuscated
