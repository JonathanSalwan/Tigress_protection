; ModuleID = 'llvm_expressions/sample24-virt-operand-registers.ll'
source_filename = "llvm_expressions/sample24-virt-operand-registers.ll"
target datalayout = "e-m:e-i64:64-f80:128-n8:16:32:64-S128"
target triple = "x86_64-pc-linux-gnu"

; Function Attrs: norecurse nounwind readnone
define i64 @SECRET(i64 %SymVar_0) local_unnamed_addr #0 {
.3:
  %.6 = shl i64 %SymVar_0, 11
  %.9 = lshr i64 %SymVar_0, 53
  %.10 = or i64 %.6, %.9
  %.13 = lshr i64 %.10, 1
  %div = udiv i64 %SymVar_0, 3
  %0 = mul i64 %.13, -112410438
  %.25 = add i64 %0, %div
  %.28 = lshr i64 %.25, 3
  %.29 = and i64 %.28, 14
  %.30 = or i64 %.29, 1
  %.36 = lshr i64 %.13, %.30
  %.42 = sub nsw i64 64, %.30
  %.48 = shl i64 %.13, %.42
  %.49 = or i64 %.48, %.36
  %.50 = add i64 %SymVar_0, 160536708
  %.53 = lshr i64 %.25, 9
  %.57 = and i64 %.53, 6
  %.58 = or i64 %.57, 1
  %.64 = lshr i64 %.50, %.58
  %.65 = shl i64 %.64, 4
  %.68 = and i64 %.65, 1008
  %.69 = or i64 %.68, %.64
  %.72 = lshr i64 %.25, 2
  %.73 = and i64 %.72, 14
  %.74 = or i64 %.73, 1
  %.80 = shl i64 %.13, %.74
  %.86 = sub nsw i64 64, %.74
  %.92 = lshr i64 %.13, %.86
  %.93 = or i64 %.92, %.80
  %.94 = shl i64 %.93, 2
  %.97 = and i64 %.94, 28
  %.98 = or i64 %.97, %.69
  %.99 = add i64 %SymVar_0, 8152287480
  %.102 = lshr i64 %.99, 4
  %.103 = and i64 %.102, 14
  %.104 = or i64 %.103, 1
  %.110 = lshr i64 %.98, %.104
  %.116 = sub nsw i64 64, %.104
  %.122 = shl i64 %.98, %.116
  %.123 = or i64 %.110, %.122
  %.124 = sub i64 %.49, %.123
  %.127 = xor i64 %.124, %.48
  %.128 = xor i64 %.122, %.48
  %.129 = and i64 %.127, %.128
  %.126 = xor i64 %.128, %.124
  %.130 = xor i64 %.126, %.129
  %.133 = icmp sgt i64 %.130, -1
  %.139 = icmp ne i64 %.124, 0
  %.160.demorgan = and i1 %.139, %.133
  br i1 %.160.demorgan, label %.3.endif.endif.endif.endif.else, label %.3.endif.endif.endif.endif.if

.3.endif.endif.endif.endif.if:                    ; preds = %.3
  %.242 = shl i64 %.25, 3
  %.245 = and i64 %.242, 120
  %.246 = or i64 %.245, %.25
  %.247 = and i64 %.98, %.246
  %.248 = shl i64 %.247, 4
  %.251 = and i64 %.248, 496
  %.252 = or i64 %.246, %.13
  %.253 = or i64 %.252, %.251
  %.258 = mul i64 %.98, %.99
  %.261 = mul i64 %.258, %.253
  br label %.3.endif.endif.endif.endif.endif

.3.endif.endif.endif.endif.else:                  ; preds = %.3
  %.267 = lshr i64 %.99, 3
  %.268 = and i64 %.267, 14
  %.269 = or i64 %.268, 1
  %.275 = shl i64 %.99, %.269
  %.281 = sub nsw i64 64, %.269
  %.287 = lshr i64 %.99, %.281
  %.288 = or i64 %.25, %.275
  %.311 = or i64 %.288, %.287
  %.363 = and i64 %.98, 255
  %1 = lshr i64 %.64, 16
  %.373 = and i64 %1, 65280
  %2 = shl i64 %.69, 16
  %.395 = and i64 %2, 4278190080
  %.401 = and i64 %.64, 9223372032576520192
  %.406 = or i64 %.401, %.373
  %.411 = or i64 %.406, %.395
  %.416 = or i64 %.411, %.363
  %.419 = mul i64 %.311, %.99
  %.422 = mul i64 %.419, %.416
  br label %.3.endif.endif.endif.endif.endif

.3.endif.endif.endif.endif.endif:                 ; preds = %.3.endif.endif.endif.endif.else, %.3.endif.endif.endif.endif.if
  %.261.sink.off0 = phi i64 [ %.261, %.3.endif.endif.endif.endif.if ], [ %.422, %.3.endif.endif.endif.endif.else ]
  ret i64 %.261.sink.off0
}

attributes #0 = { norecurse nounwind readnone }
