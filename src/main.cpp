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
    std::string s_file;
    std::string s_file_out;

    po::options_description desc("Allowed options");
    desc.add_options()
            ("help,h", "produce help message")
            ("file_in,f", po::value<std::string>(&s_file), "file with array to bench")
            ("file_out,f", po::value<std::string>(&s_file_out), "file with array to bench")
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

    if (vm.count("file_in") && vm.count("file_out")) {
        std::ifstream infile(s_file);
        std::filebuf fb;
        fb.open (s_file_out,std::ios::out);
        std::ostream os(&fb);
        launchBench(infile, os);
        fb.close();
        return 0;
    }
    if (vm.count("sandbox")) {
        std::ifstream infile("./files/test.tab");

        launchBench(infile, std::cout);

        return 0;
    }
}