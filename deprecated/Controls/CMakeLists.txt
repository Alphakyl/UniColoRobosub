cmake_minimum_required(VERSION 3.1)
project(Controls)

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11")

set(SOURCE_FILES
    PID.cpp)

add_executable(Controls ${SOURCE_FILES} PID.h main.h main.cpp)