; ModuleID = 'llvm_expressions/sample25-virt-operand-registers.ll'
source_filename = "llvm_expressions/sample25-virt-operand-registers.ll"
target datalayout = "e-m:e-i64:64-f80:128-n8:16:32:64-S128"
target triple = "x86_64-pc-linux-gnu"

; Function Attrs: norecurse nounwind readnone
define i64 @SECRET(i64 %SymVar_0) local_unnamed_addr #0 {
.3:
  %.6 = shl i64 %SymVar_0, 13
  %.9 = lshr i64 %SymVar_0, 51
  %.10 = or i64 %.6, %.9
  %div = udiv i64 %SymVar_0, 6
  %.21 = mul i64 %div, -432345564227385076
  %.24 = mul i64 %.10, %.21
  %.26 = or i64 %.10, %.21
  %.27 = add i64 %.26, %SymVar_0
  %.28 = shl nuw nsw i64 %.9, 2
  %.32 = or i64 %.27, %.28
  %.33 = shl i64 %.27, 2
  %.37 = or i64 %.32, %.33
  %.38 = add i64 %.21, %SymVar_0
  %.40 = sub nsw i64 1471924646, %.9
  %.43 = lshr i64 %.40, 2
  %.44 = and i64 %.43, 6
  %.45 = or i64 %.44, 1
  %.51 = lshr i64 %.38, %.45
  %.54 = lshr i64 %.51, 1
  %.55 = and i64 %.54, 6
  %.56 = or i64 %.55, 1
  %.62 = lshr i64 %.51, %.56
  %.163 = and i64 %.62, 4611686018427387903
  %.166 = mul i64 %.163, 81897458
  %.168 = xor i64 %.166, %.37
  %.169 = and i64 %.168, 14
  %.170 = or i64 %.169, 1
  %.176 = shl i64 %.24, %.170
  %.210 = sub nsw i64 64, %.170
  %.216 = lshr i64 %.24, %.210
  %.217 = or i64 %.216, %.176
  ret i64 %.217
}

attributes #0 = { norecurse nounwind readnone }
