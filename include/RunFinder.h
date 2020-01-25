//
// Created by bruno on 24/01/2020.
//

#ifndef SORT_RUNFINDER_H
#define SORT_RUNFINDER_H

#include <vector>

template <class T>
class runFinder {
public:
    void operator()(std::vector<T> &array, std::vector<int> &run) {
        // we assume run empty and array.size()>=2
        bool increasing = array[0] < array[1];
        run.push_back(0);
        for (int i = 1; i < array.size() - 1; i++) {
            if (increasing && array[i] >= array[i + 1] or !increasing && array[i] <= array[i + 1]) {
                run.push_back(i);
                run.push_back(i + 1);
                if (i < array.size() - 2)
                    increasing = array[i + 1] <= array[i + 2];
            }
        }
        run.push_back(array.size());
    }
};

#endif //SORT_RUNFINDER_H
