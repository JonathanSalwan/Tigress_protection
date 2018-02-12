; ModuleID = 'llvm_expressions/sample24-virt-duplicate-opcodes-3.ll'
source_filename = "llvm_expressions/sample24-virt-duplicate-opcodes-3.ll"
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
  %.70 = shl i64 %.13, %.54
  %.71 = or i64 %.61, %.70
  %.72 = shl i64 %.71, 2
  %.75 = and i64 %.72, 28
  %.76 = add i64 %SymVar_0, 160536708
  %.79 = lshr i64 %.25, 9
  %.83 = and i64 %.79, 6
  %.84 = or i64 %.83, 1
  %.90 = lshr i64 %.76, %.84
  %.91 = shl i64 %.90, 4
  %.94 = and i64 %.91, 1008
  %.95 = or i64 %.94, %.90
  %.96 = or i64 %.75, %.95
  %.97 = add i64 %SymVar_0, 8152287480
  %.100 = lshr i64 %.97, 4
  %.101 = and i64 %.100, 14
  %.102 = or i64 %.101, 1
  %.103 = sub nsw i64 64, %.102
  %.107 = shl i64 %.96, %.103
  %.116 = lshr i64 %.96, %.102
  %.117 = or i64 %.107, %.116
  %.118 = sub i64 %.49, %.117
  %.121 = xor i64 %.118, %.37
  %.122 = xor i64 %.107, %.37
  %.123 = and i64 %.121, %.122
  %.120 = xor i64 %.122, %.118
  %.124 = xor i64 %.120, %.123
  %.127 = icmp sgt i64 %.124, -1
  %.133 = icmp ne i64 %.118, 0
  %.154.demorgan = and i1 %.133, %.127
  br i1 %.154.demorgan, label %.3.endif.endif.endif.endif.else, label %.3.endif.endif.endif.endif.if

.3.endif.endif.endif.endif.if:                    ; preds = %.3
  %.237 = mul i64 %.96, %.97
  %.240 = shl i64 %.25, 3
  %.243 = and i64 %.240, 120
  %.244 = or i64 %.243, %.25
  %.245 = and i64 %.96, %.244
  %.246 = shl i64 %.245, 4
  %.249 = and i64 %.246, 496
  %.250 = or i64 %.244, %.13
  %.251 = or i64 %.250, %.249
  %.253 = mul i64 %.237, %.251
  br label %.3.endif.endif.endif.endif.endif

.3.endif.endif.endif.endif.else:                  ; preds = %.3
  %.328 = and i64 %.96, 255
  %1 = lshr i64 %.90, 16
  %.338 = and i64 %1, 65280
  %2 = shl i64 %.95, 16
  %.360 = and i64 %2, 4278190080
  %.366 = and i64 %.90, 9223372032576520192
  %.371 = or i64 %.366, %.338
  %.376 = or i64 %.371, %.360
  %.381 = or i64 %.376, %.328
  %.388 = lshr i64 %.97, 3
  %.389 = and i64 %.388, 14
  %.390 = or i64 %.389, 1
  %.391 = sub nsw i64 64, %.390
  %.397 = lshr i64 %.97, %.391
  %.406 = shl i64 %.97, %.390
  %.407 = or i64 %.25, %.406
  %.408 = or i64 %.407, %.397
  %.383 = mul i64 %.408, %.97
  %.410 = mul i64 %.383, %.381
  br label %.3.endif.endif.endif.endif.endif

.3.endif.endif.endif.endif.endif:                 ; preds = %.3.endif.endif.endif.endif.else, %.3.endif.endif.endif.endif.if
  %.253.sink.off0 = phi i64 [ %.253, %.3.endif.endif.endif.endif.if ], [ %.410, %.3.endif.endif.endif.endif.else ]
  ret i64 %.253.sink.off0
}

attributes #0 = { norecurse nounwind readnone }
