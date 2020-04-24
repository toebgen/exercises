cmake_minimum_required(VERSION 3.9.1)

project(CMakeHello)

set(CMAKE_CXX_STANDARD 14)
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -Wall")

set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/bin)

# Disable in-source builds to prevent source tree corruption
if("${CMAKE_SOURCE_DIR}" STREQUAL "${CMAKE_BINARY_DIR}")
    message(FATAL_ERROR "In-Source builds are not allowed!")
endif()

if(UNIX)
	message("This is a ${CMAKE_SYSTEM_NAME} system")
elseif(WIN32)
	message("This is a Windows System")
endif()

if(${CMAKE_SYSTEM_NAME} MATCHES Darwin)
	add_definitions(-DCMAKEMACROSAMPLE="Apple MacOS")
elseif(${CMAKE_SYSTEM_NAME} MATCHES Windows)
	add_definitions(-DCMAKEMACROSAMPLE="Windows PC")
elseif(${CMAKE_SYSTEM_NAME} MATCHES Linux)
	add_definitions(-DCMAKEMACROSAMPLE="Linux")
endif()

add_executable(hello_world main.cpp)
