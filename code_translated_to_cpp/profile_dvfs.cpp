#include "ols_scheduler.h"

// Compile to exe????

int main(int argc, char** argv) {
    CpuClock cpu_clock(1);
    // Works with 1_test_get_num_script.sh and 1_EXAMPLE_NUM_FILE.txt
    // DO NOT KNOW IF IT WORKS WITH YOUR SCRIPT?????
    // On here, it says that there is no such file or directory????
    // cat: /sys/devices/system/cpu/cpu1/cpufreq/cpuinfo_cur_freq: No such file or directory
    // sudo requires password?????
    // std::cout << cpu_clock.GetClock() << std::endl;
    // std::cout << cpu_clock.cpu_freq_ << std::endl;

    //"/home/jbao8899/Desktop/osldvfs/scripts/gpu_get_clock.sh"

    // char command[256];
    // sprintf(command, "bash ../scripts/gpu_set_clock.sh %d %d", 123456789, 0);
    // std::cout << command << std::endl;

    std::cout << system("bash ../scripts/1_test_get_num_script.sh") << std::endl;

    return 0;
}