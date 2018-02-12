; ModuleID = 'llvm_expressions/sample25-virt-dispatcher-call.ll'
source_filename = "llvm_expressions/sample25-virt-dispatcher-call.ll"
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
  %.40 = lshr i64 %.27, %.34
  %.43 = lshr i64 %.40, 1
  %.44 = and i64 %.43, 6
  %.45 = or i64 %.44, 1
  %.51 = lshr i64 %.40, %.45
  %.152 = and i64 %.51, 4611686018427387903
  %.154 = mul i64 %.152, 81897458
  %.156 = shl nuw nsw i64 %.18, 2
  %.160 = or i64 %.13, %.22
  %.161 = add i64 %.160, %SymVar_0
  %.162 = or i64 %.161, %.156
  %.163 = shl i64 %.161, 2
  %.167 = or i64 %.162, %.163
  %.168 = xor i64 %.154, %.167
  %.169 = and i64 %.168, 14
  %.170 = or i64 %.169, 1
  %.171 = sub nsw i64 64, %.170
  %.177 = lshr i64 %.24, %.171
  %.216 = shl i64 %.24, %.170
  %.217 = or i64 %.177, %.216
  ret i64 %.217
}

attributes #0 = { norecurse nounwind readnone }
