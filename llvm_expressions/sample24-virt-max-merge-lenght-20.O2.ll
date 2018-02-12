; ModuleID = 'llvm_expressions/sample24-virt-max-merge-lenght-20.ll'
source_filename = "llvm_expressions/sample24-virt-max-merge-lenght-20.ll"
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
  %.88 = lshr i64 %.76, %.84
  %.89 = shl i64 %.88, 4
  %.92 = and i64 %.89, 1008
  %.93 = or i64 %.92, %.88
  %.94 = or i64 %.75, %.93
  %.95 = add i64 %SymVar_0, 8152287480
  %.98 = lshr i64 %.95, 4
  %.99 = and i64 %.98, 14
  %.100 = or i64 %.99, 1
  %.101 = sub nsw i64 64, %.100
  %.107 = shl i64 %.94, %.101
  %.118 = lshr i64 %.94, %.100
  %.119 = or i64 %.107, %.118
  %.120 = sub i64 %.49, %.119
  %.123 = xor i64 %.120, %.37
  %.124 = xor i64 %.107, %.37
  %.125 = and i64 %.123, %.124
  %.122 = xor i64 %.124, %.120
  %.126 = xor i64 %.122, %.125
  %.129 = icmp sgt i64 %.126, -1
  %.135 = icmp ne i64 %.120, 0
  %.156.demorgan = and i1 %.135, %.129
  br i1 %.156.demorgan, label %.3.endif.endif.endif.endif.else, label %.3.endif.endif.endif.endif.if

.3.endif.endif.endif.endif.if:                    ; preds = %.3
  %.237 = mul i64 %.94, %.95
  %.240 = shl i64 %.25, 3
  %.243 = and i64 %.240, 120
  %.244 = or i64 %.243, %.25
  %.245 = and i64 %.94, %.244
  %.246 = shl i64 %.245, 4
  %.249 = and i64 %.246, 496
  %.250 = or i64 %.244, %.13
  %.251 = or i64 %.250, %.249
  %.253 = mul i64 %.237, %.251
  br label %.3.endif.endif.endif.endif.endif

.3.endif.endif.endif.endif.else:                  ; preds = %.3
  %.326 = and i64 %.94, 255
  %1 = lshr i64 %.88, 16
  %.336 = and i64 %1, 65280
  %2 = shl i64 %.93, 16
  %.358 = and i64 %2, 4278190080
  %.364 = and i64 %.88, 9223372032576520192
  %.369 = or i64 %.364, %.336
  %.374 = or i64 %.369, %.358
  %.379 = or i64 %.374, %.326
  %.386 = lshr i64 %.95, 3
  %.387 = and i64 %.386, 14
  %.388 = or i64 %.387, 1
  %.389 = sub nsw i64 64, %.388
  %.395 = lshr i64 %.95, %.389
  %.404 = shl i64 %.95, %.388
  %.405 = or i64 %.25, %.404
  %.406 = or i64 %.405, %.395
  %.381 = mul i64 %.406, %.95
  %.408 = mul i64 %.381, %.379
  br label %.3.endif.endif.endif.endif.endif

.3.endif.endif.endif.endif.endif:                 ; preds = %.3.endif.endif.endif.endif.else, %.3.endif.endif.endif.endif.if
  %.253.sink.off0 = phi i64 [ %.253, %.3.endif.endif.endif.endif.if ], [ %.408, %.3.endif.endif.endif.endif.else ]
  ret i64 %.253.sink.off0
}

attributes #0 = { norecurse nounwind readnone }
