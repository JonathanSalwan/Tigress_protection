; ModuleID = 'llvm_expressions/tigress-2-challenge-1.ll'
source_filename = "llvm_expressions/tigress-2-challenge-1.ll"
target datalayout = "e-m:e-i64:64-f80:128-n8:16:32:64-S128"
target triple = "x86_64-pc-linux-gnu"

; Function Attrs: norecurse nounwind readnone
define i64 @SECRET(i64 %SymVar_0) local_unnamed_addr #0 {
.3:
  %.6 = lshr i64 %SymVar_0, 49
  %.9 = shl i64 %SymVar_0, 15
  %.10 = or i64 %.6, %.9
  %.11 = shl nuw nsw i64 %.6, 4
  %.14 = and i64 %.11, 1008
  %.15 = add i64 %SymVar_0, -1106879319
  %.16 = or i64 %.14, %.15
  %.18 = or i64 %SymVar_0, 7625649618944
  %.20 = mul i64 %.16, %.18
  %.22 = and i64 %.10, %.18
  %.26 = lshr i64 %.15, 3
  %0 = and i64 %.26, 6
  %.29 = or i64 %0, 1
  %.34 = lshr i64 %SymVar_0, %.29
  %.36 = mul i64 %.34, %.22
  %.40 = mul i64 %.36, %.10
  %.42 = sub i64 %.20, %.40
  %.45 = xor i64 %.42, %.20
  %.46 = xor i64 %.40, %.20
  %.47 = and i64 %.45, %.46
  %.44 = xor i64 %.46, %.42
  %.48 = xor i64 %.44, %.47
  %.50 = icmp sgt i64 %.48, -1
  %.52 = icmp ne i64 %.42, 0
  %.77.demorgan = and i1 %.52, %.50
  br i1 %.77.demorgan, label %.3.endif.endif.endif.endif.endif.endif.endif, label %.3.endif.endif.endif.endif.endif.endif.if

.3.endif.endif.endif.endif.endif.endif.if:        ; preds = %.3
  %.120 = shl i64 %SymVar_0, 2
  %.123 = and i64 %.120, 60
  %.141 = or i64 %.36, %.123
  br label %.3.endif.endif.endif.endif.endif.endif.endif

.3.endif.endif.endif.endif.endif.endif.endif:     ; preds = %.3, %.3.endif.endif.endif.endif.endif.endif.if
  %.300.sink = phi i64 [ %.141, %.3.endif.endif.endif.endif.endif.endif.if ], [ %.36, %.3 ]
  %.301 = sub i64 %.10, %.300.sink
  %.307 = xor i64 %.16, %.18
  %.308 = or i64 %.301, %.307
  ret i64 %.308
}

attributes #0 = { norecurse nounwind readnone }
