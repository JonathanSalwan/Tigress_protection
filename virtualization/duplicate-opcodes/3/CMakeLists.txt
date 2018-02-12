set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} --VirtualizeDispatch=switch --VirtualizeMaxDuplicateOps=3")

message("-- Virtualization duplicate opcodes: 3")
foreach(TIGRESS_SAMPLE ${TIGRESS_SAMPLES})
    list(GET ${TIGRESS_SAMPLE} 0 TNAME)
    list(GET ${TIGRESS_SAMPLE} 1 TFILE)
    add_executable(${TNAME}-virt-duplicate-opcodes-3 ${TFILE})
endforeach(TIGRESS_SAMPLE)
