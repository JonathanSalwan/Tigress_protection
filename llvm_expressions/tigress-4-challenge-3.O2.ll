; ModuleID = './llvm_expressions/tigress-4-challenge-3.ll'
target datalayout = "e-m:e-i64:64-f80:128-n8:16:32:64-S128"
target triple = "x86_64-pc-linux-gnu"

; Function Attrs: norecurse nounwind readnone
define i64 @__arybo(i64 %SymVar_0) #0 {
.3:
  %div = udiv i64 %SymVar_0, 6
  %.35 = mul i64 %div, -432345564227385076
  %.40 = lshr i64 %SymVar_0, 51
  %.43 = shl i64 %SymVar_0, 13
  %.44 = or i64 %.40, %.43
  %.46 = mul i64 %.35, %.44
  %.49 = add i64 %.35, %SymVar_0
  %.51 = sub nsw i64 1471924646, %.40
  %.54 = lshr i64 %.51, 2
  %.55 = and i64 %.54, 6
  %.56 = or i64 %.55, 1
  %.62 = lshr i64 %.49, %.56
  %.65 = lshr i64 %.62, 1
  %.66 = and i64 %.65, 6
  %.67 = or i64 %.66, 1
  %.73 = lshr i64 %.62, %.67
  %.198 = and i64 %.73, 4611686018427387903
  %.200 = mul i64 %.198, 81897458
  %.202 = shl nuw nsw i64 %.40, 2
  %.206 = or i64 %.35, %.44
  %.207 = add i64 %.206, %SymVar_0
  %.208 = or i64 %.207, %.202
  %.209 = shl i64 %.207, 2
  %.213 = or i64 %.208, %.209
  %.214 = xor i64 %.200, %.213
  %.215 = and i64 %.214, 14
  %.216 = or i64 %.215, 1
  %.217 = sub nsw i64 64, %.216
  %.223 = lshr i64 %.46, %.217
  %.262 = shl i64 %.46, %.216
  %.263 = or i64 %.223, %.262
  ret i64 %.263
}

attributes #0 = { norecurse nounwind readnone }
