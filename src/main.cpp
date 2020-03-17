//
// Created by bruno on 24/01/2020.
//


#include "../include/Generator.h"

#include <vector>
#include <iostream>
#include <random>
#include "../include/MergingStategy.h"
#include "../include/RunFinder.h"
#include "../include/Sort.h"
#include "../include/Rules.h"
#include "../include/Bench.h"
#include <boost/program_options.hpp>
#include <fstream>
// sudo apt install libboost-program-options-dev

namespace po = boost::program_options;

int main(int argc, char* argv[]) {
    std::string file;
    int idone;
    std::string done;

    po::options_description desc("Allowed options");
    desc.add_options()
            ("help,h", "produce help message")
            ("file,f", po::value<std::string>(&file), "file with array to bench")
            ("benchmark_out_format", po::value<std::string>(&done),
             "type of output file <csv|json|console> (default: console)")
            ("benchmark_out", po::value<std::string>(&done),
             "name of output file")
            ("benchmark_repetitions", po::value<int>(&idone),
             "number of repetitions of the benchmark (default: 1)")
            ("benchmark_fun",
             "bench few fonction")
            ("sandbox",
             "sandox");

    po::variables_map vm;
    try {
        po::store(parse_command_line(argc, argv, desc), vm);
    }
    catch (std::exception &e) {
        std::cerr << e.what();
    }
    po::notify(vm);
    if (vm.count("help")) {
        std::cout << desc << "\n";
        return 0;
    }

    if (vm.count("benchmark_fun")) {

        return 0;
    }

    if (vm.count("file")) {

        return 0;
    }
    if (vm.count("sandbox")) {
        std::vector v = {1, 84,58,41,2584,1,47,51,584,1,47,9,5478,8};
        std::ifstream infile("../files/test.tab");

        launchBench(infile, std::cout);

        return 0;
    }
}