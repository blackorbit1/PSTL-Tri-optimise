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

        if(stack.nbOfRun() <= 1)
            return false;

        int s1, s2, s3, s4;

        stack.popRun(s1, s2); // h1
        stack.popRun(s3, s4); // h2

        int l1 = log_2((s2-s1)/c);
        int l2 = log_2((s4-s3)/c);
        //std::cout << "l1 " << l1 << '\n';
        //std::cout << "l2 " << l2 << '\n';


        if (l1 >= l2){
            merge(array, s1, s3, s4);
            stack.push(s1);
            return true;
        }

        stack.push(s3);
        stack.push(s1);
        return false;

    }


    bool shiverRules(std::vector<T> &array, StackOfRun &stack, MergeStrat &merge){
        const int c = 16;

        // on ne peut appliquer les regles que s'il y a au moins 2 runs dans la pile
        if(stack.nbOfRun() <= 1)
            return false;

        int s1, s2, s3, s4;
        // note : s2 == s3

        stack.popRun(s1, s2); //h1
        stack.popRun(s3, s4); //h2

        if (s2-s1 < s4-s3){
            merge(array, s1, s3, s4);
            stack.push(s1);
            return true;
        }

        // ATTENTION boucle infinie si 1e run plus long
        stack.push(s3);
        stack.push(s1);

        return false;
    }

    bool adaptativeShiverRules(std::vector<T> &array, StackOfRun &stack, MergeStrat &merge){
        const int c = 2;

        /*
        for(auto i: array){
            std::cout << i << " ";
        }
        std::cout << "\nstack size : " << stack.size() << "\n\n";
         */

        // on ne peut appliquer les regles que s'il y a au moins 2 runs dans la pile
        if(stack.nbOfRun() <= 1){
            return false;
        } else if (stack.nbOfRun() == 2){
            int s1, s2, s3, s4;
            // note : s2 == s3

            stack.popRun(s1, s2); //h1
            stack.popRun(s3, s4); //h2
            //std::cout << s1 << "-" << s2 << "-" << s3 << "-" << s4 << "\n";

            if (log_2((s2-s1)/c) >= log_2((s4-s3)/c)){
            //if (s2-s1 < s4-s3){
                //std::cout << "case 4 \n";
                merge(array, s1, s3, s4);
                stack.push(s1);
                return true;
            }

            stack.push(s3);
            stack.push(s1);
            return false;

        } else if(stack.nbOfRun() >= 3) {
            int s1, s2, s3, s4, s5, s6;

            stack.popRun(s1, s2); //h1
            stack.popRun(s3, s4); //h2
            stack.popRun(s5, s6); //h3

            // le dernier popRun n'attribut aucune valeur à s6
            //s6 = array.size();
            //std::cout << s1 << "-" << s2 << "-" << s3 << "-" << s4 << "-" << s5 << "-" << s6 << "\n";


            if (log_2((s2-s1)/c) >= log_2((s6-s5)/c)){
            //if(s2-s1 < s6-s5){
                //std::cout << "case 2 \n";
                merge(array, s3, s5, s6);
                stack.push(s3);
                stack.push(s1);
                return true;
            } else if (log_2((s4-s3)/c) >= log_2((s6-s5)/c)){
            //} else if (s4-s3 < s6-s5) {
                //std::cout << "case 3 \n";
                merge(array, s3, s5, s6);
                stack.push(s3);
                stack.push(s1);
                return true;
            } else if (log_2((s2-s1)/c) >= log_2((s4-s3)/c)){
            //} else if (s2-s1 < s4-s3){
                //std::cout << "case 4 \n";
                merge(array, s1, s3, s4);
                stack.push(s5);
                stack.push(s1);
                return true;
            }

            stack.push(s5); // s5
            stack.push(s3);
            stack.push(s1);
            return false;
        } else {
            std::cout << "enorme probleme \n";
            return false;
        }


    }
};

#endif //SORT_RULES_H
