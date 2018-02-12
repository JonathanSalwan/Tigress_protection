; ModuleID = 'llvm_expressions/sample19-virt-bogus-functions-3.ll'
source_filename = "llvm_expressions/sample19-virt-bogus-functions-3.ll"
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
  %.47 = lshr i64 %SymVar_0, %.41
  %.82 = shl i64 %SymVar_0, %.40
  %.83 = or i64 %.47, %.82
  %.89 = shl nuw i64 %div, 2
  %.93 = or i64 %.89, %div
  %.94 = and i64 %.93, 14
  %.95 = or i64 %.94, 1
  %.96 = sub nsw i64 64, %.95
  %.102 = lshr i64 %.4, %.96
  %.110 = shl i64 %.4, %.95
  %.111 = or i64 %.102, %.110
  %0 = mul i64 %SymVar_0, 343000538
  %.115 = add i64 %0, 1638886
  %.117 = lshr i64 %.115, 18
  %.243 = and i64 %.117, 14
  %.244 = or i64 %.243, 1
  %.245 = sub nsw i64 64, %.244
  %.251 = lshr i64 %.83, %.245
  %.284 = shl i64 %.83, %.244
  %.285 = or i64 %.251, %.284
  %.288 = lshr i64 %.285, 4
  %.289 = and i64 %.288, 14
  %.290 = or i64 %.289, 1
  %.291 = sub nsw i64 64, %.290
  %.297 = shl i64 %.111, %.291
  %.394 = lshr i64 %.111, %.290
  %.395 = or i64 %.297, %.394
  ret i64 %.395
}

attributes #0 = { norecurse nounwind readnone }
