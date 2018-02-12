set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} --VirtualizeDispatch=switch --VirtualizeSuperOpsRatio=0.8")

message("-- Virtualization super operators ratio: 0.8")
foreach(TIGRESS_SAMPLE ${TIGRESS_SAMPLES})
    list(GET ${TIGRESS_SAMPLE} 0 TNAME)
    list(GET ${TIGRESS_SAMPLE} 1 TFILE)
    add_executable(${TNAME}-virt-super-operators-ratio-0.8 ${TFILE})
endforeach(TIGRESS_SAMPLE)
