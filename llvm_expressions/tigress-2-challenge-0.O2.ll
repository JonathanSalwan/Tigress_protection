; ModuleID = 'llvm_expressions/tigress-2-challenge-0.ll'
source_filename = "llvm_expressions/tigress-2-challenge-0.ll"
target datalayout = "e-m:e-i64:64-f80:128-n8:16:32:64-S128"
target triple = "x86_64-pc-linux-gnu"

; Function Attrs: norecurse nounwind readnone
define i64 @SECRET(i64 %SymVar_0) local_unnamed_addr #0 {
.3:
  %.6 = mul i64 %SymVar_0, 8349898219520
  %0 = udiv i64 %.6, 7
  %.37 = or i64 %.6, %SymVar_0
  %.38 = add i64 %.37, %SymVar_0
  %.41 = mul i64 %SymVar_0, 1068786972098560
  %.42 = add i64 %.37, %.41
  %.44 = add i64 %SymVar_0, 327625093
  %.46 = mul i64 %.42, %.44
  %.48 = add i64 %.46, %.38
  %.49 = sub i64 %0, %.48
  %.55 = or i64 %.49, %.48
  %.57 = icmp sgt i64 %.55, -1
  %.59 = icmp ne i64 %.49, 0
  %.85.demorgan = and i1 %.59, %.57
  br i1 %.85.demorgan, label %.3.endif.endif.endif.endif.else, label %.3.endif.endif.endif.endif.if

.3.endif.endif.endif.endif.if:                    ; preds = %.3
  %.132 = lshr i64 %.46, 1
  %.134 = shl i64 %.132, 2
  %.137 = and i64 %.134, 28
  %.138 = shl i64 %.46, 2
  %.141 = and i64 %.138, 28
  %.142 = or i64 %.141, %.6
  %.143 = shl i64 %.46, 4
  %.146 = and i64 %.143, 16
  %.147 = or i64 %.142, %.146
  %.148 = or i64 %.147, %.137
  %.149 = shl i64 %.148, 2
  %.152 = and i64 %.149, 16
  %.153 = and i64 %.46, 14
  %.154 = or i64 %.153, 1
  %.156 = sub nsw i64 0, %.154
  %.160 = and i64 %.156, 63
  %.161 = shl i64 %.6, %.160
  %.169 = lshr i64 %.6, %.154
  %.170 = or i64 %.161, %.169
  %.171 = or i64 %.152, %.170
  %.172 = add i64 %.171, %.148
  %.173 = and i64 %.132, 14
  %.174 = or i64 %.173, 1
  %.176 = sub nsw i64 0, %.174
  %.180 = and i64 %.176, 63
  %.181 = shl i64 %.170, %.180
  %.189 = lshr i64 %.170, %.174
  %.190 = or i64 %.181, %.189
  %.222 = lshr i64 %.46, 51
  %.230 = and i64 %.222, 14
  %.231 = or i64 %.230, 1
  %.233 = sub nsw i64 0, %.231
  %.237 = and i64 %.233, 63
  %.238 = shl i64 %.190, %.237
  %.256 = lshr i64 %.190, %.231
  %.257 = or i64 %.238, %.256
  %.260 = lshr i64 %.257, 1
  %.261 = and i64 %.260, 14
  %.262 = or i64 %.261, 1
  %.264 = sub nsw i64 0, %.262
  %.268 = and i64 %.264, 63
  %.269 = lshr i64 %.172, %.268
  %.319 = shl i64 %.172, %.262
  br label %.3.endif.endif.endif.endif.endif

.3.endif.endif.endif.endif.else:                  ; preds = %.3
  %.328 = shl i64 %.38, 2
  %.331 = and i64 %.328, 28
  %.341 = shl i64 %.46, 2
  %.344 = and i64 %.341, 28
  %.345 = shl i64 %.38, 1
  %.346 = or i64 %.344, %.345
  %.347 = shl i64 %.346, 2
  %.350 = and i64 %.347, 24
  %.351 = or i64 %.346, %.331
  %.352 = or i64 %.351, %.350
  %.353 = shl i64 %.351, 2
  %.356 = and i64 %.353, 24
  %.357 = and i64 %.46, 14
  %.358 = or i64 %.357, 1
  %.360 = sub nsw i64 0, %.358
  %.364 = and i64 %.360, 63
  %.365 = shl i64 %.345, %.364
  %.373 = lshr i64 %.345, %.358
  %.374 = or i64 %.365, %.373
  %.375 = or i64 %.356, %.374
  %.376 = add i64 %.375, %.352
  %.377 = and i64 %.38, 14
  %.378 = or i64 %.377, 1
  %.380 = sub nsw i64 0, %.378
  %.384 = and i64 %.380, 63
  %.385 = shl i64 %.374, %.384
  %.393 = lshr i64 %.374, %.378
  %.394 = or i64 %.385, %.393
  %.426 = lshr i64 %.38, 50
  %.434 = and i64 %.426, 14
  %.435 = or i64 %.434, 1
  %.437 = sub nsw i64 0, %.435
  %.441 = and i64 %.437, 63
  %.442 = shl i64 %.394, %.441
  %.460 = lshr i64 %.394, %.435
  %.461 = or i64 %.442, %.460
  %.464 = lshr i64 %.461, 1
  %.465 = and i64 %.464, 14
  %.466 = or i64 %.465, 1
  %.468 = sub nsw i64 0, %.466
  %.472 = and i64 %.468, 63
  %.473 = lshr i64 %.376, %.472
  %.523 = shl i64 %.376, %.466
  br label %.3.endif.endif.endif.endif.endif

.3.endif.endif.endif.endif.endif:                 ; preds = %.3.endif.endif.endif.endif.else, %.3.endif.endif.endif.endif.if
  %.523.sink = phi i64 [ %.523, %.3.endif.endif.endif.endif.else ], [ %.319, %.3.endif.endif.endif.endif.if ]
  %.473.sink = phi i64 [ %.473, %.3.endif.endif.endif.endif.else ], [ %.269, %.3.endif.endif.endif.endif.if ]
  %.524 = or i64 %.473.sink, %.523.sink
  ret i64 %.524
}

attributes #0 = { norecurse nounwind readnone }
