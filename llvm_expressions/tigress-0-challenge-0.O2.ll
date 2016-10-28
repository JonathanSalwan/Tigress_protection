; ModuleID = 'llvm_expressions/./tigress-0-challenge-0.ll'
target datalayout = "e-m:e-i64:64-f80:128-n8:16:32:64-S128"
target triple = "x86_64-pc-linux-gnu"

; Function Attrs: norecurse nounwind readnone
define i64 @__arybo(i64 %SymVar_0) #0 {
.3:
  %.5 = or i64 %SymVar_0, 74171520
  %.6 = add i64 %SymVar_0, 886599889
  %.7 = and i64 %.6, 6
  %.8 = or i64 %.7, 1
  %.14 = shl i64 %.5, %.8
  %.15 = shl i64 %.14, 4
  %.18 = and i64 %.15, 1008
  %.19 = add i64 %SymVar_0, 500810693
  %.22 = mul i64 %.6, 951885855
  %.24 = and i64 %.22, 14
  %.25 = or i64 %.24, 1
  %.26 = sub nsw i64 64, %.25
  %.32 = shl i64 %.19, %.26
  %.45 = lshr i64 %.19, %.25
  %.46 = or i64 %.32, %.45
  %.47 = or i64 %.46, %.18
  %.56 = or i64 %.6, %SymVar_0
  %.57 = or i64 %.56, -637752949
  %.58 = add i64 %.57, %.6
  %.49 = mul i64 %.5, 746348727
  %.53 = mul i64 %.49, %.58
  %.60 = mul i64 %.53, %.47
  ret i64 %.60
}

attributes #0 = { norecurse nounwind readnone }
