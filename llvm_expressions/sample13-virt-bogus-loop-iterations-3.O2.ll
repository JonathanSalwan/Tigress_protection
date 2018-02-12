; ModuleID = 'llvm_expressions/sample13-virt-bogus-loop-iterations-3.ll'
source_filename = "llvm_expressions/sample13-virt-bogus-loop-iterations-3.ll"
target datalayout = "e-m:e-i64:64-f80:128-n8:16:32:64-S128"
target triple = "x86_64-pc-linux-gnu"

; Function Attrs: norecurse nounwind readnone
define i64 @SECRET(i64 %SymVar_0) local_unnamed_addr #0 {
.3:
  %.4 = add i64 %SymVar_0, -2401053088876216593
  %.5 = xor i64 %.4, -1824592336572793105
  %.6 = shl i64 %.4, 15
  %.7 = lshr i64 %.4, 49
  %.81 = or i64 %.6, %.7
  %.9 = add i64 %.81, %.5
  %.10 = xor i64 %.9, 4660
  %.11 = shl i64 %.9, 52
  %.12 = lshr i64 %.9, 12
  %.132 = or i64 %.11, %.12
  %.14 = add i64 %.132, %.10
  %.15 = shl i64 %.14, 26
  %.16 = lshr i64 %.14, 38
  %.173 = or i64 %.15, %.16
  %.18 = xor i64 %.14, 4660
  %.19 = add i64 %.173, %.18
  %.20 = xor i64 %.19, %.81
  %.21 = shl i64 %.19, 51
  %.22 = lshr i64 %.19, 13
  %.234 = or i64 %.21, %.22
  %.24 = add i64 %.234, %.20
  %.25 = xor i64 %.24, %.132
  %.26 = shl i64 %.24, 28
  %.27 = lshr i64 %.24, 36
  %.285 = or i64 %.26, %.27
  %.29 = add i64 %.285, %.25
  %.30 = xor i64 %.29, %.173
  %.31 = shl i64 %.29, 9
  %.32 = lshr i64 %.29, 55
  %.336 = or i64 %.31, %.32
  %.34 = add i64 %.336, %.30
  %.35 = shl i64 %.34, 47
  %.36 = lshr i64 %.34, 17
  %.377 = or i64 %.35, %.36
  %.38 = xor i64 %.34, %.234
  %.39 = add i64 %.377, %.38
  %.40 = xor i64 %.39, %.285
  %.41 = shl i64 %.39, 54
  %.42 = lshr i64 %.39, 10
  %.438 = or i64 %.41, %.42
  %.44 = add i64 %.438, %.40
  %.45 = xor i64 %.44, %.336
  %.46 = shl i64 %.44, 32
  %.47 = lshr i64 %.44, 32
  %.489 = or i64 %.46, %.47
  %.49 = add i64 %.489, %.45
  %.50 = xor i64 %.49, %.377
  %.51 = shl i64 %.49, 25
  %.52 = lshr i64 %.49, 39
  %.5310 = or i64 %.51, %.52
  %.54 = add i64 %.5310, %.50
  %.55 = shl i64 %.54, 63
  %.56 = lshr i64 %.54, 1
  %.5711 = or i64 %.55, %.56
  ret i64 %.5711
}

attributes #0 = { norecurse nounwind readnone }
