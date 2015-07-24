project(dvl)
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11")
add_executable(dvl dvl.cpp pd5Com.cpp dvlSerial.cpp)
