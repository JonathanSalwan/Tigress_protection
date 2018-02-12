set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} --VirtualizeNumberOfBogusFuns=1")

message("-- Virtualization number of bogus functions: 1")
foreach(TIGRESS_SAMPLE ${TIGRESS_SAMPLES})
    list(GET ${TIGRESS_SAMPLE} 0 TNAME)
    list(GET ${TIGRESS_SAMPLE} 1 TFILE)
    add_executable(${TNAME}-virt-bogus-functions-1 ${TFILE})
endforeach(TIGRESS_SAMPLE)
