set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} --VirtualizeDispatch=switch --VirtualizeOperands=stack")

message("-- Virtualization operand: stack")
foreach(TIGRESS_SAMPLE ${TIGRESS_SAMPLES})
    list(GET ${TIGRESS_SAMPLE} 0 TNAME)
    list(GET ${TIGRESS_SAMPLE} 1 TFILE)
    add_executable(${TNAME}-virt-operand-stack ${TFILE})
endforeach(TIGRESS_SAMPLE)
