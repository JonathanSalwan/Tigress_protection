set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} --VirtualizeNumberOfBogusFuns=0")

message("-- Virtualization number of bogus functions: 0")
foreach(TIGRESS_SAMPLE ${TIGRESS_SAMPLES})
    list(GET ${TIGRESS_SAMPLE} 0 TNAME)
    list(GET ${TIGRESS_SAMPLE} 1 TFILE)
    add_executable(${TNAME}-virt-bogus-functions-0 ${TFILE})
endforeach(TIGRESS_SAMPLE)
