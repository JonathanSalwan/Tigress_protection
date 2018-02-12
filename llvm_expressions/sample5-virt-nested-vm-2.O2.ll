; ModuleID = 'llvm_expressions/sample5-virt-nested-vm-2.ll'
source_filename = "llvm_expressions/sample5-virt-nested-vm-2.ll"
target datalayout = "e-m:e-i64:64-f80:128-n8:16:32:64-S128"
target triple = "x86_64-pc-linux-gnu"

; Function Attrs: norecurse nounwind readnone
define i64 @SECRET(i64 %SymVar_0) local_unnamed_addr #0 {
.3:
  %.4 = lshr i64 %SymVar_0, 56
  %.17 = trunc i64 %.4 to i32
  %.27 = lshr i64 %SymVar_0, 48
  %.40 = trunc i64 %.27 to i32
  %.41 = and i32 %.40, 255
  %.50 = lshr i64 %SymVar_0, 40
  %.63 = trunc i64 %.50 to i32
  %.64 = and i32 %.63, 255
  %.73 = lshr i64 %SymVar_0, 32
  %.86 = trunc i64 %.73 to i32
  %.87 = and i32 %.86, 255
  %.96 = lshr i64 %SymVar_0, 24
  %.109 = trunc i64 %.96 to i32
  %.110 = and i32 %.109, 255
  %.119 = lshr i64 %SymVar_0, 16
  %.132 = trunc i64 %.119 to i32
  %.133 = and i32 %.132, 255
  %.142 = lshr i64 %SymVar_0, 8
  %.155 = trunc i64 %.142 to i32
  %.156 = and i32 %.155, 255
  %.177 = trunc i64 %SymVar_0 to i32
  %.178 = and i32 %.177, 255
  %.226 = mul nuw nsw i32 %.178, 1025
  %.245 = lshr i32 %.226, 6
  %.265 = xor i32 %.245, %.226
  %.282 = add nuw nsw i32 %.265, %.156
  %.321 = mul nuw nsw i32 %.282, 1025
  %.340 = lshr i32 %.321, 6
  %.360 = xor i32 %.340, %.321
  %.377 = add nuw i32 %.360, %.133
  %.416 = mul i32 %.377, 1025
  %.435 = lshr i32 %.416, 6
  %.455 = xor i32 %.435, %.416
  %.472 = add i32 %.455, %.110
  %.511 = mul i32 %.472, 1025
  %.530 = lshr i32 %.511, 6
  %.550 = xor i32 %.530, %.511
  %.567 = add i32 %.550, %.87
  %.606 = mul i32 %.567, 1025
  %.625 = lshr i32 %.606, 6
  %.645 = xor i32 %.625, %.606
  %.662 = add i32 %.645, %.64
  %.701 = mul i32 %.662, 1025
  %.720 = lshr i32 %.701, 6
  %.740 = xor i32 %.720, %.701
  %.757 = add i32 %.740, %.41
  %.796 = mul i32 %.757, 1025
  %.815 = lshr i32 %.796, 6
  %.835 = xor i32 %.815, %.796
  %.852 = add i32 %.835, %.17
  %.891 = mul i32 %.852, 1025
  %.910 = lshr i32 %.891, 6
  %.930 = xor i32 %.910, %.891
  %.969 = mul i32 %.930, 9
  %.988 = lshr i32 %.969, 11
  %.1008 = xor i32 %.988, %.969
  %.1047 = mul i32 %.1008, 32769
  %.1072 = zext i32 %.1047 to i64
  ret i64 %.1072
}

attributes #0 = { norecurse nounwind readnone }
