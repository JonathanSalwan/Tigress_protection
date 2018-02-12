; ModuleID = 'llvm_expressions/sample24-virt-nested-vm-2.ll'
source_filename = "llvm_expressions/sample24-virt-nested-vm-2.ll"
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
  %.46 = lshr i64 %.13, %.30
  %.47 = or i64 %.37, %.46
  %.50 = lshr i64 %.25, 2
  %.51 = and i64 %.50, 14
  %.52 = or i64 %.51, 1
  %.53 = sub nsw i64 64, %.52
  %.57 = lshr i64 %.13, %.53
  %.68 = shl i64 %.13, %.52
  %.69 = or i64 %.57, %.68
  %.70 = shl i64 %.69, 2
  %.73 = and i64 %.70, 28
  %.74 = add i64 %SymVar_0, 160536708
  %.77 = lshr i64 %.25, 9
  %.81 = and i64 %.77, 6
  %.82 = or i64 %.81, 1
  %.86 = lshr i64 %.74, %.82
  %.87 = shl i64 %.86, 4
  %.90 = and i64 %.87, 1008
  %.91 = or i64 %.90, %.86
  %.92 = or i64 %.73, %.91
  %.93 = add i64 %SymVar_0, 8152287480
  %.96 = lshr i64 %.93, 4
  %.97 = and i64 %.96, 14
  %.98 = or i64 %.97, 1
  %.99 = sub nsw i64 64, %.98
  %.105 = shl i64 %.92, %.99
  %.114 = lshr i64 %.92, %.98
  %.115 = or i64 %.105, %.114
  %.116 = sub i64 %.47, %.115
  %.119 = xor i64 %.116, %.37
  %.120 = xor i64 %.105, %.37
  %.121 = and i64 %.119, %.120
  %.118 = xor i64 %.120, %.116
  %.122 = xor i64 %.118, %.121
  %.125 = icmp sgt i64 %.122, -1
  %.131 = icmp ne i64 %.116, 0
  %.156.demorgan = and i1 %.131, %.125
  br i1 %.156.demorgan, label %.3.endif.endif.endif.endif.else, label %.3.endif.endif.endif.endif.if

.3.endif.endif.endif.endif.if:                    ; preds = %.3
  %.237 = mul i64 %.92, %.93
  %.240 = shl i64 %.25, 3
  %.243 = and i64 %.240, 120
  %.244 = or i64 %.243, %.25
  %.245 = and i64 %.92, %.244
  %.246 = shl i64 %.245, 4
  %.249 = and i64 %.246, 496
  %.250 = or i64 %.244, %.13
  %.251 = or i64 %.250, %.249
  %.253 = mul i64 %.237, %.251
  br label %.3.endif.endif.endif.endif.endif

.3.endif.endif.endif.endif.else:                  ; preds = %.3
  %.326 = and i64 %.92, 255
  %1 = lshr i64 %.86, 16
  %.342 = and i64 %1, 65280
  %2 = shl i64 %.91, 16
  %.376 = and i64 %2, 4278190080
  %.382 = and i64 %.86, 9223372032576520192
  %.387 = or i64 %.382, %.342
  %.392 = or i64 %.387, %.376
  %.397 = or i64 %.392, %.326
  %.404 = lshr i64 %.93, 3
  %.405 = and i64 %.404, 14
  %.406 = or i64 %.405, 1
  %.407 = sub nsw i64 64, %.406
  %.411 = lshr i64 %.93, %.407
  %.422 = shl i64 %.93, %.406
  %.423 = or i64 %.25, %.422
  %.424 = or i64 %.423, %.411
  %.399 = mul i64 %.424, %.93
  %.426 = mul i64 %.399, %.397
  br label %.3.endif.endif.endif.endif.endif

.3.endif.endif.endif.endif.endif:                 ; preds = %.3.endif.endif.endif.endif.else, %.3.endif.endif.endif.endif.if
  %.253.sink.off0 = phi i64 [ %.253, %.3.endif.endif.endif.endif.if ], [ %.426, %.3.endif.endif.endif.endif.else ]
  ret i64 %.253.sink.off0
}

attributes #0 = { norecurse nounwind readnone }
