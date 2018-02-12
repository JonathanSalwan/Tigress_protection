; ModuleID = 'llvm_expressions/sample24-virt-max-merge-lenght-10.ll'
source_filename = "llvm_expressions/sample24-virt-max-merge-lenght-10.ll"
target datalayout = "e-m:e-i64:64-f80:128-n8:16:32:64-S128"
target triple = "x86_64-pc-linux-gnu"

; Function Attrs: norecurse nounwind readnone
define i64 @SECRET(i64 %SymVar_0) local_unnamed_addr #0 {
.3:
  %.6 = lshr i64 %SymVar_0, 53
  %.9 = shl i64 %SymVar_0, 11
  %.10 = or i64 %.6, %.9
  %.13 = lshr i64 %.10, 1
  %div = udiv i64 %SymVar_0, 3
  %0 = mul i64 %.13, -112410438
  %.25 = add i64 %0, %div
  %.28 = lshr i64 %.25, 3
  %.29 = and i64 %.28, 14
  %.30 = or i64 %.29, 1
  %.31 = sub nsw i64 64, %.30
  %.37 = shl i64 %.13, %.31
  %.48 = lshr i64 %.13, %.30
  %.49 = or i64 %.37, %.48
  %.52 = lshr i64 %.25, 2
  %.53 = and i64 %.52, 14
  %.54 = or i64 %.53, 1
  %.55 = sub nsw i64 64, %.54
  %.61 = lshr i64 %.13, %.55
  %.72 = shl i64 %.13, %.54
  %.73 = or i64 %.61, %.72
  %.74 = shl i64 %.73, 2
  %.77 = and i64 %.74, 28
  %.78 = add i64 %SymVar_0, 160536708
  %.81 = lshr i64 %.25, 9
  %.85 = and i64 %.81, 6
  %.86 = or i64 %.85, 1
  %.90 = lshr i64 %.78, %.86
  %.91 = shl i64 %.90, 4
  %.94 = and i64 %.91, 1008
  %.95 = or i64 %.94, %.90
  %.96 = or i64 %.77, %.95
  %.97 = add i64 %SymVar_0, 8152287480
  %.100 = lshr i64 %.97, 4
  %.101 = and i64 %.100, 14
  %.102 = or i64 %.101, 1
  %.103 = sub nsw i64 64, %.102
  %.109 = shl i64 %.96, %.103
  %.120 = lshr i64 %.96, %.102
  %.121 = or i64 %.109, %.120
  %.122 = sub i64 %.49, %.121
  %.125 = xor i64 %.122, %.37
  %.126 = xor i64 %.109, %.37
  %.127 = and i64 %.125, %.126
  %.124 = xor i64 %.126, %.122
  %.128 = xor i64 %.124, %.127
  %.131 = icmp sgt i64 %.128, -1
  %.137 = icmp ne i64 %.122, 0
  %.158.demorgan = and i1 %.137, %.131
  br i1 %.158.demorgan, label %.3.endif.endif.endif.endif.else, label %.3.endif.endif.endif.endif.if

.3.endif.endif.endif.endif.if:                    ; preds = %.3
  %.241 = mul i64 %.96, %.97
  %.244 = shl i64 %.25, 3
  %.247 = and i64 %.244, 120
  %.248 = or i64 %.247, %.25
  %.249 = and i64 %.96, %.248
  %.250 = shl i64 %.249, 4
  %.253 = and i64 %.250, 496
  %.254 = or i64 %.248, %.13
  %.255 = or i64 %.254, %.253
  %.257 = mul i64 %.241, %.255
  br label %.3.endif.endif.endif.endif.endif

.3.endif.endif.endif.endif.else:                  ; preds = %.3
  %.332 = and i64 %.96, 255
  %1 = lshr i64 %.90, 16
  %.342 = and i64 %1, 65280
  %2 = shl i64 %.95, 16
  %.364 = and i64 %2, 4278190080
  %.370 = and i64 %.90, 9223372032576520192
  %.375 = or i64 %.370, %.342
  %.380 = or i64 %.375, %.364
  %.385 = or i64 %.380, %.332
  %.392 = lshr i64 %.97, 3
  %.393 = and i64 %.392, 14
  %.394 = or i64 %.393, 1
  %.395 = sub nsw i64 64, %.394
  %.401 = lshr i64 %.97, %.395
  %.412 = shl i64 %.97, %.394
  %.413 = or i64 %.25, %.412
  %.414 = or i64 %.413, %.401
  %.387 = mul i64 %.414, %.97
  %.416 = mul i64 %.387, %.385
  br label %.3.endif.endif.endif.endif.endif

.3.endif.endif.endif.endif.endif:                 ; preds = %.3.endif.endif.endif.endif.else, %.3.endif.endif.endif.endif.if
  %.257.sink.off0 = phi i64 [ %.257, %.3.endif.endif.endif.endif.if ], [ %.416, %.3.endif.endif.endif.endif.else ]
  ret i64 %.257.sink.off0
}

attributes #0 = { norecurse nounwind readnone }
