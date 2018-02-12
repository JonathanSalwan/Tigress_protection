set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} --VirtualizeDispatch=switch --VirtualizeRandomOps=true")

message("-- Virtualization random opcodes: yes")
foreach(TIGRESS_SAMPLE ${TIGRESS_SAMPLES})
    list(GET ${TIGRESS_SAMPLE} 0 TNAME)
    list(GET ${TIGRESS_SAMPLE} 1 TFILE)
    add_executable(${TNAME}-virt-random-opcodes-true ${TFILE})
endforeach(TIGRESS_SAMPLE)
