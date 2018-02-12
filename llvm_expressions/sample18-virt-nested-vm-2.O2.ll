; ModuleID = 'llvm_expressions/sample18-virt-nested-vm-2.ll'
source_filename = "llvm_expressions/sample18-virt-nested-vm-2.ll"
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
  %.74 = icmp sgt i64 %.48, -1
  br i1 %.74, label %.3.endif.endif.endif.if, label %.3.endif.endif.endif.else

.3.endif.endif.endif.if:                          ; preds = %.3
  %.96 = lshr i64 %.12, 4
  %.97 = and i64 %.96, 14
  %.98 = or i64 %.97, 1
  %.99 = sub nsw i64 64, %.98
  %.103 = lshr i64 %.11, %.99
  %.112 = shl i64 %.11, %.98
  %.113 = or i64 %.103, %.112
  %.122 = or i64 %.35, %SymVar_0
  %.125 = lshr i64 %.122, 4
  %.126 = and i64 %.125, 6
  %.127 = or i64 %.126, 1
  %.131 = lshr i64 %.113, %.127
  br label %.3.endif.endif.endif.endif

.3.endif.endif.endif.else:                        ; preds = %.3
  %.148 = shl i64 %.11, 4
  %.151 = and i64 %.148, 1008
  %.152 = or i64 %.151, %.11
  %.153 = add i64 %.152, %.35
  %.154 = shl i64 %.153, 3
  %.157 = and i64 %.154, 248
  %.158 = or i64 %.157, %.152
  %.160 = lshr i64 %.12, 36
  %.264 = and i64 %.160, 14
  %.265 = or i64 %.264, 1
  %.266 = sub nsw i64 64, %.265
  %.270 = lshr i64 %.158, %.266
  %.301 = shl i64 %.158, %.265
  %.302 = or i64 %.270, %.301
  %.303 = shl i64 %.11, 3
  %.308 = or i64 %.35, %SymVar_0
  %.309 = or i64 %.308, %.303
  %.312 = lshr i64 %.309, 4
  %.313 = and i64 %.312, 6
  %.314 = or i64 %.313, 1
  %.318 = lshr i64 %.302, %.314
  br label %.3.endif.endif.endif.endif

.3.endif.endif.endif.endif:                       ; preds = %.3.endif.endif.endif.else, %.3.endif.endif.endif.if
  %.320 = phi i64 [ %.131, %.3.endif.endif.endif.if ], [ %.318, %.3.endif.endif.endif.else ]
  ret i64 %.320
}

attributes #0 = { norecurse nounwind readnone }
