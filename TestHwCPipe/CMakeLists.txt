message("Before 'cmake_minimum_required'")
cmake_minimum_required(VERSION 3.13)
project(example)

set(SOURCE_FILES main.cpp)
add_executable(example ${SOURCE_FILES})

add_subdirectory(./HWCPipe)

