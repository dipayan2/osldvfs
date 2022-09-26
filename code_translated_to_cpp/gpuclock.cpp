#include "gpuclock.h"

GpuClock::GpuClock() {
    this->path_     = "/sys/devices/system/cpu";
    this->gpu_freq_ = 0;
    this->gpu_util_ = 0;
}

int GpuClock::GetClock() {
    std::cout << "Getting the GPU frequency" << std::endl;

    char command[256];
    // ISO C++ forbids converting a string constant to ‘char*’, cannot set char* command = "..."
    sprintf(command, "bash ../scripts/gpu_get_clock.sh");

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
            this->gpu_freq_ = atoi(buffer); // Newline at end is fine???? Format of files being read???
            // std::cout << "The GPU frequency is " << this->gpu_freq_ << std::endl;
        }
        else {
            std::cout << "fgets() failed!" << std::endl; 
            exit(1);
        }
    }
    pclose(pipe);

    return this->gpu_freq_;
}

void GpuClock::SetClock(int new_freq) {
    // std::cout << "Setting GPU frequency to " << new_freq << std::endl;

    // Did not check if new_frequency was different for CpuClock::SetClock()????
    if (new_freq != this->gpu_freq_) {
        int increase_flag = 0;
        if (new_freq > this->gpu_freq_) {
            increase_flag = 1;
        }

        char command[256];
        sprintf(command, "bash ../scripts/gpu_set_clock.sh %d %d", new_freq, increase_flag);

        if (system(command) != 0) {
            std::cout << "Could not set GPU clock frequency" << std::endl;
            exit(1);
        }

        this->gpu_freq_ = new_freq;
    }

    return;
}