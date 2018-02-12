set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} --Transform=InitBranchFuns --Transform=AntiBranchAnalysis --Functions=SECRET")
set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -fPIC")
set(CMAKE_EXE_LINKER_FLAGS "${CMAKE_EXE_LINKER_FLAGS} -fPIC")

add_subdirectory(branchFuns)
add_subdirectory(goto2call)
add_subdirectory(goto2push)
