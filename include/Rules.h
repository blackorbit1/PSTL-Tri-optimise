//
// Created by bruno on 24/01/2020.
//

#ifndef SORT_RULES_H
#define SORT_RULES_H

#include <vector>
#include "Stack.h"
template<class MergeStrat, class T>
class noMerge {
public:
    bool operator()(std::vector<T> &array, Stack<int> &stack, MergeStrat merge) {
        return false;
    }
};


template<class MergeStrat, class T>
class merge1 {
public:
    bool operator()(std::vector<T> &array, Stack<int> &stack, MergeStrat merge) {

        if(stack.nbOfRun() <= 1)
            return false;

        int s1, s2, s3, s4;

        stack.popRun(s1, s2, s3, s4);

        if (s2-s1 < s4-s3){
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
