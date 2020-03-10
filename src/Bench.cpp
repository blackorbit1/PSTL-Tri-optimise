//
// Created by bruno on 15/02/2020.
//

#include "../include/Bench.h"
#include "../include/Sort.h"
#include "../include/VectorGenerator.h"
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
    for(int i = 0; i < argc; i++)
        std::cout << argv[i];
    std::cout << '\n';

    std::ifstream infile(path);
    std::string line;
    while (std::getline(infile, line)){
       auto temp = std::vector<int>();
       split1(line, temp);
       vects.push_back(temp);
    }

    BENCHMARK(BM_std_sortOnInt)->DenseRange(0, vects.size()-1, 1);
    BENCHMARK(BM_adaptativeShiverSortOnInt)->DenseRange(0, vects.size()-1, 1);
    BENCHMARK(BM_shiverSortOnInt)->DenseRange(0, vects.size()-1, 1);
    BENCHMARK(BM_timSortOnInt)->DenseRange(0, vects.size()-1, 1);

    ::benchmark::Initialize(&argc, argv);
    ::benchmark::RunSpecifiedBenchmarks();

}

static void BM_timSortWithstdMerge(benchmark::State& state){
    std::vector<int> vect(1000000);
    auto merge = stdMerge<int>(vect.size());
    auto runf = runFinderInsert<int>(32);
    auto mergeRules = TimSort<typeof(merge), int>();

    for (auto _ : state) {
        state.PauseTiming();
        auto gen = VectorGenerator(state.range(0));
        gen.genVector(vect);
        state.ResumeTiming();
        sort(vect, runf, merge, mergeRules);
    }
}

static void BM_timSortWithstdInplaceMerge(benchmark::State& state){
    std::vector<int> vect(1000000);
    auto merge = stdInplaceMerge<int>();
    auto runf = runFinderInsert<int>(32);
    auto mergeRules = AdaptativeShiverSort<typeof(merge), int>();

    for (auto _ : state) {
        state.PauseTiming();
        auto gen = VectorGenerator(state.range(0));
        gen.genVector(vect);
        state.ResumeTiming();
        sort(vect, runf, merge, mergeRules);
    }
}

static void BM_timSortWithstdMergeS(benchmark::State& state){
    std::vector<int> vect(1000000);
    auto merge = stdMergeS<int>(vect.size());
    auto runf = runFinderInsert<int>(32);
    auto mergeRules = AdaptativeShiverSort<typeof(merge), int>();

    for (auto _ : state) {
        state.PauseTiming();
        auto gen = VectorGenerator(state.range(0));
        gen.genVector(vect);
        state.ResumeTiming();
        sort(vect, runf, merge, mergeRules);
    }
}

static void BM_a2sWithstdMerge(benchmark::State& state){
    std::vector<int> vect(1000000);
    auto merge = stdMerge<int>(vect.size());
    auto runf = runFinderInsert<int>(32);
    auto mergeRules = AdaptativeShiverSort<typeof(merge), int>();

    for (auto _ : state) {
        state.PauseTiming();
        auto gen = VectorGenerator(state.range(0));
        gen.genVector(vect);
        state.ResumeTiming();
        sort(vect, runf, merge, mergeRules);
    }
}

static void BM_a2sWithstdInplaceMerge(benchmark::State& state){
    std::vector<int> vect(1000000);
    auto merge = stdInplaceMerge<int>();
    auto runf = runFinderInsert<int>(32);
    auto mergeRules = AdaptativeShiverSort<typeof(merge), int>();

    for (auto _ : state) {
        state.PauseTiming();
        auto gen = VectorGenerator(state.range(0));
        gen.genVector(vect);
        state.ResumeTiming();
        sort(vect, runf, merge, mergeRules);
    }
}

static void BM_a2sWithstdMergeS(benchmark::State& state){
    std::vector<int> vect(1000000);
    auto merge = stdMergeS<int>(vect.size());
    auto runf = runFinderInsert<int>(32);
    auto mergeRules = AdaptativeShiverSort<typeof(merge), int>();

    for (auto _ : state) {
        state.PauseTiming();
        auto gen = VectorGenerator(state.range(0));
        gen.genVector(vect);
        state.ResumeTiming();
        sort(vect, runf, merge, mergeRules);
    }
}

void launchTestMerge(){
    int i = rand();
    BENCHMARK(BM_timSortWithstdMerge)->Arg(i);
    BENCHMARK(BM_timSortWithstdInplaceMerge)->Arg(i);
    BENCHMARK(BM_timSortWithstdMergeS)->Arg(i);
    /*=============================================*/
    BENCHMARK(BM_a2sWithstdMerge)->Arg(i);
    BENCHMARK(BM_a2sWithstdInplaceMerge)->Arg(i);
    BENCHMARK(BM_a2sWithstdMergeS)->Arg(i);

}

void launchFewBench(int argc, char* argv[]){
    launchTestMerge();

    ::benchmark::Initialize(&argc, argv);
    ::benchmark::RunSpecifiedBenchmarks();
}