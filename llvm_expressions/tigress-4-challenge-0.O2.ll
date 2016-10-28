; ModuleID = 'llvm_expressions/tigress-4-challenge-0.ll'
target datalayout = "e-m:e-i64:64-f80:128-n8:16:32:64-S128"
target triple = "x86_64-pc-linux-gnu"

; Function Attrs: norecurse nounwind readnone
define i64 @__arybo(i64 %SymVar_0) #0 {
.3:
  %.7 = lshr i64 %SymVar_0, 55
  %.4 = shl i64 %SymVar_0, 9
  %.11 = or i64 %.4, %.7
  %.12 = or i64 %.11, 250589732864
  %0 = lshr i64 %SymVar_0, 42
  %.24 = and i64 %0, 8191
  %.36 = shl i64 %.12, 13
  %.37 = or i64 %.24, %SymVar_0
  %.38 = or i64 %.37, %.36
  %.41 = lshr i64 %.37, 1
  %.42 = and i64 %.41, 14
  %.43 = or i64 %.42, 1
  %.44 = sub nsw i64 64, %.43
  %.50 = lshr i64 %.12, %.44
  %.96 = shl i64 %.12, %.43
  %.97 = or i64 %.50, %.96
  %.125 = add i64 %SymVar_0, 104868834
  %.134 = or i64 %SymVar_0, 893657663
  %.127 = mul i64 %.125, 1004737041
  %.131 = mul i64 %.127, %.134
  %.136 = mul i64 %.131, %.38
  %.138 = shl i64 %.136, 4
  %.141 = and i64 %.138, 496
  %.143 = or i64 %.141, %.125
  %.186 = lshr i64 %.136, 3
  %.187 = and i64 %.186, 6
  %.188 = or i64 %.187, 1
  %.194 = lshr i64 %.143, %.188
  %.386 = sub i64 %.97, %.194
  %.388 = xor i64 %.386, %.97
  %1 = xor i64 %.386, -9223372036854775808
  %.868 = and i64 %1, %.97
  %.869 = xor i64 %.388, %.868
  %.1064 = icmp eq i64 %.97, %.194
  %.869.lobit = lshr i64 %.869, 63
  %.10644 = zext i1 %.1064 to i64
  %.1074 = or i64 %.869.lobit, %.10644
  %.2373 = icmp eq i64 %.1074, 0
  %.2419 = add i64 %.136, 916080512
  %.2468 = mul i64 %.143, %.2419
  br i1 %.2373, label %.3.endif.endif.endif.endif.endif.if, label %.3.endif.endif.endif.endif.endif.else

.3.endif.endif.endif.endif.endif.if:              ; preds = %.3
  %.2506 = shl i64 %.37, 2
  %.2509 = and i64 %.2506, 48
  %.2536 = or i64 %.2509, %.37
  %.2539 = lshr i64 %.2536, 3
  %.2540 = and i64 %.2539, 14
  %.2541 = or i64 %.2540, 1
  %.2542 = sub nsw i64 64, %.2541
  %.2548 = lshr i64 %.12, %.2542
  %.2568 = shl i64 %.12, %.2541
  %.2569 = or i64 %.2548, %.2568
  br label %.3.endif.endif.endif.endif.endif.endif

.3.endif.endif.endif.endif.endif.else:            ; preds = %.3
  %.2645 = lshr i64 %.136, 35
  %.2671 = and i64 %.2645, 255
  %.2675 = and i64 %.186, 65280
  %.2676 = or i64 %.2671, %.2675
  %.2680 = and i64 %.186, 16711680
  %.2681 = or i64 %.2676, %.2680
  %.2685 = and i64 %.186, 4278190080
  %.2686 = or i64 %.2681, %.2685
  %2 = shl i64 %.136, 29
  %.2701 = and i64 %2, 1095216660480
  %.2702 = or i64 %.2686, %.2701
  %.2706 = and i64 %.186, 280375465082880
  %.2707 = or i64 %.2702, %.2706
  %.2711 = and i64 %.186, 71776119061217280
  %.2712 = or i64 %.2707, %.2711
  %.2713 = lshr i64 %.136, 59
  %.2716 = shl nuw nsw i64 %.2713, 56
  %.2717 = or i64 %.2712, %.2716
  %.2718 = lshr i64 %.38, 59
  %.2830 = and i64 %.2718, 14
  %.2831 = or i64 %.2830, 1
  %.2832 = sub nsw i64 64, %.2831
  %.2838 = lshr i64 %.2717, %.2832
  %.2893 = shl i64 %.2717, %.2831
  %.2894 = or i64 %.2838, %.2893
  br label %.3.endif.endif.endif.endif.endif.endif

.3.endif.endif.endif.endif.endif.endif:           ; preds = %.3.endif.endif.endif.endif.endif.else, %.3.endif.endif.endif.endif.endif.if
  %.2569.sink = phi i64 [ %.2569, %.3.endif.endif.endif.endif.endif.if ], [ %.2894, %.3.endif.endif.endif.endif.endif.else ]
  %.2571 = mul i64 %.2468, %.2569.sink
  ret i64 %.2571
}

attributes #0 = { norecurse nounwind readnone }
