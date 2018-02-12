; ModuleID = 'llvm_expressions/sample11-virt-obfuscate-decode-byte-array-true.ll'
source_filename = "llvm_expressions/sample11-virt-obfuscate-decode-byte-array-true.ll"
target datalayout = "e-m:e-i64:64-f80:128-n8:16:32:64-S128"
target triple = "x86_64-pc-linux-gnu"

; Function Attrs: norecurse nounwind readnone
define i64 @SECRET(i64 %SymVar_0) local_unnamed_addr #0 {
.3:
  %.17 = trunc i64 %SymVar_0 to i32
  %.35 = and i32 %.17, 65535
  %.38 = add nuw nsw i32 %.35, 8
  %.42 = shl i32 %.38, 16
  %0 = lshr i64 %SymVar_0, 5
  %.67 = trunc i64 %0 to i32
  %.71 = and i32 %.67, 134215680
  %.86 = xor i32 %.71, %.38
  %.89 = xor i32 %.86, %.42
  %.96 = lshr i32 %.89, 11
  %.100 = lshr i64 %SymVar_0, 32
  %.104 = trunc i64 %.100 to i32
  %.122 = and i32 %.104, 65535
  %.99 = add i32 %.89, %.122
  %.125 = add i32 %.99, %.96
  %.129 = shl i32 %.125, 16
  %1 = lshr i64 %SymVar_0, 37
  %.tr = trunc i64 %1 to i32
  %.158 = and i32 %.tr, 134215680
  %.166 = xor i32 %.125, %.158
  %.169 = xor i32 %.166, %.129
  %.176 = lshr i32 %.169, 11
  %.179 = add i32 %.176, %.169
  %.186 = shl i32 %.179, 3
  %.189 = xor i32 %.186, %.179
  %.198 = lshr i32 %.189, 5
  %.201 = add i32 %.198, %.189
  %.212 = shl i32 %.201, 4
  %.215 = xor i32 %.212, %.201
  %.228 = lshr i32 %.215, 17
  %.231 = add i32 %.228, %.215
  %.246 = shl i32 %.231, 25
  %.249 = xor i32 %.246, %.231
  %.266 = lshr i32 %.249, 6
  %.269 = add i32 %.266, %.249
  %.282 = zext i32 %.269 to i64
  ret i64 %.282
}

attributes #0 = { norecurse nounwind readnone }
