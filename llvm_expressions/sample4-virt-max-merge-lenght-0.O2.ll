; ModuleID = 'llvm_expressions/sample4-virt-max-merge-lenght-0.ll'
source_filename = "llvm_expressions/sample4-virt-max-merge-lenght-0.ll"
target datalayout = "e-m:e-i64:64-f80:128-n8:16:32:64-S128"
target triple = "x86_64-pc-linux-gnu"

; Function Attrs: norecurse nounwind readnone
define i64 @SECRET(i64 %SymVar_0) local_unnamed_addr #0 {
.3:
  %.4 = lshr i64 %SymVar_0, 56
  %.17 = lshr i64 %SymVar_0, 48
  %.25 = and i64 %.17, 255
  %.30 = lshr i64 %SymVar_0, 40
  %.38 = and i64 %.30, 255
  %.43 = lshr i64 %SymVar_0, 32
  %.51 = and i64 %.43, 255
  %.56 = lshr i64 %SymVar_0, 24
  %.64 = and i64 %.56, 255
  %.69 = lshr i64 %SymVar_0, 16
  %.77 = and i64 %.69, 255
  %.82 = lshr i64 %SymVar_0, 8
  %.90 = and i64 %.82, 255
  %.102 = and i64 %SymVar_0, 255
  %.107 = add nuw nsw i64 %.102, 1
  %.117 = urem i64 %.107, 65521
  %.129 = add nuw nsw i64 %.117, %.90
  %.139 = urem i64 %.129, 65521
  %.151 = add nuw nsw i64 %.139, %.77
  %.161 = urem i64 %.151, 65521
  %.173 = add nuw nsw i64 %.161, %.64
  %.183 = urem i64 %.173, 65521
  %.195 = add nuw nsw i64 %.183, %.51
  %.205 = urem i64 %.195, 65521
  %.217 = add nuw nsw i64 %.205, %.38
  %.227 = urem i64 %.217, 65521
  %.239 = add nuw nsw i64 %.227, %.25
  %.249 = urem i64 %.239, 65521
  %.261 = add nuw nsw i64 %.249, %.4
  %.271 = urem i64 %.261, 65521
  %.345 = add nuw nsw i64 %.139, %.117
  %.355 = urem i64 %.345, 65521
  %.367 = add nuw nsw i64 %.161, %.355
  %.377 = urem i64 %.367, 65521
  %.389 = add nuw nsw i64 %.183, %.377
  %.399 = urem i64 %.389, 65521
  %.411 = add nuw nsw i64 %.205, %.399
  %.421 = urem i64 %.411, 65521
  %.433 = add nuw nsw i64 %.227, %.421
  %.443 = urem i64 %.433, 65521
  %.455 = add nuw nsw i64 %.249, %.443
  %.465 = urem i64 %.455, 65521
  %.477 = add nuw nsw i64 %.271, %.465
  %.487 = urem i64 %.477, 65521
  %.501 = shl nuw nsw i64 %.487, 16
  %.508 = or i64 %.501, %.271
  ret i64 %.508
}

attributes #0 = { norecurse nounwind readnone }
