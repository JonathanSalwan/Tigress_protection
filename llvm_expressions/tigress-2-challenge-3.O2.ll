; ModuleID = 'llvm_expressions/tigress-2-challenge-3.ll'
source_filename = "llvm_expressions/tigress-2-challenge-3.ll"
target datalayout = "e-m:e-i64:64-f80:128-n8:16:32:64-S128"
target triple = "x86_64-pc-linux-gnu"

; Function Attrs: norecurse nounwind readnone
define i64 @SECRET(i64 %SymVar_0) local_unnamed_addr #0 {
.3:
  %.4 = add i64 %SymVar_0, 712404564
  %.7 = lshr i64 %.4, 59
  %.11 = shl i64 %.4, 5
  %.12 = or i64 %.7, %.11
  %div = udiv i64 %.12, 5
  %.42 = add i64 %div, %SymVar_0
  %.43 = add i64 %.42, %.12
  %.44 = add i64 %SymVar_0, -1384240675
  %.47 = sub i64 %.44, %.12
  %.55 = lshr i64 %.47, 56
  %.64 = shl nuw nsw i64 %.55, 16
  %.86 = lshr i64 %.47, 16
  %.101 = shl i64 %.86, 56
  %.80 = and i64 %.47, 72057594021216248
  %.85 = or i64 %.80, %.64
  %.102 = or i64 %.85, %.101
  %div3 = lshr exact i64 %.102, 3
  %.132 = sub i64 %.43, %div3
  %.134 = xor i64 %.132, %.43
  %0 = xor i64 %.132, -9223372036854775808
  %.137 = and i64 %0, %.43
  %.138 = xor i64 %.134, %.137
  %.160 = icmp sgt i64 %.138, -1
  br i1 %.160, label %.3.endif.endif.endif.if, label %.3.endif.endif.endif.else

.3.endif.endif.endif.if:                          ; preds = %.3
  %.212 = lshr i64 %.42, 1
  %.213 = and i64 %.212, 14
  %.214 = or i64 %.213, 1
  %.215 = sub nsw i64 0, %.214
  %.220 = and i64 %.215, 63
  %.221 = lshr i64 %.12, %.220
  %.232 = shl i64 %.12, %.214
  br label %.3.endif.endif.endif.endif

.3.endif.endif.endif.else:                        ; preds = %.3
  %.81 = lshr i64 %.47, 48
  %1 = lshr i64 %.4, 43
  %.411 = and i64 %1, 65535
  %2 = lshr i64 %.4, 19
  %.439 = and i64 %2, 16711680
  %.440 = or i64 %.411, %.439
  %3 = shl i64 %.4, 13
  %.450 = and i64 %3, 4278190080
  %.451 = or i64 %.440, %.450
  %.455 = and i64 %.11, 1095216660480
  %.456 = or i64 %.451, %.455
  %4 = shl i64 %.4, 21
  %.466 = and i64 %4, 280375465082880
  %.467 = or i64 %.456, %.466
  %5 = lshr i64 %.4, 3
  %.488 = shl i64 %.12, 48
  %.489 = and i64 %.488, 71776119061217280
  %.495 = shl i64 %5, 56
  %.490 = or i64 %.467, %.495
  %.496 = or i64 %.490, %.489
  %.529 = lshr i64 %.42, 1
  %.530 = and i64 %.529, 14
  %.531 = or i64 %.530, 1
  %.532 = sub nsw i64 0, %.531
  %.537 = and i64 %.532, 63
  %.538 = lshr i64 %.496, %.537
  %.571 = shl i64 %.496, %.531
  br label %.3.endif.endif.endif.endif

.3.endif.endif.endif.endif:                       ; preds = %.3.endif.endif.endif.else, %.3.endif.endif.endif.if
  %.750.pre-phi = phi i64 [ %.531, %.3.endif.endif.endif.else ], [ %.214, %.3.endif.endif.endif.if ]
  %.571.sink = phi i64 [ %.571, %.3.endif.endif.endif.else ], [ %.232, %.3.endif.endif.endif.if ]
  %.538.sink = phi i64 [ %.538, %.3.endif.endif.endif.else ], [ %.221, %.3.endif.endif.endif.if ]
  %.81.sink = phi i64 [ %.81, %.3.endif.endif.endif.else ], [ %.47, %.3.endif.endif.endif.if ]
  %.744.sink = phi i64 [ %.496, %.3.endif.endif.endif.else ], [ %.12, %.3.endif.endif.endif.if ]
  %.572 = or i64 %.538.sink, %.571.sink
  %.573 = add i64 %SymVar_0, 5938
  %.579 = lshr i64 %.573, 7
  %.676 = add i64 %.81.sink, %.579
  %.679 = lshr i64 %.676, 2
  %.680 = and i64 %.679, 14
  %.681 = or i64 %.680, 1
  %.682 = sub nsw i64 0, %.681
  %.687 = and i64 %.682, 63
  %.688 = lshr i64 %.572, %.687
  %.755 = shl i64 %.744.sink, %.750.pre-phi
  %.756 = or i64 %.755, %.538.sink
  %.797 = shl i64 %.756, %.681
  %.798 = or i64 %.688, %.797
  ret i64 %.798
}

attributes #0 = { norecurse nounwind readnone }
