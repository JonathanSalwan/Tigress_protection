; ModuleID = 'llvm_expressions/sample2-virt-operand-registers.ll'
source_filename = "llvm_expressions/sample2-virt-operand-registers.ll"
target datalayout = "e-m:e-i64:64-f80:128-n8:16:32:64-S128"
target triple = "x86_64-pc-linux-gnu"

; Function Attrs: norecurse nounwind readnone
define i64 @SECRET(i64 %SymVar_0) local_unnamed_addr #0 {
.3:
  %.6 = lshr i64 %SymVar_0, 5
  %.8 = add i64 %SymVar_0, -275339905
  %.9 = xor i64 %.6, 810798164723513605
  %.10 = add i64 %.8, %.9
  %.11 = add i64 %.6, %SymVar_0
  %.12 = add i64 %.11, %.10
  %.14 = shl nuw nsw i64 %.6, 2
  %.16 = mul i64 %.14, %.12
  %.19 = and i64 %.16, 28
  %.20 = or i64 %.19, %.6
  %.23 = mul i64 %.6, 1015975030
  %.25 = and i64 %.23, 6
  %.26 = or i64 %.25, 1
  %.32 = lshr i64 %SymVar_0, %.26
  %.35 = lshr i64 %.10, 4
  %.36 = and i64 %.35, 14
  %.37 = or i64 %.36, 1
  %.43 = shl i64 %.32, %.37
  %.49 = sub nsw i64 64, %.37
  %.55 = lshr i64 %.32, %.49
  %.56 = or i64 %.55, %.43
  %.57 = shl i64 %.56, 3
  %.60 = and i64 %.57, 120
  %.61 = or i64 %.60, %.10
  %.62 = and i64 %.61, 15
  %.63 = or i64 %.62, 1
  %.69 = shl i64 %.20, %.63
  %.72 = sub nsw i64 64, %.63
  %.78 = lshr i64 %.20, %.72
  %.79 = or i64 %.78, %.69
  %.82 = lshr i64 %.32, 3
  %.83 = and i64 %.82, 14
  %.84 = or i64 %.83, 1
  %.90 = shl i64 %.12, %.84
  %.96 = sub nsw i64 64, %.84
  %.102 = lshr i64 %.12, %.96
  %.103 = or i64 %.102, %.90
  %.104 = sub i64 %.79, %.103
  %.107 = xor i64 %.104, %.79
  %.108 = xor i64 %.79, %.103
  %.109 = and i64 %.107, %.108
  %.106 = xor i64 %.108, %.104
  %.110 = xor i64 %.106, %.109
  %.113 = icmp eq i64 %.104, 0
  %.110.lobit = lshr i64 %.110, 63
  %.11312 = zext i1 %.113 to i64
  %.123 = or i64 %.110.lobit, %.11312
  %.138 = icmp eq i64 %.123, 0
  br i1 %.138, label %.3.endif.endif.endif.endif.if, label %.3.endif.endif.endif.endif.else

.3.endif.endif.endif.endif.if:                    ; preds = %.3
  %.166 = lshr i64 %SymVar_0, 61
  %.184 = and i64 %.6, 65280
  %.185 = or i64 %.184, %.166
  %.189 = and i64 %.6, 16711680
  %.190 = or i64 %.185, %.189
  %.194 = and i64 %.6, 4278190080
  %.195 = or i64 %.190, %.194
  %.199 = and i64 %.6, 1095216660480
  %.200 = or i64 %.195, %.199
  %.204 = and i64 %.6, 280375465082880
  %.205 = or i64 %.200, %.204
  %.209 = and i64 %.6, 71776119061217280
  %.210 = or i64 %.205, %.209
  %.219 = shl i64 %.20, 56
  %.220 = or i64 %.210, %.219
  %.265 = shl nuw nsw i64 %.62, 3
  %.266 = or i64 %.265, %.61
  %.301 = and i64 %.266, 255
  %.361 = and i64 %.10, -256
  %.367 = or i64 %.361, %.301
  %.390 = sub i64 %.367, %.220
  %.391 = shl i64 %.390, 4
  %.394 = and i64 %.391, 1008
  %.395 = or i64 %.394, %.220
  %.420 = lshr i64 %.266, 2
  %.421 = and i64 %.420, 6
  %.422 = or i64 %.421, 1
  %.428 = shl i64 %.395, %.422
  %.429 = or i64 %.390, %.32
  %.430 = add i64 %.428, %.429
  br label %.3.endif.endif.endif.endif.endif

.3.endif.endif.endif.endif.else:                  ; preds = %.3
  %.490 = shl i64 %.61, 4
  %.493 = and i64 %.490, 496
  %.494 = or i64 %.493, %.20
  %.596 = sub i64 %.61, %.494
  %.597 = shl i64 %.596, 4
  %.600 = and i64 %.597, 1008
  %.601 = or i64 %.600, %.494
  %.626 = lshr i64 %.61, 2
  %.627 = and i64 %.626, 6
  %.628 = or i64 %.627, 1
  %.634 = shl i64 %.601, %.628
  %.635 = sub i64 %.20, %.12
  %.636 = shl i64 %.635, 3
  %.639 = and i64 %.636, 248
  %.640 = or i64 %.639, %.32
  %.641 = or i64 %.640, %.596
  %.642 = add i64 %.634, %.641
  br label %.3.endif.endif.endif.endif.endif

.3.endif.endif.endif.endif.endif:                 ; preds = %.3.endif.endif.endif.endif.else, %.3.endif.endif.endif.endif.if
  %.644 = phi i64 [ %.430, %.3.endif.endif.endif.endif.if ], [ %.642, %.3.endif.endif.endif.endif.else ]
  ret i64 %.644
}

attributes #0 = { norecurse nounwind readnone }
