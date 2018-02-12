; ModuleID = 'llvm_expressions/sample19-virt-max-merge-lenght-10.ll'
source_filename = "llvm_expressions/sample19-virt-max-merge-lenght-10.ll"
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
  %.30 = shl i64 127996265, %.16
  %.34 = lshr i64 %.30, 4
  %.35 = and i64 %.34, 14
  %.36 = or i64 %.35, 1
  %.37 = sub nsw i64 64, %.36
  %.41 = lshr i64 %SymVar_0, %.37
  %.70 = shl i64 %SymVar_0, %.36
  %.71 = or i64 %.41, %.70
  %.77 = shl nuw i64 %div, 2
  %.81 = or i64 %.77, %div
  %.82 = and i64 %.81, 14
  %.83 = or i64 %.82, 1
  %.84 = sub nsw i64 64, %.83
  %.90 = lshr i64 %.4, %.84
  %.98 = shl i64 %.4, %.83
  %.99 = or i64 %.90, %.98
  %0 = mul i64 %SymVar_0, 343000538
  %.103 = add i64 %0, 1638886
  %.105 = lshr i64 %.103, 18
  %.231 = and i64 %.105, 14
  %.232 = or i64 %.231, 1
  %.233 = sub nsw i64 64, %.232
  %.239 = lshr i64 %.71, %.233
  %.272 = shl i64 %.71, %.232
  %.273 = or i64 %.239, %.272
  %.276 = lshr i64 %.273, 4
  %.277 = and i64 %.276, 14
  %.278 = or i64 %.277, 1
  %.279 = sub nsw i64 64, %.278
  %.283 = shl i64 %.99, %.279
  %.378 = lshr i64 %.99, %.278
  %.379 = or i64 %.283, %.378
  ret i64 %.379
}

attributes #0 = { norecurse nounwind readnone }
