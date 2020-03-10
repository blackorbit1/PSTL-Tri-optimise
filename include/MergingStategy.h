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
#include <cstring>
#include <iterator>


template <class T>
class stdMergeS{
public:
    stdMergeS(int size){
        this->_ptr = new T[size];
    }

    ~stdMergeS(){
        delete[] _ptr;
    }

    void operator () (std::vector<T>& vect, int start1, int start2, int end){

        if(end-start2 > start2 - start1){
            std::copy(vect.begin()+start1, vect.begin()+start2, _ptr);
            std::merge(_ptr, _ptr+(start2-start1),
                       vect.begin()+start2, vect.begin()+end,
                       vect.begin()+start1);
            return;
        }
        std::copy(vect.begin()+start2, vect.begin()+end, _ptr);

        std::reverse_iterator<T*> first(_ptr + end-start2);
        std::reverse_iterator<T*> last(_ptr);

        std::merge(first, last,
                   vect.rbegin() + vect.size() - start2, vect.rbegin() + vect.size() - start1,
                   vect.rbegin() + vect.size() - end , std::greater<T>());

    }

private:
    T* _ptr;
};

template <class T>
class stdMerge{
public:
    stdMerge(int size){
        this->_ptr = new T[size];
    }

    ~stdMerge(){
        delete[] _ptr;
    }

    void operator () (std::vector<T>& vect, int start1, int start2, int end){

        std::copy(vect.begin()+start1, vect.begin()+start2, _ptr);
        std::merge(_ptr, _ptr+(start2-start1),
                   vect.begin()+start2, vect.begin()+end,
                   vect.begin()+start1);
    }

private:
    T* _ptr;
};

template <class T>
class stdInplaceMerge{
public:
    void operator () (std::vector<T>& vect, int start1, int start2, int end){
        std::inplace_merge(vect.begin()+start1, vect.begin()+start2, vect.begin()+end);
    }
};

#endif //PSTL_TRI_OPTIMISE_MERGINGSTATEGY_H
