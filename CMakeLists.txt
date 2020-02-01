cmake_minimum_required(VERSION 3.15)
project(sort)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_FLAGS "-O2")

find_package(benchmark REQUIRED)


add_executable(sort src/main.cpp include/MergingStategy.h
        include/RunFinder.h include/Sort.h include/Rules.h include/StackOfRun.h src/Generator.cpp include/Generator.h src/ToolBox.cpp include/ToolBox.h)

target_link_libraries(sort benchmark -lpthread)