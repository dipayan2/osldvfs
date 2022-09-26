#include "cpuclock.h"

CpuClock::CpuClock(int set_cpu_id) {
    this->path_      = "/sys/devices/system/cpu";
    this->cpu_id_    = set_cpu_id;
    this->dev_count_ = 8;
    this->cpu_freq_  = 0;
    this->cpu_util_  = 0;
}

int CpuClock::GetClock() {
    // std::cout << "Getting the frequency for cpu number " << this->cpu_id_ << std::endl;

    // Seems to work:
    // char* command = "bash ../scripts/1_test_get_num_script.sh";

    // DO NOT KNOW IF THIS WORKS!!!!?????
    // Relative path???? Python got absolute path????
    char command[256];
    sprintf(command, "bash ../scripts/cpu_get_clock.sh %d", this->cpu_id_);

    char buffer[128];

    // Based on https://stackoverflow.com/a/478960
    FILE* pipe = popen(command, "r");
    if (pipe == NULL) {
        std::cout << "popen() failed!" << std::endl;
        exit(1); //Right????
    }
    else {
        if (fgets(buffer, sizeof(buffer), pipe) != NULL) {
            // There was some error checking here in Python code?????
            this->cpu_freq_ = atoi(buffer); // Newline at end is fine???? Format of files being read???
            // std::cout << "The frequency for cpu number " << this->cpu_id_ << " is " << this->cpu_freq_ << std::endl;
        }
        else {
            std::cout << "fgets() failed!" << std::endl; 
            exit(1);
        }
    }
    pclose(pipe);

    return this->cpu_freq_;
}

void CpuClock::SetClock(int new_freq) {
    // Increase flag????? Will frequency change outside these functions?????
    // std::cout << "The old frequency of cpu number " << this->cpu_id_ << " is " << this->cpu_freq_ << std::endl;

    int inc_flag = 0;
    if (new_freq > this->cpu_freq_) {
        inc_flag = 1;
    }

    char command[256];
    sprintf(command, "bash ../scripts/cpu_set_clock.sh %d %d %d", this->cpu_id_, new_freq, inc_flag);
    system(command);

    this->cpu_freq_ = new_freq;

    return;
}