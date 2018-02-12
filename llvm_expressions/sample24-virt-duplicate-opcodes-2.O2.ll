; ModuleID = 'llvm_expressions/sample24-virt-duplicate-opcodes-2.ll'
source_filename = "llvm_expressions/sample24-virt-duplicate-opcodes-2.ll"
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
  %.35 = shl i64 %.13, %.31
  %.46 = lshr i64 %.13, %.30
  %.47 = or i64 %.35, %.46
  %.50 = lshr i64 %.25, 2
  %.51 = and i64 %.50, 14
  %.52 = or i64 %.51, 1
  %.53 = sub nsw i64 64, %.52
  %.59 = lshr i64 %.13, %.53
  %.70 = shl i64 %.13, %.52
  %.71 = or i64 %.59, %.70
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
  %.109 = shl i64 %.96, %.103
  %.118 = lshr i64 %.96, %.102
  %.119 = or i64 %.109, %.118
  %.120 = sub i64 %.47, %.119
  %.123 = xor i64 %.120, %.35
  %.124 = xor i64 %.109, %.35
  %.125 = and i64 %.123, %.124
  %.122 = xor i64 %.124, %.120
  %.126 = xor i64 %.122, %.125
  %.129 = icmp sgt i64 %.126, -1
  %.135 = icmp ne i64 %.120, 0
  %.156.demorgan = and i1 %.135, %.129
  br i1 %.156.demorgan, label %.3.endif.endif.endif.endif.else, label %.3.endif.endif.endif.endif.if

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
  %.334 = and i64 %.96, 255
  %1 = lshr i64 %.90, 16
  %.344 = and i64 %1, 65280
  %2 = shl i64 %.95, 16
  %.366 = and i64 %2, 4278190080
  %.372 = and i64 %.90, 9223372032576520192
  %.377 = or i64 %.372, %.344
  %.382 = or i64 %.377, %.366
  %.387 = or i64 %.382, %.334
  %.394 = lshr i64 %.97, 3
  %.395 = and i64 %.394, 14
  %.396 = or i64 %.395, 1
  %.397 = sub nsw i64 64, %.396
  %.401 = lshr i64 %.97, %.397
  %.410 = shl i64 %.97, %.396
  %.411 = or i64 %.25, %.410
  %.412 = or i64 %.411, %.401
  %.389 = mul i64 %.412, %.97
  %.414 = mul i64 %.389, %.387
  br label %.3.endif.endif.endif.endif.endif

.3.endif.endif.endif.endif.endif:                 ; preds = %.3.endif.endif.endif.endif.else, %.3.endif.endif.endif.endif.if
  %.257.sink.off0 = phi i64 [ %.257, %.3.endif.endif.endif.endif.if ], [ %.414, %.3.endif.endif.endif.endif.else ]
  ret i64 %.257.sink.off0
}

attributes #0 = { norecurse nounwind readnone }
