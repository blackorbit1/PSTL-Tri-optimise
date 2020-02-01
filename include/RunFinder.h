//
// Created by bruno on 24/01/2020.
//

#ifndef SORT_RUNFINDER_H
#define SORT_RUNFINDER_H

#include <vector>
#include "StackOfRun.h"

template <class T>
class runFinder {
public:
    void operator()(std::vector<T> &array, StackOfRun &run) {

        // we assume run empty and array.size()>=2
        bool increasing = array[0] < array[1];
        run.push(0);
        for (int i = 1; i < array.size() - 1; i++) {
            if (increasing && array[i] > array[i + 1]) {
                run.push(i + 1);
                if (i < array.size() - 2)
                    increasing = array[i + 1] <= array[i + 2];
            }
            else if (!increasing && array[i] < array[i + 1]) {
                std::reverse(array.begin()+run.lookup(), array.begin()+i+1);
                run.push(i + 1);
                if (i < array.size() - 2)
                    increasing = array[i + 1] <= array[i + 2];
            }
        }

        if(array[array.size()-2]>array.back()){
            std::reverse(array.begin()+run.lookup(), array.end());

        }
        run.push(array.size());
    }
};

#endif //SORT_RUNFINDER_H
