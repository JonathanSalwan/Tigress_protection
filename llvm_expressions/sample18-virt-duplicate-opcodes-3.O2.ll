; ModuleID = 'llvm_expressions/sample18-virt-duplicate-opcodes-3.ll'
source_filename = "llvm_expressions/sample18-virt-duplicate-opcodes-3.ll"
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
  %.24 = shl i64 %.11, %.18
  %.33 = lshr i64 %.11, %.17
  %.34 = or i64 %.24, %.33
  %.37 = lshr i64 %SymVar_0, 55
  %.40 = shl i64 %SymVar_0, 9
  %.41 = or i64 %.37, %.40
  %.42 = or i64 %SymVar_0, 1049658519
  %.43 = sub i64 %.41, %.42
  %.44 = sub i64 %.34, %.43
  %.47 = xor i64 %.44, %.24
  %.48 = xor i64 %.24, %.43
  %.49 = and i64 %.47, %.48
  %.46 = xor i64 %.48, %.44
  %.50 = xor i64 %.46, %.49
  %.72 = icmp sgt i64 %.50, -1
  br i1 %.72, label %.3.endif.endif.endif.if, label %.3.endif.endif.endif.else

.3.endif.endif.endif.if:                          ; preds = %.3
  %.94 = lshr i64 %.12, 4
  %.95 = and i64 %.94, 14
  %.96 = or i64 %.95, 1
  %.97 = sub nsw i64 64, %.96
  %.103 = lshr i64 %.11, %.97
  %.112 = shl i64 %.11, %.96
  %.113 = or i64 %.103, %.112
  %.122 = or i64 %.37, %SymVar_0
  %.125 = lshr i64 %.122, 4
  %.126 = and i64 %.125, 6
  %.127 = or i64 %.126, 1
  %.131 = lshr i64 %.113, %.127
  br label %.3.endif.endif.endif.endif

.3.endif.endif.endif.else:                        ; preds = %.3
  %.148 = shl i64 %.11, 4
  %.151 = and i64 %.148, 1008
  %.152 = or i64 %.151, %.11
  %.153 = add i64 %.152, %.37
  %.154 = shl i64 %.153, 3
  %.157 = and i64 %.154, 248
  %.158 = or i64 %.157, %.152
  %.160 = lshr i64 %.12, 36
  %.252 = and i64 %.160, 14
  %.253 = or i64 %.252, 1
  %.254 = sub nsw i64 64, %.253
  %.260 = lshr i64 %.158, %.254
  %.291 = shl i64 %.158, %.253
  %.292 = or i64 %.260, %.291
  %.293 = shl i64 %.11, 3
  %.298 = or i64 %.37, %SymVar_0
  %.299 = or i64 %.298, %.293
  %.302 = lshr i64 %.299, 4
  %.303 = and i64 %.302, 6
  %.304 = or i64 %.303, 1
  %.308 = lshr i64 %.292, %.304
  br label %.3.endif.endif.endif.endif

.3.endif.endif.endif.endif:                       ; preds = %.3.endif.endif.endif.else, %.3.endif.endif.endif.if
  %.310 = phi i64 [ %.131, %.3.endif.endif.endif.if ], [ %.308, %.3.endif.endif.endif.else ]
  ret i64 %.310
}

attributes #0 = { norecurse nounwind readnone }
