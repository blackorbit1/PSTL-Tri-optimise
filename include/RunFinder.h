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

        // add insert sort
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

template <class T>
class runFinderInsert {
public:

    runFinderInsert(int _K): K{_K}{

    }

    void operator()(std::vector<T> &array, StackOfRun &run) {

        // we assume run empty and array.size()>=2

        // add insert sort

        bool increasing = array[0] < array[1];
        run.push(0);
        for (int i = 1; i < array.size() - 1; i++) {
            if (increasing && array[i] > array[i + 1] || !increasing && array[i] < array[i + 1]) {
                if(!increasing && array[i] < array[i + 1])
                    std::reverse(array.begin() + run.lookup(), array.begin() + i + 1);

                if(i + 1 - run.lookup() < K){
                    insertExtend(array, run.lookup(), std::min(run.lookup()+K, (int)array.size()), i);
                    i = run.lookup() + K - 1;
                    if (i > array.size())
                        break;
                }

                run.push(i + 1);
                if (i < array.size() - 2)
                    increasing = array[i + 1] <= array[i + 2];
            }
        }

        if(array[array.size()-2]>array.back())
            std::reverse(array.begin()+run.lookup(), array.end());

        run.push(array.size());

    }


private:
    const int K;
    void insertExtend(std::vector<T>& array, int start, int end, int i0){
        /**
         * sort array[start::end]
         * array[start::i0] must be start (start and io can be equals)
         */
        int i, j;
        for (i = i0 ; i < end; i++) {
            j = i;
            while (j > start && array[j-1] > array[j]) {
                std::swap(array[j], array[j-1]);
                j--;
            }
        }
    }
};


#endif //SORT_RUNFINDER_H
