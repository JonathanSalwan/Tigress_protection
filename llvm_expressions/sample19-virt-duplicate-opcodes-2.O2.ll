; ModuleID = 'llvm_expressions/sample19-virt-duplicate-opcodes-2.ll'
source_filename = "llvm_expressions/sample19-virt-duplicate-opcodes-2.ll"
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
  %.32 = shl i64 127996265, %.16
  %.36 = lshr i64 %.32, 4
  %.37 = and i64 %.36, 14
  %.38 = or i64 %.37, 1
  %.39 = sub nsw i64 64, %.38
  %.45 = lshr i64 %SymVar_0, %.39
  %.76 = shl i64 %SymVar_0, %.38
  %.77 = or i64 %.45, %.76
  %.83 = shl nuw i64 %div, 2
  %.87 = or i64 %.83, %div
  %.88 = and i64 %.87, 14
  %.89 = or i64 %.88, 1
  %.90 = sub nsw i64 64, %.89
  %.94 = lshr i64 %.4, %.90
  %.100 = shl i64 %.4, %.89
  %.101 = or i64 %.94, %.100
  %0 = mul i64 %SymVar_0, 343000538
  %.105 = add i64 %0, 1638886
  %.107 = lshr i64 %.105, 18
  %.233 = and i64 %.107, 14
  %.234 = or i64 %.233, 1
  %.235 = sub nsw i64 64, %.234
  %.241 = lshr i64 %.77, %.235
  %.272 = shl i64 %.77, %.234
  %.273 = or i64 %.241, %.272
  %.276 = lshr i64 %.273, 4
  %.277 = and i64 %.276, 14
  %.278 = or i64 %.277, 1
  %.279 = sub nsw i64 64, %.278
  %.283 = shl i64 %.101, %.279
  %.376 = lshr i64 %.101, %.278
  %.377 = or i64 %.283, %.376
  ret i64 %.377
}

attributes #0 = { norecurse nounwind readnone }
