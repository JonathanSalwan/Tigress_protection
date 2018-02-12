; ModuleID = 'llvm_expressions/sample22-virt-max-merge-lenght-10.ll'
source_filename = "llvm_expressions/sample22-virt-max-merge-lenght-10.ll"
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
  %.105 = icmp eq i64 %.90, 0
  %.147 = add i64 %.55, 916080512
  %.155 = mul i64 %.61, %.147
  br i1 %.105, label %.3.endif.endif.endif.endif.if, label %.3.endif.endif.endif.endif.else

.3.endif.endif.endif.endif.if:                    ; preds = %.3
  %.158 = shl i64 %.19, 2
  %.161 = and i64 %.158, 48
  %.162 = or i64 %.161, %.19
  %.165 = lshr i64 %.162, 3
  %.166 = and i64 %.165, 14
  %.167 = or i64 %.166, 1
  %.168 = sub nsw i64 64, %.167
  %.172 = lshr i64 %.12, %.168
  %.183 = shl i64 %.12, %.167
  %.184 = or i64 %.172, %.183
  br label %.3.endif.endif.endif.endif.endif

.3.endif.endif.endif.endif.else:                  ; preds = %.3
  %.238 = lshr i64 %.55, 35
  %.252 = and i64 %.238, 255
  %.256 = and i64 %.64, 65280
  %.257 = or i64 %.252, %.256
  %.261 = and i64 %.64, 16711680
  %.262 = or i64 %.257, %.261
  %.266 = and i64 %.64, 4278190080
  %.267 = or i64 %.262, %.266
  %2 = shl i64 %.55, 29
  %.276 = and i64 %2, 1095216660480
  %.277 = or i64 %.267, %.276
  %.281 = and i64 %.64, 280375465082880
  %.282 = or i64 %.277, %.281
  %.286 = and i64 %.64, 71776119061217280
  %.287 = or i64 %.282, %.286
  %.288 = lshr i64 %.55, 59
  %.291 = shl nuw nsw i64 %.288, 56
  %.292 = or i64 %.287, %.291
  %.293 = lshr i64 %.20, 59
  %.369 = and i64 %.293, 14
  %.370 = or i64 %.369, 1
  %.371 = sub nsw i64 64, %.370
  %.375 = lshr i64 %.292, %.371
  %.430 = shl i64 %.292, %.370
  %.431 = or i64 %.375, %.430
  br label %.3.endif.endif.endif.endif.endif

.3.endif.endif.endif.endif.endif:                 ; preds = %.3.endif.endif.endif.endif.else, %.3.endif.endif.endif.endif.if
  %.184.sink = phi i64 [ %.184, %.3.endif.endif.endif.endif.if ], [ %.431, %.3.endif.endif.endif.endif.else ]
  %.186 = mul i64 %.155, %.184.sink
  ret i64 %.186
}

attributes #0 = { norecurse nounwind readnone }
