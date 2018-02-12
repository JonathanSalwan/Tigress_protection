; ModuleID = 'llvm_expressions/tigress-2-challenge-4.ll'
source_filename = "llvm_expressions/tigress-2-challenge-4.ll"
target datalayout = "e-m:e-i64:64-f80:128-n8:16:32:64-S128"
target triple = "x86_64-pc-linux-gnu"

; Function Attrs: norecurse nounwind readnone
define i64 @SECRET(i64 %SymVar_0) local_unnamed_addr #0 {
.3:
  %.6 = lshr i64 %SymVar_0, 7
  %.12 = lshr i64 %SymVar_0, 5
  %.14 = add i64 %SymVar_0, 38602491
  %.15 = add i64 %.14, %SymVar_0
  %.16 = or i64 %.15, -5620492334951809231
  %.19 = lshr i64 %.16, 1
  %.20 = and i64 %.19, 14
  %.21 = or i64 %.20, 1
  %.22 = sub nsw i64 0, %.21
  %.27 = and i64 %.22, 55
  %.28 = shl i64 %.14, %.27
  %.39 = lshr i64 %.14, %.21
  %.40 = or i64 %.28, %.39
  %.43 = lshr i64 %.40, 2
  %0 = and i64 %.43, 6
  %.46 = or i64 %0, 1
  %.51 = shl i64 %.6, %.46
  %.52 = sub i64 %.12, %.51
  %.55 = lshr i64 %.52, 4
  %1 = and i64 %.55, 6
  %.58 = or i64 %1, 1
  %.63 = shl i64 %.6, %.58
  %.154 = lshr i64 %.14, 40
  %.182 = and i64 %.14, 1099511627775
  %2 = lshr i64 %.14, 8
  %.187 = and i64 %2, 280375465082880
  %.188 = or i64 %.187, %.182
  %.19015 = lshr i64 %.14, 56
  %.193 = shl nuw nsw i64 %.19015, 48
  %.194 = or i64 %.188, %.193
  %.199 = shl i64 %.154, 56
  %.200 = or i64 %.194, %.199
  %.201 = shl nuw nsw i64 %.6, 3
  %.205 = or i64 %.16, %.201
  %.206 = and i64 %.205, 15
  %.208 = sub nsw i64 0, %.206
  %.213 = and i64 %.208, 63
  %.214 = shl i64 %.200, %.213
  %.244 = lshr i64 %.200, %.206
  %.245 = or i64 %.214, %.244
  %.246 = add i64 %.63, %.245
  ret i64 %.246
}

attributes #0 = { norecurse nounwind readnone }
