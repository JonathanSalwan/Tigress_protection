; ModuleID = 'llvm_expressions/sample18-virt-max-merge-lenght-10.ll'
source_filename = "llvm_expressions/sample18-virt-max-merge-lenght-10.ll"
target datalayout = "e-m:e-i64:64-f80:128-n8:16:32:64-S128"
target triple = "x86_64-pc-linux-gnu"

; Function Attrs: norecurse nounwind readnone
define i64 @SECRET(i64 %SymVar_0) local_unnamed_addr #0 {
.3:
  %.6 = shl i64 %SymVar_0, 51
  %.9 = lshr i64 %SymVar_0, 13
  %.10 = or i64 %.6, %.9
  %.11 = add i64 %.10, 210061817713481728
  %.12 = sub i64 %SymVar_0, %.11
  %.15 = lshr i64 %.12, 2
  %.16 = and i64 %.15, 14
  %.17 = or i64 %.16, 1
  %.18 = sub nsw i64 64, %.17
  %.22 = shl i64 %.11, %.18
  %.31 = lshr i64 %.11, %.17
  %.32 = or i64 %.22, %.31
  %.35 = lshr i64 %SymVar_0, 55
  %.38 = shl i64 %SymVar_0, 9
  %.39 = or i64 %.35, %.38
  %.40 = or i64 %SymVar_0, 1049658519
  %.41 = sub i64 %.39, %.40
  %.42 = sub i64 %.32, %.41
  %.45 = xor i64 %.42, %.22
  %.46 = xor i64 %.22, %.41
  %.47 = and i64 %.45, %.46
  %.44 = xor i64 %.46, %.42
  %.48 = xor i64 %.44, %.47
  %.70 = icmp sgt i64 %.48, -1
  br i1 %.70, label %.3.endif.endif.endif.if, label %.3.endif.endif.endif.else

.3.endif.endif.endif.if:                          ; preds = %.3
  %.92 = lshr i64 %.12, 4
  %.93 = and i64 %.92, 14
  %.94 = or i64 %.93, 1
  %.95 = sub nsw i64 64, %.94
  %.99 = lshr i64 %.11, %.95
  %.108 = shl i64 %.11, %.94
  %.109 = or i64 %.99, %.108
  %.118 = or i64 %.35, %SymVar_0
  %.121 = lshr i64 %.118, 4
  %.122 = and i64 %.121, 6
  %.123 = or i64 %.122, 1
  %.127 = lshr i64 %.109, %.123
  br label %.3.endif.endif.endif.endif

.3.endif.endif.endif.else:                        ; preds = %.3
  %.144 = shl i64 %.11, 4
  %.147 = and i64 %.144, 1008
  %.148 = or i64 %.147, %.11
  %.149 = add i64 %.148, %.35
  %.150 = shl i64 %.149, 3
  %.153 = and i64 %.150, 248
  %.154 = or i64 %.153, %.148
  %.156 = lshr i64 %.12, 36
  %.248 = and i64 %.156, 14
  %.249 = or i64 %.248, 1
  %.250 = sub nsw i64 64, %.249
  %.254 = lshr i64 %.154, %.250
  %.285 = shl i64 %.154, %.249
  %.286 = or i64 %.254, %.285
  %.287 = shl i64 %.11, 3
  %.292 = or i64 %.35, %SymVar_0
  %.293 = or i64 %.292, %.287
  %.296 = lshr i64 %.293, 4
  %.297 = and i64 %.296, 6
  %.298 = or i64 %.297, 1
  %.302 = lshr i64 %.286, %.298
  br label %.3.endif.endif.endif.endif

.3.endif.endif.endif.endif:                       ; preds = %.3.endif.endif.endif.else, %.3.endif.endif.endif.if
  %.304 = phi i64 [ %.127, %.3.endif.endif.endif.if ], [ %.302, %.3.endif.endif.endif.else ]
  ret i64 %.304
}

attributes #0 = { norecurse nounwind readnone }
