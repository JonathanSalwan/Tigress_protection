set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} --VirtualizeAddOpaqueToVPC=true")

message("-- Virtualization add opaque to VPC: true")
foreach(TIGRESS_SAMPLE ${TIGRESS_SAMPLES})
    list(GET ${TIGRESS_SAMPLE} 0 TNAME)
    list(GET ${TIGRESS_SAMPLE} 1 TFILE)
    add_executable(${TNAME}-virt-add-opaque-to-vpc-true ${TFILE})
endforeach(TIGRESS_SAMPLE)
