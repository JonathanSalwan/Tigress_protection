; ModuleID = 'llvm_expressions/sample2-virt-max-merge-lenght-20.ll'
source_filename = "llvm_expressions/sample2-virt-max-merge-lenght-20.ll"
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
  %.42 = lshr i64 %.32, %.38
  %.51 = shl i64 %.32, %.37
  %.52 = or i64 %.42, %.51
  %.53 = shl i64 %.52, 3
  %.56 = and i64 %.53, 120
  %.57 = or i64 %.56, %.9
  %.58 = and i64 %.57, 15
  %.59 = or i64 %.58, 1
  %.60 = sub nsw i64 64, %.59
  %.64 = lshr i64 %.20, %.60
  %.70 = shl i64 %.20, %.59
  %.71 = or i64 %.64, %.70
  %.74 = lshr i64 %.32, 3
  %.75 = and i64 %.74, 14
  %.76 = or i64 %.75, 1
  %.77 = sub nsw i64 64, %.76
  %.81 = lshr i64 %.11, %.77
  %.90 = shl i64 %.11, %.76
  %.91 = or i64 %.81, %.90
  %.92 = sub i64 %.71, %.91
  %.95 = xor i64 %.92, %.71
  %.96 = xor i64 %.71, %.91
  %.97 = and i64 %.95, %.96
  %.94 = xor i64 %.96, %.92
  %.98 = xor i64 %.94, %.97
  %.101 = icmp eq i64 %.92, 0
  %.98.lobit = lshr i64 %.98, 63
  %.1014 = zext i1 %.101 to i64
  %.111 = or i64 %.98.lobit, %.1014
  %.126 = icmp eq i64 %.111, 0
  br i1 %.126, label %.3.endif.endif.endif.endif.if, label %.3.endif.endif.endif.endif.else

.3.endif.endif.endif.endif.if:                    ; preds = %.3
  %.183 = shl nuw nsw i64 %.58, 3
  %.184 = or i64 %.183, %.57
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
  %.353 = or i64 %.352, %.32
  %.354 = shl i64 %.352, 4
  %.357 = and i64 %.354, 1008
  %.380 = or i64 %.357, %.351
  %.405 = lshr i64 %.184, 2
  %.406 = and i64 %.405, 6
  %.407 = or i64 %.406, 1
  %.411 = shl i64 %.380, %.407
  %.412 = add i64 %.411, %.353
  br label %.3.endif.endif.endif.endif.endif

.3.endif.endif.endif.endif.else:                  ; preds = %.3
  %.431 = sub i64 %.20, %.11
  %.432 = shl i64 %.431, 3
  %.435 = and i64 %.432, 248
  %.448 = or i64 %.435, %.32
  %.575 = shl i64 %.57, 4
  %.578 = and i64 %.575, 496
  %.579 = or i64 %.578, %.20
  %.580 = sub i64 %.57, %.579
  %.581 = or i64 %.448, %.580
  %.582 = shl i64 %.580, 4
  %.585 = and i64 %.582, 1008
  %.586 = or i64 %.585, %.579
  %.611 = lshr i64 %.57, 2
  %.612 = and i64 %.611, 6
  %.613 = or i64 %.612, 1
  %.617 = shl i64 %.586, %.613
  %.618 = add i64 %.617, %.581
  br label %.3.endif.endif.endif.endif.endif

.3.endif.endif.endif.endif.endif:                 ; preds = %.3.endif.endif.endif.endif.else, %.3.endif.endif.endif.endif.if
  %.620 = phi i64 [ %.412, %.3.endif.endif.endif.endif.if ], [ %.618, %.3.endif.endif.endif.endif.else ]
  ret i64 %.620
}

attributes #0 = { norecurse nounwind readnone }
