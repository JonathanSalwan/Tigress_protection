; ModuleID = 'llvm_expressions/./tigress-1-challenge-1.ll'
target datalayout = "e-m:e-i64:64-f80:128-n8:16:32:64-S128"
target triple = "x86_64-pc-linux-gnu"

; Function Attrs: norecurse nounwind readnone
define i64 @__arybo(i64 %SymVar_0) #0 {
.3:
  %.6 = lshr i64 %SymVar_0, 13
  %.9 = shl i64 %SymVar_0, 51
  %.10 = or i64 %.6, %.9
  %.11 = add i64 %.10, 210061817713481728
  %.20 = sub i64 %SymVar_0, %.11
  %.23 = lshr i64 %.20, 2
  %.24 = and i64 %.23, 14
  %.25 = or i64 %.24, 1
  %.26 = sub nsw i64 64, %.25
  %.32 = shl i64 %.11, %.26
  %.60 = lshr i64 %.11, %.25
  %.61 = or i64 %.32, %.60
  %.64 = lshr i64 %SymVar_0, 55
  %.67 = shl i64 %SymVar_0, 9
  %.68 = or i64 %.64, %.67
  %.69 = or i64 %SymVar_0, 1049658519
  %.70 = sub i64 %.68, %.69
  %.138 = sub i64 %.61, %.70
  %.267 = xor i64 %.138, %.32
  %.335 = xor i64 %.32, %.70
  %.336 = and i64 %.267, %.335
  %.140 = xor i64 %.335, %.138
  %.337 = xor i64 %.140, %.336
  %.733 = icmp sgt i64 %.337, -1
  br i1 %.733, label %.3.endif.endif.endif.if, label %.3.endif.endif.endif.else

.3.endif.endif.endif.if:                          ; preds = %.3
  %.750 = lshr i64 %.20, 4
  %.751 = and i64 %.750, 14
  %.752 = or i64 %.751, 1
  %.753 = sub nsw i64 64, %.752
  %.759 = lshr i64 %.11, %.753
  %.770 = shl i64 %.11, %.752
  %.771 = or i64 %.759, %.770
  %.780 = or i64 %.64, %SymVar_0
  %.783 = lshr i64 %.780, 4
  %.784 = and i64 %.783, 6
  %.785 = or i64 %.784, 1
  %.791 = lshr i64 %.771, %.785
  br label %.3.endif.endif.endif.endif

.3.endif.endif.endif.else:                        ; preds = %.3
  %.816 = shl i64 %.11, 4
  %.819 = and i64 %.816, 1008
  %.820 = or i64 %.819, %.11
  %.821 = add i64 %.820, %.64
  %.822 = shl i64 %.821, 3
  %.825 = and i64 %.822, 248
  %.826 = or i64 %.825, %.820
  %.836 = lshr i64 %.20, 36
  %.991 = and i64 %.836, 14
  %.992 = or i64 %.991, 1
  %.993 = sub nsw i64 64, %.992
  %.999 = lshr i64 %.826, %.993
  %.1032 = shl i64 %.826, %.992
  %.1033 = or i64 %.999, %.1032
  %.1034 = shl i64 %.11, 3
  %.1039 = or i64 %.64, %SymVar_0
  %.1047 = or i64 %.1039, %.1034
  %.1050 = lshr i64 %.1047, 4
  %.1051 = and i64 %.1050, 6
  %.1052 = or i64 %.1051, 1
  %.1058 = lshr i64 %.1033, %.1052
  br label %.3.endif.endif.endif.endif

.3.endif.endif.endif.endif:                       ; preds = %.3.endif.endif.endif.else, %.3.endif.endif.endif.if
  %.1060 = phi i64 [ %.791, %.3.endif.endif.endif.if ], [ %.1058, %.3.endif.endif.endif.else ]
  ret i64 %.1060
}

attributes #0 = { norecurse nounwind readnone }
