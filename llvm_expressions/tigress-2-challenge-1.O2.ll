; ModuleID = 'llvm_expressions/./tigress-2-challenge-1.ll'
target datalayout = "e-m:e-i64:64-f80:128-n8:16:32:64-S128"
target triple = "x86_64-pc-linux-gnu"

; Function Attrs: norecurse nounwind readnone
define i64 @__arybo(i64 %SymVar_0) #0 {
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
  %.30 = and i64 %.10, %.18
  %.35 = lshr i64 %.15, 3
  %.36 = and i64 %.35, 6
  %.37 = or i64 %.36, 1
  %.43 = lshr i64 %SymVar_0, %.37
  %.45 = mul i64 %.43, %.30
  %.56 = mul i64 %.45, %.10
  %.112 = sub i64 %.20, %.56
  %.188 = xor i64 %.112, %.20
  %.243 = xor i64 %.56, %.20
  %.244 = and i64 %.188, %.243
  %.114 = xor i64 %.243, %.112
  %.245 = xor i64 %.114, %.244
  %.248 = icmp sgt i64 %.245, -1
  %.309 = icmp ne i64 %.20, %.56
  %.365.demorgan = and i1 %.309, %.248
  br i1 %.365.demorgan, label %.3.endif.endif.endif.endif.endif.endif.endif.endif.endif.else, label %.3.endif.endif.endif.endif.endif.endif.endif.endif.endif.if

.3.endif.endif.endif.endif.endif.endif.endif.endif.endif.if: ; preds = %.3
  %.785 = shl i64 %SymVar_0, 2
  %.788 = and i64 %.785, 60
  %.806 = or i64 %.45, %.788
  %.932 = sub i64 %.10, %.806
  %.938 = xor i64 %.16, %.18
  %.939 = or i64 %.932, %.938
  br label %.3.endif.endif.endif.endif.endif.endif.endif.endif.endif.endif

.3.endif.endif.endif.endif.endif.endif.endif.endif.endif.else: ; preds = %.3
  %.973 = sub i64 %.10, %.45
  %.988 = xor i64 %.16, %.18
  %.989 = or i64 %.973, %.988
  br label %.3.endif.endif.endif.endif.endif.endif.endif.endif.endif.endif

.3.endif.endif.endif.endif.endif.endif.endif.endif.endif.endif: ; preds = %.3.endif.endif.endif.endif.endif.endif.endif.endif.endif.else, %.3.endif.endif.endif.endif.endif.endif.endif.endif.endif.if
  %.991 = phi i64 [ %.939, %.3.endif.endif.endif.endif.endif.endif.endif.endif.endif.if ], [ %.989, %.3.endif.endif.endif.endif.endif.endif.endif.endif.endif.else ]
  ret i64 %.991
}

attributes #0 = { norecurse nounwind readnone }
