; ModuleID = 'llvm_expressions/sample18-virt-max-merge-lenght-30.ll'
source_filename = "llvm_expressions/sample18-virt-max-merge-lenght-30.ll"
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
  %.35 = lshr i64 %.11, %.17
  %.36 = or i64 %.24, %.35
  %.39 = lshr i64 %SymVar_0, 55
  %.42 = shl i64 %SymVar_0, 9
  %.43 = or i64 %.39, %.42
  %.44 = or i64 %SymVar_0, 1049658519
  %.45 = sub i64 %.43, %.44
  %.46 = sub i64 %.36, %.45
  %.49 = xor i64 %.46, %.24
  %.50 = xor i64 %.24, %.45
  %.51 = and i64 %.49, %.50
  %.48 = xor i64 %.50, %.46
  %.52 = xor i64 %.48, %.51
  %.74 = icmp sgt i64 %.52, -1
  br i1 %.74, label %.3.endif.endif.endif.if, label %.3.endif.endif.endif.else

.3.endif.endif.endif.if:                          ; preds = %.3
  %.96 = lshr i64 %.12, 4
  %.97 = and i64 %.96, 14
  %.98 = or i64 %.97, 1
  %.99 = sub nsw i64 64, %.98
  %.103 = lshr i64 %.11, %.99
  %.112 = shl i64 %.11, %.98
  %.113 = or i64 %.103, %.112
  %.122 = or i64 %.39, %SymVar_0
  %.125 = lshr i64 %.122, 4
  %.126 = and i64 %.125, 6
  %.127 = or i64 %.126, 1
  %.133 = lshr i64 %.113, %.127
  br label %.3.endif.endif.endif.endif

.3.endif.endif.endif.else:                        ; preds = %.3
  %.150 = shl i64 %.11, 4
  %.153 = and i64 %.150, 1008
  %.154 = or i64 %.153, %.11
  %.155 = add i64 %.154, %.39
  %.156 = shl i64 %.155, 3
  %.159 = and i64 %.156, 248
  %.160 = or i64 %.159, %.154
  %.162 = lshr i64 %.12, 36
  %.254 = and i64 %.162, 14
  %.255 = or i64 %.254, 1
  %.256 = sub nsw i64 64, %.255
  %.260 = lshr i64 %.160, %.256
  %.291 = shl i64 %.160, %.255
  %.292 = or i64 %.260, %.291
  %.293 = shl i64 %.11, 3
  %.298 = or i64 %.39, %SymVar_0
  %.299 = or i64 %.298, %.293
  %.302 = lshr i64 %.299, 4
  %.303 = and i64 %.302, 6
  %.304 = or i64 %.303, 1
  %.310 = lshr i64 %.292, %.304
  br label %.3.endif.endif.endif.endif

.3.endif.endif.endif.endif:                       ; preds = %.3.endif.endif.endif.else, %.3.endif.endif.endif.if
  %.312 = phi i64 [ %.133, %.3.endif.endif.endif.if ], [ %.310, %.3.endif.endif.endif.else ]
  ret i64 %.312
}

attributes #0 = { norecurse nounwind readnone }
