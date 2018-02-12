; ModuleID = 'llvm_expressions/sample18-virt-nested-vm-1.ll'
source_filename = "llvm_expressions/sample18-virt-nested-vm-1.ll"
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
  %.105 = lshr i64 %.11, %.99
  %.116 = shl i64 %.11, %.98
  %.117 = or i64 %.105, %.116
  %.126 = or i64 %.39, %SymVar_0
  %.129 = lshr i64 %.126, 4
  %.130 = and i64 %.129, 6
  %.131 = or i64 %.130, 1
  %.137 = lshr i64 %.117, %.131
  br label %.3.endif.endif.endif.endif

.3.endif.endif.endif.else:                        ; preds = %.3
  %.154 = shl i64 %.11, 4
  %.157 = and i64 %.154, 1008
  %.158 = or i64 %.157, %.11
  %.159 = add i64 %.158, %.39
  %.160 = shl i64 %.159, 3
  %.163 = and i64 %.160, 248
  %.164 = or i64 %.163, %.158
  %.166 = lshr i64 %.12, 36
  %.258 = and i64 %.166, 14
  %.259 = or i64 %.258, 1
  %.260 = sub nsw i64 64, %.259
  %.266 = lshr i64 %.164, %.260
  %.299 = shl i64 %.164, %.259
  %.300 = or i64 %.266, %.299
  %.301 = shl i64 %.11, 3
  %.306 = or i64 %.39, %SymVar_0
  %.307 = or i64 %.306, %.301
  %.310 = lshr i64 %.307, 4
  %.311 = and i64 %.310, 6
  %.312 = or i64 %.311, 1
  %.318 = lshr i64 %.300, %.312
  br label %.3.endif.endif.endif.endif

.3.endif.endif.endif.endif:                       ; preds = %.3.endif.endif.endif.else, %.3.endif.endif.endif.if
  %.320 = phi i64 [ %.137, %.3.endif.endif.endif.if ], [ %.318, %.3.endif.endif.endif.else ]
  ret i64 %.320
}

attributes #0 = { norecurse nounwind readnone }
