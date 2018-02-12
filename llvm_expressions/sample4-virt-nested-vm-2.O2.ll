; ModuleID = 'llvm_expressions/sample4-virt-nested-vm-2.ll'
source_filename = "llvm_expressions/sample4-virt-nested-vm-2.ll"
target datalayout = "e-m:e-i64:64-f80:128-n8:16:32:64-S128"
target triple = "x86_64-pc-linux-gnu"

; Function Attrs: norecurse nounwind readnone
define i64 @SECRET(i64 %SymVar_0) local_unnamed_addr #0 {
.3:
  %.4 = lshr i64 %SymVar_0, 56
  %.27 = lshr i64 %SymVar_0, 48
  %.41 = and i64 %.27, 255
  %.50 = lshr i64 %SymVar_0, 40
  %.64 = and i64 %.50, 255
  %.73 = lshr i64 %SymVar_0, 32
  %.87 = and i64 %.73, 255
  %.96 = lshr i64 %SymVar_0, 24
  %.110 = and i64 %.96, 255
  %.119 = lshr i64 %SymVar_0, 16
  %.133 = and i64 %.119, 255
  %.142 = lshr i64 %SymVar_0, 8
  %.156 = and i64 %.142, 255
  %.178 = and i64 %SymVar_0, 255
  %.187 = add nuw nsw i64 %.178, 1
  %.201 = urem i64 %.187, 65521
  %.221 = add nuw nsw i64 %.201, %.156
  %.235 = urem i64 %.221, 65521
  %.255 = add nuw nsw i64 %.235, %.133
  %.269 = urem i64 %.255, 65521
  %.289 = add nuw nsw i64 %.269, %.110
  %.303 = urem i64 %.289, 65521
  %.323 = add nuw nsw i64 %.303, %.87
  %.337 = urem i64 %.323, 65521
  %.357 = add nuw nsw i64 %.337, %.64
  %.371 = urem i64 %.357, 65521
  %.391 = add nuw nsw i64 %.371, %.41
  %.405 = urem i64 %.391, 65521
  %.425 = add nuw nsw i64 %.405, %.4
  %.439 = urem i64 %.425, 65521
  %.565 = add nuw nsw i64 %.235, %.201
  %.579 = urem i64 %.565, 65521
  %.599 = add nuw nsw i64 %.269, %.579
  %.613 = urem i64 %.599, 65521
  %.633 = add nuw nsw i64 %.303, %.613
  %.647 = urem i64 %.633, 65521
  %.667 = add nuw nsw i64 %.337, %.647
  %.681 = urem i64 %.667, 65521
  %.701 = add nuw nsw i64 %.371, %.681
  %.715 = urem i64 %.701, 65521
  %.735 = add nuw nsw i64 %.405, %.715
  %.749 = urem i64 %.735, 65521
  %.769 = add nuw nsw i64 %.439, %.749
  %.783 = urem i64 %.769, 65521
  %.805 = shl nuw nsw i64 %.783, 16
  %.816 = or i64 %.805, %.439
  ret i64 %.816
}

attributes #0 = { norecurse nounwind readnone }
