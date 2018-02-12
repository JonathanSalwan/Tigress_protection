; ModuleID = 'llvm_expressions/sample12-virt-operand-registers.ll'
source_filename = "llvm_expressions/sample12-virt-operand-registers.ll"
target datalayout = "e-m:e-i64:64-f80:128-n8:16:32:64-S128"
target triple = "x86_64-pc-linux-gnu"

; Function Attrs: norecurse nounwind readnone
define i64 @SECRET(i64 %SymVar_0) local_unnamed_addr #0 {
.3:
  %.5 = trunc i64 %SymVar_0 to i32
  %.14 = lshr i32 %.5, 24
  %.31 = lshr i32 %.5, 16
  %.43 = and i32 %.31, 255
  %.48 = lshr i32 %.5, 8
  %.60 = and i32 %.48, 255
  %.76 = and i64 %SymVar_0, 255
  %.89 = xor i64 %.76, -2128831035
  %.95 = mul nsw i64 %.89, 16777619
  %.96 = trunc i64 %.95 to i32
  %.103 = xor i32 %.96, %.60
  %.109 = mul i32 %.103, 16777619
  %.117 = xor i32 %.109, %.43
  %.123 = mul i32 %.117, 16777619
  %.131 = xor i32 %.123, %.14
  %.137 = mul i32 %.131, 16777619
  %.151 = zext i32 %.137 to i64
  ret i64 %.151
}

attributes #0 = { norecurse nounwind readnone }
