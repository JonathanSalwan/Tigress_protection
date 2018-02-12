; ModuleID = 'llvm_expressions/tigress-4-challenge-2.ll'
source_filename = "llvm_expressions/tigress-4-challenge-2.ll"
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
  %.47 = add i64 %0, %div
  %.50 = lshr i64 %.47, 3
  %.51 = and i64 %.50, 14
  %.52 = or i64 %.51, 1
  %.53 = sub nsw i64 0, %.52
  %.58 = and i64 %.53, 63
  %.59 = shl i64 %.13, %.58
  %.70 = lshr i64 %.13, %.52
  %.71 = or i64 %.59, %.70
  %.74 = lshr i64 %.47, 2
  %.75 = and i64 %.74, 14
  %.76 = or i64 %.75, 1
  %.77 = sub nsw i64 0, %.76
  %.82 = and i64 %.77, 63
  %.83 = lshr i64 %.13, %.82
  %.94 = shl i64 %.13, %.76
  %.95 = or i64 %.83, %.94
  %.96 = shl i64 %.95, 2
  %.99 = and i64 %.96, 28
  %.100 = add i64 %SymVar_0, 160536708
  %.103 = lshr i64 %.47, 9
  %1 = and i64 %.103, 6
  %.109 = or i64 %1, 1
  %.114 = lshr i64 %.100, %.109
  %.115 = shl i64 %.114, 4
  %.118 = and i64 %.115, 1008
  %.119 = or i64 %.118, %.114
  %.120 = or i64 %.99, %.119
  %.121 = add i64 %SymVar_0, 8152287480
  %.124 = lshr i64 %.121, 4
  %.125 = and i64 %.124, 14
  %.126 = or i64 %.125, 1
  %.127 = sub nsw i64 0, %.126
  %.132 = and i64 %.127, 63
  %.133 = shl i64 %.120, %.132
  %.144 = lshr i64 %.120, %.126
  %.145 = or i64 %.133, %.144
  %.146 = sub i64 %.71, %.145
  %.149 = xor i64 %.146, %.71
  %.150 = xor i64 %.145, %.71
  %.151 = and i64 %.149, %.150
  %.147 = xor i64 %.145, %.59
  %.148 = xor i64 %.147, %.146
  %.152 = xor i64 %.148, %.151
  %.154 = icmp sgt i64 %.152, -1
  %.156 = icmp ne i64 %.146, 0
  %.186.demorgan = and i1 %.156, %.154
  br i1 %.186.demorgan, label %.3.endif.endif.endif.endif.else, label %.3.endif.endif.endif.endif.if

.3.endif.endif.endif.endif.if:                    ; preds = %.3
  %.296 = shl i64 %.47, 3
  %.299 = and i64 %.296, 120
  %.300 = or i64 %.299, %.47
  %.301 = and i64 %.120, %.300
  %.302 = shl i64 %.301, 4
  %.305 = and i64 %.302, 496
  br label %.3.endif.endif.endif.endif.endif

.3.endif.endif.endif.endif.else:                  ; preds = %.3
  %.408 = and i64 %.120, 255
  %2 = lshr i64 %.114, 16
  %.424 = and i64 %2, 65280
  %3 = shl i64 %.119, 16
  %.458 = and i64 %3, 4278190080
  %.464 = and i64 %.114, 9223372032576520192
  %.469 = or i64 %.464, %.424
  %.474 = or i64 %.469, %.458
  %.479 = or i64 %.474, %.408
  %.486 = lshr i64 %.121, 3
  %.487 = and i64 %.486, 14
  %.488 = or i64 %.487, 1
  %.489 = sub nsw i64 0, %.488
  %.494 = and i64 %.489, 63
  %.495 = lshr i64 %.121, %.494
  %.506 = shl i64 %.121, %.488
  br label %.3.endif.endif.endif.endif.endif

.3.endif.endif.endif.endif.endif:                 ; preds = %.3.endif.endif.endif.endif.else, %.3.endif.endif.endif.endif.if
  %.506.sink = phi i64 [ %.506, %.3.endif.endif.endif.endif.else ], [ %.13, %.3.endif.endif.endif.endif.if ]
  %.495.sink = phi i64 [ %.495, %.3.endif.endif.endif.endif.else ], [ %.305, %.3.endif.endif.endif.endif.if ]
  %.242.sink = phi i64 [ %.47, %.3.endif.endif.endif.endif.else ], [ %.300, %.3.endif.endif.endif.endif.if ]
  %.479.pn = phi i64 [ %.479, %.3.endif.endif.endif.endif.else ], [ %.120, %.3.endif.endif.endif.endif.if ]
  %.483.sink.in = mul i64 %.479.pn, %.121
  %.507 = or i64 %.495.sink, %.506.sink
  %.508 = or i64 %.507, %.242.sink
  %.510 = mul i64 %.483.sink.in, %.508
  ret i64 %.510
}

attributes #0 = { norecurse nounwind readnone }
