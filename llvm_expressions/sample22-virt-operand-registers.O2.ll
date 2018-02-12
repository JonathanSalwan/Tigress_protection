; ModuleID = 'llvm_expressions/sample22-virt-operand-registers.ll'
source_filename = "llvm_expressions/sample22-virt-operand-registers.ll"
target datalayout = "e-m:e-i64:64-f80:128-n8:16:32:64-S128"
target triple = "x86_64-pc-linux-gnu"

; Function Attrs: norecurse nounwind readnone
define i64 @SECRET(i64 %SymVar_0) local_unnamed_addr #0 {
.3:
  %.4 = shl i64 %SymVar_0, 9
  %.11 = lshr i64 %SymVar_0, 55
  %.7 = or i64 %.11, %.4
  %.12 = or i64 %.7, 250589732864
  %.15 = shl i64 %.12, 13
  %0 = lshr i64 %SymVar_0, 42
  %.18 = and i64 %0, 8191
  %.19 = or i64 %.18, %SymVar_0
  %.20 = or i64 %.19, %.15
  %.23 = lshr i64 %.19, 1
  %.24 = and i64 %.23, 14
  %.25 = or i64 %.24, 1
  %.31 = shl i64 %.12, %.25
  %.37 = sub nsw i64 64, %.25
  %.43 = lshr i64 %.12, %.37
  %.44 = or i64 %.43, %.31
  %.45 = add i64 %SymVar_0, 104868834
  %.46 = or i64 %SymVar_0, 893657663
  %.51 = mul i64 %.45, 1004737041
  %.54 = mul i64 %.51, %.46
  %.57 = mul i64 %.54, %.20
  %.59 = shl i64 %.57, 4
  %.62 = and i64 %.59, 496
  %.63 = or i64 %.62, %.45
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
  br i1 %.109, label %.3.endif.endif.endif.endif.if, label %.3.endif.endif.endif.endif.else

.3.endif.endif.endif.endif.if:                    ; preds = %.3
  %.137 = shl i64 %.19, 2
  %.140 = and i64 %.137, 48
  %.141 = or i64 %.140, %.19
  %.144 = lshr i64 %.141, 3
  %.145 = and i64 %.144, 14
  %.146 = or i64 %.145, 1
  %.152 = shl i64 %.12, %.146
  %.158 = sub nsw i64 64, %.146
  %.164 = lshr i64 %.12, %.158
  %.165 = or i64 %.164, %.152
  %.187 = add i64 %.57, 916080512
  %.189 = mul i64 %.63, %.187
  %.192 = mul i64 %.189, %.165
  br label %.3.endif.endif.endif.endif.endif

.3.endif.endif.endif.endif.else:                  ; preds = %.3
  %.233 = lshr i64 %.57, 35
  %.247 = and i64 %.233, 255
  %.251 = and i64 %.66, 65280
  %.252 = or i64 %.247, %.251
  %.256 = and i64 %.66, 16711680
  %.257 = or i64 %.252, %.256
  %.261 = and i64 %.66, 4278190080
  %.262 = or i64 %.257, %.261
  %2 = shl i64 %.57, 29
  %.271 = and i64 %2, 1095216660480
  %.272 = or i64 %.262, %.271
  %.276 = and i64 %.66, 280375465082880
  %.277 = or i64 %.272, %.276
  %.281 = and i64 %.66, 71776119061217280
  %.282 = or i64 %.277, %.281
  %.283 = lshr i64 %.57, 59
  %.286 = shl nuw nsw i64 %.283, 56
  %.287 = or i64 %.282, %.286
  %.288 = lshr i64 %.20, 59
  %.364 = and i64 %.288, 14
  %.365 = or i64 %.364, 1
  %.371 = shl i64 %.287, %.365
  %.421 = sub nsw i64 64, %.365
  %.427 = lshr i64 %.287, %.421
  %.428 = or i64 %.371, %.427
  %.436 = add i64 %.57, 916080512
  %.438 = mul i64 %.63, %.436
  %.441 = mul i64 %.438, %.428
  br label %.3.endif.endif.endif.endif.endif

.3.endif.endif.endif.endif.endif:                 ; preds = %.3.endif.endif.endif.endif.else, %.3.endif.endif.endif.endif.if
  %.192.sink.off0 = phi i64 [ %.192, %.3.endif.endif.endif.endif.if ], [ %.441, %.3.endif.endif.endif.endif.else ]
  ret i64 %.192.sink.off0
}

attributes #0 = { norecurse nounwind readnone }
