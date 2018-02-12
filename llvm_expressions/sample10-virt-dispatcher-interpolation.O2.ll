; ModuleID = 'llvm_expressions/sample10-virt-dispatcher-interpolation.ll'
source_filename = "llvm_expressions/sample10-virt-dispatcher-interpolation.ll"
target datalayout = "e-m:e-i64:64-f80:128-n8:16:32:64-S128"
target triple = "x86_64-pc-linux-gnu"

; Function Attrs: norecurse nounwind readnone
define i64 @SECRET(i64 %SymVar_0) local_unnamed_addr #0 {
.3:
  %.53 = mul i64 %SymVar_0, -4417276706812531889
  %.56 = mul i64 %SymVar_0, -7788283243316379648
  %.57 = lshr i64 %.53, 33
  %.581 = or i64 %.57, %.56
  %.60 = mul i64 %.581, -7046029288634856825
  %.62 = xor i64 %.60, 2870177450012600269
  %.63 = shl i64 %.62, 27
  %.64 = lshr i64 %.62, 37
  %.652 = or i64 %.63, %.64
  %.68 = mul i64 %.652, -7046029288634856825
  %.70 = add i64 %.68, -8796714831421723037
  %.72 = lshr i64 %.70, 33
  %.73 = xor i64 %.72, %.70
  %.75 = mul i64 %.73, -4417276706812531889
  %.78 = lshr i64 %.75, 29
  %.79 = xor i64 %.78, %.75
  %.81 = mul i64 %.79, 1609587929392839161
  %.84 = lshr i64 %.81, 32
  %.85 = xor i64 %.84, %.81
  ret i64 %.85
}

attributes #0 = { norecurse nounwind readnone }
