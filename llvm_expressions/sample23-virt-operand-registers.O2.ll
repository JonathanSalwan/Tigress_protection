; ModuleID = 'llvm_expressions/sample23-virt-operand-registers.ll'
source_filename = "llvm_expressions/sample23-virt-operand-registers.ll"
target datalayout = "e-m:e-i64:64-f80:128-n8:16:32:64-S128"
target triple = "x86_64-pc-linux-gnu"

; Function Attrs: norecurse nounwind readnone
define i64 @SECRET(i64 %SymVar_0) local_unnamed_addr #0 {
.3:
  %.4 = add i64 %SymVar_0, 1059198491
  %.7 = shl i64 %SymVar_0, 7
  %.10 = lshr i64 %SymVar_0, 57
  %.11 = or i64 %.7, %.10
  %.18 = mul i64 %.4, 218063048984025710
  %.22 = lshr exact i64 %.18, 1
  %.23 = and i64 %.22, 14
  %.24 = or i64 %.23, 1
  %.30 = shl i64 %.11, %.24
  %.51 = sub nsw i64 64, %.24
  %.57 = lshr i64 %.11, %.51
  %.58 = or i64 %.57, %.30
  %.61 = lshr i64 %.58, 4
  %.62 = and i64 %.61, 14
  %.63 = or i64 %.62, 1
  %.69 = shl i64 %.4, %.63
  %.75 = sub nsw i64 64, %.63
  %.81 = lshr i64 %.4, %.75
  %.82 = or i64 %.81, %.69
  %.84 = add i64 %SymVar_0, 11366125
  %.85 = add i64 %.84, %.58
  %.86 = or i64 %.4, %SymVar_0
  %.87 = add i64 %.58, 728434157
  %.88 = and i64 %.85, %.87
  %.89 = add i64 %.88, %.86
  %.90 = shl i64 %.85, 4
  %.93 = and i64 %.90, 1008
  %.94 = or i64 %.89, %.93
  %.95 = add i64 %.94, %.85
  %.97 = mul i64 %.82, %.95
  ret i64 %.97
}

attributes #0 = { norecurse nounwind readnone }
