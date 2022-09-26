#include "ols_scheduler.h"
#include <assert.h>

// Compile to exe????

// path member variable is the same for all three clocks
// And is never used?????

int main(int argc, char** argv) {
    CpuClock cpu_clock(1);
    GpuClock gpu_clock;
    MemClock mem_clock;


    // CONSTRUCTORS SEEM RIGHT:

    // // CPU clock constructor values in Python code:
    // // self.path = "/sys/devices/system/cpu"
    // // self.cpu_id = cpu_id 
	// // self.dev_count = 8
	// // self.cpu_freq = 0
    // // self.cpu_util = 0
    // assert(cpu_clock.path_      == "/sys/devices/system/cpu");
    // assert(cpu_clock.cpu_id_    == 1); // We used 1 in constructor
    // assert(cpu_clock.dev_count_ == 8);
    // assert(cpu_clock.cpu_freq_  == 0);
    // assert(cpu_clock.cpu_util_  == 0);

    // // GPU clock constructor default values in Python code:
	// // self.path = "/sys/devices/system/cpu"
	// // self.gpu_freq = 0
	// // self.gpu_util = 0
    // assert(gpu_clock.path_     == "/sys/devices/system/cpu");
    // assert(gpu_clock.gpu_freq_ == 0);
    // assert(gpu_clock.gpu_util_ == 0);

    // //Memory clock constructor default values in Python code:
	// // self.path = "/sys/devices/system/cpu"
	// // self.mem_freq = 0
	// // self.mem_util = 0
    // assert(mem_clock.path_     == "/sys/devices/system/cpu");
    // assert(mem_clock.mem_freq_ == 0);
    // assert(mem_clock.mem_util_ == 0);

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

    // Returns 0 if succeeds
    // std::cout << system("bash ../scripts/1_test_get_num_script.sh") << std::endl;

    return 0;
}