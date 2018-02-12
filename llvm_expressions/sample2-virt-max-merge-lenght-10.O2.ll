; ModuleID = 'llvm_expressions/sample2-virt-max-merge-lenght-10.ll'
source_filename = "llvm_expressions/sample2-virt-max-merge-lenght-10.ll"
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
  %.53 = shl i64 %.32, %.37
  %.54 = or i64 %.42, %.53
  %.55 = shl i64 %.54, 3
  %.58 = and i64 %.55, 120
  %.59 = or i64 %.58, %.9
  %.60 = and i64 %.59, 15
  %.61 = or i64 %.60, 1
  %.62 = sub nsw i64 64, %.61
  %.68 = lshr i64 %.20, %.62
  %.76 = shl i64 %.20, %.61
  %.77 = or i64 %.68, %.76
  %.80 = lshr i64 %.32, 3
  %.81 = and i64 %.80, 14
  %.82 = or i64 %.81, 1
  %.83 = sub nsw i64 64, %.82
  %.87 = lshr i64 %.11, %.83
  %.98 = shl i64 %.11, %.82
  %.99 = or i64 %.87, %.98
  %.100 = sub i64 %.77, %.99
  %.103 = xor i64 %.100, %.77
  %.104 = xor i64 %.77, %.99
  %.105 = and i64 %.103, %.104
  %.102 = xor i64 %.104, %.100
  %.106 = xor i64 %.102, %.105
  %.109 = icmp eq i64 %.100, 0
  %.106.lobit = lshr i64 %.106, 63
  %.1094 = zext i1 %.109 to i64
  %.119 = or i64 %.106.lobit, %.1094
  %.134 = icmp eq i64 %.119, 0
  br i1 %.134, label %.3.endif.endif.endif.endif.if, label %.3.endif.endif.endif.endif.else

.3.endif.endif.endif.endif.if:                    ; preds = %.3
  %.193 = shl nuw nsw i64 %.60, 3
  %.194 = or i64 %.193, %.59
  %.229 = and i64 %.194, 255
  %.289 = and i64 %.9, -256
  %.295 = or i64 %.289, %.229
  %.307 = lshr i64 %SymVar_0, 61
  %.325 = and i64 %.6, 65280
  %.326 = or i64 %.325, %.307
  %.330 = and i64 %.6, 16711680
  %.331 = or i64 %.326, %.330
  %.335 = and i64 %.6, 4278190080
  %.336 = or i64 %.331, %.335
  %.340 = and i64 %.6, 1095216660480
  %.341 = or i64 %.336, %.340
  %.345 = and i64 %.6, 280375465082880
  %.346 = or i64 %.341, %.345
  %.350 = and i64 %.6, 71776119061217280
  %.351 = or i64 %.346, %.350
  %.360 = shl i64 %.20, 56
  %.361 = or i64 %.351, %.360
  %.362 = sub i64 %.295, %.361
  %.363 = or i64 %.362, %.32
  %.364 = shl i64 %.362, 4
  %.367 = and i64 %.364, 1008
  %.390 = or i64 %.367, %.361
  %.415 = lshr i64 %.194, 2
  %.416 = and i64 %.415, 6
  %.417 = or i64 %.416, 1
  %.423 = shl i64 %.390, %.417
  %.424 = add i64 %.423, %.363
  br label %.3.endif.endif.endif.endif.endif

.3.endif.endif.endif.endif.else:                  ; preds = %.3
  %.443 = sub i64 %.20, %.11
  %.444 = shl i64 %.443, 3
  %.447 = and i64 %.444, 248
  %.460 = or i64 %.447, %.32
  %.589 = shl i64 %.59, 4
  %.592 = and i64 %.589, 496
  %.593 = or i64 %.592, %.20
  %.594 = sub i64 %.59, %.593
  %.595 = or i64 %.460, %.594
  %.596 = shl i64 %.594, 4
  %.599 = and i64 %.596, 1008
  %.600 = or i64 %.599, %.593
  %.625 = lshr i64 %.59, 2
  %.626 = and i64 %.625, 6
  %.627 = or i64 %.626, 1
  %.633 = shl i64 %.600, %.627
  %.634 = add i64 %.633, %.595
  br label %.3.endif.endif.endif.endif.endif

.3.endif.endif.endif.endif.endif:                 ; preds = %.3.endif.endif.endif.endif.else, %.3.endif.endif.endif.endif.if
  %.636 = phi i64 [ %.424, %.3.endif.endif.endif.endif.if ], [ %.634, %.3.endif.endif.endif.endif.else ]
  ret i64 %.636
}

attributes #0 = { norecurse nounwind readnone }
