//
// Created by bruno on 24/01/2020.
//

#ifndef SORT_SORT_H
#define SORT_SORT_H

#include <vector>
#include <iostream>

template <class T, typename RunFinder, typename MergeStrat, typename Rules>
void sort(std::vector<T>& array, RunFinder runF, MergeStrat merge, Rules rules){
    auto run = std::vector<int>();
    runF(array, run);

    auto stack = std::vector<int>();

    while(run.size()){
        int temp = run.back(); run.pop_back();
        stack.push_back(run.back()); run.pop_back();
        stack.push_back(temp);
        while (rules(array, stack, merge))
            ; //nothing
    }

    for(auto i: stack){
        std::cout << i << ' ';
    }
    std::cout << '\n';

    for(auto i: array){
        std::cout << i << ' ';
    }
    std::cout << '\n';


    while (stack.size() != 2){
        int s2 = stack.back(); stack.pop_back();
        int s1 = stack.back(); stack.pop_back();
        int s4 = stack.back(); stack.pop_back();
        int s3 = stack.back(); stack.pop_back();
        std::cout << s1 << ' ' << s3 << ' ' << s4 << '\n';
        merge(array, s1, s3, s4);

        stack.push_back(s1);
        stack.push_back(s4);
    }

}

#endif //SORT_SORT_H
