; ModuleID = 'llvm_expressions/sample22-virt-max-merge-lenght-30.ll'
source_filename = "llvm_expressions/sample22-virt-max-merge-lenght-30.ll"
target datalayout = "e-m:e-i64:64-f80:128-n8:16:32:64-S128"
target triple = "x86_64-pc-linux-gnu"

; Function Attrs: norecurse nounwind readnone
define i64 @SECRET(i64 %SymVar_0) local_unnamed_addr #0 {
.3:
  %.7 = lshr i64 %SymVar_0, 55
  %.4 = shl i64 %SymVar_0, 9
  %.11 = or i64 %.4, %.7
  %.12 = or i64 %.11, 250589732864
  %0 = lshr i64 %SymVar_0, 42
  %.15 = and i64 %0, 8191
  %.18 = shl i64 %.12, 13
  %.19 = or i64 %.15, %SymVar_0
  %.20 = or i64 %.19, %.18
  %.23 = lshr i64 %.19, 1
  %.24 = and i64 %.23, 14
  %.25 = or i64 %.24, 1
  %.26 = sub nsw i64 64, %.25
  %.30 = lshr i64 %.12, %.26
  %.39 = shl i64 %.12, %.25
  %.40 = or i64 %.30, %.39
  %.42 = add i64 %SymVar_0, 104868834
  %.51 = or i64 %SymVar_0, 893657663
  %.44 = mul i64 %.42, 1004737041
  %.48 = mul i64 %.44, %.51
  %.53 = mul i64 %.48, %.20
  %.55 = shl i64 %.53, 4
  %.58 = and i64 %.55, 496
  %.59 = or i64 %.58, %.42
  %.62 = lshr i64 %.53, 3
  %.63 = and i64 %.62, 6
  %.64 = or i64 %.63, 1
  %.68 = lshr i64 %.59, %.64
  %.69 = sub i64 %.40, %.68
  %.71 = xor i64 %.69, %.40
  %1 = xor i64 %.69, -9223372036854775808
  %.74 = and i64 %1, %.40
  %.75 = xor i64 %.71, %.74
  %.78 = icmp eq i64 %.69, 0
  %.75.lobit = lshr i64 %.75, 63
  %.783 = zext i1 %.78 to i64
  %.88 = or i64 %.75.lobit, %.783
  %.103 = icmp eq i64 %.88, 0
  %.145 = add i64 %.53, 916080512
  %.153 = mul i64 %.59, %.145
  br i1 %.103, label %.3.endif.endif.endif.endif.if, label %.3.endif.endif.endif.endif.else

.3.endif.endif.endif.endif.if:                    ; preds = %.3
  %.156 = shl i64 %.19, 2
  %.159 = and i64 %.156, 48
  %.160 = or i64 %.159, %.19
  %.163 = lshr i64 %.160, 3
  %.164 = and i64 %.163, 14
  %.165 = or i64 %.164, 1
  %.166 = sub nsw i64 64, %.165
  %.170 = lshr i64 %.12, %.166
  %.179 = shl i64 %.12, %.165
  %.180 = or i64 %.170, %.179
  br label %.3.endif.endif.endif.endif.endif

.3.endif.endif.endif.endif.else:                  ; preds = %.3
  %.234 = lshr i64 %.53, 35
  %.248 = and i64 %.234, 255
  %.252 = and i64 %.62, 65280
  %.253 = or i64 %.248, %.252
  %.257 = and i64 %.62, 16711680
  %.258 = or i64 %.253, %.257
  %.262 = and i64 %.62, 4278190080
  %.263 = or i64 %.258, %.262
  %2 = shl i64 %.53, 29
  %.272 = and i64 %2, 1095216660480
  %.273 = or i64 %.263, %.272
  %.277 = and i64 %.62, 280375465082880
  %.278 = or i64 %.273, %.277
  %.282 = and i64 %.62, 71776119061217280
  %.283 = or i64 %.278, %.282
  %.284 = lshr i64 %.53, 59
  %.287 = shl nuw nsw i64 %.284, 56
  %.288 = or i64 %.283, %.287
  %.289 = lshr i64 %.20, 59
  %.365 = and i64 %.289, 14
  %.366 = or i64 %.365, 1
  %.367 = sub nsw i64 64, %.366
  %.371 = lshr i64 %.288, %.367
  %.424 = shl i64 %.288, %.366
  %.425 = or i64 %.371, %.424
  br label %.3.endif.endif.endif.endif.endif

.3.endif.endif.endif.endif.endif:                 ; preds = %.3.endif.endif.endif.endif.else, %.3.endif.endif.endif.endif.if
  %.180.sink = phi i64 [ %.180, %.3.endif.endif.endif.endif.if ], [ %.425, %.3.endif.endif.endif.endif.else ]
  %.182 = mul i64 %.153, %.180.sink
  ret i64 %.182
}

attributes #0 = { norecurse nounwind readnone }
