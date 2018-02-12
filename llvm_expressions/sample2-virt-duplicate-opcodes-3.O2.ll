; ModuleID = 'llvm_expressions/sample2-virt-duplicate-opcodes-3.ll'
source_filename = "llvm_expressions/sample2-virt-duplicate-opcodes-3.ll"
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
  %.30 = lshr i64 %SymVar_0, %.26
  %.33 = lshr i64 %.9, 4
  %.34 = and i64 %.33, 14
  %.35 = or i64 %.34, 1
  %.36 = sub nsw i64 64, %.35
  %.40 = lshr i64 %.30, %.36
  %.49 = shl i64 %.30, %.35
  %.50 = or i64 %.40, %.49
  %.51 = shl i64 %.50, 3
  %.54 = and i64 %.51, 120
  %.55 = or i64 %.54, %.9
  %.56 = and i64 %.55, 15
  %.57 = or i64 %.56, 1
  %.58 = sub nsw i64 64, %.57
  %.62 = lshr i64 %.20, %.58
  %.70 = shl i64 %.20, %.57
  %.71 = or i64 %.62, %.70
  %.74 = lshr i64 %.30, 3
  %.75 = and i64 %.74, 14
  %.76 = or i64 %.75, 1
  %.77 = sub nsw i64 64, %.76
  %.81 = lshr i64 %.11, %.77
  %.92 = shl i64 %.11, %.76
  %.93 = or i64 %.81, %.92
  %.94 = sub i64 %.71, %.93
  %.97 = xor i64 %.94, %.71
  %.98 = xor i64 %.71, %.93
  %.99 = and i64 %.97, %.98
  %.96 = xor i64 %.98, %.94
  %.100 = xor i64 %.96, %.99
  %.103 = icmp eq i64 %.94, 0
  %.100.lobit = lshr i64 %.100, 63
  %.1034 = zext i1 %.103 to i64
  %.113 = or i64 %.100.lobit, %.1034
  %.128 = icmp eq i64 %.113, 0
  br i1 %.128, label %.3.endif.endif.endif.endif.if, label %.3.endif.endif.endif.endif.else

.3.endif.endif.endif.endif.if:                    ; preds = %.3
  %.183 = shl nuw nsw i64 %.56, 3
  %.184 = or i64 %.183, %.55
  %.219 = and i64 %.184, 255
  %.279 = and i64 %.9, -256
  %.285 = or i64 %.279, %.219
  %.297 = lshr i64 %SymVar_0, 61
  %.315 = and i64 %.6, 65280
  %.316 = or i64 %.315, %.297
  %.320 = and i64 %.6, 16711680
  %.321 = or i64 %.316, %.320
  %.325 = and i64 %.6, 4278190080
  %.326 = or i64 %.321, %.325
  %.330 = and i64 %.6, 1095216660480
  %.331 = or i64 %.326, %.330
  %.335 = and i64 %.6, 280375465082880
  %.336 = or i64 %.331, %.335
  %.340 = and i64 %.6, 71776119061217280
  %.341 = or i64 %.336, %.340
  %.350 = shl i64 %.20, 56
  %.351 = or i64 %.341, %.350
  %.352 = sub i64 %.285, %.351
  %.353 = or i64 %.352, %.30
  %.354 = shl i64 %.352, 4
  %.357 = and i64 %.354, 1008
  %.380 = or i64 %.357, %.351
  %.405 = lshr i64 %.184, 2
  %.406 = and i64 %.405, 6
  %.407 = or i64 %.406, 1
  %.413 = shl i64 %.380, %.407
  %.414 = add i64 %.413, %.353
  br label %.3.endif.endif.endif.endif.endif

.3.endif.endif.endif.endif.else:                  ; preds = %.3
  %.433 = sub i64 %.20, %.11
  %.434 = shl i64 %.433, 3
  %.437 = and i64 %.434, 248
  %.448 = or i64 %.437, %.30
  %.575 = shl i64 %.55, 4
  %.578 = and i64 %.575, 496
  %.579 = or i64 %.578, %.20
  %.580 = sub i64 %.55, %.579
  %.581 = or i64 %.448, %.580
  %.582 = shl i64 %.580, 4
  %.585 = and i64 %.582, 1008
  %.586 = or i64 %.585, %.579
  %.611 = lshr i64 %.55, 2
  %.612 = and i64 %.611, 6
  %.613 = or i64 %.612, 1
  %.619 = shl i64 %.586, %.613
  %.620 = add i64 %.619, %.581
  br label %.3.endif.endif.endif.endif.endif

.3.endif.endif.endif.endif.endif:                 ; preds = %.3.endif.endif.endif.endif.else, %.3.endif.endif.endif.endif.if
  %.622 = phi i64 [ %.414, %.3.endif.endif.endif.endif.if ], [ %.620, %.3.endif.endif.endif.endif.else ]
  ret i64 %.622
}

attributes #0 = { norecurse nounwind readnone }
