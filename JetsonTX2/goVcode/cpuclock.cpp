#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <algorithm>

#include <boost/lexical_cast.hpp>
#include <boost/regex.hpp>
#include <boost/date_time.hpp>
#include <boost/date_time/posix_time/posix_time.hpp>

#include "cpuclock.h"

CpuClock::CpuClock(int set_cpu_id) {
    this->path_      = "/sys/devices/system/cpu";
    this->cpu_id_    = set_cpu_id;
    this->dev_count_ = 8;
    this->cpu_freq_  = 0;
    this->cpu_load  = 0.0;
    // Initializing the per-core variable for later perusal
    for (int i = 0; i < 6; i++){ 
        this->cpu_util_[i] = -1;
        this->cpu_time_[i] = 0;
        this->cpu_idle_[i] = 0;       
    }
    
}

long long CpuClock::GetClock() {
    // std::cout << "Getting the frequency for cpu number " << this->cpu_id_ << std::endl;

    // Seems to work:
    // char* command = "bash ../scripts/1_test_get_num_script.sh";

    // DO NOT KNOW IF THIS WORKS!!!!?????
    // Relative path???? Python got absolute path????
    char command[256];
    snprintf(command,256, "bash ../scripts/cpu_get_clock.sh %d", this->cpu_id_);

    char buffer[128];

    // Based on https://stackoverflow.com/a/478960
    FILE* pipe = popen(command, "r");
    if (pipe == NULL) {
        std::cout << "popen() failed while trying to get the CPU frequency for CPU number " << this->cpu_id_ << std::endl;
        exit(1);
    }
    else {
        if (fgets(buffer, sizeof(buffer), pipe) != NULL) {
            // There was some error checking here in Python code?????
            this->cpu_freq_ = atoll(buffer); // Newline at end is fine???? Format of files being read???
            // std::cout << "The frequency for cpu number " << this->cpu_id_ << " is " << this->cpu_freq_ << std::endl;
        }
        else {
            std::cout << "fgets() failed while trying to get the CPU frequency for CPU number " << this->cpu_id_ << std::endl; 
            exit(1);
        }
    }
    pclose(pipe);

    return this->cpu_freq_;
}

void CpuClock::SetClock(long long new_freq) {
    // std::cout << "Setting frequency of cpu number " << this->cpu_id_ << " to " << new_freq << std::endl;

    // Did not check if new_freq is different because it was not causing issues

    if (new_freq != this->cpu_freq_) {
        int increase_flag = 0;
        if (new_freq > this->cpu_freq_) {
            increase_flag = 1;
        }

        char command[256];
        snprintf(command,256, "bash ../scripts/cpu_set_clock.sh %d %lld %d", this->cpu_id_, new_freq, increase_flag);
    
        if (system(command) != 0) {
            std::cout << "Could not set clock frequency for CPU number " << this->cpu_id_ << std::endl;
            exit(1);
        }

        this->cpu_freq_ = new_freq;
    }
    return;
}

double CpuClock::GetUtilization() {
    /*
    The file for CPU Usage looks like this: 
    0 0 1197858456989 1011678547142 50156791
    1 0 1197858456995 1197574086967 0
    2 0 1197858456997 1197831394038 0
    3 0 1197858456998 1002111657919 81145230
    4 0 1197858457000 994804318858 42110913
    5 0 1197858457001 999061595664 22807188

    We need to read the two data from column 3 andf column 4 to get the idle time and then we can use them to calculate the utilization
    */
    std::ifstream cpuload("/sys/devices/system/cpu/cpufreq/cpuload/cpu_usage"); // Open the file to read data 
    if (!cpuload) {
        std::cerr << "Unable to open file!" << std::endl;
        return -1.0;
    }
    std::vector<unsigned long long> total_time_list;
    std::vector<unsigned long long> idle_time_list;

    std::string line;
	while ( std::getline(cpuload, line) ) {


        std::stringstream ss(line);  // Create string stream for parsing the line
        int id;
        unsigned long long u_val0;
        unsigned long long total_time;
        unsigned long long idle_time;
        unsigned long long u_val1;

        // Read from the string stream into the variables
        ss >> id >> u_val0 >> total_time >> idle_time >> u_val1;

        total_time_list.push_back( total_time);
        idle_time_list.push_back( idle_time);
			
	}

    // The file has been read, updated the values for calculation
    if (total_time_list.size() < 6){
        std::cerr << " The CPU data is incomplete" << std::endl;
        return -1.0;
    }
    double temp_load = 0.0;

    for(int idx = 0; idx < 6; idx++){
        if (this->cpu_time_[idx] == 0){
            // printf("I'm in 0 condition\n");
            this->cpu_util_[idx] = -1;
            this->cpu_time_[idx] = total_time_list[idx];
            this->cpu_idle_[idx] = idle_time_list[idx];
        }
        else{
            unsigned long long dtime = total_time_list[idx] - this->cpu_time_[idx];
            unsigned long long id_time = idle_time_list[idx] - this->cpu_idle_[idx];
            
            this->cpu_util_[idx] = 100.0 * ( 1.0 - ( (double) id_time / (double) dtime ));
            // printf("I'm in non zero condition %llu, %llu,  %lf \n",id_time, dtime, this->cpu_util_[idx] );
            this->cpu_time_[idx] = total_time_list[idx];
            this->cpu_idle_[idx] = idle_time_list[idx];
        }

        if (this-> cpu_util_[idx] > temp_load ){
            temp_load = this-> cpu_util_[idx];
        }
    }

    this->cpu_load = temp_load;
    return this->cpu_load;
}
