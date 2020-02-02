//
// Created by bruno on 24/01/2020.
//

#ifndef SORT_SORT_H
#define SORT_SORT_H

#include <vector>
#include <iostream>
#include "Rules.h"
#include "RunFinder.h"
#include "MergingStategy.h"

template <class T, class RunFinder, class MergeStrat, class Rules>
void sort(std::vector<T>& array, RunFinder& runF, MergeStrat& merge, Rules& rules){
    auto run = StackOfRun();
    runF(array, run);
    auto stack = StackOfRun();

    while(!run.empty()){
        stack.push(run.pop());
        while (rules(array, stack, merge))
            ; //nothing
    }

    while (stack.nbOfRun() > 1){
        int s1, s2, s3, s4;

        stack.popRun(s1, s2);
        stack.popRun(s3, s4);
        merge(array, s1, s3, s4);

        stack.push(s1);
    }
}


template <class T>
void shiverSort(std::vector<T>& array){
    auto merge = stdMerge<int>(array.size());
    auto runf = runFinder<int>();
    auto mergeRules = ShiverSort<typeof(merge), int>();
    sort(array, runf, merge, mergeRules);
}

template <class T>
void naiveMerge(std::vector<T>& array){
    auto merge = stdMerge<int>(array.size());
    auto runf = runFinder<int>();
    auto mergeRules = noMerge<typeof(merge), int>();
    sort(array, runf, merge, mergeRules);
}

template <class T>
void adaptativeShiverSort(std::vector<T>& array){
    auto merge = stdMerge<int>(array.size());
    auto runf = runFinder<int>();
    auto mergeRules = AdaptativeShiverSort<typeof(merge), int>();
    sort(array, runf, merge, mergeRules);
}
#endif //SORT_SORT_H
