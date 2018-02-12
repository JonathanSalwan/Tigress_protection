; ModuleID = 'llvm_expressions/sample5-virt-operand-registers.ll'
source_filename = "llvm_expressions/sample5-virt-operand-registers.ll"
target datalayout = "e-m:e-i64:64-f80:128-n8:16:32:64-S128"
target triple = "x86_64-pc-linux-gnu"

; Function Attrs: norecurse nounwind readnone
define i64 @SECRET(i64 %SymVar_0) local_unnamed_addr #0 {
.3:
  %.10 = trunc i64 %SymVar_0 to i32
  %.11 = and i32 %.10, 255
  %.37 = mul nuw nsw i32 %.11, 1025
  %.53 = lshr i32 %.37, 6
  %.58 = xor i32 %.53, %.37
  %.67 = lshr i64 %SymVar_0, 8
  %.74 = trunc i64 %.67 to i32
  %.75 = and i32 %.74, 255
  %.80 = add nuw nsw i32 %.58, %.75
  %.101 = mul nuw nsw i32 %.80, 1025
  %.117 = lshr i32 %.101, 6
  %.122 = xor i32 %.117, %.101
  %.131 = lshr i64 %SymVar_0, 16
  %.138 = trunc i64 %.131 to i32
  %.139 = and i32 %.138, 255
  %.144 = add nuw i32 %.122, %.139
  %.165 = mul i32 %.144, 1025
  %.181 = lshr i32 %.165, 6
  %.186 = xor i32 %.181, %.165
  %.195 = lshr i64 %SymVar_0, 24
  %.202 = trunc i64 %.195 to i32
  %.203 = and i32 %.202, 255
  %.208 = add i32 %.186, %.203
  %.229 = mul i32 %.208, 1025
  %.245 = lshr i32 %.229, 6
  %.250 = xor i32 %.245, %.229
  %.259 = lshr i64 %SymVar_0, 32
  %.266 = trunc i64 %.259 to i32
  %.267 = and i32 %.266, 255
  %.272 = add i32 %.250, %.267
  %.293 = mul i32 %.272, 1025
  %.309 = lshr i32 %.293, 6
  %.314 = xor i32 %.309, %.293
  %.323 = lshr i64 %SymVar_0, 40
  %.330 = trunc i64 %.323 to i32
  %.331 = and i32 %.330, 255
  %.336 = add i32 %.314, %.331
  %.357 = mul i32 %.336, 1025
  %.373 = lshr i32 %.357, 6
  %.378 = xor i32 %.373, %.357
  %.387 = lshr i64 %SymVar_0, 48
  %.394 = trunc i64 %.387 to i32
  %.395 = and i32 %.394, 255
  %.400 = add i32 %.378, %.395
  %.421 = mul i32 %.400, 1025
  %.437 = lshr i32 %.421, 6
  %.442 = xor i32 %.437, %.421
  %.451 = lshr i64 %SymVar_0, 56
  %.458 = trunc i64 %.451 to i32
  %.464 = add i32 %.442, %.458
  %.485 = mul i32 %.464, 1025
  %.501 = lshr i32 %.485, 6
  %.506 = xor i32 %.501, %.485
  %.527 = mul i32 %.506, 9
  %.543 = lshr i32 %.527, 11
  %.548 = xor i32 %.543, %.527
  %.569 = mul i32 %.548, 32769
  %.582 = zext i32 %.569 to i64
  ret i64 %.582
}

attributes #0 = { norecurse nounwind readnone }
