; ModuleID = 'llvm_expressions/sample2-virt-nested-vm-2.ll'
source_filename = "llvm_expressions/sample2-virt-nested-vm-2.ll"
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
  %.55 = shl i64 %.32, %.37
  %.56 = or i64 %.44, %.55
  %.57 = shl i64 %.56, 3
  %.60 = and i64 %.57, 120
  %.61 = or i64 %.60, %.9
  %.62 = and i64 %.61, 15
  %.63 = or i64 %.62, 1
  %.64 = sub nsw i64 64, %.63
  %.70 = lshr i64 %.20, %.64
  %.78 = shl i64 %.20, %.63
  %.79 = or i64 %.70, %.78
  %.82 = lshr i64 %.32, 3
  %.83 = and i64 %.82, 14
  %.84 = or i64 %.83, 1
  %.85 = sub nsw i64 64, %.84
  %.91 = lshr i64 %.11, %.85
  %.102 = shl i64 %.11, %.84
  %.103 = or i64 %.91, %.102
  %.104 = sub i64 %.79, %.103
  %.107 = xor i64 %.104, %.79
  %.108 = xor i64 %.79, %.103
  %.109 = and i64 %.107, %.108
  %.106 = xor i64 %.108, %.104
  %.110 = xor i64 %.106, %.109
  %.113 = icmp eq i64 %.104, 0
  %.110.lobit = lshr i64 %.110, 63
  %.11312 = zext i1 %.113 to i64
  %.123 = or i64 %.110.lobit, %.11312
  %.142 = icmp eq i64 %.123, 0
  br i1 %.142, label %.3.endif.endif.endif.endif.if, label %.3.endif.endif.endif.endif.else

.3.endif.endif.endif.endif.if:                    ; preds = %.3
  %.203 = shl nuw nsw i64 %.62, 3
  %.204 = or i64 %.203, %.61
  %.255 = and i64 %.204, 255
  %.323 = and i64 %.9, -256
  %.329 = or i64 %.323, %.255
  %.341 = lshr i64 %SymVar_0, 61
  %.371 = and i64 %.6, 65280
  %.372 = or i64 %.371, %.341
  %.376 = and i64 %.6, 16711680
  %.377 = or i64 %.372, %.376
  %.381 = and i64 %.6, 4278190080
  %.382 = or i64 %.377, %.381
  %.386 = and i64 %.6, 1095216660480
  %.387 = or i64 %.382, %.386
  %.391 = and i64 %.6, 280375465082880
  %.392 = or i64 %.387, %.391
  %.396 = and i64 %.6, 71776119061217280
  %.397 = or i64 %.392, %.396
  %.412 = shl i64 %.20, 56
  %.413 = or i64 %.397, %.412
  %.414 = sub i64 %.329, %.413
  %.415 = or i64 %.414, %.32
  %.416 = shl i64 %.414, 4
  %.419 = and i64 %.416, 1008
  %.442 = or i64 %.419, %.413
  %.467 = lshr i64 %.204, 2
  %.468 = and i64 %.467, 6
  %.469 = or i64 %.468, 1
  %.475 = shl i64 %.442, %.469
  %.476 = add i64 %.475, %.415
  br label %.3.endif.endif.endif.endif.endif

.3.endif.endif.endif.endif.else:                  ; preds = %.3
  %.495 = sub i64 %.20, %.11
  %.496 = shl i64 %.495, 3
  %.499 = and i64 %.496, 248
  %.512 = or i64 %.499, %.32
  %.667 = shl i64 %.61, 4
  %.670 = and i64 %.667, 496
  %.671 = or i64 %.670, %.20
  %.672 = sub i64 %.61, %.671
  %.673 = or i64 %.512, %.672
  %.674 = shl i64 %.672, 4
  %.677 = and i64 %.674, 1008
  %.678 = or i64 %.677, %.671
  %.703 = lshr i64 %.61, 2
  %.704 = and i64 %.703, 6
  %.705 = or i64 %.704, 1
  %.711 = shl i64 %.678, %.705
  %.712 = add i64 %.711, %.673
  br label %.3.endif.endif.endif.endif.endif

.3.endif.endif.endif.endif.endif:                 ; preds = %.3.endif.endif.endif.endif.else, %.3.endif.endif.endif.endif.if
  %.714 = phi i64 [ %.476, %.3.endif.endif.endif.endif.if ], [ %.712, %.3.endif.endif.endif.endif.else ]
  ret i64 %.714
}

attributes #0 = { norecurse nounwind readnone }
