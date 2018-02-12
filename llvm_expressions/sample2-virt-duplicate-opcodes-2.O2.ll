; ModuleID = 'llvm_expressions/sample2-virt-duplicate-opcodes-2.ll'
source_filename = "llvm_expressions/sample2-virt-duplicate-opcodes-2.ll"
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
  %.51 = shl i64 %.30, %.35
  %.52 = or i64 %.40, %.51
  %.53 = shl i64 %.52, 3
  %.56 = and i64 %.53, 120
  %.57 = or i64 %.56, %.9
  %.58 = and i64 %.57, 15
  %.59 = or i64 %.58, 1
  %.60 = sub nsw i64 64, %.59
  %.64 = lshr i64 %.20, %.60
  %.72 = shl i64 %.20, %.59
  %.73 = or i64 %.64, %.72
  %.76 = lshr i64 %.30, 3
  %.77 = and i64 %.76, 14
  %.78 = or i64 %.77, 1
  %.79 = sub nsw i64 64, %.78
  %.83 = lshr i64 %.11, %.79
  %.94 = shl i64 %.11, %.78
  %.95 = or i64 %.83, %.94
  %.96 = sub i64 %.73, %.95
  %.99 = xor i64 %.96, %.73
  %.100 = xor i64 %.73, %.95
  %.101 = and i64 %.99, %.100
  %.98 = xor i64 %.100, %.96
  %.102 = xor i64 %.98, %.101
  %.105 = icmp eq i64 %.96, 0
  %.102.lobit = lshr i64 %.102, 63
  %.1054 = zext i1 %.105 to i64
  %.115 = or i64 %.102.lobit, %.1054
  %.130 = icmp eq i64 %.115, 0
  br i1 %.130, label %.3.endif.endif.endif.endif.if, label %.3.endif.endif.endif.endif.else

.3.endif.endif.endif.endif.if:                    ; preds = %.3
  %.187 = shl nuw nsw i64 %.58, 3
  %.188 = or i64 %.187, %.57
  %.223 = and i64 %.188, 255
  %.283 = and i64 %.9, -256
  %.289 = or i64 %.283, %.223
  %.301 = lshr i64 %SymVar_0, 61
  %.319 = and i64 %.6, 65280
  %.320 = or i64 %.319, %.301
  %.324 = and i64 %.6, 16711680
  %.325 = or i64 %.320, %.324
  %.329 = and i64 %.6, 4278190080
  %.330 = or i64 %.325, %.329
  %.334 = and i64 %.6, 1095216660480
  %.335 = or i64 %.330, %.334
  %.339 = and i64 %.6, 280375465082880
  %.340 = or i64 %.335, %.339
  %.344 = and i64 %.6, 71776119061217280
  %.345 = or i64 %.340, %.344
  %.354 = shl i64 %.20, 56
  %.355 = or i64 %.345, %.354
  %.356 = sub i64 %.289, %.355
  %.357 = or i64 %.356, %.30
  %.358 = shl i64 %.356, 4
  %.361 = and i64 %.358, 1008
  %.384 = or i64 %.361, %.355
  %.409 = lshr i64 %.188, 2
  %.410 = and i64 %.409, 6
  %.411 = or i64 %.410, 1
  %.417 = shl i64 %.384, %.411
  %.418 = add i64 %.417, %.357
  br label %.3.endif.endif.endif.endif.endif

.3.endif.endif.endif.endif.else:                  ; preds = %.3
  %.437 = sub i64 %.20, %.11
  %.438 = shl i64 %.437, 3
  %.441 = and i64 %.438, 248
  %.452 = or i64 %.441, %.30
  %.581 = shl i64 %.57, 4
  %.584 = and i64 %.581, 496
  %.585 = or i64 %.584, %.20
  %.586 = sub i64 %.57, %.585
  %.587 = or i64 %.452, %.586
  %.588 = shl i64 %.586, 4
  %.591 = and i64 %.588, 1008
  %.592 = or i64 %.591, %.585
  %.617 = lshr i64 %.57, 2
  %.618 = and i64 %.617, 6
  %.619 = or i64 %.618, 1
  %.625 = shl i64 %.592, %.619
  %.626 = add i64 %.625, %.587
  br label %.3.endif.endif.endif.endif.endif

.3.endif.endif.endif.endif.endif:                 ; preds = %.3.endif.endif.endif.endif.else, %.3.endif.endif.endif.endif.if
  %.628 = phi i64 [ %.418, %.3.endif.endif.endif.endif.if ], [ %.626, %.3.endif.endif.endif.endif.else ]
  ret i64 %.628
}

attributes #0 = { norecurse nounwind readnone }
