; ModuleID = 'llvm_expressions/sample2-collberg-0.ll'
source_filename = "llvm_expressions/sample2-collberg-0.ll"
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
  %.25 = and i64 %.23, 6
  %.26 = or i64 %.25, 1
  %.30 = lshr i64 %SymVar_0, %.26
  %.33 = lshr i64 %.9, 4
  %.34 = and i64 %.33, 14
  %.35 = or i64 %.34, 1
  %.36 = sub nsw i64 64, %.35
  %.40 = lshr i64 %.30, %.36
  %.49 = shl i64 %.30, %.35
  %.50 = or i64 %.40, %.49
  %.51 = shl i64 %.50, 3
  %.54 = and i64 %.51, 120
  %.55 = or i64 %.54, %.9
  %.56 = and i64 %.55, 15
  %.57 = or i64 %.56, 1
  %.58 = sub nsw i64 64, %.57
  %.62 = lshr i64 %.20, %.58
  %.68 = shl i64 %.20, %.57
  %.69 = or i64 %.62, %.68
  %.72 = lshr i64 %.30, 3
  %.73 = and i64 %.72, 14
  %.74 = or i64 %.73, 1
  %.75 = sub nsw i64 64, %.74
  %.79 = lshr i64 %.11, %.75
  %.88 = shl i64 %.11, %.74
  %.89 = or i64 %.79, %.88
  %.90 = sub i64 %.69, %.89
  %.93 = xor i64 %.90, %.69
  %.94 = xor i64 %.69, %.89
  %.95 = and i64 %.93, %.94
  %.92 = xor i64 %.94, %.90
  %.96 = xor i64 %.92, %.95
  %.99 = icmp eq i64 %.90, 0
  %.96.lobit = lshr i64 %.96, 63
  %.994 = zext i1 %.99 to i64
  %.109 = or i64 %.96.lobit, %.994
  %.128 = icmp eq i64 %.109, 0
  br i1 %.128, label %.3.endif.endif.endif.endif.if, label %.3.endif.endif.endif.endif.else

.3.endif.endif.endif.endif.if:                    ; preds = %.3
  %.183 = shl nuw nsw i64 %.56, 3
  %.184 = or i64 %.183, %.55
  %.235 = and i64 %.184, 255
  %.303 = and i64 %.9, -256
  %.309 = or i64 %.303, %.235
  %.321 = lshr i64 %SymVar_0, 61
  %.351 = and i64 %.6, 65280
  %.352 = or i64 %.351, %.321
  %.356 = and i64 %.6, 16711680
  %.357 = or i64 %.352, %.356
  %.361 = and i64 %.6, 4278190080
  %.362 = or i64 %.357, %.361
  %.366 = and i64 %.6, 1095216660480
  %.367 = or i64 %.362, %.366
  %.371 = and i64 %.6, 280375465082880
  %.372 = or i64 %.367, %.371
  %.376 = and i64 %.6, 71776119061217280
  %.377 = or i64 %.372, %.376
  %.392 = shl i64 %.20, 56
  %.393 = or i64 %.377, %.392
  %.394 = sub i64 %.309, %.393
  %.395 = or i64 %.394, %.30
  %.396 = shl i64 %.394, 4
  %.399 = and i64 %.396, 1008
  %.422 = or i64 %.399, %.393
  %.447 = lshr i64 %.184, 2
  %.448 = and i64 %.447, 6
  %.449 = or i64 %.448, 1
  %.453 = shl i64 %.422, %.449
  %.454 = add i64 %.453, %.395
  br label %.3.endif.endif.endif.endif.endif

.3.endif.endif.endif.endif.else:                  ; preds = %.3
  %.473 = sub i64 %.20, %.11
  %.474 = shl i64 %.473, 3
  %.477 = and i64 %.474, 248
  %.488 = or i64 %.477, %.30
  %.639 = shl i64 %.55, 4
  %.642 = and i64 %.639, 496
  %.643 = or i64 %.642, %.20
  %.644 = sub i64 %.55, %.643
  %.645 = or i64 %.488, %.644
  %.646 = shl i64 %.644, 4
  %.649 = and i64 %.646, 1008
  %.650 = or i64 %.649, %.643
  %.675 = lshr i64 %.55, 2
  %.676 = and i64 %.675, 6
  %.677 = or i64 %.676, 1
  %.681 = shl i64 %.650, %.677
  %.682 = add i64 %.681, %.645
  br label %.3.endif.endif.endif.endif.endif

.3.endif.endif.endif.endif.endif:                 ; preds = %.3.endif.endif.endif.endif.else, %.3.endif.endif.endif.endif.if
  %.684 = phi i64 [ %.454, %.3.endif.endif.endif.endif.if ], [ %.682, %.3.endif.endif.endif.endif.else ]
  ret i64 %.684
}

attributes #0 = { norecurse nounwind readnone }
