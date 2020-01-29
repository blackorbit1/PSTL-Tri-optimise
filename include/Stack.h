//
// Created by bruno on 28/01/2020.
//

#ifndef SORT_STACK_H
#define SORT_STACK_H

#include <vector>

template<class T>
class Stack: public std::vector<T>{ // public for debug
public:
    void push(T elem){
        this->push_back(elem);
    }

    T pop(){
        T tmp = this->back();
        this->pop_back();
        return tmp;
    }

    T lookup(){
        return this->back();
    }

    int size(){
        return std::vector<T>::size();
    }

    int nbOfRun(){
        return size() - 1;
    }

    void popRun(int& s1, int& s2, int& s3, int& s4){
        s1 = pop();
        s3 = pop();
        s2 = s3 - 1;
        s4 = lookup();
    }

};

#endif //SORT_STACK_H
