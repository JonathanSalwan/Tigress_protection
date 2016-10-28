; ModuleID = 'llvm_expressions/./tigress-0-challenge-4.ll'
target datalayout = "e-m:e-i64:64-f80:128-n8:16:32:64-S128"
target triple = "x86_64-pc-linux-gnu"

; Function Attrs: norecurse nounwind readnone
define i64 @__arybo(i64 %SymVar_0) #0 {
.3:
  %.6 = lshr i64 %SymVar_0, 5
  %.7 = xor i64 %.6, 810798164723513605
  %.8 = add i64 %SymVar_0, -275339905
  %.9 = add i64 %.8, %.7
  %.13 = add i64 %.6, %SymVar_0
  %.14 = add i64 %.13, %.9
  %.20 = shl nuw nsw i64 %.6, 2
  %.22 = mul i64 %.20, %.14
  %.25 = and i64 %.22, 28
  %.29 = or i64 %.25, %.6
  %.35 = mul i64 %.6, 1015975030
  %.37 = and i64 %.35, 6
  %.38 = or i64 %.37, 1
  %.44 = lshr i64 %SymVar_0, %.38
  %.53 = lshr i64 %.9, 4
  %.54 = and i64 %.53, 14
  %.55 = or i64 %.54, 1
  %.56 = sub nsw i64 64, %.55
  %.62 = lshr i64 %.44, %.56
  %.94 = shl i64 %.44, %.55
  %.95 = or i64 %.62, %.94
  %.96 = shl i64 %.95, 3
  %.99 = and i64 %.96, 120
  %.106 = or i64 %.99, %.9
  %.107 = and i64 %.106, 15
  %.108 = or i64 %.107, 1
  %.109 = sub nsw i64 64, %.108
  %.115 = lshr i64 %.29, %.109
  %.226 = shl i64 %.29, %.108
  %.227 = or i64 %.115, %.226
  %.256 = lshr i64 %.44, 3
  %.257 = and i64 %.256, 14
  %.258 = or i64 %.257, 1
  %.259 = sub nsw i64 64, %.258
  %.265 = lshr i64 %.14, %.259
  %.302 = shl i64 %.14, %.258
  %.303 = or i64 %.265, %.302
  %.604 = sub i64 %.227, %.303
  %.1132 = xor i64 %.604, %.227
  %.1433 = xor i64 %.227, %.303
  %.1434 = and i64 %.1132, %.1433
  %.606 = xor i64 %.1433, %.604
  %.1435 = xor i64 %.606, %.1434
  %.1739 = icmp eq i64 %.227, %.303
  %.1435.lobit = lshr i64 %.1435, 63
  %.17395 = zext i1 %.1739 to i64
  %.1749 = or i64 %.1435.lobit, %.17395
  %.3673 = icmp eq i64 %.1749, 0
  br i1 %.3673, label %.3.endif.endif.endif.endif.endif.if, label %.3.endif.endif.endif.endif.endif.else

.3.endif.endif.endif.endif.endif.if:              ; preds = %.3
  %.3729 = shl nuw nsw i64 %.107, 3
  %.3730 = or i64 %.3729, %.106
  %.3765 = and i64 %.3730, 255
  %.3825 = and i64 %.9, -256
  %.3831 = or i64 %.3825, %.3765
  %.3843 = lshr i64 %SymVar_0, 61
  %.3861 = and i64 %.6, 65280
  %.3862 = or i64 %.3861, %.3843
  %.3866 = and i64 %.6, 16711680
  %.3867 = or i64 %.3862, %.3866
  %.3871 = and i64 %.6, 4278190080
  %.3872 = or i64 %.3867, %.3871
  %.3876 = and i64 %.6, 1095216660480
  %.3877 = or i64 %.3872, %.3876
  %.3881 = and i64 %.6, 280375465082880
  %.3882 = or i64 %.3877, %.3881
  %.3886 = and i64 %.6, 71776119061217280
  %.3887 = or i64 %.3882, %.3886
  %.3896 = shl i64 %.29, 56
  %.3897 = or i64 %.3887, %.3896
  %.3898 = sub i64 %.3831, %.3897
  %.3899 = or i64 %.3898, %.44
  %.3900 = shl i64 %.3898, 4
  %.3903 = and i64 %.3900, 1008
  %.3926 = or i64 %.3903, %.3897
  %.3951 = lshr i64 %.3730, 2
  %.3952 = and i64 %.3951, 6
  %.3953 = or i64 %.3952, 1
  %.3959 = shl i64 %.3926, %.3953
  %.3960 = add i64 %.3959, %.3899
  br label %.3.endif.endif.endif.endif.endif.endif

.3.endif.endif.endif.endif.endif.else:            ; preds = %.3
  %.3999 = sub i64 %.29, %.14
  %.4000 = shl i64 %.3999, 3
  %.4003 = and i64 %.4000, 248
  %.4019 = or i64 %.4003, %.44
  %.4814 = shl i64 %.106, 4
  %.4817 = and i64 %.4814, 496
  %.4844 = or i64 %.4817, %.29
  %.4845 = sub i64 %.106, %.4844
  %.4846 = or i64 %.4019, %.4845
  %.4847 = shl i64 %.4845, 4
  %.4850 = and i64 %.4847, 1008
  %.4851 = or i64 %.4850, %.4844
  %.4876 = lshr i64 %.106, 2
  %.4877 = and i64 %.4876, 6
  %.4878 = or i64 %.4877, 1
  %.4884 = shl i64 %.4851, %.4878
  %.4885 = add i64 %.4884, %.4846
  br label %.3.endif.endif.endif.endif.endif.endif

.3.endif.endif.endif.endif.endif.endif:           ; preds = %.3.endif.endif.endif.endif.endif.else, %.3.endif.endif.endif.endif.endif.if
  %.4887 = phi i64 [ %.3960, %.3.endif.endif.endif.endif.endif.if ], [ %.4885, %.3.endif.endif.endif.endif.endif.else ]
  ret i64 %.4887
}

attributes #0 = { norecurse nounwind readnone }
