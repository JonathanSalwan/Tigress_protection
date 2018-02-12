; ModuleID = 'llvm_expressions/sample19-virt-max-merge-lenght-20.ll'
source_filename = "llvm_expressions/sample19-virt-max-merge-lenght-20.ll"
target datalayout = "e-m:e-i64:64-f80:128-n8:16:32:64-S128"
target triple = "x86_64-pc-linux-gnu"

; Function Attrs: norecurse nounwind readnone
define i64 @SECRET(i64 %SymVar_0) local_unnamed_addr #0 {
.3:
  %.4 = add i64 %SymVar_0, -902749805
  %div = udiv i64 %SymVar_0, 7
  %.14 = lshr i64 %div, 3
  %.15 = and i64 %.14, 14
  %.16 = or i64 %.15, 1
  %.34 = shl i64 127996265, %.16
  %.38 = lshr i64 %.34, 4
  %.39 = and i64 %.38, 14
  %.40 = or i64 %.39, 1
  %.41 = sub nsw i64 64, %.40
  %.45 = lshr i64 %SymVar_0, %.41
  %.78 = shl i64 %SymVar_0, %.40
  %.79 = or i64 %.45, %.78
  %.85 = shl nuw i64 %div, 2
  %.89 = or i64 %.85, %div
  %.90 = and i64 %.89, 14
  %.91 = or i64 %.90, 1
  %.92 = sub nsw i64 64, %.91
  %.96 = lshr i64 %.4, %.92
  %.104 = shl i64 %.4, %.91
  %.105 = or i64 %.96, %.104
  %0 = mul i64 %SymVar_0, 343000538
  %.109 = add i64 %0, 1638886
  %.111 = lshr i64 %.109, 18
  %.237 = and i64 %.111, 14
  %.238 = or i64 %.237, 1
  %.239 = sub nsw i64 64, %.238
  %.245 = lshr i64 %.79, %.239
  %.278 = shl i64 %.79, %.238
  %.279 = or i64 %.245, %.278
  %.282 = lshr i64 %.279, 4
  %.283 = and i64 %.282, 14
  %.284 = or i64 %.283, 1
  %.285 = sub nsw i64 64, %.284
  %.289 = shl i64 %.105, %.285
  %.382 = lshr i64 %.105, %.284
  %.383 = or i64 %.289, %.382
  ret i64 %.383
}

attributes #0 = { norecurse nounwind readnone }
