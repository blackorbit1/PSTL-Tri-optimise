cmake_minimum_required(VERSION 3.15)
project(sort)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_FLAGS "-O2")

add_executable(sort src/main.cpp include/MergingStategy.h src/Benchmark.cpp include/Benchmark.h include/RunFinder.h include/Sort.h include/Rules.h include/Stack.h)