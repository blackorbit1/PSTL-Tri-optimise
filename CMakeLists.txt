cmake_minimum_required(VERSION 3.15)
project(sort)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_FLAGS "-O3")

find_package(benchmark REQUIRED)
find_package( Boost 1.40 COMPONENTS program_options REQUIRED )
include_directories( ${Boost_INCLUDE_DIR} )

add_executable(sort src/main.cpp include/MergingStategy.h
        include/RunFinder.h include/Sort.h include/Rules.h include/StackOfRun.h src/Generator.cpp include/Generator.h src/ToolBox.cpp include/ToolBox.h src/Bench.cpp include/Bench.h src/VectorGenerator.cpp include/VectorGenerator.h)

target_link_libraries(sort benchmark -lpthread ${Boost_LIBRARIES})