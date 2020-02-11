//
// Created by bruno on 01/02/2020.
//

#include "../include/ToolBox.h"

/**
 * https://stackoverflow.com/questions/11376288/fast-computing-of-log2-for-64-bit-integers
 *
 */
const int tab32[32] = {
        0,  9,  1, 10, 13, 21,  2, 29,
        11, 14, 16, 18, 22, 25,  3, 30,
        8, 12, 20, 28, 15, 17, 24,  7,
        19, 27, 23,  6, 26,  5,  4, 31};

int log_2 (unsigned int value) {
    value |= value >> 1;
    value |= value >> 2;
    value |= value >> 4;
    value |= value >> 8;
    value |= value >> 16;
    return tab32[(unsigned int)(value*0x07C4ACDD) >> 27];
}

int msb_geq(int l, int r){
    return !((l < r) && (l < l^r));
}
