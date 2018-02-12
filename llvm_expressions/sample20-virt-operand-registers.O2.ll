; ModuleID = 'llvm_expressions/sample20-virt-operand-registers.ll'
source_filename = "llvm_expressions/sample20-virt-operand-registers.ll"
target datalayout = "e-m:e-i64:64-f80:128-n8:16:32:64-S128"
target triple = "x86_64-pc-linux-gnu"

; Function Attrs: norecurse nounwind readnone
define i64 @SECRET(i64 %SymVar_0) local_unnamed_addr #0 {
.3:
  %.4 = and i64 %SymVar_0, 8722064
  %.5 = or i64 %.4, 520257826
  %.8 = mul i64 %SymVar_0, 107672031
  %.10 = and i64 %.5, %SymVar_0
  %.13 = lshr i64 %.10, 7
  %.16 = shl i64 %.10, 57
  %.17 = or i64 %.13, %.16
  %.18 = add i64 %.17, %.8
  %.24 = lshr i64 %.18, 56
  %0 = lshr i64 %.18, 54
  %.191 = and i64 %0, %.24
  %.192 = shl nuw nsw i64 %.191, 4
  %.195 = and i64 %.192, 208
  %.196 = or i64 %.195, %.5
  %.199 = lshr exact i64 %.10, 1
  %.200 = and i64 %.199, 8
  %.201 = or i64 %.200, 1
  %.207 = lshr i64 %.196, %.201
  %.213 = sub nsw i64 64, %.201
  %.219 = shl i64 %.196, %.213
  %.220 = or i64 %.207, %.219
  %.265 = or i64 %.24, %0
  %.266 = and i64 %.265, 14
  %.267 = or i64 %.266, 1
  %.273 = shl i64 %.220, %.267
  %.345 = sub nsw i64 64, %.267
  %.351 = lshr i64 %.220, %.345
  %.352 = or i64 %.273, %.351
  ret i64 %.352
}

attributes #0 = { norecurse nounwind readnone }
