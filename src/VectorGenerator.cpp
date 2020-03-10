//
// Created by bruno on 25/02/2020.
//

#include <random>
#include <functional>
#include "../include/VectorGenerator.h"
#include <climits>

VectorGenerator::VectorGenerator():seed{42} {
}

VectorGenerator::VectorGenerator(int seed):seed{seed} {
}

void VectorGenerator::genVector(std::vector<int> &vector) {
    std::mt19937 mt(seed);
    std::uniform_int_distribution<> dis(INT_MIN, INT_MAX);
    std::generate(vector.begin(), vector.end(), std::bind(dis, std::ref(mt)));
}

