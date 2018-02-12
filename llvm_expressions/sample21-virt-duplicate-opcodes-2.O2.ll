; ModuleID = 'llvm_expressions/sample21-virt-duplicate-opcodes-2.ll'
source_filename = "llvm_expressions/sample21-virt-duplicate-opcodes-2.ll"
target datalayout = "e-m:e-i64:64-f80:128-n8:16:32:64-S128"
target triple = "x86_64-pc-linux-gnu"

; Function Attrs: norecurse nounwind readnone
define i64 @SECRET(i64 %SymVar_0) local_unnamed_addr #0 {
.3:
  %.6 = shl i64 %SymVar_0, 61
  %.9 = lshr i64 %SymVar_0, 3
  %.10 = or i64 %.6, %.9
  %.11 = add i64 %.10, -1072693119
  %.12 = or i64 %.11, %SymVar_0
  %.13 = add i64 %.12, -300260246
  %.26 = shl i64 %SymVar_0, 4
  %.27 = add i64 %.26, 32
  %.30 = and i64 %.27, 1008
  %.31 = lshr i64 %.13, 32
  %.69 = and i64 %.31, 16711680
  %.70 = and i64 %.31, 16777215
  %.7211 = lshr i64 %.13, 56
  %.75 = shl nuw nsw i64 %.7211, 24
  %.76 = or i64 %.70, %.75
  %.99 = shl i64 %.13, 32
  %.100 = and i64 %.99, 1095216660480
  %.101 = or i64 %.76, %.100
  %.106 = and i64 %.99, 280375465082880
  %.107 = or i64 %.101, %.106
  %.112 = and i64 %.99, 71776119061217280
  %.113 = or i64 %.107, %.112
  %.115 = lshr i64 %.13, 24
  %.118 = shl i64 %.115, 56
  %.119 = or i64 %.113, %.118
  %.120 = or i64 %.119, %.30
  %.122 = and i64 %.120, 255
  %0 = lshr i64 %.107, 32
  %.138 = and i64 %0, 65280
  %1 = shl i64 %.120, 32
  %.164 = and i64 %1, 280375465082880
  %.168 = and i64 %.113, 71776119061217280
  %.171 = and i64 %.119, -72057594037927936
  %.139 = or i64 %.75, %.69
  %.144 = or i64 %.139, %.100
  %.149 = or i64 %.144, %.138
  %.154 = or i64 %.149, %.168
  %.165 = or i64 %.154, %.171
  %.170 = or i64 %.165, %.122
  %.175 = or i64 %.170, %.164
  %.181 = lshr i64 %.11, 32
  %.220 = and i64 %.181, 16777215
  %.22230 = lshr i64 %.11, 56
  %.225 = shl nuw nsw i64 %.22230, 24
  %.226 = or i64 %.220, %.225
  %.249 = shl i64 %.11, 32
  %.250 = and i64 %.249, 1095216660480
  %.251 = or i64 %.226, %.250
  %.256 = and i64 %.249, 280375465082880
  %.257 = or i64 %.251, %.256
  %.262 = and i64 %.249, 71776119061217280
  %.263 = or i64 %.257, %.262
  %.265 = lshr i64 %.11, 24
  %.268 = shl i64 %.265, 56
  %.269 = or i64 %.263, %.268
  %.271 = add i64 %.175, %.269
  %.281 = lshr i64 %.271, 63
  %.313 = shl i64 %.271, 1
  %.314 = or i64 %.281, %.313
  ret i64 %.314
}

attributes #0 = { norecurse nounwind readnone }
