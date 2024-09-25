#include <assert.h>
#include <iostream>
#include <csignal>

#include "crave_governor.h"

int main(int argc, char** argv) {

    int gov_choice = 0;

    if(argc != 2){
        gov_choice = 0;
    }
    else{
        int num1 = std::atoi(argv[1]);
        gov_choice = num1;
    }


    // Lists of the permitted frequencies for the CPU, GPU, and memory
    std::vector<long long> cpu_freq_list{345600,499200,652800,806400,960000,1113600,1267200,1420800}; // Size: 8
    std::vector<long long> gpu_freq_list{114750000,216750000,318750000,420750000,522750000,624750000,726750000,854250000,930750000,1032750000,1122000000,1236750000,1300500000}; // Size: 13
    std::vector<long long> mem_freq_list{40800000,68000000,102000000,204000000,408000000,665600000,800000000,1062400000,1331200000,1600000000,1866000000}; // Size: 11

    // gpu driven governor setting
    // governor_settings gpu_cluster = {
    //     {600000000, {{"cpu", 1400000}, {"mem", 825000000}}},
    //     {543000000, {{"cpu", 1200000}, {"mem", 728000000}}},
    //     {480000000, {{"cpu", 1000000}, {"mem", 633000000}}},
    //     {420000000, {{"cpu", 800000},  {"mem", 543000000}}},
    //     {350000000, {{"cpu", 600000},  {"mem", 413000000}}},
    //     {266000000, {{"cpu", 400000},  {"mem", 275000000}}},
    //     {177000000, {{"cpu", 200000},  {"mem", 165000000}}}
    // };
    
    // // Initial Settings
    // governor_settings cpu_cluster = {
    //     {345600, {{"gpu", 522750000}, {"mem", 800000000}}},
    //     {499200, {{"gpu", 318750000}, {"mem", 800000000}}},
    //     {652800, {{"gpu", 726750000}, {"mem", 665600000}}},
    //     {806400, {{"gpu", 624750000}, {"mem", 1331200000}}},
    //     {960000, {{"gpu", 726750000}, {"mem", 1331200000}}},
    //     {1113600, {{"gpu", 726750000}, {"mem", 1331200000}}},
    //     {1267200, {{"gpu", 726750000}, {"mem", 1331200000}}},
    //     {1420800, {{"gpu", 726750000}, {"mem", 1331200000}}}
    // };

    // governor_settings gpu_cluster = {
    //     {114750000, {{"cpu", 960000},  {"mem", 665600000}}},
    //     {216750000, {{"cpu", 1420800}, {"mem", 665600000}}},
    //     {318750000, {{"cpu", 1420800}, {"mem", 656000000}}},
    //     {420750000, {{"cpu", 1420800}, {"mem", 1331200000}}},
    //     {522750000, {{"cpu", 1420800}, {"mem", 1331200000}}},
    //     {624750000, {{"cpu", 1420800}, {"mem", 1331200000}}},
    //     {726750000, {{"cpu", 1420800}, {"mem", 1331200000}}},
    //     {854250000, {{"cpu", 1113600}, {"mem", 1331200000}}},
    //     {930750000, {{"cpu", 1267200}, {"mem", 1331200000}}},
    //     {1032750000,{{"cpu", 1420800}, {"mem", 1062400000}}},
    //     {1122000000,{{"cpu", 1267200}, {"mem", 1331200000}}},
    //     {1236750000,{{"cpu", 1267200}, {"mem", 1331200000}}},
    //     {1300500000,{{"cpu", 1420800}, {"mem", 1331200000}}}
    // };

    // governor_settings mem_cluster = {
    //     {40800000,  {{"cpu", 345600}, {"gpu", 318750000}}},
    //     {68000000,  {{"cpu", 499200}, {"gpu", 318750000}}},
    //     {102000000, {{"cpu", 806400}, {"gpu", 216750000}}},
    //     {204000000, {{"cpu", 960000}, {"gpu", 318750000}}},
    //     {408000000, {{"cpu", 1420800},{"gpu", 624750000}}},
    //     {665600000, {{"cpu", 1420800},{"gpu", 624750000}}},
    //     {800000000, {{"cpu", 1420800},{"gpu", 624750000}}},
    //     {1062400000,{{"cpu", 1420800},{"gpu", 726750000}}},
    //     {1331200000,{{"cpu", 1420800},{"gpu", 726750000}}},
    //     {1600000000,{{"cpu", 1420800},{"gpu", 624750000}}},
    //     {1866000000,{{"cpu", 1420800},{"gpu", 624750000}}}
    // };

// Trying new clusters
    governor_settings cpu_cluster = {
        {345600, {{"gpu", 522750000}, {"mem", mem_freq_list[6]}}},
        {499200, {{"gpu", 318750000}, {"mem", mem_freq_list[6]}}},
        {652800, {{"gpu", 726750000}, {"mem", mem_freq_list[7]}}},
        {806400, {{"gpu", 624750000}, {"mem", mem_freq_list[7]}}},
        {960000, {{"gpu", 726750000}, {"mem", mem_freq_list[8]}}},
        {1113600, {{"gpu", 726750000}, {"mem", mem_freq_list[8]}}},
        {1267200, {{"gpu", 726750000}, {"mem", mem_freq_list[9]}}},
        {1420800, {{"gpu", 726750000}, {"mem", mem_freq_list[10]}}}
    };

    governor_settings gpu_cluster = {
        {114750000, {{"cpu", 960000},  {"mem", mem_freq_list[5]}}},
        {216750000, {{"cpu", 1420800}, {"mem",  mem_freq_list[5]}}},
        {318750000, {{"cpu", 1420800}, {"mem",  mem_freq_list[6]}}},
        {420750000, {{"cpu", 1420800}, {"mem",  mem_freq_list[6]}}},
        {522750000, {{"cpu", 1420800}, {"mem",  mem_freq_list[7]}}},
        {624750000, {{"cpu", 1420800}, {"mem",  mem_freq_list[7]}}},
        {726750000, {{"cpu", 1420800}, {"mem",  mem_freq_list[8]}}},
        {854250000, {{"cpu", 1113600}, {"mem",  mem_freq_list[8]}}},
        {930750000, {{"cpu", 1267200}, {"mem",  mem_freq_list[8]}}},
        {1032750000,{{"cpu", 1420800}, {"mem",  mem_freq_list[9]}}},
        {1122000000,{{"cpu", 1267200}, {"mem",  mem_freq_list[9]}}},
        {1236750000,{{"cpu", 1267200}, {"mem",  mem_freq_list[10]}}},
        {1300500000,{{"cpu", 1420800}, {"mem",  mem_freq_list[10]}}}
    };

    governor_settings mem_cluster = {
        {40800000,  {{"cpu", 345600}, {"gpu", gpu_freq_list[0]}}},
        {68000000,  {{"cpu", 499200}, {"gpu", gpu_freq_list[1]}}},
        {102000000, {{"cpu", 806400}, {"gpu", gpu_freq_list[2]}}},
        {204000000, {{"cpu", 960000}, {"gpu", gpu_freq_list[5]}}},
        {408000000, {{"cpu", 1420800},{"gpu", gpu_freq_list[5]}}},
        {665600000, {{"cpu", 1420800},{"gpu", gpu_freq_list[8]}}},
        {800000000, {{"cpu", 1420800},{"gpu", gpu_freq_list[8]}}},
        {1062400000,{{"cpu", 1420800},{"gpu", gpu_freq_list[10]}}},
        {1331200000,{{"cpu", 1420800},{"gpu", gpu_freq_list[10]}}},
        {1600000000,{{"cpu", 1420800},{"gpu", gpu_freq_list[12]}}},
        {1866000000,{{"cpu", 1420800},{"gpu", gpu_freq_list[12]}}}
    };

    // Note we need better to study better frequency combination than these

    // Create an instance of the governor class, and then we set the polling interval in miliseconds. And then we schedule it.
    CRAVEGovernor run_governor(0, 0, 200, cpu_cluster,mem_cluster,gpu_cluster); 
    if(gov_choice == 0){
        run_governor.ScheduleCRAVE();
    }
    else if(gov_choice == 1){
        run_governor.ScheduleCoCAP();
    }
    else if(gov_choice == 2){
        std::cout << "We will check what can we do .. 2"<<std::endl;
    }
    else{
        std::cout<< "Incorrect Governor.. Exit"<<std::endl;
    }

    return 0;
}