set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} --AntiBranchAnalysisKinds=branchFuns")

message("-- Virtualization and anti branch analysis: branchFuns")
foreach(TIGRESS_SAMPLE ${TIGRESS_SAMPLES})
    list(GET ${TIGRESS_SAMPLE} 0 TNAME)
    list(GET ${TIGRESS_SAMPLE} 1 TFILE)
    add_executable(${TNAME}-virt-anti-branch-analysis-branchFuns ${TFILE})
endforeach(TIGRESS_SAMPLE)
