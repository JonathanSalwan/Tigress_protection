; ModuleID = 'llvm_expressions/sample25-virt-bogus-loop-iterations-3.ll'
source_filename = "llvm_expressions/sample25-virt-bogus-loop-iterations-3.ll"
target datalayout = "e-m:e-i64:64-f80:128-n8:16:32:64-S128"
target triple = "x86_64-pc-linux-gnu"

; Function Attrs: norecurse nounwind readnone
define i64 @SECRET(i64 %SymVar_0) local_unnamed_addr #0 {
.3:
  %div = udiv i64 %SymVar_0, 6
  %.13 = mul i64 %div, -432345564227385076
  %.18 = lshr i64 %SymVar_0, 51
  %.21 = shl i64 %SymVar_0, 13
  %.22 = or i64 %.18, %.21
  %.24 = mul i64 %.13, %.22
  %.27 = add i64 %.13, %SymVar_0
  %.29 = sub nsw i64 1471924646, %.18
  %.32 = lshr i64 %.29, 2
  %.33 = and i64 %.32, 6
  %.34 = or i64 %.33, 1
  %.38 = lshr i64 %.27, %.34
  %.41 = lshr i64 %.38, 1
  %.42 = and i64 %.41, 6
  %.43 = or i64 %.42, 1
  %.47 = lshr i64 %.38, %.43
  %.148 = and i64 %.47, 4611686018427387903
  %.150 = mul i64 %.148, 81897458
  %.152 = shl nuw nsw i64 %.18, 2
  %.156 = or i64 %.13, %.22
  %.157 = add i64 %.156, %SymVar_0
  %.158 = or i64 %.157, %.152
  %.159 = shl i64 %.157, 2
  %.163 = or i64 %.158, %.159
  %.164 = xor i64 %.150, %.163
  %.165 = and i64 %.164, 14
  %.166 = or i64 %.165, 1
  %.167 = sub nsw i64 64, %.166
  %.171 = lshr i64 %.24, %.167
  %.208 = shl i64 %.24, %.166
  %.209 = or i64 %.171, %.208
  ret i64 %.209
}

attributes #0 = { norecurse nounwind readnone }
