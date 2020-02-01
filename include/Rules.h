//
// Created by bruno on 24/01/2020.
//

#ifndef SORT_RULES_H
#define SORT_RULES_H

#include <vector>
#include "StackOfRun.h"
#include "ToolBox.h"
template<class MergeStrat, class T>
class noMerge {
public:
    bool operator()(std::vector<T> &array, StackOfRun &stack, MergeStrat &merge) {
        return false;
    }
};


template<class MergeStrat, class T>
class ShiverSort {
public:
    bool operator()(std::vector<T> &array, StackOfRun &stack, MergeStrat &merge) {
        const int c = 16;
        if(stack.nbOfRun() <= 1)
            return false;

        int s1, s2, s3, s4;

        stack.popRun(s1, s2); // h1
        stack.popRun(s3, s4); // h2

        if (log_2((s2-s1)/c) >= log_2((s4-s3)/c)){
            merge(array, s1, s3, s4);
            stack.push(s1);
            return true;
        }

        stack.push(s3);
        stack.push(s1);
        return false;

    }
};

#endif //SORT_RULES_H
