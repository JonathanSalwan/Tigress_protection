; ModuleID = 'llvm_expressions/tigress-1-challenge-1.ll'
source_filename = "llvm_expressions/tigress-1-challenge-1.ll"
target datalayout = "e-m:e-i64:64-f80:128-n8:16:32:64-S128"
target triple = "x86_64-pc-linux-gnu"

; Function Attrs: norecurse nounwind readnone
define i64 @SECRET(i64 %SymVar_0) local_unnamed_addr #0 {
.3:
  %.6 = lshr i64 %SymVar_0, 13
  %.9 = shl i64 %SymVar_0, 51
  %.10 = or i64 %.6, %.9
  %.11 = add i64 %.10, 210061817713481728
  %.12 = sub i64 %SymVar_0, %.11
  %.15 = lshr i64 %.12, 2
  %.16 = and i64 %.15, 14
  %.17 = or i64 %.16, 1
  %.18 = sub nsw i64 0, %.17
  %.23 = and i64 %.18, 63
  %.24 = shl i64 %.11, %.23
  %.35 = lshr i64 %.11, %.17
  %.36 = or i64 %.24, %.35
  %.39 = lshr i64 %SymVar_0, 55
  %.42 = shl i64 %SymVar_0, 9
  %.43 = or i64 %.39, %.42
  %.44 = or i64 %SymVar_0, 1049658519
  %.45 = sub i64 %.43, %.44
  %.46 = sub i64 %.36, %.45
  %.49 = xor i64 %.46, %.36
  %.50 = xor i64 %.36, %.45
  %.51 = and i64 %.49, %.50
  %.47 = xor i64 %.24, %.45
  %.48 = xor i64 %.47, %.46
  %.52 = xor i64 %.48, %.51
  %.76 = icmp sgt i64 %.52, -1
  br i1 %.76, label %.3.endif.endif.endif.if, label %.3.endif.endif.endif.else

.3.endif.endif.endif.if:                          ; preds = %.3
  %.98 = lshr i64 %.12, 4
  %.99 = and i64 %.98, 14
  %.100 = or i64 %.99, 1
  %.101 = sub nsw i64 0, %.100
  %.106 = and i64 %.101, 63
  %.107 = lshr i64 %.11, %.106
  %.118 = shl i64 %.11, %.100
  %.119 = or i64 %.107, %.118
  br label %.3.endif.endif.endif.endif

.3.endif.endif.endif.else:                        ; preds = %.3
  %.156 = shl i64 %.11, 4
  %.159 = and i64 %.156, 1008
  %.160 = or i64 %.159, %.11
  %.161 = add i64 %.160, %.39
  %.162 = shl i64 %.161, 3
  %.165 = and i64 %.162, 248
  %.166 = or i64 %.165, %.160
  %.168 = lshr i64 %.12, 36
  %.260 = and i64 %.168, 14
  %.261 = or i64 %.260, 1
  %.262 = sub nsw i64 0, %.261
  %.267 = and i64 %.262, 63
  %.268 = lshr i64 %.166, %.267
  %.301 = shl i64 %.166, %.261
  %.302 = or i64 %.268, %.301
  %.303 = shl i64 %.11, 3
  %.306 = and i64 %.303, 104
  %.308 = or i64 %.306, %.44
  br label %.3.endif.endif.endif.endif

.3.endif.endif.endif.endif:                       ; preds = %.3.endif.endif.endif.else, %.3.endif.endif.endif.if
  %.308.sink = phi i64 [ %.308, %.3.endif.endif.endif.else ], [ %.44, %.3.endif.endif.endif.if ]
  %.302.sink = phi i64 [ %.302, %.3.endif.endif.endif.else ], [ %.119, %.3.endif.endif.endif.if ]
  %.309 = or i64 %.308.sink, %.39
  %.312 = lshr i64 %.309, 4
  %0 = and i64 %.312, 6
  %.315 = or i64 %0, 1
  %.320 = lshr i64 %.302.sink, %.315
  ret i64 %.320
}

attributes #0 = { norecurse nounwind readnone }
