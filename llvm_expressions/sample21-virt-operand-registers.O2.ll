; ModuleID = 'llvm_expressions/sample21-virt-operand-registers.ll'
source_filename = "llvm_expressions/sample21-virt-operand-registers.ll"
target datalayout = "e-m:e-i64:64-f80:128-n8:16:32:64-S128"
target triple = "x86_64-pc-linux-gnu"

; Function Attrs: norecurse nounwind readnone
define i64 @SECRET(i64 %SymVar_0) local_unnamed_addr #0 {
.3:
  %.6 = lshr i64 %SymVar_0, 3
  %.9 = shl i64 %SymVar_0, 61
  %.10 = or i64 %.6, %.9
  %.11 = add i64 %.10, -1072693119
  %.12 = lshr i64 %.11, 32
  %.51 = and i64 %.12, 16777215
  %.5320 = lshr i64 %.11, 56
  %.56 = shl nuw nsw i64 %.5320, 24
  %.57 = or i64 %.51, %.56
  %.80 = shl i64 %.11, 32
  %.81 = and i64 %.80, 1095216660480
  %.82 = or i64 %.57, %.81
  %.87 = and i64 %.80, 280375465082880
  %.88 = or i64 %.82, %.87
  %.93 = and i64 %.80, 71776119061217280
  %.94 = or i64 %.88, %.93
  %.96 = lshr i64 %.11, 24
  %.99 = shl i64 %.96, 56
  %.100 = or i64 %.94, %.99
  %.106 = or i64 %.11, %SymVar_0
  %.107 = add i64 %.106, -300260246
  %.120 = lshr i64 %.107, 32
  %.158 = and i64 %.120, 16711680
  %.159 = and i64 %.120, 16777215
  %.16139 = lshr i64 %.107, 56
  %.164 = shl nuw nsw i64 %.16139, 24
  %.165 = or i64 %.159, %.164
  %.188 = shl i64 %.107, 32
  %.189 = and i64 %.188, 1095216660480
  %.190 = or i64 %.165, %.189
  %.195 = and i64 %.188, 280375465082880
  %.196 = or i64 %.190, %.195
  %.201 = and i64 %.188, 71776119061217280
  %.202 = or i64 %.196, %.201
  %.204 = lshr i64 %.107, 24
  %.207 = shl i64 %.204, 56
  %.208 = or i64 %.202, %.207
  %.210 = shl i64 %SymVar_0, 4
  %.211 = add i64 %.210, 32
  %.214 = and i64 %.211, 1008
  %.215 = or i64 %.208, %.214
  %.217 = and i64 %.215, 255
  %0 = lshr i64 %.196, 32
  %.233 = and i64 %0, 65280
  %1 = shl i64 %.215, 32
  %.259 = and i64 %1, 280375465082880
  %.263 = and i64 %.202, 71776119061217280
  %.266 = and i64 %.208, -72057594037927936
  %.234 = or i64 %.164, %.158
  %.239 = or i64 %.234, %.189
  %.244 = or i64 %.239, %.233
  %.249 = or i64 %.244, %.263
  %.260 = or i64 %.249, %.266
  %.265 = or i64 %.260, %.217
  %.270 = or i64 %.265, %.259
  %.271 = add i64 %.270, %.100
  %.280 = shl i64 %.271, 1
  %.313 = lshr i64 %.271, 63
  %.314 = or i64 %.280, %.313
  ret i64 %.314
}

attributes #0 = { norecurse nounwind readnone }
