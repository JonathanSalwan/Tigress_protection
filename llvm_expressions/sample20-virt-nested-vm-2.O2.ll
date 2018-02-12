; ModuleID = 'llvm_expressions/sample20-virt-nested-vm-2.ll'
source_filename = "llvm_expressions/sample20-virt-nested-vm-2.ll"
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
  %.199 = and i64 %.24, %0
  %.200 = shl nuw nsw i64 %.199, 4
  %.203 = and i64 %.200, 208
  %.232 = or i64 %.203, %.5
  %.235 = lshr exact i64 %.6, 1
  %.236 = and i64 %.235, 8
  %.237 = or i64 %.236, 1
  %.238 = sub nsw i64 64, %.237
  %.242 = shl i64 %.232, %.238
  %.253 = lshr i64 %.232, %.237
  %.254 = or i64 %.242, %.253
  %.299 = or i64 %0, %.24
  %.300 = and i64 %.299, 14
  %.301 = or i64 %.300, 1
  %.302 = sub nsw i64 64, %.301
  %.308 = lshr i64 %.254, %.302
  %.381 = shl i64 %.254, %.301
  %.382 = or i64 %.308, %.381
  ret i64 %.382
}

attributes #0 = { norecurse nounwind readnone }
