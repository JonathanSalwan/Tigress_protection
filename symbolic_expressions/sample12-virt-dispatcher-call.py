#!/usr/bin/env python2
## -*- coding: utf-8 -*-

import sys

def sx(bits, value):
    sign_bit = 1 << (bits - 1)
    return (value & (sign_bit - 1)) - (value & sign_bit)

SymVar_0 = int(sys.argv[1])
ref_676 = SymVar_0
ref_687 = ref_676 # MOV operation
ref_699 = ref_687 # MOV operation
ref_701 = ref_699 # MOV operation
ref_5700 = ref_701 # MOV operation
ref_5896 = ref_5700 # MOV operation
ref_6098 = (ref_5896 & 0xFFFFFFFF) # MOV operation
ref_7457 = (ref_6098 & 0xFFFFFFFF) # MOV operation
ref_7461 = (ref_7457 & 0xFFFFFFFF) # MOV operation
ref_7495 = (((ref_7461 & 0xFFFFFFFF) >> 24) & 0xFF) # Byte reference - MOV operation
ref_7496 = (((ref_7461 & 0xFFFFFFFF) >> 16) & 0xFF) # Byte reference - MOV operation
ref_7497 = (((ref_7461 & 0xFFFFFFFF) >> 8) & 0xFF) # Byte reference - MOV operation
ref_7498 = ((ref_7461 & 0xFFFFFFFF) & 0xFF) # Byte reference - MOV operation
ref_7549 = ref_7498 # MOVZX operation
ref_7551 = (ref_7549 & 0xFF) # MOVZX operation
ref_7557 = (ref_7551 & 0xFFFFFFFF) # MOV operation
ref_7583 = (ref_7557 & 0xFFFFFFFF) # MOV operation
ref_7593 = (ref_7583 & 0xFF) # MOVZX operation
ref_7595 = ((ref_7593 & 0xFFFFFFFF) ^ ((((0x81) << 8 | 0x1C) << 8 | 0x9D) << 8 | 0xC5)) # XOR operation
ref_7602 = (ref_7595 & 0xFFFFFFFF) # MOV operation
ref_7606 = (((sx(0x20, 0x1000193) * sx(0x20, (ref_7602 & 0xFFFFFFFF))) & 0xFFFFFFFFFFFFFFFF) & 0xFFFFFFFF) # IMUL operation
ref_7651 = ref_7497 # MOVZX operation
ref_7653 = (ref_7651 & 0xFF) # MOVZX operation
ref_7655 = (ref_7606 & 0xFFFFFFFF) # MOV operation
ref_7657 = (ref_7655 & 0xFFFFFFFF) # MOV operation
ref_7659 = (ref_7653 & 0xFFFFFFFF) # MOV operation
ref_7685 = (ref_7659 & 0xFFFFFFFF) # MOV operation
ref_7695 = (ref_7685 & 0xFF) # MOVZX operation
ref_7697 = ((ref_7695 & 0xFFFFFFFF) ^ (ref_7657 & 0xFFFFFFFF)) # XOR operation
ref_7704 = (ref_7697 & 0xFFFFFFFF) # MOV operation
ref_7708 = (((sx(0x20, 0x1000193) * sx(0x20, (ref_7704 & 0xFFFFFFFF))) & 0xFFFFFFFFFFFFFFFF) & 0xFFFFFFFF) # IMUL operation
ref_7753 = ref_7496 # MOVZX operation
ref_7755 = (ref_7753 & 0xFF) # MOVZX operation
ref_7757 = (ref_7708 & 0xFFFFFFFF) # MOV operation
ref_7759 = (ref_7757 & 0xFFFFFFFF) # MOV operation
ref_7761 = (ref_7755 & 0xFFFFFFFF) # MOV operation
ref_7787 = (ref_7761 & 0xFFFFFFFF) # MOV operation
ref_7797 = (ref_7787 & 0xFF) # MOVZX operation
ref_7799 = ((ref_7797 & 0xFFFFFFFF) ^ (ref_7759 & 0xFFFFFFFF)) # XOR operation
ref_7806 = (ref_7799 & 0xFFFFFFFF) # MOV operation
ref_7810 = (((sx(0x20, 0x1000193) * sx(0x20, (ref_7806 & 0xFFFFFFFF))) & 0xFFFFFFFFFFFFFFFF) & 0xFFFFFFFF) # IMUL operation
ref_7827 = ref_7495 # MOVZX operation
ref_7829 = (ref_7827 & 0xFF) # MOVZX operation
ref_7831 = (ref_7810 & 0xFFFFFFFF) # MOV operation
ref_7833 = (ref_7831 & 0xFFFFFFFF) # MOV operation
ref_7835 = (ref_7829 & 0xFFFFFFFF) # MOV operation
ref_7861 = (ref_7835 & 0xFFFFFFFF) # MOV operation
ref_7871 = (ref_7861 & 0xFF) # MOVZX operation
ref_7873 = ((ref_7871 & 0xFFFFFFFF) ^ (ref_7833 & 0xFFFFFFFF)) # XOR operation
ref_7880 = (ref_7873 & 0xFFFFFFFF) # MOV operation
ref_7884 = (((sx(0x20, 0x1000193) * sx(0x20, (ref_7880 & 0xFFFFFFFF))) & 0xFFFFFFFFFFFFFFFF) & 0xFFFFFFFF) # IMUL operation
ref_7899 = (ref_7884 & 0xFFFFFFFF) # MOV operation
ref_8621 = (ref_7899 & 0xFFFFFFFF) # MOV operation
ref_8823 = (ref_8621 & 0xFFFFFFFF) # MOV operation
ref_9496 = (ref_8823 & 0xFFFFFFFF) # MOV operation
ref_9684 = (ref_9496 & 0xFFFFFFFF) # MOV operation
ref_9724 = (ref_9684 & 0xFFFFFFFF) # MOV operation
ref_9748 = (ref_9724 & 0xFFFFFFFF) # MOV operation
ref_9760 = ref_9748 # MOV operation
ref_9762 = ref_9760 # MOV operation

print ref_9762 & 0xffffffffffffffff
