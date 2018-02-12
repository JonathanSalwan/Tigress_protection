; ModuleID = 'llvm_expressions/sample19-virt-duplicate-opcodes-3.ll'
source_filename = "llvm_expressions/sample19-virt-duplicate-opcodes-3.ll"
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
  %.43 = lshr i64 %SymVar_0, %.37
  %.76 = shl i64 %SymVar_0, %.36
  %.77 = or i64 %.43, %.76
  %.83 = shl nuw i64 %div, 2
  %.87 = or i64 %.83, %div
  %.88 = and i64 %.87, 14
  %.89 = or i64 %.88, 1
  %.90 = sub nsw i64 64, %.89
  %.96 = lshr i64 %.4, %.90
  %.102 = shl i64 %.4, %.89
  %.103 = or i64 %.96, %.102
  %0 = mul i64 %SymVar_0, 343000538
  %.107 = add i64 %0, 1638886
  %.109 = lshr i64 %.107, 18
  %.235 = and i64 %.109, 14
  %.236 = or i64 %.235, 1
  %.237 = sub nsw i64 64, %.236
  %.243 = lshr i64 %.77, %.237
  %.274 = shl i64 %.77, %.236
  %.275 = or i64 %.243, %.274
  %.278 = lshr i64 %.275, 4
  %.279 = and i64 %.278, 14
  %.280 = or i64 %.279, 1
  %.281 = sub nsw i64 64, %.280
  %.285 = shl i64 %.103, %.281
  %.378 = lshr i64 %.103, %.280
  %.379 = or i64 %.285, %.378
  ret i64 %.379
}

attributes #0 = { norecurse nounwind readnone }
