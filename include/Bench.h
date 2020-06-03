//
// Created by bruno on 15/02/2020.
//

#ifndef SORT_BENCH_H
#define SORT_BENCH_H

#include <string>
#include <sstream>
#include <iostream>
#include <iterator>
#include <chrono>
#include <array>
#include <boost/sort/sort.hpp>

class TimWrap{
public:
    void operator ()(std::vector<int>& vect){
        timSort(vect);
    }
};

class AdaptiveShiverSortWrap{
public:
    void operator ()(std::vector<int>& vect){
        adaptativeShiverSort(vect);
    }
};

class IntroWrap{
public:
    void operator ()(std::vector<int>& vect){
        sort(vect.begin(), vect.end());
    }
};

class MergeSortWrap{
public:
    void operator ()(std::vector<int>& vect){
        mergeSort(vect.begin(), vect.end());
    }
};

class HybrMergeSortWrap{
public:
    void operator ()(std::vector<int>& vect){
        hybridMergeSort(vect.begin(), vect.end());
    }
};

template <class T>
class BenchMark{
public:
    BenchMark(std::vector<int>& _vect, char* _name, char* _metaData){
        this->metaData = std::string (_metaData);
        this->name = std::string(_name);
        this->baseArray = std::vector(_vect);
        sort = T();
    }

    void launchBench(){
        std::vector<int> toSort(baseArray.size());

        for(int i = 0; i < 3; i++){
            std::copy(baseArray.begin(), baseArray.end(), toSort.begin());
//            std::cout << baseArray.size() << '\n';
//            std::cout << toSort.size() << '\n';
            sort(toSort);
            std::cerr << "Loading in cache\n";
        }

        for(int i = 0; i < K; i++){
            std::copy(baseArray.begin(), baseArray.end(), toSort.begin());

            std::chrono::time_point<std::chrono::system_clock> start, end;
            start = std::chrono::system_clock::now();

            sort(toSort);

            end = std::chrono::system_clock::now();

            time[i] = std::chrono::duration_cast<std::chrono::nanoseconds>(end-start).count();
        }

//        for(auto i: time){
//            std::cout << i << ' ';
//        }
//        std::cout << '\n';
        std::sort(time.begin(), time.end());

//        for(auto i: time){
//            std::cout << i << ' ';
//        }
//        std::cout << '\n';
    }
    template <class U>
    friend std::ostream& operator<<(std::ostream& out, const BenchMark<U>& b);
    static const int K = 33 ;

private:
    std::vector<int> baseArray;
    std::array<int, K> time;
    std::string name;
    std::string metaData;
    T sort;
};

template <class U>
std::ostream& operator<<(std::ostream& out, const BenchMark<U>& b){
    out << "\t{\n" <<
            "\t\t\"meta\": \"" << b.metaData << "\",\n" <<
            "\t\t\"time\": \"" << b.time[b.K/2+1] << "\",\n" <<
//            "\t\t\"interquartile_range\": \"" << b.time[((b.K)*3)/4+1] - b.time[(b.K)/4+1] << "\",\n" <<
            "\t\t\"algo\": \"" << b.name << "\"\n" <<
            "\t}\n";
    return out;
}

template <class Container>
void split(std::string str, Container& cont){

    std::stringstream stream(str);
    int n;

    while(stream >> n){
        cont.push_back(n);
    }
}

void launchBench(std::istream& infile, std::ostream& out){
    std::string meta;
    std::string line;
    std::vector<int> vect;

//    std::vector<BenchMark<TimWrap>> arrayTim;
//    std::vector<BenchMark<AdaptiveShiverSortWrap>> arrayASS;
    std::vector<BenchMark<IntroWrap>> arrayIntro;
//    std::vector<BenchMark<MergeSortWrap>> arrayMerge;
//    std::vector<BenchMark<HybrMergeSortWrap>> arrayMergeIns;

    while(std::getline(infile, line) && std::getline(infile, meta)){
        split(line, vect);


//        arrayTim.push_back(BenchMark<TimWrap>(vect, "TimSort", (char*)meta.c_str()));
//        arrayASS.push_back(BenchMark<AdaptiveShiverSortWrap>(vect, "AdaptativeShiverSort", (char*)meta.c_str()));
        arrayIntro.push_back(BenchMark<IntroWrap>(vect, "stdSort", (char*)meta.c_str()));
//        arrayMerge.push_back(BenchMark<MergeSortWrap>(vect, "MergeSort", (char*)meta.c_str()));
//        arrayMergeIns.push_back(BenchMark<HybrMergeSortWrap>(vect, "HybridMergeSort", (char*)meta.c_str()));

//        arrayTim.back().launchBench();
//        arrayASS.back().launchBench();
        arrayIntro.back().launchBench();
//        arrayMerge.back().launchBench();
//        arrayMergeIns.back().launchBench();
    }

    out << "{\n"
        << "\t\"content\": [";

    for(int i = 0; i < arrayIntro.size(); i++){
        if(i != arrayIntro.size()-1)
            out << arrayIntro[i] << ',';
//            out << arrayTim[i] << ',' << arrayASS[i] << ',' << arrayIntro[i] << ',' << arrayMerge[i] << ',' << arrayMergeIns[i] << ',';
        else
            out << arrayIntro[i];
//            out << arrayTim[i] << ',' << arrayASS[i] << ',' << arrayIntro[i] << ',' << arrayMerge[i] << ',' << arrayMergeIns[i];
    }

    out << "\t]\n}";
}


#endif //SORT_BENCH_H
