; ModuleID = 'llvm_expressions/sample22-virt-nested-vm-2.ll'
source_filename = "llvm_expressions/sample22-virt-nested-vm-2.ll"
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
  %.41 = shl i64 %.12, %.25
  %.42 = or i64 %.30, %.41
  %.44 = add i64 %SymVar_0, 104868834
  %.53 = or i64 %SymVar_0, 893657663
  %.46 = mul i64 %.44, 1004737041
  %.50 = mul i64 %.46, %.53
  %.55 = mul i64 %.50, %.20
  %.57 = shl i64 %.55, 4
  %.60 = and i64 %.57, 496
  %.61 = or i64 %.60, %.44
  %.64 = lshr i64 %.55, 3
  %.65 = and i64 %.64, 6
  %.66 = or i64 %.65, 1
  %.70 = lshr i64 %.61, %.66
  %.71 = sub i64 %.42, %.70
  %.73 = xor i64 %.71, %.42
  %1 = xor i64 %.71, -9223372036854775808
  %.76 = and i64 %1, %.42
  %.77 = xor i64 %.73, %.76
  %.80 = icmp eq i64 %.71, 0
  %.77.lobit = lshr i64 %.77, 63
  %.803 = zext i1 %.80 to i64
  %.90 = or i64 %.77.lobit, %.803
  %.109 = icmp eq i64 %.90, 0
  %.151 = add i64 %.55, 916080512
  %.159 = mul i64 %.61, %.151
  br i1 %.109, label %.3.endif.endif.endif.endif.if, label %.3.endif.endif.endif.endif.else

.3.endif.endif.endif.endif.if:                    ; preds = %.3
  %.162 = shl i64 %.19, 2
  %.165 = and i64 %.162, 48
  %.166 = or i64 %.165, %.19
  %.169 = lshr i64 %.166, 3
  %.170 = and i64 %.169, 14
  %.171 = or i64 %.170, 1
  %.172 = sub nsw i64 64, %.171
  %.176 = lshr i64 %.12, %.172
  %.187 = shl i64 %.12, %.171
  %.188 = or i64 %.176, %.187
  br label %.3.endif.endif.endif.endif.endif

.3.endif.endif.endif.endif.else:                  ; preds = %.3
  %.242 = lshr i64 %.55, 35
  %.268 = and i64 %.242, 255
  %.272 = and i64 %.64, 65280
  %.273 = or i64 %.268, %.272
  %.277 = and i64 %.64, 16711680
  %.278 = or i64 %.273, %.277
  %.282 = and i64 %.64, 4278190080
  %.283 = or i64 %.278, %.282
  %2 = shl i64 %.55, 29
  %.298 = and i64 %2, 1095216660480
  %.299 = or i64 %.283, %.298
  %.303 = and i64 %.64, 280375465082880
  %.304 = or i64 %.299, %.303
  %.308 = and i64 %.64, 71776119061217280
  %.309 = or i64 %.304, %.308
  %.310 = lshr i64 %.55, 59
  %.313 = shl nuw nsw i64 %.310, 56
  %.314 = or i64 %.309, %.313
  %.315 = lshr i64 %.20, 59
  %.427 = and i64 %.315, 14
  %.428 = or i64 %.427, 1
  %.429 = sub nsw i64 64, %.428
  %.433 = lshr i64 %.314, %.429
  %.488 = shl i64 %.314, %.428
  %.489 = or i64 %.433, %.488
  br label %.3.endif.endif.endif.endif.endif

.3.endif.endif.endif.endif.endif:                 ; preds = %.3.endif.endif.endif.endif.else, %.3.endif.endif.endif.endif.if
  %.188.sink = phi i64 [ %.188, %.3.endif.endif.endif.endif.if ], [ %.489, %.3.endif.endif.endif.endif.else ]
  %.190 = mul i64 %.159, %.188.sink
  ret i64 %.190
}

attributes #0 = { norecurse nounwind readnone }
