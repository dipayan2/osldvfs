#include "memclock.h"

MemClock::MemClock() {
    this->path_     = "/sys/devices/system/cpu";
    this->mem_freq_ = 0;
    this->mem_util_ = 0;
}

int MemClock::GetClock() {
    // std::cout << "Getting the memory frequency" << std::endl;

    char command[256];
    // ISO C++ forbids converting a string constant to ‘char*’, cannot set char* command = "..."
    sprintf(command, "bash ../scripts/mem_get_clock.sh");

    char buffer[128];

    // Based on https://stackoverflow.com/a/478960
    FILE* pipe = popen(command, "r");
    if (pipe == NULL) {
        std::cout << "popen() failed when trying to get the memory frequency" << std::endl;
        exit(1); //Right????
    }
    else {
        if (fgets(buffer, sizeof(buffer), pipe) != NULL) {
            // There was some error checking here in Python code?????
            this->mem_freq_ = atoi(buffer); // Newline at end is fine???? Format of files being read???
            // std::cout << "The memory frequency is " << this->mem_freq_ << std::endl;
        }
        else {
            std::cout << "fgets() failed when trying to get the memory frequency" << std::endl; 
            exit(1);
        }
    }
    pclose(pipe);

    return this->mem_freq_;
}

void MemClock::SetClock(int new_freq) {
    // std::cout << "Setting the memory frequency to " << new_freq << std::endl;

    if (new_freq != this->mem_freq_) {
        int increase_flag = 0;
        if (new_freq > this->mem_freq_) {
            increase_flag = 1;
        }

        char command[256];
        sprintf(command, "bash ../scripts/mem_set_clock.sh %d %d", new_freq, increase_flag);

        if (system(command) != 0) {
            std::cout << "Could not set memory clock frequency" << std::endl;
            exit(1);
        }

        this->mem_freq_ = new_freq;
    }
    return;
}