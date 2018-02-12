set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} --VirtualizeEncodeByteArray=true --VirtualizeObfuscateDecodeByteArray=false")

message("-- Virtualization obfuscate decode byte array: false")
foreach(TIGRESS_SAMPLE ${TIGRESS_SAMPLES})
    list(GET ${TIGRESS_SAMPLE} 0 TNAME)
    list(GET ${TIGRESS_SAMPLE} 1 TFILE)
    add_executable(${TNAME}-virt-obfuscate-decode-byte-array-false ${TFILE})
endforeach(TIGRESS_SAMPLE)
