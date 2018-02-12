; ModuleID = 'llvm_expressions/sample24-virt-obfuscate-decode-byte-array-false.ll'
source_filename = "llvm_expressions/sample24-virt-obfuscate-decode-byte-array-false.ll"
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
  %.92 = lshr i64 %.78, %.86
  %.93 = shl i64 %.92, 4
  %.96 = and i64 %.93, 1008
  %.97 = or i64 %.96, %.92
  %.98 = or i64 %.77, %.97
  %.99 = add i64 %SymVar_0, 8152287480
  %.102 = lshr i64 %.99, 4
  %.103 = and i64 %.102, 14
  %.104 = or i64 %.103, 1
  %.105 = sub nsw i64 64, %.104
  %.111 = shl i64 %.98, %.105
  %.122 = lshr i64 %.98, %.104
  %.123 = or i64 %.111, %.122
  %.124 = sub i64 %.49, %.123
  %.127 = xor i64 %.124, %.37
  %.128 = xor i64 %.111, %.37
  %.129 = and i64 %.127, %.128
  %.126 = xor i64 %.128, %.124
  %.130 = xor i64 %.126, %.129
  %.133 = icmp sgt i64 %.130, -1
  %.139 = icmp ne i64 %.124, 0
  %.160.demorgan = and i1 %.139, %.133
  br i1 %.160.demorgan, label %.3.endif.endif.endif.endif.else, label %.3.endif.endif.endif.endif.if

.3.endif.endif.endif.endif.if:                    ; preds = %.3
  %.245 = mul i64 %.98, %.99
  %.248 = shl i64 %.25, 3
  %.251 = and i64 %.248, 120
  %.252 = or i64 %.251, %.25
  %.253 = and i64 %.98, %.252
  %.254 = shl i64 %.253, 4
  %.257 = and i64 %.254, 496
  %.258 = or i64 %.252, %.13
  %.259 = or i64 %.258, %.257
  %.261 = mul i64 %.245, %.259
  br label %.3.endif.endif.endif.endif.endif

.3.endif.endif.endif.endif.else:                  ; preds = %.3
  %.338 = and i64 %.98, 255
  %1 = lshr i64 %.92, 16
  %.348 = and i64 %1, 65280
  %2 = shl i64 %.97, 16
  %.370 = and i64 %2, 4278190080
  %.376 = and i64 %.92, 9223372032576520192
  %.381 = or i64 %.376, %.348
  %.386 = or i64 %.381, %.370
  %.391 = or i64 %.386, %.338
  %.398 = lshr i64 %.99, 3
  %.399 = and i64 %.398, 14
  %.400 = or i64 %.399, 1
  %.401 = sub nsw i64 64, %.400
  %.407 = lshr i64 %.99, %.401
  %.418 = shl i64 %.99, %.400
  %.419 = or i64 %.25, %.418
  %.420 = or i64 %.419, %.407
  %.393 = mul i64 %.420, %.99
  %.422 = mul i64 %.393, %.391
  br label %.3.endif.endif.endif.endif.endif

.3.endif.endif.endif.endif.endif:                 ; preds = %.3.endif.endif.endif.endif.else, %.3.endif.endif.endif.endif.if
  %.261.sink.off0 = phi i64 [ %.261, %.3.endif.endif.endif.endif.if ], [ %.422, %.3.endif.endif.endif.endif.else ]
  ret i64 %.261.sink.off0
}

attributes #0 = { norecurse nounwind readnone }
