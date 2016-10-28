; ModuleID = 'llvm_expressions/tigress-4-challenge-1.ll'
target datalayout = "e-m:e-i64:64-f80:128-n8:16:32:64-S128"
target triple = "x86_64-pc-linux-gnu"

; Function Attrs: norecurse nounwind readnone
define i64 @__arybo(i64 %SymVar_0) #0 {
.3:
  %.6 = lshr i64 %SymVar_0, 57
  %.9 = shl i64 %SymVar_0, 7
  %.10 = or i64 %.6, %.9
  %.11 = add i64 %SymVar_0, 1059198491
  %.18 = mul i64 %.11, 218063048984025710
  %.22 = lshr exact i64 %.18, 1
  %.23 = and i64 %.22, 14
  %.24 = or i64 %.23, 1
  %.25 = sub nsw i64 64, %.24
  %.31 = lshr i64 %.10, %.25
  %.57 = shl i64 %.10, %.24
  %.58 = or i64 %.31, %.57
  %.59 = add i64 %SymVar_0, 11366125
  %.60 = add i64 %.59, %.58
  %.61 = shl i64 %.60, 4
  %.64 = and i64 %.61, 1008
  %.65 = add i64 %.58, 728434157
  %.66 = and i64 %.60, %.65
  %.67 = or i64 %.11, %SymVar_0
  %.68 = add i64 %.66, %.67
  %.69 = or i64 %.64, %.68
  %.70 = add i64 %.69, %.60
  %.74 = lshr i64 %.58, 4
  %.75 = and i64 %.74, 14
  %.76 = or i64 %.75, 1
  %.77 = sub nsw i64 64, %.76
  %.83 = lshr i64 %.11, %.77
  %.94 = shl i64 %.11, %.76
  %.95 = or i64 %.83, %.94
  %.97 = mul i64 %.70, %.95
  ret i64 %.97
}

attributes #0 = { norecurse nounwind readnone }
