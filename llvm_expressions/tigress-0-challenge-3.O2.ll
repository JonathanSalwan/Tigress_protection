; ModuleID = 'llvm_expressions/tigress-0-challenge-3.ll'
source_filename = "llvm_expressions/tigress-0-challenge-3.ll"
target datalayout = "e-m:e-i64:64-f80:128-n8:16:32:64-S128"
target triple = "x86_64-pc-linux-gnu"

; Function Attrs: norecurse nounwind readnone
define i64 @SECRET(i64 %SymVar_0) local_unnamed_addr #0 {
.3:
  %.6 = shl i64 %SymVar_0, 63
  %.9 = lshr i64 %SymVar_0, 1
  %.10 = or i64 %.6, %.9
  %.13 = mul i64 %.10, %.10
  %0 = lshr i64 %SymVar_0, 3
  %1 = and i64 %0, 6
  %.28 = or i64 %1, 1
  %.33 = lshr i64 %SymVar_0, %.28
  %.34 = or i64 %.33, 1021570277
  %.35 = sub i64 %.13, %.34
  %.36 = and i64 %SymVar_0, -2
  %.37 = add i64 %SymVar_0, 40
  %.47 = lshr i64 %.37, 4
  %2 = and i64 %.47, 6
  %.50 = or i64 %2, 1
  %.55 = shl i64 %.36, %.50
  %.58 = lshr exact i64 %.55, 1
  %.59 = and i64 %.58, 14
  %.60 = or i64 %.59, 1
  %.61 = sub nsw i64 0, %.60
  %.66 = and i64 %.61, 63
  %.67 = lshr i64 %.35, %.66
  %.97 = shl i64 %.35, %.60
  %.98 = or i64 %.67, %.97
  ret i64 %.98
}

attributes #0 = { norecurse nounwind readnone }
