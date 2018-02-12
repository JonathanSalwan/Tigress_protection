; ModuleID = 'llvm_expressions/sample12-virt-duplicate-opcodes-3.ll'
source_filename = "llvm_expressions/sample12-virt-duplicate-opcodes-3.ll"
target datalayout = "e-m:e-i64:64-f80:128-n8:16:32:64-S128"
target triple = "x86_64-pc-linux-gnu"

; Function Attrs: norecurse nounwind readnone
define i64 @SECRET(i64 %SymVar_0) local_unnamed_addr #0 {
.3:
  %.5 = trunc i64 %SymVar_0 to i32
  %.12 = lshr i32 %.5, 24
  %.29 = lshr i32 %.5, 16
  %.41 = and i32 %.29, 255
  %.46 = lshr i32 %.5, 8
  %.58 = and i32 %.46, 255
  %.74 = and i64 %SymVar_0, 255
  %.87 = xor i64 %.74, -2128831035
  %.93 = mul nsw i64 %.87, 16777619
  %.94 = trunc i64 %.93 to i32
  %.101 = xor i32 %.94, %.58
  %.107 = mul i32 %.101, 16777619
  %.115 = xor i32 %.107, %.41
  %.121 = mul i32 %.115, 16777619
  %.129 = xor i32 %.121, %.12
  %.135 = mul i32 %.129, 16777619
  %.149 = zext i32 %.135 to i64
  ret i64 %.149
}

attributes #0 = { norecurse nounwind readnone }
