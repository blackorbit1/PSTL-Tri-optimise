//
// Created by bruno on 24/01/2020.
//

#ifndef SORT_SORT_H
#define SORT_SORT_H

#include <vector>
#include <iostream>

template <class T, class RunFinder, class MergeStrat, class Rules>
void sort(std::vector<T>& array, RunFinder& runF, MergeStrat& merge, Rules& rules){
    auto run = Stack<int>();
    runF(array, run);
    auto stack = Stack<int>();


    while(run.size()!=0){

        stack.push(run.pop());

        while (rules(array, stack, merge))
            ; //nothing
    }

    while (stack.size() > 2){
        int s1 = stack.pop();
        int s2 = stack.pop();

        merge(array, s1, s2, stack.lookup());
        stack.push_back(s1);
    }

    for(int i: stack){
        std::cout << i << " ";
    }
    std::cout << '\n';

}

#endif //SORT_SORT_H
