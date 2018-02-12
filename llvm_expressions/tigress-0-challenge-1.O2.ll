; ModuleID = 'llvm_expressions/tigress-0-challenge-1.ll'
source_filename = "llvm_expressions/tigress-0-challenge-1.ll"
target datalayout = "e-m:e-i64:64-f80:128-n8:16:32:64-S128"
target triple = "x86_64-pc-linux-gnu"

; Function Attrs: norecurse nounwind readnone
define i64 @SECRET(i64 %SymVar_0) local_unnamed_addr #0 {
.3:
  %.5 = and i64 %SymVar_0, 573319932
  %.6 = add nsw i64 %.5, -341319700
  %mulconv = mul nsw i64 %.6, 502412191
  %.11 = add i64 %SymVar_0, 584234876
  %.12 = add i64 %.11, %mulconv
  %.13 = xor i64 %.12, %.6
  %.14 = and i64 %SymVar_0, 335886564
  %.15 = add nsw i64 %.14, -1595821287
  %.18 = lshr i64 %.15, 3
  %0 = and i64 %.18, 6
  %.21 = or i64 %0, 1
  %.26 = lshr i64 %.12, %.21
  %.27 = add i64 %.26, %SymVar_0
  %.30 = mul i64 %.27, %.15
  %.33 = icmp eq i64 %.13, %.30
  %.77 = shl i64 %.12, 2
  %.80 = and i64 %.77, 28
  br i1 %.33, label %.3.endif.endif.endif.endif.else, label %.3.endif.endif.endif.endif.if

.3.endif.endif.endif.endif.if:                    ; preds = %.3
  %.81 = lshr i64 %.6, 48
  %.96 = and i64 %.81, 255
  %.984 = lshr i64 %.6, 56
  %.101 = shl nuw nsw i64 %.984, 8
  %.102 = or i64 %.96, %.101
  %1 = lshr i64 %.6, 16
  %.125 = and i64 %1, 16711680
  %.126 = or i64 %.102, %.125
  %.131 = and i64 %1, 4278190080
  %.132 = or i64 %.126, %.131
  %2 = shl nsw i64 %.6, 16
  %.149 = and i64 %2, 1095216660480
  %.150 = or i64 %.132, %.149
  %.155 = and i64 %2, 262783279038464
  %.156 = or i64 %.150, %.155
  %.177 = shl i64 %.6, 48
  %.178 = and i64 %.177, 70931694131085312
  %.179 = or i64 %.156, %.178
  %.181 = lshr i64 %.6, 8
  %.184 = shl i64 %.181, 56
  %.185 = or i64 %.179, %.184
  %.186 = or i64 %.185, %.80
  %.189 = lshr i64 %.12, 1
  %.190 = and i64 %.189, 14
  %.191 = or i64 %.190, 1
  %.192 = sub nsw i64 0, %.191
  %.197 = and i64 %.192, 63
  %.198 = shl i64 %.186, %.197
  %.209 = lshr i64 %.186, %.191
  %.210 = or i64 %.198, %.209
  %.213 = and i64 %.6, 12
  %.214 = or i64 %.213, 1
  %.215 = sub nsw i64 0, %.214
  %.220 = and i64 %.215, 63
  %.221 = lshr i64 %.15, %.220
  %.229 = shl i64 %.15, %.214
  %.230 = or i64 %.221, %.229
  %.231 = shl nsw i64 %.230, 2
  %.234 = and i64 %.231, 60
  %.247 = lshr i64 %.27, 16
  %.274 = and i64 %.247, 65535
  %.302 = and i64 %.27, -4294967296
  %.317 = or i64 %.302, %.274
  %.318 = or i64 %.317, %.234
  %.319 = xor i64 %.318, %.230
  br label %.3.endif.endif.endif.endif.endif

.3.endif.endif.endif.endif.else:                  ; preds = %.3
  %.387 = or i64 %.80, %.6
  %.391 = lshr i64 %.12, 1
  %.392 = and i64 %.391, 14
  %.393 = or i64 %.392, 1
  %.394 = sub nsw i64 0, %.393
  %.399 = and i64 %.394, 63
  %.400 = shl i64 %.387, %.399
  %.411 = lshr i64 %.387, %.393
  %.412 = or i64 %.400, %.411
  %.427 = xor i64 %.27, %.15
  br label %.3.endif.endif.endif.endif.endif

.3.endif.endif.endif.endif.endif:                 ; preds = %.3.endif.endif.endif.endif.else, %.3.endif.endif.endif.endif.if
  %.427.sink = phi i64 [ %.427, %.3.endif.endif.endif.endif.else ], [ %.319, %.3.endif.endif.endif.endif.if ]
  %.412.sink = phi i64 [ %.412, %.3.endif.endif.endif.endif.else ], [ %.210, %.3.endif.endif.endif.endif.if ]
  %.430 = lshr i64 %.427.sink, 3
  %.431 = and i64 %.430, 14
  %.432 = or i64 %.431, 1
  %.433 = sub nsw i64 0, %.432
  %.438 = and i64 %.433, 63
  %.439 = lshr i64 %.412.sink, %.438
  %.475 = shl i64 %.412.sink, %.432
  %.476 = or i64 %.439, %.475
  ret i64 %.476
}

attributes #0 = { norecurse nounwind readnone }
