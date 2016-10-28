; ModuleID = 'llvm_expressions/./tigress-1-challenge-2.ll'
target datalayout = "e-m:e-i64:64-f80:128-n8:16:32:64-S128"
target triple = "x86_64-pc-linux-gnu"

; Function Attrs: norecurse nounwind readnone
define i64 @__arybo(i64 %SymVar_0) #0 {
.3:
  %.4 = add i64 %SymVar_0, -902749805
  %div = udiv i64 %SymVar_0, 7
  %.36 = lshr i64 %div, 3
  %.37 = and i64 %.36, 14
  %.38 = or i64 %.37, 1
  %.56 = shl i64 127996265, %.38
  %.60 = lshr i64 %.56, 4
  %.61 = and i64 %.60, 14
  %.62 = or i64 %.61, 1
  %.68 = shl i64 %SymVar_0, %.62
  %.98 = sub nsw i64 64, %.62
  %.104 = lshr i64 %SymVar_0, %.98
  %.105 = or i64 %.104, %.68
  %.111 = shl nuw i64 %div, 2
  %.115 = or i64 %.111, %div
  %.116 = and i64 %.115, 14
  %.117 = or i64 %.116, 1
  %.118 = sub nsw i64 64, %.117
  %.124 = lshr i64 %.4, %.118
  %.132 = shl i64 %.4, %.117
  %.133 = or i64 %.124, %.132
  %0 = mul i64 %SymVar_0, 343000538
  %.137 = add i64 %0, 1638886
  %.139 = lshr i64 %.137, 18
  %.280 = and i64 %.139, 14
  %.281 = or i64 %.280, 1
  %.287 = shl i64 %.105, %.281
  %.315 = sub nsw i64 64, %.281
  %.321 = lshr i64 %.105, %.315
  %.322 = or i64 %.287, %.321
  %.325 = lshr i64 %.322, 4
  %.326 = and i64 %.325, 14
  %.327 = or i64 %.326, 1
  %.333 = lshr i64 %.133, %.327
  %.425 = sub nsw i64 64, %.327
  %.431 = shl i64 %.133, %.425
  %.432 = or i64 %.431, %.333
  ret i64 %.432
}

attributes #0 = { norecurse nounwind readnone }
