cmake_minimum_required(VERSION 3.20)

project(
    multiphaselbm
    LANGUAGES CXX CUDA)

set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_SOURCE_DIR}/executable)
set(CMAKE_EXPORT_COMPILE_COMMANDS ON)
make_directory(${CMAKE_SOURCE_DIR}/executable/output)

add_definitions(-Wall --std c++20) 

include(cmake/thrust.cmake)

include_directories(${CMAKE_SOURCE_DIR}/headers)
add_subdirectory(${CMAKE_SOURCE_DIR}/impl)