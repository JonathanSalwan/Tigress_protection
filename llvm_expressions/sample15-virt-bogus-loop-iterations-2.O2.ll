; ModuleID = 'llvm_expressions/sample15-virt-bogus-loop-iterations-2.ll'
source_filename = "llvm_expressions/sample15-virt-bogus-loop-iterations-2.ll"
target datalayout = "e-m:e-i64:64-f80:128-n8:16:32:64-S128"
target triple = "x86_64-pc-linux-gnu"

; Function Attrs: norecurse nounwind readnone
define i64 @SECRET(i64 %SymVar_0) local_unnamed_addr #0 {
.3:
  %.27 = add i64 %SymVar_0, 524114809
  %.28 = shl i64 %.27, 14
  %.29 = lshr i64 %.27, 50
  %.301 = or i64 %.28, %.29
  %.31 = xor i64 %.301, %SymVar_0
  %.32 = shl i64 %.31, 14
  %.33 = lshr i64 %.31, 50
  %.342 = or i64 %.32, %.33
  %.35 = xor i64 %.342, 524114809
  %.36 = add i64 %.35, %SymVar_0
  ret i64 %.36
}

attributes #0 = { norecurse nounwind readnone }
