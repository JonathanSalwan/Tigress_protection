set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} --VirtualizeBogusLoopIterations=2")

message("-- Virtualization number of bogus loop iterations: 2")
foreach(TIGRESS_SAMPLE ${TIGRESS_SAMPLES})
    list(GET ${TIGRESS_SAMPLE} 0 TNAME)
    list(GET ${TIGRESS_SAMPLE} 1 TFILE)
    add_executable(${TNAME}-virt-bogus-loop-iterations-2 ${TFILE})
endforeach(TIGRESS_SAMPLE)
