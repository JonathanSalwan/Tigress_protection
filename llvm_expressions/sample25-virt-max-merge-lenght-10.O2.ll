; ModuleID = 'llvm_expressions/sample25-virt-max-merge-lenght-10.ll'
source_filename = "llvm_expressions/sample25-virt-max-merge-lenght-10.ll"
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
  %.49 = lshr i64 %.38, %.43
  %.150 = and i64 %.49, 4611686018427387903
  %.152 = mul i64 %.150, 81897458
  %.154 = shl nuw nsw i64 %.18, 2
  %.158 = or i64 %.13, %.22
  %.159 = add i64 %.158, %SymVar_0
  %.160 = or i64 %.159, %.154
  %.161 = shl i64 %.159, 2
  %.165 = or i64 %.160, %.161
  %.166 = xor i64 %.152, %.165
  %.167 = and i64 %.166, 14
  %.168 = or i64 %.167, 1
  %.169 = sub nsw i64 64, %.168
  %.173 = lshr i64 %.24, %.169
  %.210 = shl i64 %.24, %.168
  %.211 = or i64 %.173, %.210
  ret i64 %.211
}

attributes #0 = { norecurse nounwind readnone }
