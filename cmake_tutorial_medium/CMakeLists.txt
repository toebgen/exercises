cmake_minimum_required(VERSION 3.10)

project(CMakeHello)

# Disable in-source builds to prevent source tree corruption
if("${CMAKE_SOURCE_DIR}" STREQUAL "${CMAKE_BINARY_DIR}")
    message(FATAL_ERROR "In-Source builds are not allowed!")
endif()

if(${CMAKE_SYSTEM_NAME} MATCHES Darwin)
    add_definitions(-DCMAKEMACROSAMPLE="Apple MacOS")
elseif(${CMAKE_SYSTEM_NAME} MATCHES Windows)
    add_definitions(-DCMAKEMACROSAMPLE="Windows PC")
elseif(${CMAKE_SYSTEM_NAME} MATCHES Linux)
    add_definitions(-DCMAKEMACROSAMPLE="Linux")
endif()

if(${CMAKE_BUILD_TYPE} MATCHES Debug)
    message("Debug Build")
elseif(${CMAKE_BUILD_TYPE} MATCHES Release)
    message("Release Build")
else()
    message("Build type not defined")
endif()

set(CMAKE_CXX_STANDARD 14)

# Add flags, keep previously existing ones as well
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -Wall")

set(EXECUTABLE_OUTPUT_PATH ${CMAKE_BINARY_DIR}/bin)
set(LIBRARY_OUTPUT_PATH ${CMAKE_BINARY_DIR}/lib)

message(${CMAKE_BINARY_DIR})

add_subdirectory(lib/math)

add_executable(hello_world main.cpp)

find_package(Boost 1.65 REQUIRED)
message("Boost Found")
include_directories(${Boost_INCLUDE_DORS})
target_link_libraries(hello_world ${Boost_LIBRARIES})

target_link_libraries(hello_world math)
