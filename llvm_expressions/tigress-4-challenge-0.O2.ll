; ModuleID = 'llvm_expressions/tigress-4-challenge-0.ll'
source_filename = "llvm_expressions/tigress-4-challenge-0.ll"
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
  %.26 = sub nsw i64 0, %.25
  %.31 = and i64 %.26, 63
  %.32 = lshr i64 %.12, %.31
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
  %1 = and i64 %.66, 6
  %.69 = or i64 %1, 1
  %.74 = lshr i64 %.63, %.69
  %.75 = sub i64 %.44, %.74
  %.78 = xor i64 %.75, %.44
  %.79 = xor i64 %.74, %.44
  %.80 = and i64 %.78, %.79
  %.77 = xor i64 %.79, %.75
  %.81 = xor i64 %.77, %.80
  %.82 = lshr i64 %.81, 63
  %.84 = icmp eq i64 %.75, 0
  %.843 = zext i1 %.84 to i64
  %.94 = or i64 %.82, %.843
  %.113 = icmp eq i64 %.94, 0
  %.155 = add i64 %.57, 916080512
  %.163 = mul i64 %.63, %.155
  br i1 %.113, label %.3.endif.endif.endif.endif.if, label %.3.endif.endif.endif.endif.else

.3.endif.endif.endif.endif.if:                    ; preds = %.3
  %.166 = shl i64 %.19, 2
  %.169 = and i64 %.166, 60
  %.170 = or i64 %.169, %.20
  %.173 = lshr i64 %.170, 3
  br label %.3.endif.endif.endif.endif.endif

.3.endif.endif.endif.endif.else:                  ; preds = %.3
  %.270 = lshr i64 %.57, 35
  %.296 = and i64 %.270, 255
  %.300 = and i64 %.66, 65280
  %.301 = or i64 %.296, %.300
  %.305 = and i64 %.66, 16711680
  %.306 = or i64 %.301, %.305
  %.310 = and i64 %.66, 4278190080
  %.311 = or i64 %.306, %.310
  %2 = shl i64 %.57, 29
  %.326 = and i64 %2, 1095216660480
  %.327 = or i64 %.311, %.326
  %.331 = and i64 %.66, 280375465082880
  %.332 = or i64 %.327, %.331
  %.336 = and i64 %.66, 71776119061217280
  %.337 = or i64 %.332, %.336
  %.338 = lshr i64 %.57, 59
  %.341 = shl nuw nsw i64 %.338, 56
  %.342 = or i64 %.337, %.341
  %.343 = lshr i64 %.20, 56
  %.372 = and i64 %.20, 65280
  %.374 = or i64 %.343, %.372
  %.394 = and i64 %.20, 4278190080
  %.399 = and i64 %.20, 1095216660480
  %.433 = and i64 %.20, 71776119061217280
  %.450 = shl i64 %.19, 56
  %.391 = or i64 %.374, %.394
  %.396 = or i64 %.391, %.399
  %.401 = or i64 %.396, %.433
  %.451 = or i64 %.401, %.450
  %.454 = lshr i64 %.20, 59
  br label %.3.endif.endif.endif.endif.endif

.3.endif.endif.endif.endif.endif:                 ; preds = %.3.endif.endif.endif.endif.else, %.3.endif.endif.endif.endif.if
  %.454.sink = phi i64 [ %.454, %.3.endif.endif.endif.endif.else ], [ %.173, %.3.endif.endif.endif.endif.if ]
  %.342.sink = phi i64 [ %.342, %.3.endif.endif.endif.endif.else ], [ %.12, %.3.endif.endif.endif.endif.if ]
  %.507.sink = phi i64 [ %.451, %.3.endif.endif.endif.endif.else ], [ %.170, %.3.endif.endif.endif.endif.if ]
  %.455 = and i64 %.454.sink, 14
  %.456 = or i64 %.455, 1
  %.457 = sub nsw i64 0, %.456
  %.462 = and i64 %.457, 63
  %.463 = lshr i64 %.342.sink, %.462
  %.510 = lshr i64 %.507.sink, 3
  %3 = and i64 %.510, 14
  %.513 = or i64 %3, 1
  %.518 = shl i64 %.342.sink, %.513
  %.519 = or i64 %.518, %.463
  %.521 = mul i64 %.163, %.519
  ret i64 %.521
}

attributes #0 = { norecurse nounwind readnone }
