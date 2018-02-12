; ModuleID = 'llvm_expressions/sample22-virt-bogus-functions-3.ll'
source_filename = "llvm_expressions/sample22-virt-bogus-functions-3.ll"
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
  %.32 = lshr i64 %.12, %.26
  %.43 = shl i64 %.12, %.25
  %.44 = or i64 %.32, %.43
  %.46 = add i64 %SymVar_0, 104868834
  %.55 = or i64 %SymVar_0, 893657663
  %.48 = mul i64 %.46, 1004737041
  %.52 = mul i64 %.48, %.55
  %.57 = mul i64 %.52, %.20
  %.59 = shl i64 %.57, 4
  %.62 = and i64 %.59, 496
  %.63 = or i64 %.62, %.46
  %.66 = lshr i64 %.57, 3
  %.67 = and i64 %.66, 6
  %.68 = or i64 %.67, 1
  %.74 = lshr i64 %.63, %.68
  %.75 = sub i64 %.44, %.74
  %.77 = xor i64 %.75, %.44
  %1 = xor i64 %.75, -9223372036854775808
  %.80 = and i64 %1, %.44
  %.81 = xor i64 %.77, %.80
  %.84 = icmp eq i64 %.75, 0
  %.81.lobit = lshr i64 %.81, 63
  %.843 = zext i1 %.84 to i64
  %.94 = or i64 %.81.lobit, %.843
  %.109 = icmp eq i64 %.94, 0
  %.151 = add i64 %.57, 916080512
  %.159 = mul i64 %.63, %.151
  br i1 %.109, label %.3.endif.endif.endif.endif.if, label %.3.endif.endif.endif.endif.else

.3.endif.endif.endif.endif.if:                    ; preds = %.3
  %.162 = shl i64 %.19, 2
  %.165 = and i64 %.162, 48
  %.166 = or i64 %.165, %.19
  %.169 = lshr i64 %.166, 3
  %.170 = and i64 %.169, 14
  %.171 = or i64 %.170, 1
  %.172 = sub nsw i64 64, %.171
  %.178 = lshr i64 %.12, %.172
  %.189 = shl i64 %.12, %.171
  %.190 = or i64 %.178, %.189
  br label %.3.endif.endif.endif.endif.endif

.3.endif.endif.endif.endif.else:                  ; preds = %.3
  %.244 = lshr i64 %.57, 35
  %.258 = and i64 %.244, 255
  %.262 = and i64 %.66, 65280
  %.263 = or i64 %.258, %.262
  %.267 = and i64 %.66, 16711680
  %.268 = or i64 %.263, %.267
  %.272 = and i64 %.66, 4278190080
  %.273 = or i64 %.268, %.272
  %2 = shl i64 %.57, 29
  %.282 = and i64 %2, 1095216660480
  %.283 = or i64 %.273, %.282
  %.287 = and i64 %.66, 280375465082880
  %.288 = or i64 %.283, %.287
  %.292 = and i64 %.66, 71776119061217280
  %.293 = or i64 %.288, %.292
  %.294 = lshr i64 %.57, 59
  %.297 = shl nuw nsw i64 %.294, 56
  %.298 = or i64 %.293, %.297
  %.299 = lshr i64 %.20, 59
  %.375 = and i64 %.299, 14
  %.376 = or i64 %.375, 1
  %.377 = sub nsw i64 64, %.376
  %.383 = lshr i64 %.298, %.377
  %.438 = shl i64 %.298, %.376
  %.439 = or i64 %.383, %.438
  br label %.3.endif.endif.endif.endif.endif

.3.endif.endif.endif.endif.endif:                 ; preds = %.3.endif.endif.endif.endif.else, %.3.endif.endif.endif.endif.if
  %.190.sink = phi i64 [ %.190, %.3.endif.endif.endif.endif.if ], [ %.439, %.3.endif.endif.endif.endif.else ]
  %.192 = mul i64 %.159, %.190.sink
  ret i64 %.192
}

attributes #0 = { norecurse nounwind readnone }
