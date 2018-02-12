; ModuleID = 'llvm_expressions/sample19-virt-bogus-functions-0.ll'
source_filename = "llvm_expressions/sample19-virt-bogus-functions-0.ll"
target datalayout = "e-m:e-i64:64-f80:128-n8:16:32:64-S128"
target triple = "x86_64-pc-linux-gnu"

; Function Attrs: norecurse nounwind readnone
define i64 @SECRET(i64 %SymVar_0) local_unnamed_addr #0 {
.3:
  %.4 = add i64 %SymVar_0, -902749805
  %div = udiv i64 %SymVar_0, 7
  %.14 = lshr i64 %div, 3
  %.15 = and i64 %.14, 14
  %.16 = or i64 %.15, 1
  %.30 = shl i64 127996265, %.16
  %.34 = lshr i64 %.30, 4
  %.35 = and i64 %.34, 14
  %.36 = or i64 %.35, 1
  %.37 = sub nsw i64 64, %.36
  %.41 = lshr i64 %SymVar_0, %.37
  %.70 = shl i64 %SymVar_0, %.36
  %.71 = or i64 %.41, %.70
  %.77 = shl nuw i64 %div, 2
  %.81 = or i64 %.77, %div
  %.82 = and i64 %.81, 14
  %.83 = or i64 %.82, 1
  %.84 = sub nsw i64 64, %.83
  %.88 = lshr i64 %.4, %.84
  %.94 = shl i64 %.4, %.83
  %.95 = or i64 %.88, %.94
  %0 = mul i64 %SymVar_0, 343000538
  %.99 = add i64 %0, 1638886
  %.101 = lshr i64 %.99, 18
  %.227 = and i64 %.101, 14
  %.228 = or i64 %.227, 1
  %.229 = sub nsw i64 64, %.228
  %.233 = lshr i64 %.71, %.229
  %.264 = shl i64 %.71, %.228
  %.265 = or i64 %.233, %.264
  %.268 = lshr i64 %.265, 4
  %.269 = and i64 %.268, 14
  %.270 = or i64 %.269, 1
  %.271 = sub nsw i64 64, %.270
  %.275 = shl i64 %.95, %.271
  %.362 = lshr i64 %.95, %.270
  %.363 = or i64 %.275, %.362
  ret i64 %.363
}

attributes #0 = { norecurse nounwind readnone }
