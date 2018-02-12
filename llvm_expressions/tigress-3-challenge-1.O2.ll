; ModuleID = 'llvm_expressions/tigress-3-challenge-1.ll'
source_filename = "llvm_expressions/tigress-3-challenge-1.ll"
target datalayout = "e-m:e-i64:64-f80:128-n8:16:32:64-S128"
target triple = "x86_64-pc-linux-gnu"

; Function Attrs: norecurse nounwind readnone
define i64 @SECRET(i64 %SymVar_0) local_unnamed_addr #0 {
.3:
  %.8 = lshr i64 %SymVar_0, 49
  %.5 = shl i64 %SymVar_0, 15
  %.13 = or i64 %.5, %.8
  %.16 = or i64 %.13, 21199854960640
  %.17 = or i64 %.16, %SymVar_0
  %.18 = and i64 %.16, %SymVar_0
  %.19 = sub i64 %.17, %.18
  %.22 = lshr i64 %.19, 7
  %div = udiv i64 %SymVar_0, 7
  %sub = and i64 %div, 15
  %.57 = or i64 %sub, 1
  %.64 = sub nsw i64 0, %.57
  %.69 = and i64 %.64, 63
  %.70 = lshr i64 %.22, %.69
  %.82 = shl i64 %.22, %.57
  %.83 = xor i64 %.70, -1
  %.84 = and i64 %.82, %.83
  %.85 = add i64 %.84, %.70
  %div1 = udiv i64 %.16, 7
  %.115 = sub i64 %.85, %div1
  %.117 = xor i64 %.85, -9223372036854775808
  %.118 = and i64 %.115, %.117
  %.129 = icmp sgt i64 %.118, -1
  br i1 %.129, label %.3.endif.endif.if, label %.3.endif.endif.else

.3.endif.endif.if:                                ; preds = %.3
  %.200 = mul i64 %.22, %.22
  %.209 = shl nuw nsw i64 %sub, 3
  %.210 = or i64 %.8, 7
  %.211 = xor i64 %.210, 56
  %.212 = add nuw nsw i64 %.8, 1
  %.213 = add nuw nsw i64 %.212, %.211
  %.219 = and i64 %.213, 62
  %.220 = or i64 %.219, 1
  %.221 = lshr i64 %SymVar_0, %.220
  %.224 = shl i64 %.221, 7
  %.227 = add i64 %.209, %.16
  %.230 = add i64 %.227, %.224
  %.233 = add i64 %.230, %.200
  %.236 = add i64 %.233, %div
  %.237 = xor i64 %.233, -1
  %.238 = and i64 %.236, %.237
  %.240 = xor i64 %.236, -1
  %.241 = and i64 %.233, %.240
  %.243 = mul i64 %.238, %.241
  %.245 = and i64 %.236, %.233
  %.247 = or i64 %.236, %.233
  %.249 = mul i64 %.245, %.247
  %.251 = add i64 %.243, %.249
  %.252 = xor i64 %.230, -1
  %.253 = and i64 %.16, %.252
  %.254 = add i64 %.253, %.230
  %.255 = and i64 %.251, %.254
  %.257 = xor i64 %.251, %.254
  br label %.3.endif.endif.endif

.3.endif.endif.else:                              ; preds = %.3
  %.291 = lshr i64 %div, 2
  %sub2 = and i64 %.291, 14
  %.297 = or i64 %sub2, 1
  %.305 = xor i64 %sub2, 63
  %.306 = shl i64 %div, %.305
  %.321 = lshr i64 %div, %.297
  %.322 = xor i64 %.306, -1
  %.323 = and i64 %.321, %.322
  %.324 = add i64 %.323, %.306
  %.356 = mul i64 %.22, %.22
  %.359 = or i64 %.8, 7
  %.360 = xor i64 %.359, 56
  %.361 = add nuw nsw i64 %.8, 1
  %.362 = add nuw nsw i64 %.361, %.360
  %.368 = and i64 %.362, 62
  %.369 = or i64 %.368, 1
  %.370 = lshr i64 %SymVar_0, %.369
  %.373 = shl i64 %.370, 7
  %.376 = add i64 %.373, %.16
  %.379 = add i64 %.376, %.356
  %.382 = add i64 %.324, %.379
  %.383 = xor i64 %.379, -1
  %.384 = and i64 %.382, %.383
  %.386 = xor i64 %.382, -1
  %.387 = and i64 %.379, %.386
  %.389 = mul i64 %.384, %.387
  %.391 = and i64 %.382, %.379
  %.393 = or i64 %.382, %.379
  %.395 = mul i64 %.391, %.393
  %.397 = add i64 %.389, %.395
  %.398 = xor i64 %.376, -1
  %.399 = and i64 %.16, %.398
  %.400 = add i64 %.399, %.376
  %.401 = and i64 %.397, %.400
  %.403 = xor i64 %.397, %.400
  br label %.3.endif.endif.endif

.3.endif.endif.endif:                             ; preds = %.3.endif.endif.else, %.3.endif.endif.if
  %.403.sink = phi i64 [ %.403, %.3.endif.endif.else ], [ %.257, %.3.endif.endif.if ]
  %.402.sink.in = phi i64 [ %.401, %.3.endif.endif.else ], [ %.255, %.3.endif.endif.if ]
  %.402.sink = shl i64 %.402.sink.in, 1
  %.404 = add i64 %.402.sink, %.403.sink
  ret i64 %.404
}

attributes #0 = { norecurse nounwind readnone }
