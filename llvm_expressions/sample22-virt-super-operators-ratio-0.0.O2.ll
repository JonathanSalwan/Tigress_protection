; ModuleID = 'llvm_expressions/sample22-virt-super-operators-ratio-0.0.ll'
source_filename = "llvm_expressions/sample22-virt-super-operators-ratio-0.0.ll"
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
  %.41 = shl i64 %.12, %.25
  %.42 = or i64 %.32, %.41
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
  %.72 = lshr i64 %.61, %.66
  %.73 = sub i64 %.42, %.72
  %.75 = xor i64 %.73, %.42
  %1 = xor i64 %.73, -9223372036854775808
  %.78 = and i64 %1, %.42
  %.79 = xor i64 %.75, %.78
  %.82 = icmp eq i64 %.73, 0
  %.79.lobit = lshr i64 %.79, 63
  %.823 = zext i1 %.82 to i64
  %.92 = or i64 %.79.lobit, %.823
  %.107 = icmp eq i64 %.92, 0
  %.149 = add i64 %.55, 916080512
  %.157 = mul i64 %.61, %.149
  br i1 %.107, label %.3.endif.endif.endif.endif.if, label %.3.endif.endif.endif.endif.else

.3.endif.endif.endif.endif.if:                    ; preds = %.3
  %.160 = shl i64 %.19, 2
  %.163 = and i64 %.160, 48
  %.164 = or i64 %.163, %.19
  %.167 = lshr i64 %.164, 3
  %.168 = and i64 %.167, 14
  %.169 = or i64 %.168, 1
  %.170 = sub nsw i64 64, %.169
  %.176 = lshr i64 %.12, %.170
  %.185 = shl i64 %.12, %.169
  %.186 = or i64 %.176, %.185
  br label %.3.endif.endif.endif.endif.endif

.3.endif.endif.endif.endif.else:                  ; preds = %.3
  %.240 = lshr i64 %.55, 35
  %.254 = and i64 %.240, 255
  %.258 = and i64 %.64, 65280
  %.259 = or i64 %.254, %.258
  %.263 = and i64 %.64, 16711680
  %.264 = or i64 %.259, %.263
  %.268 = and i64 %.64, 4278190080
  %.269 = or i64 %.264, %.268
  %2 = shl i64 %.55, 29
  %.278 = and i64 %2, 1095216660480
  %.279 = or i64 %.269, %.278
  %.283 = and i64 %.64, 280375465082880
  %.284 = or i64 %.279, %.283
  %.288 = and i64 %.64, 71776119061217280
  %.289 = or i64 %.284, %.288
  %.290 = lshr i64 %.55, 59
  %.293 = shl nuw nsw i64 %.290, 56
  %.294 = or i64 %.289, %.293
  %.295 = lshr i64 %.20, 59
  %.371 = and i64 %.295, 14
  %.372 = or i64 %.371, 1
  %.373 = sub nsw i64 64, %.372
  %.379 = lshr i64 %.294, %.373
  %.432 = shl i64 %.294, %.372
  %.433 = or i64 %.379, %.432
  br label %.3.endif.endif.endif.endif.endif

.3.endif.endif.endif.endif.endif:                 ; preds = %.3.endif.endif.endif.endif.else, %.3.endif.endif.endif.endif.if
  %.186.sink = phi i64 [ %.186, %.3.endif.endif.endif.endif.if ], [ %.433, %.3.endif.endif.endif.endif.else ]
  %.188 = mul i64 %.157, %.186.sink
  ret i64 %.188
}

attributes #0 = { norecurse nounwind readnone }
