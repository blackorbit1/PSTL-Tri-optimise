//
// Created by bruno on 24/01/2020.
//

/**
 * Few implementation for merging two sorted array (collapse or not)
 *
 */

#ifndef PSTL_TRI_OPTIMISE_MERGINGSTATEGY_H
#define PSTL_TRI_OPTIMISE_MERGINGSTATEGY_H

#include <vector>
#include <algorithm>

template <class T>
class stdMerge{
public:
    void operator () (std::vector<T>& vect, int start1, int start2, int end){
        std::merge(vect.begin()+start1, vect.begin()+start2,
                   vect.begin()+start2, vect.begin()+end,
                   vect.begin()+start1);
    }
};

template <class T>
class stdInplaceMerge{
public:
    void operator () (std::vector<T>& vect, int start1, int start2, int end){
        std::inplace_merge(vect.begin()+start1, vect.begin()+start2, vect.begin()+end);
    }
};

#endif //PSTL_TRI_OPTIMISE_MERGINGSTATEGY_H
