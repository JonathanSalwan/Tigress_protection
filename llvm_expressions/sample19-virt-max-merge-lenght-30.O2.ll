; ModuleID = 'llvm_expressions/sample19-virt-max-merge-lenght-30.ll'
source_filename = "llvm_expressions/sample19-virt-max-merge-lenght-30.ll"
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
  %.43 = lshr i64 %SymVar_0, %.39
  %.74 = shl i64 %SymVar_0, %.38
  %.75 = or i64 %.43, %.74
  %.81 = shl nuw i64 %div, 2
  %.85 = or i64 %.81, %div
  %.86 = and i64 %.85, 14
  %.87 = or i64 %.86, 1
  %.88 = sub nsw i64 64, %.87
  %.92 = lshr i64 %.4, %.88
  %.100 = shl i64 %.4, %.87
  %.101 = or i64 %.92, %.100
  %0 = mul i64 %SymVar_0, 343000538
  %.105 = add i64 %0, 1638886
  %.107 = lshr i64 %.105, 18
  %.233 = and i64 %.107, 14
  %.234 = or i64 %.233, 1
  %.235 = sub nsw i64 64, %.234
  %.239 = lshr i64 %.75, %.235
  %.270 = shl i64 %.75, %.234
  %.271 = or i64 %.239, %.270
  %.274 = lshr i64 %.271, 4
  %.275 = and i64 %.274, 14
  %.276 = or i64 %.275, 1
  %.277 = sub nsw i64 64, %.276
  %.281 = shl i64 %.101, %.277
  %.372 = lshr i64 %.101, %.276
  %.373 = or i64 %.281, %.372
  ret i64 %.373
}

attributes #0 = { norecurse nounwind readnone }
