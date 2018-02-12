; ModuleID = 'llvm_expressions/sample24-virt-max-merge-lenght-30.ll'
source_filename = "llvm_expressions/sample24-virt-max-merge-lenght-30.ll"
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
  %.57 = lshr i64 %.13, %.51
  %.66 = shl i64 %.13, %.50
  %.67 = or i64 %.57, %.66
  %.68 = shl i64 %.67, 2
  %.71 = and i64 %.68, 28
  %.72 = add i64 %SymVar_0, 160536708
  %.75 = lshr i64 %.25, 9
  %.79 = and i64 %.75, 6
  %.80 = or i64 %.79, 1
  %.84 = lshr i64 %.72, %.80
  %.85 = shl i64 %.84, 4
  %.88 = and i64 %.85, 1008
  %.89 = or i64 %.88, %.84
  %.90 = or i64 %.71, %.89
  %.91 = add i64 %SymVar_0, 8152287480
  %.94 = lshr i64 %.91, 4
  %.95 = and i64 %.94, 14
  %.96 = or i64 %.95, 1
  %.97 = sub nsw i64 64, %.96
  %.101 = shl i64 %.90, %.97
  %.110 = lshr i64 %.90, %.96
  %.111 = or i64 %.101, %.110
  %.112 = sub i64 %.45, %.111
  %.115 = xor i64 %.112, %.35
  %.116 = xor i64 %.101, %.35
  %.117 = and i64 %.115, %.116
  %.114 = xor i64 %.116, %.112
  %.118 = xor i64 %.114, %.117
  %.121 = icmp sgt i64 %.118, -1
  %.127 = icmp ne i64 %.112, 0
  %.148.demorgan = and i1 %.127, %.121
  br i1 %.148.demorgan, label %.3.endif.endif.endif.endif.else, label %.3.endif.endif.endif.endif.if

.3.endif.endif.endif.endif.if:                    ; preds = %.3
  %.229 = mul i64 %.90, %.91
  %.232 = shl i64 %.25, 3
  %.235 = and i64 %.232, 120
  %.236 = or i64 %.235, %.25
  %.237 = and i64 %.90, %.236
  %.238 = shl i64 %.237, 4
  %.241 = and i64 %.238, 496
  %.242 = or i64 %.236, %.13
  %.243 = or i64 %.242, %.241
  %.245 = mul i64 %.229, %.243
  br label %.3.endif.endif.endif.endif.endif

.3.endif.endif.endif.endif.else:                  ; preds = %.3
  %.318 = and i64 %.90, 255
  %1 = lshr i64 %.84, 16
  %.328 = and i64 %1, 65280
  %2 = shl i64 %.89, 16
  %.350 = and i64 %2, 4278190080
  %.356 = and i64 %.84, 9223372032576520192
  %.361 = or i64 %.356, %.328
  %.366 = or i64 %.361, %.350
  %.371 = or i64 %.366, %.318
  %.378 = lshr i64 %.91, 3
  %.379 = and i64 %.378, 14
  %.380 = or i64 %.379, 1
  %.381 = sub nsw i64 64, %.380
  %.387 = lshr i64 %.91, %.381
  %.396 = shl i64 %.91, %.380
  %.397 = or i64 %.25, %.396
  %.398 = or i64 %.397, %.387
  %.373 = mul i64 %.398, %.91
  %.400 = mul i64 %.373, %.371
  br label %.3.endif.endif.endif.endif.endif

.3.endif.endif.endif.endif.endif:                 ; preds = %.3.endif.endif.endif.endif.else, %.3.endif.endif.endif.endif.if
  %.245.sink.off0 = phi i64 [ %.245, %.3.endif.endif.endif.endif.if ], [ %.400, %.3.endif.endif.endif.endif.else ]
  ret i64 %.245.sink.off0
}

attributes #0 = { norecurse nounwind readnone }
