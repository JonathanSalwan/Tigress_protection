; ModuleID = 'llvm_expressions/sample2-virt-bogus-loop-iterations-2.ll'
source_filename = "llvm_expressions/sample2-virt-bogus-loop-iterations-2.ll"
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
  %.132 = icmp eq i64 %.117, 0
  br i1 %.132, label %.3.endif.endif.endif.endif.if, label %.3.endif.endif.endif.endif.else

.3.endif.endif.endif.endif.if:                    ; preds = %.3
  %.191 = shl nuw nsw i64 %.60, 3
  %.192 = or i64 %.191, %.59
  %.227 = and i64 %.192, 255
  %.287 = and i64 %.9, -256
  %.293 = or i64 %.287, %.227
  %.305 = lshr i64 %SymVar_0, 61
  %.323 = and i64 %.6, 65280
  %.324 = or i64 %.323, %.305
  %.328 = and i64 %.6, 16711680
  %.329 = or i64 %.324, %.328
  %.333 = and i64 %.6, 4278190080
  %.334 = or i64 %.329, %.333
  %.338 = and i64 %.6, 1095216660480
  %.339 = or i64 %.334, %.338
  %.343 = and i64 %.6, 280375465082880
  %.344 = or i64 %.339, %.343
  %.348 = and i64 %.6, 71776119061217280
  %.349 = or i64 %.344, %.348
  %.358 = shl i64 %.20, 56
  %.359 = or i64 %.349, %.358
  %.360 = sub i64 %.293, %.359
  %.361 = or i64 %.360, %.32
  %.362 = shl i64 %.360, 4
  %.365 = and i64 %.362, 1008
  %.388 = or i64 %.365, %.359
  %.413 = lshr i64 %.192, 2
  %.414 = and i64 %.413, 6
  %.415 = or i64 %.414, 1
  %.419 = shl i64 %.388, %.415
  %.420 = add i64 %.419, %.361
  br label %.3.endif.endif.endif.endif.endif

.3.endif.endif.endif.endif.else:                  ; preds = %.3
  %.439 = sub i64 %.20, %.11
  %.440 = shl i64 %.439, 3
  %.443 = and i64 %.440, 248
  %.456 = or i64 %.443, %.32
  %.585 = shl i64 %.59, 4
  %.588 = and i64 %.585, 496
  %.589 = or i64 %.588, %.20
  %.590 = sub i64 %.59, %.589
  %.591 = or i64 %.456, %.590
  %.592 = shl i64 %.590, 4
  %.595 = and i64 %.592, 1008
  %.596 = or i64 %.595, %.589
  %.621 = lshr i64 %.59, 2
  %.622 = and i64 %.621, 6
  %.623 = or i64 %.622, 1
  %.627 = shl i64 %.596, %.623
  %.628 = add i64 %.627, %.591
  br label %.3.endif.endif.endif.endif.endif

.3.endif.endif.endif.endif.endif:                 ; preds = %.3.endif.endif.endif.endif.else, %.3.endif.endif.endif.endif.if
  %.630 = phi i64 [ %.420, %.3.endif.endif.endif.endif.if ], [ %.628, %.3.endif.endif.endif.endif.else ]
  ret i64 %.630
}

attributes #0 = { norecurse nounwind readnone }
