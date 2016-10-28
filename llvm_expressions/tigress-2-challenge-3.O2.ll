; ModuleID = 'llvm_expressions/./tigress-2-challenge-3.ll'
target datalayout = "e-m:e-i64:64-f80:128-n8:16:32:64-S128"
target triple = "x86_64-pc-linux-gnu"

; Function Attrs: norecurse nounwind readnone
define i64 @__arybo(i64 %SymVar_0) #0 {
.3:
  %.4 = add i64 %SymVar_0, 712404564
  %.7 = lshr i64 %.4, 59
  %.11 = shl i64 %.4, 5
  %.12 = or i64 %.7, %.11
  %div = udiv i64 %.12, 5
  %.42 = add i64 %div, %SymVar_0
  %.52 = add i64 %.42, %.12
  %.53 = add i64 %SymVar_0, -1384240675
  %.65 = sub i64 %.53, %.12
  %.99 = lshr i64 %.65, 56
  %.108 = shl nuw nsw i64 %.99, 16
  %.195 = lshr i64 %.65, 16
  %.210 = shl i64 %.195, 56
  %.163 = and i64 %.65, 72057594021216248
  %.181 = or i64 %.163, %.108
  %.211 = or i64 %.181, %.210
  %div2 = lshr exact i64 %.211, 3
  %.478 = sub i64 %.52, %div2
  %.480 = xor i64 %.478, %.52
  %0 = xor i64 %.478, -9223372036854775808
  %.1007 = and i64 %0, %.52
  %.1008 = xor i64 %.480, %.1007
  %.2429 = icmp sgt i64 %.1008, -1
  br i1 %.2429, label %.3.endif.endif.endif.if, label %.3.endif.endif.endif.else

.3.endif.endif.endif.if:                          ; preds = %.3
  %.2476 = lshr i64 %.42, 1
  %.2477 = and i64 %.2476, 14
  %.2478 = or i64 %.2477, 1
  %.2479 = sub nsw i64 64, %.2478
  %.2485 = lshr i64 %.12, %.2479
  %.2496 = shl i64 %.12, %.2478
  %.2497 = or i64 %.2485, %.2496
  %.2498 = add i64 %SymVar_0, 5938
  %.2504 = lshr i64 %.2498, 7
  %.2565 = add i64 %.65, %.2504
  %.2568 = lshr i64 %.2565, 2
  %.2569 = and i64 %.2568, 14
  %.2570 = or i64 %.2569, 1
  %.2571 = sub nsw i64 64, %.2570
  %.2577 = lshr i64 %.2497, %.2571
  %.2642 = shl i64 %.2497, %.2570
  %.2643 = or i64 %.2577, %.2642
  br label %.3.endif.endif.endif.endif

.3.endif.endif.endif.else:                        ; preds = %.3
  %.177 = lshr i64 %.65, 48
  %1 = lshr i64 %.4, 43
  %.2684 = and i64 %1, 65535
  %2 = lshr i64 %.4, 19
  %.2721 = and i64 %2, 16711680
  %.2722 = or i64 %.2684, %.2721
  %3 = shl i64 %.4, 13
  %.2741 = and i64 %3, 4278190080
  %.2742 = or i64 %.2722, %.2741
  %.2755 = and i64 %.11, 1095216660480
  %.2756 = or i64 %.2742, %.2755
  %4 = shl i64 %.4, 21
  %.2775 = and i64 %4, 280375465082880
  %.2776 = or i64 %.2756, %.2775
  %5 = lshr i64 %.4, 3
  %.2815 = shl i64 %.12, 48
  %.2816 = and i64 %.2815, 71776119061217280
  %.2822 = shl i64 %5, 56
  %.2817 = or i64 %.2776, %.2822
  %.2823 = or i64 %.2817, %.2816
  %.2865 = lshr i64 %.42, 1
  %.2866 = and i64 %.2865, 14
  %.2867 = or i64 %.2866, 1
  %.2868 = sub nsw i64 64, %.2867
  %.2874 = lshr i64 %.2823, %.2868
  %.2946 = shl i64 %.2823, %.2867
  %.2947 = or i64 %.2874, %.2946
  %.2948 = add i64 %SymVar_0, 5938
  %.2954 = lshr i64 %.2948, 7
  %.3151 = add nuw nsw i64 %.177, %.2954
  %.3154 = lshr i64 %.3151, 2
  %.3155 = and i64 %.3154, 14
  %.3156 = or i64 %.3155, 1
  %.3157 = sub nsw i64 64, %.3156
  %.3163 = lshr i64 %.2947, %.3157
  %.3350 = shl i64 %.2947, %.3156
  %.3351 = or i64 %.3163, %.3350
  br label %.3.endif.endif.endif.endif

.3.endif.endif.endif.endif:                       ; preds = %.3.endif.endif.endif.else, %.3.endif.endif.endif.if
  %.3353 = phi i64 [ %.2643, %.3.endif.endif.endif.if ], [ %.3351, %.3.endif.endif.endif.else ]
  ret i64 %.3353
}

attributes #0 = { norecurse nounwind readnone }
