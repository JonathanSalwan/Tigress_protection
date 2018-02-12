; ModuleID = 'llvm_expressions/sample2-virt-random-opcodes-false.ll'
source_filename = "llvm_expressions/sample2-virt-random-opcodes-false.ll"
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
  %.124 = icmp eq i64 %.109, 0
  br i1 %.124, label %.3.endif.endif.endif.endif.if, label %.3.endif.endif.endif.endif.else

.3.endif.endif.endif.endif.if:                    ; preds = %.3
  %.179 = shl nuw nsw i64 %.56, 3
  %.180 = or i64 %.179, %.55
  %.215 = and i64 %.180, 255
  %.275 = and i64 %.9, -256
  %.281 = or i64 %.275, %.215
  %.293 = lshr i64 %SymVar_0, 61
  %.311 = and i64 %.6, 65280
  %.312 = or i64 %.311, %.293
  %.316 = and i64 %.6, 16711680
  %.317 = or i64 %.312, %.316
  %.321 = and i64 %.6, 4278190080
  %.322 = or i64 %.317, %.321
  %.326 = and i64 %.6, 1095216660480
  %.327 = or i64 %.322, %.326
  %.331 = and i64 %.6, 280375465082880
  %.332 = or i64 %.327, %.331
  %.336 = and i64 %.6, 71776119061217280
  %.337 = or i64 %.332, %.336
  %.346 = shl i64 %.20, 56
  %.347 = or i64 %.337, %.346
  %.348 = sub i64 %.281, %.347
  %.349 = or i64 %.348, %.30
  %.350 = shl i64 %.348, 4
  %.353 = and i64 %.350, 1008
  %.376 = or i64 %.353, %.347
  %.401 = lshr i64 %.180, 2
  %.402 = and i64 %.401, 6
  %.403 = or i64 %.402, 1
  %.407 = shl i64 %.376, %.403
  %.408 = add i64 %.407, %.349
  br label %.3.endif.endif.endif.endif.endif

.3.endif.endif.endif.endif.else:                  ; preds = %.3
  %.427 = sub i64 %.20, %.11
  %.428 = shl i64 %.427, 3
  %.431 = and i64 %.428, 248
  %.442 = or i64 %.431, %.30
  %.569 = shl i64 %.55, 4
  %.572 = and i64 %.569, 496
  %.573 = or i64 %.572, %.20
  %.574 = sub i64 %.55, %.573
  %.575 = or i64 %.442, %.574
  %.576 = shl i64 %.574, 4
  %.579 = and i64 %.576, 1008
  %.580 = or i64 %.579, %.573
  %.605 = lshr i64 %.55, 2
  %.606 = and i64 %.605, 6
  %.607 = or i64 %.606, 1
  %.611 = shl i64 %.580, %.607
  %.612 = add i64 %.611, %.575
  br label %.3.endif.endif.endif.endif.endif

.3.endif.endif.endif.endif.endif:                 ; preds = %.3.endif.endif.endif.endif.else, %.3.endif.endif.endif.endif.if
  %.614 = phi i64 [ %.408, %.3.endif.endif.endif.endif.if ], [ %.612, %.3.endif.endif.endif.endif.else ]
  ret i64 %.614
}

attributes #0 = { norecurse nounwind readnone }
