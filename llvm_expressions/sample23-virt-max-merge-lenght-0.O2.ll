; ModuleID = 'llvm_expressions/sample23-virt-max-merge-lenght-0.ll'
source_filename = "llvm_expressions/sample23-virt-max-merge-lenght-0.ll"
target datalayout = "e-m:e-i64:64-f80:128-n8:16:32:64-S128"
target triple = "x86_64-pc-linux-gnu"

; Function Attrs: norecurse nounwind readnone
define i64 @SECRET(i64 %SymVar_0) local_unnamed_addr #0 {
.3:
  %.6 = lshr i64 %SymVar_0, 57
  %.9 = shl i64 %SymVar_0, 7
  %.10 = or i64 %.6, %.9
  %.11 = add i64 %SymVar_0, 1059198491
  %.18 = mul i64 %.11, 218063048984025710
  %.22 = lshr exact i64 %.18, 1
  %.23 = and i64 %.22, 14
  %.24 = or i64 %.23, 1
  %.25 = sub nsw i64 64, %.24
  %.31 = lshr i64 %.10, %.25
  %.55 = shl i64 %.10, %.24
  %.56 = or i64 %.31, %.55
  %.57 = add i64 %SymVar_0, 11366125
  %.58 = add i64 %.57, %.56
  %.59 = shl i64 %.58, 4
  %.62 = and i64 %.59, 1008
  %.63 = add i64 %.56, 728434157
  %.64 = and i64 %.58, %.63
  %.65 = or i64 %.11, %SymVar_0
  %.66 = add i64 %.64, %.65
  %.67 = or i64 %.62, %.66
  %.68 = add i64 %.67, %.58
  %.72 = lshr i64 %.56, 4
  %.73 = and i64 %.72, 14
  %.74 = or i64 %.73, 1
  %.75 = sub nsw i64 64, %.74
  %.81 = lshr i64 %.11, %.75
  %.90 = shl i64 %.11, %.74
  %.91 = or i64 %.81, %.90
  %.93 = mul i64 %.68, %.91
  ret i64 %.93
}

attributes #0 = { norecurse nounwind readnone }
