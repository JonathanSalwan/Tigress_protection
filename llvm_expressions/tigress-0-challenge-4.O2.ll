; ModuleID = 'llvm_expressions/tigress-0-challenge-4.ll'
source_filename = "llvm_expressions/tigress-0-challenge-4.ll"
target datalayout = "e-m:e-i64:64-f80:128-n8:16:32:64-S128"
target triple = "x86_64-pc-linux-gnu"

; Function Attrs: norecurse nounwind readnone
define i64 @SECRET(i64 %SymVar_0) local_unnamed_addr #0 {
.3:
  %.6 = lshr i64 %SymVar_0, 5
  %.7 = xor i64 %.6, 810798164723513605
  %.8 = add i64 %SymVar_0, -275339905
  %.9 = add i64 %.8, %.7
  %.10 = add i64 %.6, %SymVar_0
  %.11 = add i64 %.10, %.9
  %.14 = shl nuw nsw i64 %.6, 2
  %.16 = mul i64 %.14, %.11
  %.19 = and i64 %.16, 28
  %.20 = or i64 %.19, %.6
  %.23 = mul i64 %.6, 1015975030
  %0 = and i64 %.23, 6
  %.27 = or i64 %0, 1
  %.32 = lshr i64 %SymVar_0, %.27
  %.35 = lshr i64 %.9, 4
  %.36 = and i64 %.35, 14
  %.37 = or i64 %.36, 1
  %.38 = sub nsw i64 0, %.37
  %.43 = and i64 %.38, 63
  %.44 = lshr i64 %.32, %.43
  %.55 = shl i64 %.32, %.37
  %.56 = or i64 %.44, %.55
  %.57 = shl i64 %.56, 3
  %.60 = and i64 %.57, 120
  %.61 = or i64 %.60, %.9
  %.62 = and i64 %.61, 15
  %.63 = or i64 %.62, 1
  %.64 = sub nsw i64 0, %.63
  %.69 = and i64 %.64, 63
  %.70 = lshr i64 %.20, %.69
  %.78 = shl i64 %.20, %.63
  %.79 = or i64 %.70, %.78
  %.82 = lshr i64 %.32, 3
  %.83 = and i64 %.82, 14
  %.84 = or i64 %.83, 1
  %.85 = sub nsw i64 0, %.84
  %.90 = and i64 %.85, 63
  %.91 = lshr i64 %.11, %.90
  %.102 = shl i64 %.11, %.84
  %.103 = or i64 %.91, %.102
  %.104 = sub i64 %.79, %.103
  %.107 = xor i64 %.104, %.79
  %.108 = xor i64 %.79, %.103
  %.109 = and i64 %.107, %.108
  %.106 = xor i64 %.108, %.104
  %.110 = xor i64 %.106, %.109
  %.111 = lshr i64 %.110, 63
  %.113 = icmp eq i64 %.104, 0
  %.1133 = zext i1 %.113 to i64
  %.123 = or i64 %.111, %.1133
  %.138 = icmp eq i64 %.123, 0
  br i1 %.138, label %.3.endif.endif.endif.endif.if, label %.3.endif.endif.endif.endif.else

.3.endif.endif.endif.endif.if:                    ; preds = %.3
  %.199 = shl nuw nsw i64 %.62, 3
  %.200 = or i64 %.199, %.61
  %.235 = and i64 %.200, 255
  %.295 = and i64 %.9, -256
  %.301 = or i64 %.295, %.235
  %.313 = lshr i64 %SymVar_0, 61
  %.331 = and i64 %.6, 65280
  %.332 = or i64 %.331, %.313
  %.336 = and i64 %.6, 16711680
  %.337 = or i64 %.332, %.336
  %.341 = and i64 %.6, 4278190080
  %.342 = or i64 %.337, %.341
  %.346 = and i64 %.6, 1095216660480
  %.347 = or i64 %.342, %.346
  %.351 = and i64 %.6, 280375465082880
  %.352 = or i64 %.347, %.351
  %.356 = and i64 %.6, 71776119061217280
  %.357 = or i64 %.352, %.356
  %.366 = shl i64 %.20, 56
  %.367 = or i64 %.357, %.366
  %.368 = sub i64 %.301, %.367
  %.369 = or i64 %.368, %.32
  br label %.3.endif.endif.endif.endif.endif

.3.endif.endif.endif.endif.else:                  ; preds = %.3
  %.449 = sub i64 %.20, %.11
  %.450 = shl i64 %.449, 3
  %.453 = and i64 %.450, 248
  %.466 = or i64 %.453, %.32
  %.597 = shl i64 %.61, 4
  %.600 = and i64 %.597, 496
  %.601 = or i64 %.600, %.20
  %.602 = sub i64 %.61, %.601
  %.603 = or i64 %.466, %.602
  br label %.3.endif.endif.endif.endif.endif

.3.endif.endif.endif.endif.endif:                 ; preds = %.3.endif.endif.endif.endif.else, %.3.endif.endif.endif.endif.if
  %.602.sink = phi i64 [ %.602, %.3.endif.endif.endif.endif.else ], [ %.368, %.3.endif.endif.endif.endif.if ]
  %.601.sink = phi i64 [ %.601, %.3.endif.endif.endif.endif.else ], [ %.367, %.3.endif.endif.endif.endif.if ]
  %.529.sink.in = phi i64 [ %.61, %.3.endif.endif.endif.endif.else ], [ %.200, %.3.endif.endif.endif.endif.if ]
  %.603.sink = phi i64 [ %.603, %.3.endif.endif.endif.endif.else ], [ %.369, %.3.endif.endif.endif.endif.if ]
  %.604 = shl i64 %.602.sink, 4
  %.607 = and i64 %.604, 1008
  %.608 = or i64 %.607, %.601.sink
  %.633 = lshr i64 %.529.sink.in, 2
  %1 = and i64 %.633, 6
  %2 = or i64 %1, 1
  %.641 = shl i64 %.608, %2
  %.642 = add i64 %.641, %.603.sink
  ret i64 %.642
}

attributes #0 = { norecurse nounwind readnone }
