; ModuleID = 'llvm_expressions/sample5-virt-duplicate-opcodes-3.ll'
source_filename = "llvm_expressions/sample5-virt-duplicate-opcodes-3.ll"
target datalayout = "e-m:e-i64:64-f80:128-n8:16:32:64-S128"
target triple = "x86_64-pc-linux-gnu"

; Function Attrs: norecurse nounwind readnone
define i64 @SECRET(i64 %SymVar_0) local_unnamed_addr #0 {
.3:
  %.4 = lshr i64 %SymVar_0, 56
  %.11 = trunc i64 %.4 to i32
  %.17 = lshr i64 %SymVar_0, 48
  %.24 = trunc i64 %.17 to i32
  %.25 = and i32 %.24, 255
  %.30 = lshr i64 %SymVar_0, 40
  %.37 = trunc i64 %.30 to i32
  %.38 = and i32 %.37, 255
  %.43 = lshr i64 %SymVar_0, 32
  %.50 = trunc i64 %.43 to i32
  %.51 = and i32 %.50, 255
  %.56 = lshr i64 %SymVar_0, 24
  %.63 = trunc i64 %.56 to i32
  %.64 = and i32 %.63, 255
  %.69 = lshr i64 %SymVar_0, 16
  %.76 = trunc i64 %.69 to i32
  %.77 = and i32 %.76, 255
  %.82 = lshr i64 %SymVar_0, 8
  %.89 = trunc i64 %.82 to i32
  %.90 = and i32 %.89, 255
  %.101 = trunc i64 %SymVar_0 to i32
  %.102 = and i32 %.101, 255
  %.130 = mul nuw nsw i32 %.102, 1025
  %.141 = lshr i32 %.130, 6
  %.153 = xor i32 %.141, %.130
  %.162 = add nuw nsw i32 %.153, %.90
  %.185 = mul nuw nsw i32 %.162, 1025
  %.196 = lshr i32 %.185, 6
  %.208 = xor i32 %.196, %.185
  %.217 = add nuw i32 %.208, %.77
  %.240 = mul i32 %.217, 1025
  %.251 = lshr i32 %.240, 6
  %.263 = xor i32 %.251, %.240
  %.272 = add i32 %.263, %.64
  %.295 = mul i32 %.272, 1025
  %.306 = lshr i32 %.295, 6
  %.318 = xor i32 %.306, %.295
  %.327 = add i32 %.318, %.51
  %.350 = mul i32 %.327, 1025
  %.361 = lshr i32 %.350, 6
  %.373 = xor i32 %.361, %.350
  %.382 = add i32 %.373, %.38
  %.405 = mul i32 %.382, 1025
  %.416 = lshr i32 %.405, 6
  %.428 = xor i32 %.416, %.405
  %.437 = add i32 %.428, %.25
  %.460 = mul i32 %.437, 1025
  %.471 = lshr i32 %.460, 6
  %.483 = xor i32 %.471, %.460
  %.492 = add i32 %.483, %.11
  %.515 = mul i32 %.492, 1025
  %.526 = lshr i32 %.515, 6
  %.538 = xor i32 %.526, %.515
  %.561 = mul i32 %.538, 9
  %.572 = lshr i32 %.561, 11
  %.584 = xor i32 %.572, %.561
  %.607 = mul i32 %.584, 32769
  %.620 = zext i32 %.607 to i64
  ret i64 %.620
}

attributes #0 = { norecurse nounwind readnone }
