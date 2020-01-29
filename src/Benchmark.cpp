//
// Created by bruno on 24/01/2020.
//

#include <random>
#include <algorithm>
#include <functional>
#include <iostream>

#include "../include/Benchmark.h"
#include "../include/MergingStategy.h"



void benchMerge() {
    const int max = 50000;
    std::random_device rd;
    std::mt19937 mt(rd());
    std::uniform_int_distribution<> dis(0, max);

    std::vector<int> v1(max);

    std::generate(v1.begin(), v1.end(), std::bind(dis, std::ref(mt)));

    std::sort(v1.begin(), v1.begin()+max/2+1);
    std::sort(v1.begin()+max/2 + 1, v1.end());

    auto v2 = std::vector(v1);
    auto v3 = std::vector(v1);
    auto v4 = std::vector(v1);
    auto v5 = std::vector(v1);

    auto merge1 = stdMerge<int>(max);
    auto merge2 = stdInplaceMerge<int>();

    std::cout << "inplace_merge: " << chronom(v2, merge2, 0, max/2+1, max) << "\n";
    std::cout << "inplace_merge: " << chronom(v5, merge2, 0, max/2+1, max) << "\n";
    std::cout << "merge_lib: " << chronom(v3, merge1, 0, max/2+1, max) << "\n";
    std::cout << "merge_lib: " << chronom(v4, merge1, 0, max/2+1, max) << "\n";



}
