set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} --VirtualizeEncodeByteArray=true")

message("-- Virtualization encode byte array: true")
foreach(TIGRESS_SAMPLE ${TIGRESS_SAMPLES})
    list(GET ${TIGRESS_SAMPLE} 0 TNAME)
    list(GET ${TIGRESS_SAMPLE} 1 TFILE)
    add_executable(${TNAME}-virt-encode-byte-array-true ${TFILE})
endforeach(TIGRESS_SAMPLE)
