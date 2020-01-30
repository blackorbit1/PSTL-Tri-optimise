//
// Created by bruno on 24/01/2020.
//

#ifndef SORT_SORT_H
#define SORT_SORT_H

#include <vector>
#include <iostream>

template <class T, class RunFinder, class MergeStrat, class Rules>
void sort(std::vector<T>& array, RunFinder& runF, MergeStrat& merge, Rules& rules){
    auto run = StackOfRun();
    runF(array, run);
    auto stack = StackOfRun();

    while(run.size()!=0){
        stack.push(run.pop());
        while (rules(array, stack, merge))
            ; //nothing
    }

    int s1, s2;
    while (stack.nbOfRun() > 1){
        stack.popRun(s1, s2);
        merge(array, s1, s2, stack.lookup());
        stack.push(s1);
    }
}

#endif //SORT_SORT_H
