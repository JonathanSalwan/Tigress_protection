; ModuleID = 'llvm_expressions/tigress-4-challenge-2.ll'
target datalayout = "e-m:e-i64:64-f80:128-n8:16:32:64-S128"
target triple = "x86_64-pc-linux-gnu"

; Function Attrs: norecurse nounwind readnone
define i64 @__arybo(i64 %SymVar_0) #0 {
.3:
  %.6 = lshr i64 %SymVar_0, 53
  %.9 = shl i64 %SymVar_0, 11
  %.10 = or i64 %.6, %.9
  %.13 = lshr i64 %.10, 1
  %div = udiv i64 %SymVar_0, 3
  %0 = mul i64 %.13, -112410438
  %.57 = add i64 %0, %div
  %.60 = lshr i64 %.57, 3
  %.61 = and i64 %.60, 14
  %.62 = or i64 %.61, 1
  %.63 = sub nsw i64 64, %.62
  %.69 = shl i64 %.13, %.63
  %.134 = lshr i64 %.13, %.62
  %.135 = or i64 %.69, %.134
  %.192 = lshr i64 %.57, 2
  %.193 = and i64 %.192, 14
  %.194 = or i64 %.193, 1
  %.195 = sub nsw i64 64, %.194
  %.201 = lshr i64 %.13, %.195
  %.266 = shl i64 %.13, %.194
  %.267 = or i64 %.201, %.266
  %.268 = shl i64 %.267, 2
  %.271 = and i64 %.268, 28
  %.272 = add i64 %SymVar_0, 160536708
  %.319 = lshr i64 %.57, 9
  %.323 = and i64 %.319, 6
  %.324 = or i64 %.323, 1
  %.330 = lshr i64 %.272, %.324
  %.331 = shl i64 %.330, 4
  %.334 = and i64 %.331, 1008
  %.394 = or i64 %.334, %.330
  %.395 = or i64 %.271, %.394
  %.396 = add i64 %SymVar_0, 8152287480
  %.399 = lshr i64 %.396, 4
  %.400 = and i64 %.399, 14
  %.401 = or i64 %.400, 1
  %.402 = sub nsw i64 64, %.401
  %.408 = shl i64 %.395, %.402
  %.680 = lshr i64 %.395, %.401
  %.681 = or i64 %.408, %.680
  %.1360 = sub i64 %.135, %.681
  %.2174 = xor i64 %.1360, %.69
  %.2853 = xor i64 %.408, %.69
  %.2854 = and i64 %.2174, %.2853
  %.1362 = xor i64 %.2853, %.1360
  %.2855 = xor i64 %.1362, %.2854
  %.2858 = icmp sgt i64 %.2855, -1
  %.3543 = icmp ne i64 %.135, %.681
  %.8221.demorgan = and i1 %.3543, %.2858
  br i1 %.8221.demorgan, label %.3.endif.endif.endif.endif.endif.else, label %.3.endif.endif.endif.endif.endif.if

.3.endif.endif.endif.endif.endif.if:              ; preds = %.3
  %.8490 = mul i64 %.395, %.396
  %.8537 = shl i64 %.57, 3
  %.8540 = and i64 %.8537, 120
  %.8585 = or i64 %.8540, %.57
  %.8846 = and i64 %.395, %.8585
  %.8847 = shl i64 %.8846, 4
  %.8850 = and i64 %.8847, 496
  %.8861 = or i64 %.8585, %.13
  %.8862 = or i64 %.8861, %.8850
  %.8864 = mul i64 %.8490, %.8862
  br label %.3.endif.endif.endif.endif.endif.endif

.3.endif.endif.endif.endif.endif.else:            ; preds = %.3
  %.8963 = and i64 %.395, 255
  %1 = lshr i64 %.330, 16
  %.8979 = and i64 %1, 65280
  %2 = shl i64 %.394, 16
  %.9013 = and i64 %2, 4278190080
  %.9019 = and i64 %.330, 9223372032576520192
  %.9024 = or i64 %.9019, %.8979
  %.9029 = or i64 %.9024, %.9013
  %.9034 = or i64 %.9029, %.8963
  %.9041 = lshr i64 %.396, 3
  %.9042 = and i64 %.9041, 14
  %.9043 = or i64 %.9042, 1
  %.9044 = sub nsw i64 64, %.9043
  %.9050 = lshr i64 %.396, %.9044
  %.9061 = shl i64 %.396, %.9043
  %.9062 = or i64 %.57, %.9061
  %.9063 = or i64 %.9062, %.9050
  %.9036 = mul i64 %.9063, %.396
  %.9065 = mul i64 %.9036, %.9034
  br label %.3.endif.endif.endif.endif.endif.endif

.3.endif.endif.endif.endif.endif.endif:           ; preds = %.3.endif.endif.endif.endif.endif.else, %.3.endif.endif.endif.endif.endif.if
  %.8864.sink.off0 = phi i64 [ %.8864, %.3.endif.endif.endif.endif.endif.if ], [ %.9065, %.3.endif.endif.endif.endif.endif.else ]
  ret i64 %.8864.sink.off0
}

attributes #0 = { norecurse nounwind readnone }
