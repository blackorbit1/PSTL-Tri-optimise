//
// Created by bruno on 24/01/2020.
//

#include <vector>
#include <iostream>
#include <random>
#include "../include/MergingStategy.h"
#include "../include/Benchmark.h"
#include "../include/RunFinder.h"
#include "../include/Sort.h"
#include "../include/Rules.h"
int main(){

//    std::vector<int> vect = {3, 4, 5, 6, 0, 1, 20, 18, 25, 21, 22, 23, 1000, 7, 8, -5, -7, -9};
//    std::vector<int> vect = {10, 9, 8};
    const int max = 2000;
    std::random_device rd;
    std::mt19937 mt(rd());
    std::uniform_int_distribution<> dis(0, max*2);

    std::vector<int> vect(max);

    std::generate(vect.begin(), vect.end(), std::bind(dis, std::ref(mt)));

    StackOfRun run;

    auto merge = stdInplaceMerge<int>();
    auto runf = runFinder<int>();
    auto noMerg = merge1<typeof(merge), int>();

    runf(vect, run);
    for(auto i: run){
        std::cout << i << " ";
    }
    std::cout << '\n';

    for(auto i: vect){
        std::cout << i << " ";
    }
    std::cout << '\n';

    sort(vect, runf, merge, noMerg);


    for(auto i: vect){
        std::cout << i << " ";
    }
    std::cout << '\n';

    assert(std::is_sorted(vect.begin(), vect.end()));

    return 0;
}