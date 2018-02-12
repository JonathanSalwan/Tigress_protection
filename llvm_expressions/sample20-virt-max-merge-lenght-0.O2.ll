; ModuleID = 'llvm_expressions/sample20-virt-max-merge-lenght-0.ll'
source_filename = "llvm_expressions/sample20-virt-max-merge-lenght-0.ll"
target datalayout = "e-m:e-i64:64-f80:128-n8:16:32:64-S128"
target triple = "x86_64-pc-linux-gnu"

; Function Attrs: norecurse nounwind readnone
define i64 @SECRET(i64 %SymVar_0) local_unnamed_addr #0 {
.3:
  %.4 = and i64 %SymVar_0, 8722064
  %.5 = or i64 %.4, 520257826
  %.6 = and i64 %.5, %SymVar_0
  %.13 = shl i64 %.6, 57
  %.16 = lshr i64 %.6, 7
  %.17 = or i64 %.13, %.16
  %.20 = mul i64 %SymVar_0, 107672031
  %.22 = add i64 %.17, %.20
  %.24 = lshr i64 %.22, 56
  %0 = lshr i64 %.22, 54
  %.163 = and i64 %.24, %0
  %.164 = shl nuw nsw i64 %.163, 4
  %.167 = and i64 %.164, 208
  %.196 = or i64 %.167, %.5
  %.199 = lshr exact i64 %.6, 1
  %.200 = and i64 %.199, 8
  %.201 = or i64 %.200, 1
  %.202 = sub nsw i64 64, %.201
  %.206 = shl i64 %.196, %.202
  %.215 = lshr i64 %.196, %.201
  %.216 = or i64 %.206, %.215
  %.261 = or i64 %0, %.24
  %.262 = and i64 %.261, 14
  %.263 = or i64 %.262, 1
  %.264 = sub nsw i64 64, %.263
  %.268 = lshr i64 %.216, %.264
  %.339 = shl i64 %.216, %.263
  %.340 = or i64 %.268, %.339
  ret i64 %.340
}

attributes #0 = { norecurse nounwind readnone }
