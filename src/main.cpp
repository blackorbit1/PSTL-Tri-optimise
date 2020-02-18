//
// Created by bruno on 24/01/2020.
//

//#define MY_BENCH_EXEC

#ifndef MY_BENCH_EXEC
#include "../include/Generator.h"

#include <benchmark/benchmark.h>
#include <vector>
#include <iostream>
#include <random>
#include "../include/MergingStategy.h"
#include "../include/RunFinder.h"
#include "../include/Sort.h"
#include "../include/Rules.h"
#include "../include/Bench.h"
#include <boost/program_options.hpp>
// sudo apt install libboost-program-options-dev

namespace po = boost::program_options;


static void BM_std_sortOnInt(benchmark::State& state){
    std::vector<int>* vect = nullptr;

    for (auto _ : state){
        state.PauseTiming();
        vect = genRandomInt(2<<12);
        state.ResumeTiming();
        std::sort((*vect).begin(), (*vect).end());

        state.PauseTiming();
        delete vect;
        state.ResumeTiming();
    }
}

int main(int argc, char* argv[]){
    std::string file;

    po::options_description desc("Allowed options");
    desc.add_options()
            ("help,h", "produce help message")
            ("file,f", po::value<std::string>(&file), "file with array to bench")
            ;

    po::variables_map vm;
    try {
        po::store(parse_command_line(argc, argv, desc), vm);
    }
    catch (std::exception &e){
        ; // it's okayyy
    }
    po::notify(vm);
    if (vm.count("help")) {
        std::cout << desc << "\n";
        return 0;
    }

    if (vm.count("file")) {
        launchBench("../files/test.tab", argc, argv);
        return 0;
    }
//
//
//    const int max = 100000;
//    std::random_device rd;
//    std::mt19937 mt(rd());
//    std::uniform_int_distribution<> dis(0, max*2);
//
//    std::vector<int> vect(max);
//    std::generate(vect.begin(), vect.end(), std::bind(dis, std::ref(mt)));
//
//    adaptativeShiverSort(vect);
//
//    assert(std::is_sorted(vect.begin(), vect.end()));
//    return 0;
}

//
//int main(int argc, char** argv){
//    int k = 2;
//
//    BENCHMARK(BM_std_sortOnInt);
//    BENCHMARK(BM_std_sortOnInt);
//    ::benchmark::Initialize(&argc, argv);
//    ::benchmark::RunSpecifiedBenchmarks();
//}

#else

#include <benchmark/benchmark.h>
#include "../include/Generator.h"
#include "../include/Sort.h"

static void BM_std_sortOnInt(benchmark::State& state){
    std::vector<int>* vect = nullptr;
    
    for (auto _ : state){
        state.PauseTiming();
        vect = genRandomInt(state.range(0));
        state.ResumeTiming();
        std::sort((*vect).begin(), (*vect).end());

        state.PauseTiming();
        delete vect;
        state.ResumeTiming();
    }
}

BENCHMARK(BM_std_sortOnInt)->RangeMultiplier(2)->Range(8<<8, 8<<12);


static void BM_shiverSortOnRandomInt(benchmark::State& state){
    std::vector<int>* vect = nullptr;

    for (auto _ : state){
        state.PauseTiming();
        vect = genRandomInt(state.range(0));
        state.ResumeTiming();
        shiverSort(*vect);

        state.PauseTiming();
        delete vect;
        vect = nullptr;
        state.ResumeTiming();
    }
}

BENCHMARK(BM_shiverSortOnRandomInt)->RangeMultiplier(2)->Range(8<<8, 8<<12);


static void BM_adaptativeShiverSortOnRandomInt(benchmark::State& state){
    std::vector<int>* vect = nullptr;

    for (auto _ : state){
        state.PauseTiming();
        vect = genRandomInt(state.range(0));
        state.ResumeTiming();
        adaptativeShiverSort(*vect);

        state.PauseTiming();
        delete vect;
        vect = nullptr;
        state.ResumeTiming();
    }
}

BENCHMARK(BM_adaptativeShiverSortOnRandomInt)->RangeMultiplier(2)->Range(8<<8, 8<<12);


static void BM_TimSortOnRandomInt(benchmark::State& state){
    std::vector<int>* vect = nullptr;

    for (auto _ : state){
        state.PauseTiming();
        vect = genRandomInt(state.range(0));
        state.ResumeTiming();
        timSort(*vect);

        state.PauseTiming();
        delete vect;
        vect = nullptr;
        state.ResumeTiming();
    }
}

BENCHMARK(BM_TimSortOnRandomInt)->RangeMultiplier(2)->Range(8<<8, 8<<12);
BENCHMARK_MAIN();

#endif // MY_BENCH_EXEC