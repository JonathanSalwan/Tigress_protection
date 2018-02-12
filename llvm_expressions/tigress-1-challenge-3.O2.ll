; ModuleID = 'llvm_expressions/tigress-1-challenge-3.ll'
source_filename = "llvm_expressions/tigress-1-challenge-3.ll"
target datalayout = "e-m:e-i64:64-f80:128-n8:16:32:64-S128"
target triple = "x86_64-pc-linux-gnu"

; Function Attrs: norecurse nounwind readnone
define i64 @SECRET(i64 %SymVar_0) local_unnamed_addr #0 {
.3:
  %.6 = mul i64 %SymVar_0, 107672031
  %.8 = and i64 %SymVar_0, 8722064
  %.9 = or i64 %.8, 520257826
  %.10 = and i64 %.9, %SymVar_0
  %.13 = lshr i64 %.10, 7
  %.16 = shl i64 %.10, 57
  %.17 = or i64 %.13, %.16
  %.18 = add i64 %.17, %.6
  %.24 = lshr i64 %.18, 56
  %0 = lshr i64 %.18, 54
  %.169 = and i64 %.24, %0
  %.170 = shl nuw nsw i64 %.169, 4
  %.173 = and i64 %.170, 208
  %.202 = or i64 %.173, %.9
  %.205 = lshr exact i64 %.10, 1
  %.206 = and i64 %.205, 8
  %.207 = or i64 %.206, 1
  %.208 = sub nsw i64 0, %.207
  %.213 = and i64 %.208, 63
  %.214 = shl i64 %.202, %.213
  %.225 = lshr i64 %.202, %.207
  %.226 = or i64 %.214, %.225
  %.271 = or i64 %.24, %0
  %.272 = and i64 %.271, 14
  %.273 = or i64 %.272, 1
  %.274 = sub nsw i64 0, %.273
  %.279 = and i64 %.274, 63
  %.280 = lshr i64 %.226, %.279
  %.357 = shl i64 %.226, %.273
  %.358 = or i64 %.280, %.357
  ret i64 %.358
}

attributes #0 = { norecurse nounwind readnone }
