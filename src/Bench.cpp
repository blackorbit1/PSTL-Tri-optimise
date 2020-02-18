//
// Created by bruno on 15/02/2020.
//

#include "../include/Bench.h"
#include "../include/Sort.h"
#include <fstream>

auto vects = std::vector<std::vector<int>>();

static void BM_std_sortOnInt(benchmark::State& state){

    for (auto _ : state) {
        state.PauseTiming();
        std::vector<int> vect = std::vector<int>(vects[state.range(0)].size());
        std::copy(vects[state.range(0)].begin(), vects[state.range(0)].end(), vect.begin());
        state.ResumeTiming();
        std::sort(vect.begin(), vect.end());
    }
}

static void BM_adaptativeShiverSortOnInt(benchmark::State& state){

    for (auto _ : state) {
        state.PauseTiming();
        std::vector<int> vect = std::vector<int>(vects[state.range(0)].size());
        std::copy(vects[state.range(0)].begin(), vects[state.range(0)].end(), vect.begin());
        state.ResumeTiming();
        adaptativeShiverSort(vect);
    }
}

static void BM_shiverSortOnInt(benchmark::State& state){

    for (auto _ : state) {
        state.PauseTiming();
        std::vector<int> vect = std::vector<int>(vects[state.range(0)].size());
        std::copy(vects[state.range(0)].begin(), vects[state.range(0)].end(), vect.begin());
        state.ResumeTiming();
        shiverSort(vect);
    }
}

static void BM_timSortOnInt(benchmark::State& state){

    for (auto _ : state) {
        state.PauseTiming();
        std::vector<int> vect = std::vector<int>(vects[state.range(0)].size());
        std::copy(vects[state.range(0)].begin(), vects[state.range(0)].end(), vect.begin());
        state.ResumeTiming();
        timSort(vect);
    }
}

void launchBench(std::string path, int argc, char* argv[]){

    std::ifstream infile(path);
    std::string line;
    int i = 0;
    while (std::getline(infile, line)){
       auto temp = std::vector<int>();
       split1(line, temp);
       vects.push_back(temp);
       std::cout << line << "\n";
    }


    BENCHMARK(BM_std_sortOnInt)->DenseRange(0, vects.size()-1, 1);
    BENCHMARK(BM_adaptativeShiverSortOnInt)->DenseRange(0, vects.size()-1, 1);
    BENCHMARK(BM_shiverSortOnInt)->DenseRange(0, vects.size()-1, 1);
    BENCHMARK(BM_timSortOnInt)->DenseRange(0, vects.size()-1, 1);


    ::benchmark::Initialize(&argc, argv);
    ::benchmark::RunSpecifiedBenchmarks();

}
