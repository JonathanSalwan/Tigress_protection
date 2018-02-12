; ModuleID = 'sample2-virt-nested-vm-3.ll'
source_filename = "sample2-virt-nested-vm-3.ll"
target datalayout = "e-m:e-i64:64-f80:128-n8:16:32:64-S128"
target triple = "x86_64-pc-linux-gnu"

; Function Attrs: norecurse nounwind readnone
define i64 @SECRET(i64 %SymVar_0) local_unnamed_addr #0 {
.3:
  %.6 = lshr i64 %SymVar_0, 5
  %.7 = xor i64 %.6, 810798164723513605
  %.8 = add i64 %SymVar_0, -275339905
  %.9 = add i64 %.8, %.7
  %.10 = add i64 %.6, %SymVar_0
  %.11 = add i64 %.10, %.9
  %.14 = shl nuw nsw i64 %.6, 2
  %.16 = mul i64 %.14, %.11
  %.19 = and i64 %.16, 28
  %.20 = or i64 %.19, %.6
  %.23 = mul i64 %.6, 1015975030
  %.25 = and i64 %.23, 6
  %.26 = or i64 %.25, 1
  %.30 = lshr i64 %SymVar_0, %.26
  %.33 = lshr i64 %.9, 4
  %.34 = and i64 %.33, 14
  %.35 = or i64 %.34, 1
  %.36 = sub nsw i64 64, %.35
  %.40 = lshr i64 %.30, %.36
  %.51 = shl i64 %.30, %.35
  %.52 = or i64 %.40, %.51
  %.53 = shl i64 %.52, 3
  %.56 = and i64 %.53, 120
  %.57 = or i64 %.56, %.9
  %.58 = and i64 %.57, 15
  %.59 = or i64 %.58, 1
  %.60 = sub nsw i64 64, %.59
  %.64 = lshr i64 %.20, %.60
  %.72 = shl i64 %.20, %.59
  %.73 = or i64 %.64, %.72
  %.76 = lshr i64 %.30, 3
  %.77 = and i64 %.76, 14
  %.78 = or i64 %.77, 1
  %.79 = sub nsw i64 64, %.78
  %.83 = lshr i64 %.11, %.79
  %.94 = shl i64 %.11, %.78
  %.95 = or i64 %.83, %.94
  %.96 = sub i64 %.73, %.95
  %.99 = xor i64 %.96, %.73
  %.100 = xor i64 %.73, %.95
  %.101 = and i64 %.99, %.100
  %.98 = xor i64 %.100, %.96
  %.102 = xor i64 %.98, %.101
  %.105 = icmp eq i64 %.96, 0
  %.102.lobit = lshr i64 %.102, 63
  %.10512 = zext i1 %.105 to i64
  %.115 = or i64 %.102.lobit, %.10512
  %.142 = icmp eq i64 %.115, 0
  br i1 %.142, label %.3.endif.endif.endif.endif.if, label %.3.endif.endif.endif.endif.else

.3.endif.endif.endif.endif.if:                    ; preds = %.3
  %.199 = shl nuw nsw i64 %.58, 3
  %.200 = or i64 %.199, %.57
  %.283 = and i64 %.200, 255
  %.367 = and i64 %.9, -256
  %.373 = or i64 %.367, %.283
  %.385 = lshr i64 %SymVar_0, 61
  %.439 = and i64 %.6, 65280
  %.440 = or i64 %.439, %.385
  %.444 = and i64 %.6, 16711680
  %.445 = or i64 %.440, %.444
  %.449 = and i64 %.6, 4278190080
  %.450 = or i64 %.445, %.449
  %.454 = and i64 %.6, 1095216660480
  %.455 = or i64 %.450, %.454
  %.459 = and i64 %.6, 280375465082880
  %.460 = or i64 %.455, %.459
  %.464 = and i64 %.6, 71776119061217280
  %.465 = or i64 %.460, %.464
  %.492 = shl i64 %.20, 56
  %.493 = or i64 %.465, %.492
  %.494 = sub i64 %.373, %.493
  %.495 = or i64 %.494, %.30
  %.496 = shl i64 %.494, 4
  %.499 = and i64 %.496, 1008
  %.522 = or i64 %.499, %.493
  %.547 = lshr i64 %.200, 2
  %.548 = and i64 %.547, 6
  %.549 = or i64 %.548, 1
  %.555 = shl i64 %.522, %.549
  %.556 = add i64 %.555, %.495
  br label %.3.endif.endif.endif.endif.endif

.3.endif.endif.endif.endif.else:                  ; preds = %.3
  %.575 = sub i64 %.20, %.11
  %.576 = shl i64 %.575, 3
  %.579 = and i64 %.576, 248
  %.590 = or i64 %.579, %.30
  %.791 = shl i64 %.57, 4
  %.794 = and i64 %.791, 496
  %.795 = or i64 %.794, %.20
  %.796 = sub i64 %.57, %.795
  %.797 = or i64 %.590, %.796
  %.798 = shl i64 %.796, 4
  %.801 = and i64 %.798, 1008
  %.802 = or i64 %.801, %.795
  %.827 = lshr i64 %.57, 2
  %.828 = and i64 %.827, 6
  %.829 = or i64 %.828, 1
  %.835 = shl i64 %.802, %.829
  %.836 = add i64 %.835, %.797
  br label %.3.endif.endif.endif.endif.endif

.3.endif.endif.endif.endif.endif:                 ; preds = %.3.endif.endif.endif.endif.else, %.3.endif.endif.endif.endif.if
  %.838 = phi i64 [ %.556, %.3.endif.endif.endif.endif.if ], [ %.836, %.3.endif.endif.endif.endif.else ]
  ret i64 %.838
}

attributes #0 = { norecurse nounwind readnone }
