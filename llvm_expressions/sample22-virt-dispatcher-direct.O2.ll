; ModuleID = 'llvm_expressions/sample22-virt-dispatcher-direct.ll'
source_filename = "llvm_expressions/sample22-virt-dispatcher-direct.ll"
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
  %.112 = icmp eq i64 %.92, 0
  %.149 = add i64 %.55, 916080512
  %.157 = mul i64 %.61, %.149
  br i1 %.112, label %.3.endif.endif.endif.endif.else, label %.3.endif.endif.endif.endif.if

.3.endif.endif.endif.endif.if:                    ; preds = %.3
  %.167 = lshr i64 %.55, 35
  %.181 = and i64 %.167, 255
  %.185 = and i64 %.64, 65280
  %.186 = or i64 %.181, %.185
  %.190 = and i64 %.64, 16711680
  %.191 = or i64 %.186, %.190
  %.195 = and i64 %.64, 4278190080
  %.196 = or i64 %.191, %.195
  %2 = shl i64 %.55, 29
  %.205 = and i64 %2, 1095216660480
  %.206 = or i64 %.196, %.205
  %.210 = and i64 %.64, 280375465082880
  %.211 = or i64 %.206, %.210
  %.215 = and i64 %.64, 71776119061217280
  %.216 = or i64 %.211, %.215
  %.217 = lshr i64 %.55, 59
  %.220 = shl nuw nsw i64 %.217, 56
  %.221 = or i64 %.216, %.220
  %.222 = lshr i64 %.20, 59
  %.298 = and i64 %.222, 14
  %.299 = or i64 %.298, 1
  %.300 = sub nsw i64 64, %.299
  %.306 = lshr i64 %.221, %.300
  %.359 = shl i64 %.221, %.299
  %.360 = or i64 %.306, %.359
  br label %.3.endif.endif.endif.endif.endif

.3.endif.endif.endif.endif.else:                  ; preds = %.3
  %.407 = shl i64 %.19, 2
  %.410 = and i64 %.407, 48
  %.411 = or i64 %.410, %.19
  %.414 = lshr i64 %.411, 3
  %.415 = and i64 %.414, 14
  %.416 = or i64 %.415, 1
  %.417 = sub nsw i64 64, %.416
  %.423 = lshr i64 %.12, %.417
  %.432 = shl i64 %.12, %.416
  %.433 = or i64 %.423, %.432
  br label %.3.endif.endif.endif.endif.endif

.3.endif.endif.endif.endif.endif:                 ; preds = %.3.endif.endif.endif.endif.else, %.3.endif.endif.endif.endif.if
  %.360.sink = phi i64 [ %.360, %.3.endif.endif.endif.endif.if ], [ %.433, %.3.endif.endif.endif.endif.else ]
  %.362 = mul i64 %.157, %.360.sink
  ret i64 %.362
}

attributes #0 = { norecurse nounwind readnone }
