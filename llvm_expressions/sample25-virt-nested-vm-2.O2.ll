; ModuleID = 'llvm_expressions/sample25-virt-nested-vm-2.ll'
source_filename = "llvm_expressions/sample25-virt-nested-vm-2.ll"
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
  %.172 = and i64 %.47, 4611686018427387903
  %.174 = mul i64 %.172, 81897458
  %.176 = shl nuw nsw i64 %.18, 2
  %.180 = or i64 %.13, %.22
  %.181 = add i64 %.180, %SymVar_0
  %.182 = or i64 %.181, %.176
  %.183 = shl i64 %.181, 2
  %.187 = or i64 %.182, %.183
  %.188 = xor i64 %.174, %.187
  %.189 = and i64 %.188, 14
  %.190 = or i64 %.189, 1
  %.191 = sub nsw i64 64, %.190
  %.195 = lshr i64 %.24, %.191
  %.232 = shl i64 %.24, %.190
  %.233 = or i64 %.195, %.232
  ret i64 %.233
}

attributes #0 = { norecurse nounwind readnone }
