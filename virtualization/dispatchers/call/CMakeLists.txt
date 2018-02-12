set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} --VirtualizeDispatch=call")

message("-- Virtualization dispatcher: call")
foreach(TIGRESS_SAMPLE ${TIGRESS_SAMPLES})
    list(GET ${TIGRESS_SAMPLE} 0 TNAME)
    list(GET ${TIGRESS_SAMPLE} 1 TFILE)
    add_executable(${TNAME}-virt-dispatcher-call ${TFILE})
endforeach(TIGRESS_SAMPLE)
