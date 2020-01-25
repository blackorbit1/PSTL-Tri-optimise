//
// Created by bruno on 24/01/2020.
//

#include <random>
#include <algorithm>
#include <functional>
#include <iostream>
#include <assert.h>
#include <chrono>
#include "../include/Benchmark.h"
#include "../include/MergingStategy.h"


static int chronom(std::vector<int> &vect, void (*fct)(std::vector<int>&, int, int, int), int s1, int s2, int _end){
    for(auto i = 0; i < vect.size(); i++){
        vect[i]++; // load in cache memory
    }

    std::chrono::time_point<std::chrono::system_clock> start, end;
    start = std::chrono::system_clock::now();

    fct(vect, s1, s2, _end);

    end = std::chrono::system_clock::now();

    int elapsed_seconds = std::chrono::duration_cast<std::chrono::microseconds>
            (end-start).count();

    assert(std::is_sorted(vect.begin()+s1, vect.begin()+_end));

    return elapsed_seconds;
}

void benchMerge() {
    const int max = 5000000;
    std::random_device rd;
    std::mt19937 mt(rd());
    std::uniform_int_distribution<> dis(0, max);

    std::vector<int> v1(max);

    std::generate(v1.begin(), v1.end(), std::bind(dis, std::ref(mt)));

    std::sort(v1.begin(), v1.begin()+max/2+1);
    std::sort(v1.begin()+max/2 + 1, v1.end());

    auto v2 = std::vector(v1);
    auto v3 = std::vector(v1);
//
//    std::cout << "merge_lib: " << chronom(v3, merge1, 0, max/2+1, max) << "\n";
//    std::cout << "inplace_merge: " << chronom(v2, merge2, 0, max/2+1, max) << "\n";

}
