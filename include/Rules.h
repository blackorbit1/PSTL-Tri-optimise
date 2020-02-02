//
// Created by bruno on 24/01/2020.
//

#ifndef SORT_RULES_H
#define SORT_RULES_H

#include <vector>
#include "StackOfRun.h"
#include "ToolBox.h"

#include <iostream>



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
        const int c = 2;

        if (stack.nbOfRun() <= 1)
            return false;

        int s1, s2, s3, s4;

        stack.popRun(s1, s2); // h1
        stack.popRun(s3, s4); // h2

        int l1 = log_2((s2 - s1) / c);
        int l2 = log_2((s4 - s3) / c);

        if (l1 >= l2) {
            merge(array, s1, s3, s4);
            stack.push(s1);
            return true;
        }

        stack.push(s3);
        stack.push(s1);
        return false;

    }
};


template<class MergeStrat, class T>
class AdaptativeShiverSort {
public:
    bool operator()(std::vector<T> &array, StackOfRun &stack, MergeStrat &merge) {
        const int c = 2;
        int nbOfRun = nbOfRun;
        // on ne peut appliquer les regles que s'il y a au moins 2 runs dans la pile
        if(stack.nbOfRun() <= 1){
            return false;
        }

        int s1, s2, s3, s4;

        stack.popRun(s1, s2); //h1
        stack.popRun(s3, s4); //h2
        int l1 = log_2((s2-s1)/c);
        int l2 = log_2((s4-s3)/c);

        if(nbOfRun >= 3) {
            int s5, s6;
            stack.popRun(s5, s6); //h3
            int l3 = log_2((s6-s5)/c);

            if (l1 >= l3){ // Case #1
                merge(array, s3, s5, s6);
                stack.push(s3);
                stack.push(s1);
                return true;
            } else if (l2>=l3){ // Case #2
                merge(array, s3, s5, s6);
                stack.push(s3);
                stack.push(s1);
                return true;
            }
            stack.push(s5);
        }

        if (l1 >= l2){ // Case #4
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
