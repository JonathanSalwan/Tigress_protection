; ModuleID = 'llvm_expressions/sample12-virt-nested-vm-2.ll'
source_filename = "llvm_expressions/sample12-virt-nested-vm-2.ll"
target datalayout = "e-m:e-i64:64-f80:128-n8:16:32:64-S128"
target triple = "x86_64-pc-linux-gnu"

; Function Attrs: norecurse nounwind readnone
define i64 @SECRET(i64 %SymVar_0) local_unnamed_addr #0 {
.3:
  %.5 = trunc i64 %SymVar_0 to i32
  %.20 = lshr i32 %.5, 24
  %.37 = lshr i32 %.5, 16
  %.49 = and i32 %.37, 255
  %.54 = lshr i32 %.5, 8
  %.66 = and i32 %.54, 255
  %.82 = and i64 %SymVar_0, 255
  %.95 = xor i64 %.82, -2128831035
  %.101 = mul nsw i64 %.95, 16777619
  %.102 = trunc i64 %.101 to i32
  %.109 = xor i32 %.102, %.66
  %.115 = mul i32 %.109, 16777619
  %.123 = xor i32 %.115, %.49
  %.129 = mul i32 %.123, 16777619
  %.137 = xor i32 %.129, %.20
  %.143 = mul i32 %.137, 16777619
  %.173 = zext i32 %.143 to i64
  ret i64 %.173
}

attributes #0 = { norecurse nounwind readnone }
