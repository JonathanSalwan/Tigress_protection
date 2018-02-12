; ModuleID = 'llvm_expressions/sample17-virt-operand-registers.ll'
source_filename = "llvm_expressions/sample17-virt-operand-registers.ll"
target datalayout = "e-m:e-i64:64-f80:128-n8:16:32:64-S128"
target triple = "x86_64-pc-linux-gnu"

; Function Attrs: norecurse nounwind readnone
define i64 @SECRET(i64 %SymVar_0) local_unnamed_addr #0 {
.3:
  %.6 = lshr i64 %SymVar_0, 7
  %.9 = shl i64 %SymVar_0, 57
  %.10 = or i64 %.6, %.9
  %.11 = add i64 %SymVar_0, 58
  %.12 = or i64 %.11, %.6
  %.13 = shl i64 %.12, 4
  %.16 = and i64 %.13, 1008
  %.17 = or i64 %.16, %.10
  %.20 = lshr i64 %SymVar_0, 11
  %.23 = shl i64 %SymVar_0, 53
  %.24 = or i64 %.20, %.23
  %.25 = add nuw nsw i64 %.6, 223017115
  %.26 = and i64 %.25, 492486502
  %.27 = sub i64 %.24, %.26
  %.28 = and i64 %.27, 14
  %.29 = or i64 %.28, 1
  %.35 = lshr i64 %.17, %.29
  %.38 = sub nsw i64 64, %.29
  %.44 = shl i64 %.17, %.38
  %.45 = or i64 %.44, %.35
  %.48 = lshr i64 %.17, 1
  %.49 = and i64 %.48, 14
  %.50 = or i64 %.49, 1
  %.56 = lshr i64 %.27, %.50
  %.62 = sub nsw i64 64, %.50
  %.68 = shl i64 %.27, %.62
  %.69 = or i64 %.68, %.56
  %.70.neg = add i64 %SymVar_0, -541408995
  %.71 = sub i64 %.70.neg, %.10
  %.72 = sub i64 %.69, %.71
  %.73 = or i64 %.72, %.71
  %.76 = lshr i64 %.73, 1
  %.77 = and i64 %.76, 6
  %.78 = or i64 %.77, 1
  %.84 = shl i64 %.45, %.78
  ret i64 %.84
}

attributes #0 = { norecurse nounwind readnone }
