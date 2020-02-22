//
// Created by bruno on 15/02/2020.
//

#ifndef SORT_BENCH_H
#define SORT_BENCH_H

#include <string>
#include <sstream>
#include <iostream>
#include <iterator>
#include <benchmark/benchmark.h>


void launchBench(std::string path, int argc, char* argv[]);

template <class Container>
void split1(std::string str, Container& cont){

    std::stringstream stream(str);
    int n;

    while(stream >> n){
        cont.push_back(n);
    }
}


#endif //SORT_BENCH_H
