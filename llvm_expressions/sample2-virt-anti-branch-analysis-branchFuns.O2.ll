; ModuleID = 'llvm_expressions/sample2-virt-anti-branch-analysis-branchFuns.ll'
source_filename = "llvm_expressions/sample2-virt-anti-branch-analysis-branchFuns.ll"
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
  %.32 = lshr i64 %SymVar_0, %.26
  %.35 = lshr i64 %.9, 4
  %.36 = and i64 %.35, 14
  %.37 = or i64 %.36, 1
  %.38 = sub nsw i64 64, %.37
  %.44 = lshr i64 %.32, %.38
  %.55 = shl i64 %.32, %.37
  %.56 = or i64 %.44, %.55
  %.57 = shl i64 %.56, 3
  %.60 = and i64 %.57, 120
  %.61 = or i64 %.60, %.9
  %.62 = and i64 %.61, 15
  %.63 = or i64 %.62, 1
  %.64 = sub nsw i64 64, %.63
  %.70 = lshr i64 %.20, %.64
  %.78 = shl i64 %.20, %.63
  %.79 = or i64 %.70, %.78
  %.82 = lshr i64 %.32, 3
  %.83 = and i64 %.82, 14
  %.84 = or i64 %.83, 1
  %.85 = sub nsw i64 64, %.84
  %.91 = lshr i64 %.11, %.85
  %.102 = shl i64 %.11, %.84
  %.103 = or i64 %.91, %.102
  %.104 = sub i64 %.79, %.103
  %.107 = xor i64 %.104, %.79
  %.108 = xor i64 %.79, %.103
  %.109 = and i64 %.107, %.108
  %.106 = xor i64 %.108, %.104
  %.110 = xor i64 %.106, %.109
  %.113 = icmp eq i64 %.104, 0
  %.110.lobit = lshr i64 %.110, 63
  %.1138 = zext i1 %.113 to i64
  %.123 = or i64 %.110.lobit, %.1138
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
  %.370 = shl i64 %.368, 4
  %.373 = and i64 %.370, 1008
  %.396 = or i64 %.373, %.367
  %.421 = lshr i64 %.200, 2
  %.422 = and i64 %.421, 6
  %.423 = or i64 %.422, 1
  %.429 = shl i64 %.396, %.423
  %.430 = add i64 %.429, %.369
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
  %.604 = shl i64 %.602, 4
  %.607 = and i64 %.604, 1008
  %.608 = or i64 %.607, %.601
  %.633 = lshr i64 %.61, 2
  %.634 = and i64 %.633, 6
  %.635 = or i64 %.634, 1
  %.641 = shl i64 %.608, %.635
  %.642 = add i64 %.641, %.603
  br label %.3.endif.endif.endif.endif.endif

.3.endif.endif.endif.endif.endif:                 ; preds = %.3.endif.endif.endif.endif.else, %.3.endif.endif.endif.endif.if
  %.644 = phi i64 [ %.430, %.3.endif.endif.endif.endif.if ], [ %.642, %.3.endif.endif.endif.endif.else ]
  ret i64 %.644
}

attributes #0 = { norecurse nounwind readnone }
