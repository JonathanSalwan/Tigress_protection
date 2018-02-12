; ModuleID = 'llvm_expressions/sample17-virt-add-opaque-to-vpc-false.ll'
source_filename = "llvm_expressions/sample17-virt-add-opaque-to-vpc-false.ll"
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
  %.36 = shl i64 %.17, %.30
  %.44 = lshr i64 %.17, %.29
  %.45 = or i64 %.36, %.44
  %.46.neg = add i64 %SymVar_0, -541408995
  %.47 = sub i64 %.46.neg, %.10
  %.50 = lshr i64 %.17, 1
  %.51 = and i64 %.50, 14
  %.52 = or i64 %.51, 1
  %.53 = sub nsw i64 64, %.52
  %.59 = shl i64 %.27, %.53
  %.70 = lshr i64 %.27, %.52
  %.71 = or i64 %.59, %.70
  %.72 = sub i64 %.71, %.47
  %.73 = or i64 %.72, %.47
  %.76 = lshr i64 %.73, 1
  %.77 = and i64 %.76, 6
  %.78 = or i64 %.77, 1
  %.84 = shl i64 %.45, %.78
  ret i64 %.84
}

attributes #0 = { norecurse nounwind readnone }
