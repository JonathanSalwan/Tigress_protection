; ModuleID = 'llvm_expressions/sample2-virt-dispatcher-indirect.ll'
source_filename = "llvm_expressions/sample2-virt-dispatcher-indirect.ll"
target datalayout = "e-m:e-i64:64-f80:128-n8:16:32:64-S128"
target triple = "x86_64-pc-linux-gnu"

; Function Attrs: norecurse nounwind readnone
define i64 @SECRET(i64 %SymVar_0) local_unnamed_addr #0 {
.3:
  %.6 = lshr i64 %SymVar_0, 5
  %.7 = xor i64 %.6, 810798164723513605
  %.8 = add i64 %SymVar_0, -275339905
  %.9 = add i64 %.8, %.7
  %.10 = add i64 %.6, %SymVar_0
  %.11 = add i64 %.10, %.9
  %.14 = shl nuw nsw i64 %.6, 2
  %.16 = mul i64 %.14, %.11
  %.19 = and i64 %.16, 28
  %.20 = or i64 %.19, %.6
  %.23 = mul i64 %.6, 1015975030
  %.25 = and i64 %.23, 6
  %.26 = or i64 %.25, 1
  %.32 = lshr i64 %SymVar_0, %.26
  %.35 = lshr i64 %.9, 4
  %.36 = and i64 %.35, 14
  %.37 = or i64 %.36, 1
  %.38 = sub nsw i64 64, %.37
  %.44 = lshr i64 %.32, %.38
  %.53 = shl i64 %.32, %.37
  %.54 = or i64 %.44, %.53
  %.55 = shl i64 %.54, 3
  %.58 = and i64 %.55, 120
  %.59 = or i64 %.58, %.9
  %.60 = and i64 %.59, 15
  %.61 = or i64 %.60, 1
  %.62 = sub nsw i64 64, %.61
  %.68 = lshr i64 %.20, %.62
  %.74 = shl i64 %.20, %.61
  %.75 = or i64 %.68, %.74
  %.78 = lshr i64 %.32, 3
  %.79 = and i64 %.78, 14
  %.80 = or i64 %.79, 1
  %.81 = sub nsw i64 64, %.80
  %.87 = lshr i64 %.11, %.81
  %.96 = shl i64 %.11, %.80
  %.97 = or i64 %.87, %.96
  %.98 = sub i64 %.75, %.97
  %.101 = xor i64 %.98, %.75
  %.102 = xor i64 %.75, %.97
  %.103 = and i64 %.101, %.102
  %.100 = xor i64 %.102, %.98
  %.104 = xor i64 %.100, %.103
  %.107 = icmp eq i64 %.98, 0
  %.104.lobit = lshr i64 %.104, 63
  %.1075 = zext i1 %.107 to i64
  %.117 = or i64 %.104.lobit, %.1075
  %.137 = icmp eq i64 %.117, 0
  br i1 %.137, label %.3.endif.endif.endif.endif.else, label %.3.endif.endif.endif.endif.if

.3.endif.endif.endif.endif.if:                    ; preds = %.3
  %.160 = sub i64 %.20, %.11
  %.161 = shl i64 %.160, 3
  %.164 = and i64 %.161, 248
  %.177 = or i64 %.164, %.32
  %.306 = shl i64 %.59, 4
  %.309 = and i64 %.306, 496
  %.310 = or i64 %.309, %.20
  %.311 = sub i64 %.59, %.310
  %.312 = or i64 %.177, %.311
  %.313 = shl i64 %.311, 4
  %.316 = and i64 %.313, 1008
  %.317 = or i64 %.316, %.310
  %.342 = lshr i64 %.59, 2
  %.343 = and i64 %.342, 6
  %.344 = or i64 %.343, 1
  %.348 = shl i64 %.317, %.344
  %.349 = add i64 %.348, %.312
  br label %.3.endif.endif.endif.endif.endif

.3.endif.endif.endif.endif.else:                  ; preds = %.3
  %.399 = shl nuw nsw i64 %.60, 3
  %.400 = or i64 %.399, %.59
  %.435 = and i64 %.400, 255
  %.495 = and i64 %.9, -256
  %.501 = or i64 %.495, %.435
  %.513 = lshr i64 %SymVar_0, 61
  %.531 = and i64 %.6, 65280
  %.532 = or i64 %.531, %.513
  %.536 = and i64 %.6, 16711680
  %.537 = or i64 %.532, %.536
  %.541 = and i64 %.6, 4278190080
  %.542 = or i64 %.537, %.541
  %.546 = and i64 %.6, 1095216660480
  %.547 = or i64 %.542, %.546
  %.551 = and i64 %.6, 280375465082880
  %.552 = or i64 %.547, %.551
  %.556 = and i64 %.6, 71776119061217280
  %.557 = or i64 %.552, %.556
  %.566 = shl i64 %.20, 56
  %.567 = or i64 %.557, %.566
  %.568 = sub i64 %.501, %.567
  %.569 = or i64 %.568, %.32
  %.570 = shl i64 %.568, 4
  %.573 = and i64 %.570, 1008
  %.596 = or i64 %.573, %.567
  %.621 = lshr i64 %.400, 2
  %.622 = and i64 %.621, 6
  %.623 = or i64 %.622, 1
  %.627 = shl i64 %.596, %.623
  %.628 = add i64 %.627, %.569
  br label %.3.endif.endif.endif.endif.endif

.3.endif.endif.endif.endif.endif:                 ; preds = %.3.endif.endif.endif.endif.else, %.3.endif.endif.endif.endif.if
  %.630 = phi i64 [ %.349, %.3.endif.endif.endif.endif.if ], [ %.628, %.3.endif.endif.endif.endif.else ]
  ret i64 %.630
}

attributes #0 = { norecurse nounwind readnone }
