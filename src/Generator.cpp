//
// Created by bruno on 01/02/2020.
//

#include <random>
#include <algorithm>
#include <functional>
#include "../include/Generator.h"


std::vector<int> *genRandomInt(int nbElem) {
    auto vect = new std::vector<int>(nbElem);
    std::random_device rd;
    std::mt19937 mt(rd());
    std::uniform_int_distribution<> dis(0, nbElem*2);

    std::generate((*vect).begin(), (*vect).end(), std::bind(dis, std::ref(mt)));

    return vect;
}
