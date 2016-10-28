; ModuleID = 'llvm_expressions/./tigress-2-challenge-2.ll'
target datalayout = "e-m:e-i64:64-f80:128-n8:16:32:64-S128"
target triple = "x86_64-pc-linux-gnu"

; Function Attrs: norecurse nounwind readnone
define i64 @__arybo(i64 %SymVar_0) #0 {
.3:
  %.4 = or i64 %SymVar_0, 689476123
  %.5 = add i64 %.4, 1569874
  %.6 = and i64 %.5, 306692729
  %.9 = mul i64 %.6, %SymVar_0
  %.11 = add i64 %.9, -8011755
  %.14 = lshr i64 %.5, 4
  %.15 = and i64 %.14, 14
  %.16 = or i64 %.15, 1
  %.17 = sub nsw i64 64, %.16
  %.23 = lshr i64 %SymVar_0, %.17
  %.34 = shl i64 %SymVar_0, %.16
  %.35 = or i64 %.34, %.11
  %.36 = or i64 %.35, %.23
  %.39 = lshr i64 %.36, 2
  %.40 = and i64 %.39, 14
  %.41 = or i64 %.40, 1
  %.42 = sub nsw i64 64, %.41
  %.48 = shl i64 %.36, %.42
  %.59 = lshr i64 %.36, %.41
  %.60 = or i64 %.48, %.59
  %.61 = shl i64 %.60, 4
  %.64 = and i64 %.61, 1008
  %.65 = or i64 %.64, %.5
  %div = udiv i64 %.65, 7
  %.95 = add i64 %.36, 1
  %.96 = or i64 %.95, %SymVar_0
  %.97 = and i64 %.96, 6
  %.98 = or i64 %.97, 1
  %.104 = shl i64 %.36, %.98
  %.107 = lshr i64 %.104, 4
  %.108 = and i64 %.107, 14
  %.109 = or i64 %.108, 1
  %.110 = sub nsw i64 64, %.109
  %.116 = lshr i64 %div, %.110
  %.164 = shl i64 %div, %.109
  %.165 = or i64 %.116, %.164
  ret i64 %.165
}

attributes #0 = { norecurse nounwind readnone }
