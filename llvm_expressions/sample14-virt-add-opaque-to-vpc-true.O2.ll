; ModuleID = 'llvm_expressions/sample14-virt-add-opaque-to-vpc-true.ll'
source_filename = "llvm_expressions/sample14-virt-add-opaque-to-vpc-true.ll"
target datalayout = "e-m:e-i64:64-f80:128-n8:16:32:64-S128"
target triple = "x86_64-pc-linux-gnu"

; Function Attrs: norecurse nounwind readnone
define i64 @SECRET(i64 %SymVar_0) local_unnamed_addr #0 {
.3:
  %.4 = lshr i64 %SymVar_0, 32
  %.45 = shl i64 %SymVar_0, 3
  %.53 = and i64 %.45, 34359738360
  %.56 = add nuw nsw i64 %.53, 8
  %.57 = xor i64 %.56, %.4
  %.82 = mul i64 %.57, -7070675565921424023
  %.85 = lshr i64 %.82, 47
  %.86 = xor i64 %.82, %.4
  %.87 = xor i64 %.86, %.85
  %.112 = mul i64 %.87, -7070675565921424023
  %.115 = lshr i64 %.112, 47
  %.116 = xor i64 %.115, %.112
  %.141 = mul i64 %.116, -7070675565921424023
  ret i64 %.141
}

attributes #0 = { norecurse nounwind readnone }
