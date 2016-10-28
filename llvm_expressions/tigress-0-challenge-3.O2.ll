; ModuleID = 'llvm_expressions/./tigress-0-challenge-3.ll'
target datalayout = "e-m:e-i64:64-f80:128-n8:16:32:64-S128"
target triple = "x86_64-pc-linux-gnu"

; Function Attrs: norecurse nounwind readnone
define i64 @__arybo(i64 %SymVar_0) #0 {
.3:
  %.6 = shl i64 %SymVar_0, 63
  %.9 = lshr i64 %SymVar_0, 1
  %.10 = or i64 %.6, %.9
  %.13 = mul i64 %.10, %.10
  %0 = lshr i64 %SymVar_0, 3
  %.26 = and i64 %0, 6
  %.27 = or i64 %.26, 1
  %.33 = lshr i64 %SymVar_0, %.27
  %.34 = or i64 %.33, 1021570277
  %.35 = sub i64 %.13, %.34
  %.36 = shl nuw i64 %.9, 1
  %.37 = add i64 %SymVar_0, 40
  %.43 = lshr i64 %.37, 4
  %.48 = and i64 %.43, 6
  %.49 = or i64 %.48, 1
  %.55 = shl i64 %.36, %.49
  %.58 = lshr exact i64 %.55, 1
  %.59 = and i64 %.58, 14
  %.60 = or i64 %.59, 1
  %.61 = sub nsw i64 64, %.60
  %.67 = lshr i64 %.35, %.61
  %.97 = shl i64 %.35, %.60
  %.98 = or i64 %.67, %.97
  ret i64 %.98
}

attributes #0 = { norecurse nounwind readnone }
