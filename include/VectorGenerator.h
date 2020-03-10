//
// Created by bruno on 25/02/2020.
//

#ifndef SORT_VECTORGENERATOR_H
#define SORT_VECTORGENERATOR_H


#include <vector>

class VectorGenerator {
public:
    VectorGenerator();
    VectorGenerator(int seed);
    void genVector(std::vector<int>&vector);
private:
    int seed;
};


#endif //SORT_VECTORGENERATOR_H
