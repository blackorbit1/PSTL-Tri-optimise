//
// Created by bruno on 24/01/2020.
//

#ifndef SORT_BENCHMARK_H
#define SORT_BENCHMARK_H

#include <assert.h>
#include <chrono>

void benchMerge();

template <class T>
int chronom(std::vector<int> &vect, T &fct, int s1, int s2, int _end){
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


#endif //SORT_BENCHMARK_H
