; ModuleID = 'llvm_expressions/sample20-virt-duplicate-opcodes-2.ll'
source_filename = "llvm_expressions/sample20-virt-duplicate-opcodes-2.ll"
target datalayout = "e-m:e-i64:64-f80:128-n8:16:32:64-S128"
target triple = "x86_64-pc-linux-gnu"

; Function Attrs: norecurse nounwind readnone
define i64 @SECRET(i64 %SymVar_0) local_unnamed_addr #0 {
.3:
  %.4 = and i64 %SymVar_0, 8722064
  %.5 = or i64 %.4, 520257826
  %.6 = and i64 %.5, %SymVar_0
  %.13 = shl i64 %.6, 57
  %.16 = lshr i64 %.6, 7
  %.17 = or i64 %.13, %.16
  %.20 = mul i64 %SymVar_0, 107672031
  %.22 = add i64 %.17, %.20
  %.24 = lshr i64 %.22, 56
  %0 = lshr i64 %.22, 54
  %.163 = and i64 %.24, %0
  %.164 = shl nuw nsw i64 %.163, 4
  %.167 = and i64 %.164, 208
  %.196 = or i64 %.167, %.5
  %.199 = lshr exact i64 %.6, 1
  %.200 = and i64 %.199, 8
  %.201 = or i64 %.200, 1
  %.202 = sub nsw i64 64, %.201
  %.208 = shl i64 %.196, %.202
  %.217 = lshr i64 %.196, %.201
  %.218 = or i64 %.208, %.217
  %.263 = or i64 %0, %.24
  %.264 = and i64 %.263, 14
  %.265 = or i64 %.264, 1
  %.266 = sub nsw i64 64, %.265
  %.270 = lshr i64 %.218, %.266
  %.343 = shl i64 %.218, %.265
  %.344 = or i64 %.270, %.343
  ret i64 %.344
}

attributes #0 = { norecurse nounwind readnone }
