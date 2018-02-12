; ModuleID = 'llvm_expressions/sample17-virt-obfuscate-decode-byte-array-false.ll'
source_filename = "llvm_expressions/sample17-virt-obfuscate-decode-byte-array-false.ll"
target datalayout = "e-m:e-i64:64-f80:128-n8:16:32:64-S128"
target triple = "x86_64-pc-linux-gnu"

; Function Attrs: norecurse nounwind readnone
define i64 @SECRET(i64 %SymVar_0) local_unnamed_addr #0 {
.3:
  %.6 = shl i64 %SymVar_0, 57
  %.9 = lshr i64 %SymVar_0, 7
  %.10 = or i64 %.6, %.9
  %.11 = add i64 %SymVar_0, 58
  %.12 = or i64 %.9, %.11
  %.13 = shl i64 %.12, 4
  %.16 = and i64 %.13, 1008
  %.17 = or i64 %.16, %.10
  %.20 = shl i64 %SymVar_0, 53
  %.23 = lshr i64 %SymVar_0, 11
  %.24 = or i64 %.20, %.23
  %.25 = add nuw nsw i64 %.9, 223017115
  %.26 = and i64 %.25, 492486502
  %.27 = sub i64 %.24, %.26
  %.28 = and i64 %.27, 14
  %.29 = or i64 %.28, 1
  %.30 = sub nsw i64 64, %.29
  %.34 = shl i64 %.17, %.30
  %.42 = lshr i64 %.17, %.29
  %.43 = or i64 %.34, %.42
  %.44.neg = add i64 %SymVar_0, -541408995
  %.45 = sub i64 %.44.neg, %.10
  %.48 = lshr i64 %.17, 1
  %.49 = and i64 %.48, 14
  %.50 = or i64 %.49, 1
  %.51 = sub nsw i64 64, %.50
  %.55 = shl i64 %.27, %.51
  %.66 = lshr i64 %.27, %.50
  %.67 = or i64 %.55, %.66
  %.68 = sub i64 %.67, %.45
  %.69 = or i64 %.68, %.45
  %.72 = lshr i64 %.69, 1
  %.73 = and i64 %.72, 6
  %.74 = or i64 %.73, 1
  %.78 = shl i64 %.43, %.74
  ret i64 %.78
}

attributes #0 = { norecurse nounwind readnone }
