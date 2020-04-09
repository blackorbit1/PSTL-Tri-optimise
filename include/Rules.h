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

        stack.popRun(s1, s2); // r1
        stack.popRun(s3, s4); // r2

        int l1 = ((s2 - s1) / c);
        int l2 = ((s4 - s3) / c);

        if (msb_geq(l1, l2)) {
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
        int nbOfRun = stack.nbOfRun();
        // on ne peut appliquer les regles que s'il y a au moins 2 runs dans la pile
        if(stack.nbOfRun() <= 1){
            return false;
        }

        int s1, s2, s3, s4;

        stack.popRun(s1, s2); // r1
        stack.popRun(s3, s4); // r2
        int l1 = (s2-s1);
        int l2 = (s4-s3);

        if(nbOfRun >= 3) {
            int s5, s6;
            stack.popRun(s5, s6); // r3
            int l3 =  (s6-s5);
            if (msb_geq(l1, l3)){ // Case #1
                merge(array, s3, s5, s6);
                stack.push(s3);
                stack.push(s1);
                return true;
            } else if (msb_geq(l2, l3)){ // Case #2
                merge(array, s3, s5, s6);
                stack.push(s3);
                stack.push(s1);
                return true;
            }
            stack.push(s5);
        }

        if (msb_geq(l1, l2)){ // Case #4
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
class TimSort {
public:
    bool operator()(std::vector<T> &array, StackOfRun &stack, MergeStrat &merge) {
        int nbOfRun = stack.nbOfRun();

        if(nbOfRun < 2)
            return false;

        int s1, s2, s3, s4;
        int s5, s6, s7, s8;

        stack.popRun(s1, s2); // r1
        stack.popRun(s3, s4); // r2

        int r1, r2, r3, r4;

        r1 = s2 - s1;
        r2 = s4 - s3;

        if (nbOfRun >= 3){
            stack.popRun(s5, s6); // r3
            r3 = s6 - s5;
            if(r1 > r3) { // case 1
                merge(array, s3, s5, s6);
                stack.push(s3);
                stack.push(s1);
                return true;
            }
        }
        if(nbOfRun >= 2 && r1 >= r2) {
            merge(array, s1, s3, s4);
            if(nbOfRun > 2)
                stack.push(s5);
            stack.push(s1);
            return true;
        }
        if(nbOfRun >= 3 && r1 + r2 >= r3){
            merge(array, s1, s3, s4);
            stack.push(s5);
            stack.push(s1);
            return true;
        }

        if(nbOfRun >= 4){
            stack.popRun(s7, s8); // r3
            r4 = s8 - s7;
            if(r2 + r3 >= r4){
                merge(array, s1, s3, s4);
                stack.push(s7);
                stack.push(s5);
                stack.push(s1);
                return true;
            }
            stack.push(s7);
        }

        if (nbOfRun != 2){
            stack.push(s5);
        }
        stack.push(s3);
        stack.push(s1);
        return false;
    }
};

#endif //SORT_RULES_H
