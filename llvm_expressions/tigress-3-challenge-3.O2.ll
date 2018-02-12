; ModuleID = 'llvm_expressions/tigress-3-challenge-3.ll'
source_filename = "llvm_expressions/tigress-3-challenge-3.ll"
target datalayout = "e-m:e-i64:64-f80:128-n8:16:32:64-S128"
target triple = "x86_64-pc-linux-gnu"

; Function Attrs: norecurse nounwind readnone
define i64 @SECRET(i64 %SymVar_0) local_unnamed_addr #0 {
.3:
  %.4 = shl i64 %SymVar_0, 1
  %.6 = and i64 %.4, -1699145734
  %.7 = xor i64 %SymVar_0, 849572866
  %.8 = sub i64 %.6, %.7
  %.11 = lshr i64 %.8, 3
  %.12 = or i64 %.11, 7
  %.13 = xor i64 %.12, 56
  %.14 = add nuw nsw i64 %.11, 1
  %.15 = add nuw nsw i64 %.14, %.13
  %.21 = and i64 %.15, 62
  %.22 = or i64 %.21, 1
  %.23 = shl i64 %SymVar_0, %.22
  %.26 = shl i64 %.23, 1
  %.31 = or i64 %SymVar_0, 612496968
  %.34 = lshr i64 %.8, 55
  %.37 = shl i64 %.8, 9
  %.40 = or i64 %.34, %.37
  %.41 = shl i64 %.40, 1
  %.43 = or i64 %.41, 1998889626
  %.45 = xor i64 %.40, 999444813
  %.46 = sub i64 %.43, %.45
  %.47 = xor i64 %.46, 8191
  %.48 = and i64 %.47, %.31
  %.51 = shl i64 %.48, 1
  %.52 = xor i64 %.46, %.31
  %.53 = sub i64 %.51, %.52
  %.54 = lshr i64 %.53, 10
  %.68 = and i64 %.54, 14
  %.117 = or i64 %.68, 1
  %.124 = sub nsw i64 0, %.117
  %.129 = and i64 %.124, 63
  %.130 = shl i64 %.26, %.129
  %.131 = xor i64 %.130, -1
  %.168 = lshr i64 %.26, %.117
  %.169 = and i64 %.168, %.131
  %.170 = add i64 %.169, %.130
  %.173 = lshr i64 %.23, 2
  %.174 = or i64 %.173, 7
  %.175 = xor i64 %.174, 56
  %.176 = add nuw nsw i64 %.173, 1
  %.177 = add nuw i64 %.176, %.175
  %.183 = and i64 %.177, 62
  %.184 = or i64 %.183, 1
  %.185 = shl i64 %.8, %.184
  %.186 = and i64 %.170, %.185
  %.188 = shl i64 %.186, 1
  %.189 = xor i64 %.170, %.185
  %.190 = add i64 %.188, %.189
  ret i64 %.190
}

attributes #0 = { norecurse nounwind readnone }
