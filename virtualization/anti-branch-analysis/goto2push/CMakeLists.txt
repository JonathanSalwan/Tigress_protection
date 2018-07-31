set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -no-pie --AntiBranchAnalysisKinds=goto2push")

message("-- Virtualization and anti branch analysis: goto2push")
foreach(TIGRESS_SAMPLE ${TIGRESS_SAMPLES})
    list(GET ${TIGRESS_SAMPLE} 0 TNAME)
    list(GET ${TIGRESS_SAMPLE} 1 TFILE)
    add_executable(${TNAME}-virt-anti-branch-analysis-goto2push ${TFILE})
endforeach(TIGRESS_SAMPLE)
