//
// Created by bruno on 24/01/2020.
//

#ifndef SORT_RULES_H
#define SORT_RULES_H

#include <vector>

template<class MergeStrat, class T>
class noMerge {
public:
    bool operator()(std::vector<T> &array, std::vector<int> &stack, MergeStrat merge) {
        return false;
    }
};

#endif //SORT_RULES_H
