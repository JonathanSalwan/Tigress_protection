; ModuleID = 'llvm_expressions/sample4-virt-operand-registers.ll'
source_filename = "llvm_expressions/sample4-virt-operand-registers.ll"
target datalayout = "e-m:e-i64:64-f80:128-n8:16:32:64-S128"
target triple = "x86_64-pc-linux-gnu"

; Function Attrs: norecurse nounwind readnone
define i64 @SECRET(i64 %SymVar_0) local_unnamed_addr #0 {
.3:
  %.11 = and i64 %SymVar_0, 255
  %.16 = add nuw nsw i64 %.11, 1
  %.26 = urem i64 %.16, 65521
  %.61 = lshr i64 %SymVar_0, 8
  %.69 = and i64 %.61, 255
  %.74 = add nuw nsw i64 %.26, %.69
  %.84 = urem i64 %.74, 65521
  %.94 = add nuw nsw i64 %.84, %.26
  %.104 = urem i64 %.94, 65521
  %.119 = lshr i64 %SymVar_0, 16
  %.127 = and i64 %.119, 255
  %.132 = add nuw nsw i64 %.84, %.127
  %.142 = urem i64 %.132, 65521
  %.152 = add nuw nsw i64 %.104, %.142
  %.162 = urem i64 %.152, 65521
  %.177 = lshr i64 %SymVar_0, 24
  %.185 = and i64 %.177, 255
  %.190 = add nuw nsw i64 %.142, %.185
  %.200 = urem i64 %.190, 65521
  %.210 = add nuw nsw i64 %.162, %.200
  %.220 = urem i64 %.210, 65521
  %.235 = lshr i64 %SymVar_0, 32
  %.243 = and i64 %.235, 255
  %.248 = add nuw nsw i64 %.200, %.243
  %.258 = urem i64 %.248, 65521
  %.268 = add nuw nsw i64 %.220, %.258
  %.278 = urem i64 %.268, 65521
  %.293 = lshr i64 %SymVar_0, 40
  %.301 = and i64 %.293, 255
  %.306 = add nuw nsw i64 %.258, %.301
  %.316 = urem i64 %.306, 65521
  %.326 = add nuw nsw i64 %.278, %.316
  %.336 = urem i64 %.326, 65521
  %.351 = lshr i64 %SymVar_0, 48
  %.359 = and i64 %.351, 255
  %.364 = add nuw nsw i64 %.316, %.359
  %.374 = urem i64 %.364, 65521
  %.384 = add nuw nsw i64 %.336, %.374
  %.394 = urem i64 %.384, 65521
  %.409 = lshr i64 %SymVar_0, 56
  %.422 = add nuw nsw i64 %.374, %.409
  %.432 = urem i64 %.422, 65521
  %.442 = add nuw nsw i64 %.394, %.432
  %.452 = urem i64 %.442, 65521
  %.464 = shl nuw nsw i64 %.452, 16
  %.474 = or i64 %.464, %.432
  ret i64 %.474
}

attributes #0 = { norecurse nounwind readnone }
