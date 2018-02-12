set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} --VirtualizeDispatch=switch") # first level
set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} --Transform=Virtualize --Functions=SECRET --VirtualizeDispatch=switch") # second level
set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} --Transform=Virtualize --Functions=SECRET --VirtualizeDispatch=switch") # third level

message("-- Virtualization nested vm: 3")
foreach(TIGRESS_SAMPLE ${TIGRESS_SAMPLES})
    list(GET ${TIGRESS_SAMPLE} 0 TNAME)
    list(GET ${TIGRESS_SAMPLE} 1 TFILE)
    add_executable(${TNAME}-virt-nested-vm-3 ${TFILE})
endforeach(TIGRESS_SAMPLE)
