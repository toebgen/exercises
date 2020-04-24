cmake_minimum_required(VERSION 3.10)

set(LIBRARY_OUTPUT_PATH ${CMAKE_BINARY_DIR}/lib)

add_library(math SHARED operations.cpp)