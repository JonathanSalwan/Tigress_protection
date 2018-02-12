cmake_minimum_required (VERSION 2.6)

set(TIGRESS_DIR ${CMAKE_SOURCE_DIR}/tigress-2.1)
set(TIGRESS_BIN ${CMAKE_BINARY_DIR}/scripts/tigress-compiler)
set(TIGRESS_HOME ${TIGRESS_DIR})

set(TIGRESS_SAMPLE3  sample3  ${CMAKE_SOURCE_DIR}/samples/sample3.c)      # md5
set(TIGRESS_SAMPLE4  sample4  ${CMAKE_SOURCE_DIR}/samples/sample4.c)      # adler32
set(TIGRESS_SAMPLE5  sample5  ${CMAKE_SOURCE_DIR}/samples/sample5.c)      # Jenkins's one-at-a-time
set(TIGRESS_SAMPLE8  sample8  ${CMAKE_SOURCE_DIR}/samples/sample8.c)      # SipHash
set(TIGRESS_SAMPLE10 sample10 ${CMAKE_SOURCE_DIR}/samples/sample10.c)     # xxhash
set(TIGRESS_SAMPLE11 sample11 ${CMAKE_SOURCE_DIR}/samples/sample11.c)     # SuperFastHash
set(TIGRESS_SAMPLE12 sample12 ${CMAKE_SOURCE_DIR}/samples/sample12.c)     # Fowler-Noll-Vo Hash (FNV1a)
set(TIGRESS_SAMPLE13 sample13 ${CMAKE_SOURCE_DIR}/samples/sample13.c)     # SpookyHash
set(TIGRESS_SAMPLE14 sample14 ${CMAKE_SOURCE_DIR}/samples/sample14.c)     # CityHash
set(TIGRESS_SAMPLE15 sample15 ${CMAKE_SOURCE_DIR}/samples/sample15.c)     # JodyHash

# We cannot leak these source files to not spoil the Tigress challenge :)
#set(TIGRESS_SAMPLE17 sample17 ${CMAKE_SOURCE_DIR}/samples/sample17.c)     # collberg 0001-0
#set(TIGRESS_SAMPLE18 sample18 ${CMAKE_SOURCE_DIR}/samples/sample18.c)     # collberg 0001-1
#set(TIGRESS_SAMPLE19 sample19 ${CMAKE_SOURCE_DIR}/samples/sample19.c)     # collberg 0001-2
#set(TIGRESS_SAMPLE20 sample20 ${CMAKE_SOURCE_DIR}/samples/sample20.c)     # collberg 0001-3
#set(TIGRESS_SAMPLE21 sample21 ${CMAKE_SOURCE_DIR}/samples/sample21.c)     # collberg 0001-4
#set(TIGRESS_SAMPLE22 sample22 ${CMAKE_SOURCE_DIR}/samples/sample22.c)     # collberg 0004-0
#set(TIGRESS_SAMPLE23 sample23 ${CMAKE_SOURCE_DIR}/samples/sample23.c)     # collberg 0004-1
#set(TIGRESS_SAMPLE24 sample24 ${CMAKE_SOURCE_DIR}/samples/sample24.c)     # collberg 0004-2
#set(TIGRESS_SAMPLE25 sample25 ${CMAKE_SOURCE_DIR}/samples/sample25.c)     # collberg 0004-3
#set(TIGRESS_SAMPLE26 sample26 ${CMAKE_SOURCE_DIR}/samples/sample26.c)     # collberg 0004-4

set(TIGRESS_SAMPLES
    TIGRESS_SAMPLE3
    TIGRESS_SAMPLE4
    TIGRESS_SAMPLE5
    TIGRESS_SAMPLE8
    TIGRESS_SAMPLE10
    TIGRESS_SAMPLE11
    TIGRESS_SAMPLE12
    TIGRESS_SAMPLE13
    TIGRESS_SAMPLE14
    TIGRESS_SAMPLE15
    #TIGRESS_SAMPLE17
    #TIGRESS_SAMPLE18
    #TIGRESS_SAMPLE19
    #TIGRESS_SAMPLE20
    #TIGRESS_SAMPLE21
    #TIGRESS_SAMPLE22
    #TIGRESS_SAMPLE23
    #TIGRESS_SAMPLE24
    #TIGRESS_SAMPLE25
    #TIGRESS_SAMPLE26
)

set(CMAKE_C_COMPILER ${TIGRESS_BIN})
set(ENV{TIGRESS_HOME} "${TIGRESS_HOME}")

configure_file(
    ${CMAKE_SOURCE_DIR}/scripts/tigress-compiler.in
    ${CMAKE_BINARY_DIR}/scripts/tigress-compiler
    IMMEDIATE @ONLY
)

project (tigress)

message("-- Tigress directory: ${TIGRESS_DIR}")
message("-- Tigress binary: ${TIGRESS_BIN}")

add_subdirectory(virtualization)
