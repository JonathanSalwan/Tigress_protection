set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} --VirtualizeAddOpaqueToVPC=false")

message("-- Virtualization add opaque to VPC: false")
foreach(TIGRESS_SAMPLE ${TIGRESS_SAMPLES})
    list(GET ${TIGRESS_SAMPLE} 0 TNAME)
    list(GET ${TIGRESS_SAMPLE} 1 TFILE)
    add_executable(${TNAME}-virt-add-opaque-to-vpc-false ${TFILE})
endforeach(TIGRESS_SAMPLE)
