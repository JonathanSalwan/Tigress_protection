; ModuleID = ""
target triple = "x86_64-pc-linux-gnu"
target datalayout = ""

define i64 @"SECRET"(i64 %"SymVar_0") nounwind
{
.3:
  %".4" = zext i8 49 to i64
  %".5" = and i64 %".4", 63
  %".6" = lshr i64 %"SymVar_0", %".5"
  %".7" = zext i8 15 to i64
  %".8" = and i64 %".7", 63
  %".9" = shl i64 %"SymVar_0", %".8"
  %".10" = or i64 %".6", %".9"
  %".11" = and i64 63, %".10"
  %".12" = zext i8 4 to i64
  %".13" = and i64 %".12", 63
  %".14" = shl i64 %".11", %".13"
  %".15" = sub i64 %"SymVar_0", 1106879319
  %".16" = or i64 %".14", %".15"
  %".17" = sext i64 %".16" to i128
  %".18" = or i64 7625649618944, %"SymVar_0"
  %".19" = sext i64 %".18" to i128
  %".20" = mul i128 %".17", %".19"
  %".21" = trunc i128 %".20" to i64
  %".22" = and i64 %".10", %".18"
  %".23" = sext i64 %".22" to i128
  %".24" = zext i8 3 to i64
  %".25" = and i64 %".24", 63
  %".26" = lshr i64 %".15", %".25"
  %".27" = and i64 7, %".26"
  %".28" = or i64 1, %".27"
  %".29" = trunc i64 %".28" to i32
  %".30" = zext i32 %".29" to i64
  %".31" = trunc i64 %".30" to i8
  %".32" = zext i8 %".31" to i64
  %".33" = and i64 %".32", 63
  %".34" = lshr i64 %"SymVar_0", %".33"
  %".35" = sext i64 %".34" to i128
  %".36" = mul i128 %".23", %".35"
  %".37" = trunc i128 %".36" to i64
  %".38" = sext i64 %".37" to i128
  %".39" = sext i64 %".10" to i128
  %".40" = mul i128 %".38", %".39"
  %".41" = trunc i128 %".40" to i64
  %".42" = sub i64 %".21", %".41"
  %".43" = xor i64 %".41", %".42"
  %".44" = xor i64 %".21", %".43"
  %".45" = xor i64 %".21", %".42"
  %".46" = xor i64 %".21", %".41"
  %".47" = and i64 %".45", %".46"
  %".48" = xor i64 %".44", %".47"
  %".49" = lshr i64 %".48", 63
  %".50" = trunc i64 %".49" to i1
  %".51" = xor i1 %".50", -1
  %".52" = icmp eq i64 %".42", 0
  br i1 %".52", label %".3.if", label %".3.else"
.3.if:
  br label %".3.endif"
.3.else:
  br label %".3.endif"
.3.endif:
  %".56" = phi i1 [1, %".3.if"], [0, %".3.else"]
  %".57" = xor i1 %".56", -1
  %".58" = and i1 %".51", %".57"
  %".59" = icmp eq i1 %".58", 1
  br i1 %".59", label %".3.endif.if", label %".3.endif.else"
.3.endif.if:
  br label %".3.endif.endif"
.3.endif.else:
  br label %".3.endif.endif"
.3.endif.endif:
  %".63" = phi i8 [1, %".3.endif.if"], [0, %".3.endif.else"]
  %".64" = zext i8 %".63" to i64
  %".65" = lshr i64 %".41", 8
  %".66" = trunc i64 %".65" to i56
  %".67" = zext i56 %".66" to i64
  %".68" = shl i64 %".67", 8
  %".69" = or i64 %".64", %".68"
  %".70" = trunc i64 %".69" to i8
  %".71" = zext i8 %".70" to i32
  %".72" = zext i32 %".71" to i64
  %".73" = trunc i64 %".72" to i32
  %".74" = zext i32 %".73" to i64
  %".75" = trunc i64 %".74" to i32
  %".76" = sub i32 %".75", 0
  %".77" = icmp eq i32 %".76", 0
  br i1 %".77", label %".3.endif.endif.if", label %".3.endif.endif.else"
.3.endif.endif.if:
  br label %".3.endif.endif.endif"
.3.endif.endif.else:
  br label %".3.endif.endif.endif"
.3.endif.endif.endif:
  %".81" = phi i1 [1, %".3.endif.endif.if"], [0, %".3.endif.endif.else"]
  %".82" = icmp eq i1 %".81", 0
  br i1 %".82", label %".3.endif.endif.endif.if", label %".3.endif.endif.endif.else"
.3.endif.endif.endif.if:
  br label %".3.endif.endif.endif.endif"
.3.endif.endif.endif.else:
  br label %".3.endif.endif.endif.endif"
.3.endif.endif.endif.endif:
  %".86" = phi i8 [1, %".3.endif.endif.endif.if"], [0, %".3.endif.endif.endif.else"]
  %".87" = zext i8 %".86" to i64
  %".88" = lshr i64 0, 8
  %".89" = trunc i64 %".88" to i56
  %".90" = zext i56 %".89" to i64
  %".91" = shl i64 %".90", 8
  %".92" = or i64 %".87", %".91"
  %".93" = trunc i64 %".92" to i8
  %".94" = zext i8 %".93" to i32
  %".95" = zext i32 %".94" to i64
  %".96" = trunc i64 %".95" to i32
  %".97" = zext i32 %".96" to i64
  %".98" = trunc i64 %".97" to i32
  %".99" = trunc i64 %".97" to i32
  %".100" = and i32 %".98", %".99"
  %".101" = icmp eq i32 %".100", 0
  br i1 %".101", label %".3.endif.endif.endif.endif.if", label %".3.endif.endif.endif.endif.else"
.3.endif.endif.endif.endif.if:
  br label %".3.endif.endif.endif.endif.endif"
.3.endif.endif.endif.endif.else:
  br label %".3.endif.endif.endif.endif.endif"
.3.endif.endif.endif.endif.endif:
  %".105" = phi i1 [1, %".3.endif.endif.endif.endif.if"], [0, %".3.endif.endif.endif.endif.else"]
  %".106" = icmp eq i1 %".105", 1
  br i1 %".106", label %".3.endif.endif.endif.endif.endif.if", label %".3.endif.endif.endif.endif.endif.else"
.3.endif.endif.endif.endif.endif.if:
  br label %".3.endif.endif.endif.endif.endif.endif"
.3.endif.endif.endif.endif.endif.else:
  br label %".3.endif.endif.endif.endif.endif.endif"
.3.endif.endif.endif.endif.endif.endif:
  %".110" = phi i1 [1, %".3.endif.endif.endif.endif.endif.if"], [0, %".3.endif.endif.endif.endif.endif.else"]
  br i1 %".110", label %".3.endif.endif.endif.endif.endif.endif.if", label %".3.endif.endif.endif.endif.endif.endif.else"
.3.endif.endif.endif.endif.endif.endif.if:
  %".112" = zext i8 49 to i64
  %".113" = and i64 %".112", 63
  %".114" = lshr i64 %"SymVar_0", %".113"
  %".115" = zext i8 15 to i64
  %".116" = and i64 %".115", 63
  %".117" = shl i64 %"SymVar_0", %".116"
  %".118" = or i64 %".114", %".117"
  %".119" = or i64 7625649618944, %"SymVar_0"
  %".120" = and i64 15, %".119"
  %".121" = zext i8 2 to i64
  %".122" = and i64 %".121", 63
  %".123" = shl i64 %".120", %".122"
  %".124" = and i64 %".118", %".119"
  %".125" = sext i64 %".124" to i128
  %".126" = sub i64 %"SymVar_0", 1106879319
  %".127" = zext i8 3 to i64
  %".128" = and i64 %".127", 63
  %".129" = lshr i64 %".126", %".128"
  %".130" = and i64 7, %".129"
  %".131" = or i64 1, %".130"
  %".132" = trunc i64 %".131" to i32
  %".133" = zext i32 %".132" to i64
  %".134" = trunc i64 %".133" to i8
  %".135" = zext i8 %".134" to i64
  %".136" = and i64 %".135", 63
  %".137" = lshr i64 %"SymVar_0", %".136"
  %".138" = sext i64 %".137" to i128
  %".139" = mul i128 %".125", %".138"
  %".140" = trunc i128 %".139" to i64
  %".141" = or i64 %".123", %".140"
  %".142" = trunc i64 %".141" to i8
  %".143" = zext i8 %".142" to i32
  %".144" = lshr i64 %".141", 8
  %".145" = trunc i64 %".144" to i8
  %".146" = zext i8 %".145" to i32
  %".147" = shl i32 %".146", 8
  %".148" = or i32 %".143", %".147"
  %".149" = lshr i64 %".141", 16
  %".150" = trunc i64 %".149" to i8
  %".151" = zext i8 %".150" to i32
  %".152" = shl i32 %".151", 16
  %".153" = or i32 %".148", %".152"
  %".154" = lshr i64 %".141", 24
  %".155" = trunc i64 %".154" to i8
  %".156" = zext i8 %".155" to i32
  %".157" = shl i32 %".156", 24
  %".158" = or i32 %".153", %".157"
  %".159" = zext i32 %".158" to i64
  %".160" = trunc i64 %".159" to i32
  %".161" = zext i32 %".160" to i64
  %".162" = trunc i64 %".161" to i32
  %".163" = zext i32 %".162" to i64
  %".164" = trunc i64 %".163" to i32
  %".165" = zext i32 %".164" to i64
  %".166" = trunc i64 %".165" to i32
  %".167" = zext i32 %".166" to i64
  %".168" = trunc i64 %".167" to i32
  %".169" = zext i32 %".168" to i64
  %".170" = trunc i64 %".169" to i32
  %".171" = zext i32 %".170" to i64
  %".172" = trunc i64 %".171" to i32
  %".173" = zext i32 %".172" to i64
  %".174" = trunc i64 %".173" to i32
  %".175" = zext i32 %".174" to i64
  %".176" = trunc i64 %".175" to i32
  %".177" = zext i32 %".176" to i64
  %".178" = trunc i64 %".177" to i32
  %".179" = zext i32 %".178" to i64
  %".180" = trunc i64 %".179" to i32
  %".181" = zext i32 %".180" to i64
  %".182" = trunc i64 %".181" to i32
  %".183" = trunc i32 %".182" to i8
  %".184" = zext i8 %".183" to i64
  %".185" = trunc i64 %".181" to i32
  %".186" = lshr i32 %".185", 8
  %".187" = trunc i32 %".186" to i8
  %".188" = zext i8 %".187" to i64
  %".189" = shl i64 %".188", 8
  %".190" = or i64 %".184", %".189"
  %".191" = trunc i64 %".181" to i32
  %".192" = lshr i32 %".191", 16
  %".193" = trunc i32 %".192" to i8
  %".194" = zext i8 %".193" to i64
  %".195" = shl i64 %".194", 16
  %".196" = or i64 %".190", %".195"
  %".197" = trunc i64 %".181" to i32
  %".198" = lshr i32 %".197", 24
  %".199" = trunc i32 %".198" to i8
  %".200" = zext i8 %".199" to i64
  %".201" = shl i64 %".200", 24
  %".202" = or i64 %".196", %".201"
  %".203" = lshr i64 %".141", 32
  %".204" = trunc i64 %".203" to i8
  %".205" = zext i8 %".204" to i32
  %".206" = lshr i64 %".141", 40
  %".207" = trunc i64 %".206" to i8
  %".208" = zext i8 %".207" to i32
  %".209" = shl i32 %".208", 8
  %".210" = or i32 %".205", %".209"
  %".211" = lshr i64 %".141", 48
  %".212" = trunc i64 %".211" to i8
  %".213" = zext i8 %".212" to i32
  %".214" = shl i32 %".213", 16
  %".215" = or i32 %".210", %".214"
  %".216" = lshr i64 %".141", 56
  %".217" = trunc i64 %".216" to i8
  %".218" = zext i8 %".217" to i32
  %".219" = shl i32 %".218", 24
  %".220" = or i32 %".215", %".219"
  %".221" = zext i32 %".220" to i64
  %".222" = trunc i64 %".221" to i32
  %".223" = zext i32 %".222" to i64
  %".224" = trunc i64 %".223" to i32
  %".225" = zext i32 %".224" to i64
  %".226" = trunc i64 %".225" to i32
  %".227" = zext i32 %".226" to i64
  %".228" = trunc i64 %".227" to i32
  %".229" = zext i32 %".228" to i64
  %".230" = trunc i64 %".229" to i32
  %".231" = zext i32 %".230" to i64
  %".232" = trunc i64 %".231" to i32
  %".233" = zext i32 %".232" to i64
  %".234" = trunc i64 %".233" to i32
  %".235" = zext i32 %".234" to i64
  %".236" = trunc i64 %".235" to i32
  %".237" = zext i32 %".236" to i64
  %".238" = trunc i64 %".237" to i32
  %".239" = zext i32 %".238" to i64
  %".240" = trunc i64 %".239" to i32
  %".241" = zext i32 %".240" to i64
  %".242" = trunc i64 %".241" to i32
  %".243" = zext i32 %".242" to i64
  %".244" = trunc i64 %".243" to i32
  %".245" = trunc i32 %".244" to i8
  %".246" = zext i8 %".245" to i64
  %".247" = shl i64 %".246", 32
  %".248" = or i64 %".202", %".247"
  %".249" = trunc i64 %".243" to i32
  %".250" = lshr i32 %".249", 8
  %".251" = trunc i32 %".250" to i8
  %".252" = zext i8 %".251" to i64
  %".253" = shl i64 %".252", 40
  %".254" = or i64 %".248", %".253"
  %".255" = trunc i64 %".243" to i32
  %".256" = lshr i32 %".255", 16
  %".257" = trunc i32 %".256" to i8
  %".258" = zext i8 %".257" to i64
  %".259" = shl i64 %".258", 48
  %".260" = or i64 %".254", %".259"
  %".261" = trunc i64 %".243" to i32
  %".262" = lshr i32 %".261", 24
  %".263" = trunc i32 %".262" to i8
  %".264" = zext i8 %".263" to i64
  %".265" = shl i64 %".264", 56
  %".266" = or i64 %".260", %".265"
  %".267" = sub i64 %".118", %".266"
  %".268" = and i64 63, %".118"
  %".269" = zext i8 4 to i64
  %".270" = and i64 %".269", 63
  %".271" = shl i64 %".268", %".270"
  %".272" = or i64 %".271", %".126"
  %".273" = xor i64 %".272", %".119"
  %".274" = or i64 %".267", %".273"
  br label %".3.endif.endif.endif.endif.endif.endif.endif"
.3.endif.endif.endif.endif.endif.endif.else:
  %".276" = zext i8 49 to i64
  %".277" = and i64 %".276", 63
  %".278" = lshr i64 %"SymVar_0", %".277"
  %".279" = zext i8 15 to i64
  %".280" = and i64 %".279", 63
  %".281" = shl i64 %"SymVar_0", %".280"
  %".282" = or i64 %".278", %".281"
  %".283" = or i64 7625649618944, %"SymVar_0"
  %".284" = and i64 %".282", %".283"
  %".285" = sext i64 %".284" to i128
  %".286" = sub i64 %"SymVar_0", 1106879319
  %".287" = zext i8 3 to i64
  %".288" = and i64 %".287", 63
  %".289" = lshr i64 %".286", %".288"
  %".290" = and i64 7, %".289"
  %".291" = or i64 1, %".290"
  %".292" = trunc i64 %".291" to i32
  %".293" = zext i32 %".292" to i64
  %".294" = trunc i64 %".293" to i8
  %".295" = zext i8 %".294" to i64
  %".296" = and i64 %".295", 63
  %".297" = lshr i64 %"SymVar_0", %".296"
  %".298" = sext i64 %".297" to i128
  %".299" = mul i128 %".285", %".298"
  %".300" = trunc i128 %".299" to i64
  %".301" = sub i64 %".282", %".300"
  %".302" = and i64 63, %".282"
  %".303" = zext i8 4 to i64
  %".304" = and i64 %".303", 63
  %".305" = shl i64 %".302", %".304"
  %".306" = or i64 %".305", %".286"
  %".307" = xor i64 %".306", %".283"
  %".308" = or i64 %".301", %".307"
  br label %".3.endif.endif.endif.endif.endif.endif.endif"
.3.endif.endif.endif.endif.endif.endif.endif:
  %".310" = phi i64 [%".274", %".3.endif.endif.endif.endif.endif.endif.if"], [%".308", %".3.endif.endif.endif.endif.endif.endif.else"]
  ret i64 %".310"
}
