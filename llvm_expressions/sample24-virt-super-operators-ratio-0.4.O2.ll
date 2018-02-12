; ModuleID = 'llvm_expressions/sample24-virt-super-operators-ratio-0.4.ll'
source_filename = "llvm_expressions/sample24-virt-super-operators-ratio-0.4.ll"
target datalayout = "e-m:e-i64:64-f80:128-n8:16:32:64-S128"
target triple = "x86_64-pc-linux-gnu"

; Function Attrs: norecurse nounwind readnone
define i64 @SECRET(i64 %SymVar_0) local_unnamed_addr #0 {
.3:
  %.6 = lshr i64 %SymVar_0, 53
  %.9 = shl i64 %SymVar_0, 11
  %.10 = or i64 %.6, %.9
  %.13 = lshr i64 %.10, 1
  %div = udiv i64 %SymVar_0, 3
  %0 = mul i64 %.13, -112410438
  %.25 = add i64 %0, %div
  %.28 = lshr i64 %.25, 3
  %.29 = and i64 %.28, 14
  %.30 = or i64 %.29, 1
  %.31 = sub nsw i64 64, %.30
  %.35 = shl i64 %.13, %.31
  %.44 = lshr i64 %.13, %.30
  %.45 = or i64 %.35, %.44
  %.48 = lshr i64 %.25, 2
  %.49 = and i64 %.48, 14
  %.50 = or i64 %.49, 1
  %.51 = sub nsw i64 64, %.50
  %.55 = lshr i64 %.13, %.51
  %.64 = shl i64 %.13, %.50
  %.65 = or i64 %.55, %.64
  %.66 = shl i64 %.65, 2
  %.69 = and i64 %.66, 28
  %.70 = add i64 %SymVar_0, 160536708
  %.73 = lshr i64 %.25, 9
  %.77 = and i64 %.73, 6
  %.78 = or i64 %.77, 1
  %.82 = lshr i64 %.70, %.78
  %.83 = shl i64 %.82, 4
  %.86 = and i64 %.83, 1008
  %.87 = or i64 %.86, %.82
  %.88 = or i64 %.69, %.87
  %.89 = add i64 %SymVar_0, 8152287480
  %.92 = lshr i64 %.89, 4
  %.93 = and i64 %.92, 14
  %.94 = or i64 %.93, 1
  %.95 = sub nsw i64 64, %.94
  %.99 = shl i64 %.88, %.95
  %.108 = lshr i64 %.88, %.94
  %.109 = or i64 %.99, %.108
  %.110 = sub i64 %.45, %.109
  %.113 = xor i64 %.110, %.35
  %.114 = xor i64 %.99, %.35
  %.115 = and i64 %.113, %.114
  %.112 = xor i64 %.114, %.110
  %.116 = xor i64 %.112, %.115
  %.119 = icmp sgt i64 %.116, -1
  %.125 = icmp ne i64 %.110, 0
  %.146.demorgan = and i1 %.125, %.119
  br i1 %.146.demorgan, label %.3.endif.endif.endif.endif.else, label %.3.endif.endif.endif.endif.if

.3.endif.endif.endif.endif.if:                    ; preds = %.3
  %.225 = mul i64 %.88, %.89
  %.228 = shl i64 %.25, 3
  %.231 = and i64 %.228, 120
  %.232 = or i64 %.231, %.25
  %.233 = and i64 %.88, %.232
  %.234 = shl i64 %.233, 4
  %.237 = and i64 %.234, 496
  %.238 = or i64 %.232, %.13
  %.239 = or i64 %.238, %.237
  %.241 = mul i64 %.225, %.239
  br label %.3.endif.endif.endif.endif.endif

.3.endif.endif.endif.endif.else:                  ; preds = %.3
  %.312 = and i64 %.88, 255
  %1 = lshr i64 %.82, 16
  %.322 = and i64 %1, 65280
  %2 = shl i64 %.87, 16
  %.344 = and i64 %2, 4278190080
  %.350 = and i64 %.82, 9223372032576520192
  %.355 = or i64 %.350, %.322
  %.360 = or i64 %.355, %.344
  %.365 = or i64 %.360, %.312
  %.372 = lshr i64 %.89, 3
  %.373 = and i64 %.372, 14
  %.374 = or i64 %.373, 1
  %.375 = sub nsw i64 64, %.374
  %.379 = lshr i64 %.89, %.375
  %.388 = shl i64 %.89, %.374
  %.389 = or i64 %.25, %.388
  %.390 = or i64 %.389, %.379
  %.367 = mul i64 %.390, %.89
  %.392 = mul i64 %.367, %.365
  br label %.3.endif.endif.endif.endif.endif

.3.endif.endif.endif.endif.endif:                 ; preds = %.3.endif.endif.endif.endif.else, %.3.endif.endif.endif.endif.if
  %.241.sink.off0 = phi i64 [ %.241, %.3.endif.endif.endif.endif.if ], [ %.392, %.3.endif.endif.endif.endif.else ]
  ret i64 %.241.sink.off0
}

attributes #0 = { norecurse nounwind readnone }
