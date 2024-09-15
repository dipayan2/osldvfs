#include <assert.h>

#include "crave_governor.h"

int main(int argc, char** argv) {
    // Lists of the permitted frequencies for the CPU, GPU, and memory
    std::vector<long long> cpu_freq_list{200000, 300000, 400000, 500000, 600000, 700000, 800000, 900000, 1000000, 1100000, 1200000, 1300000, 1400000};
    std::vector<long long> gpu_freq_list{600000000, 543000000, 480000000, 420000000, 350000000, 266000000, 177000000};
    std::vector<long long> mem_freq_list{165000000, 206000000, 275000000, 413000000, 543000000, 633000000, 728000000, 825000000};

    // These maps are descriptions of what should be done in certain situations
    // You enter a value (something's frequency????)
    // and it tells you what values the frequencies of the
    // other components should be set to.

    // gpu driven governor setting
    governor_settings gpu_cluster = {
        {600000000, {{"cpu", 1400000}, {"mem", 825000000}}},
        {543000000, {{"cpu", 1200000}, {"mem", 728000000}}},
        {480000000, {{"cpu", 1000000}, {"mem", 633000000}}},
        {420000000, {{"cpu", 800000},  {"mem", 543000000}}},
        {350000000, {{"cpu", 600000},  {"mem", 413000000}}},
        {266000000, {{"cpu", 400000},  {"mem", 275000000}}},
        {177000000, {{"cpu", 200000},  {"mem", 165000000}}}
    };
    
    // memory driven governor setting
    governor_settings mem_cluster = {
        {165000000, {{"gpu", 177000000}, {"cpu", 200000}}},
        {206000000, {{"gpu", 177000000}, {"cpu", 400000}}},
        {275000000, {{"gpu", 266000000}, {"cpu", 600000}}},
        {413000000, {{"gpu", 350000000}, {"cpu", 800000}}},
        {543000000, {{"gpu", 420000000}, {"cpu", 1000000}}},
        {633000000, {{"gpu", 480000000}, {"cpu", 1100000}}},
        {728000000, {{"gpu", 543000000}, {"cpu", 1200000}}},
        {825000000, {{"gpu", 600000000}, {"cpu", 1400000}}}
    };

    // cpu driven governor setting
    governor_settings cpu_cluster = {
        {200000,  {{"gpu", 177000000}, {"mem", 165000000}}},
        {300000,  {{"gpu", 177000000}, {"mem", 165000000}}},
        {400000,  {{"gpu", 177000000}, {"mem", 165000000}}},
        {500000,  {{"gpu", 266000000}, {"mem", 275000000}}},
        {600000,  {{"gpu", 266000000}, {"mem", 275000000}}},
        {700000,  {{"gpu", 350000000}, {"mem", 413000000}}},
        {800000,  {{"gpu", 350000000}, {"mem", 413000000}}},
        {900000,  {{"gpu", 420000000}, {"mem", 543000000}}},
        {1000000, {{"gpu", 420000000}, {"mem", 543000000}}},
        {1100000, {{"gpu", 480000000}, {"mem", 633000000}}},
        {1200000, {{"gpu", 480000000}, {"mem", 633000000}}},
        {1300000, {{"gpu", 600000000}, {"mem", 825000000}}},
        {1400000, {{"gpu", 600000000}, {"mem", 825000000}}}
    };

    // What is this???
    governor_settings cpu_nu05_cluster0 = {
        {200000,  {{"gpu", 600000000}, {"mem", 543000000}}},
        {300000,  {{"gpu", 350000000}, {"mem", 633000000}}},
        {400000,  {{"gpu", 177000000}, {"mem", 825000000}}},
        {500000,  {{"gpu", 350000000}, {"mem", 543000000}}},
        {600000,  {{"gpu", 543000000}, {"mem", 543000000}}},
        {700000,  {{"gpu", 350000000}, {"mem", 633000000}}},
        {800000,  {{"gpu", 350000000}, {"mem", 543000000}}},
        {900000,  {{"gpu", 177000000}, {"mem", 543000000}}},
        {1000000, {{"gpu", 420000000}, {"mem", 275000000}}},
        {1100000, {{"gpu", 480000000}, {"mem", 275000000}}},
        {1200000, {{"gpu", 480000000}, {"mem", 206000000}}},
        {1300000, {{"gpu", 350000000}, {"mem", 206000000}}},
        {1400000, {{"gpu", 177000000}, {"mem", 165000000}}}
    };

    governor_settings mem_cluster0 = {
        {165000000, {{"gpu", 177000000}, {"cpu", 1400000}}},
        {206000000, {{"gpu", 480000000}, {"cpu", 1200000}}},
        {275000000, {{"gpu", 420000000}, {"cpu", 1000000}}},
        {413000000, {{"gpu", 177000000}, {"cpu", 900000}}},
        {543000000, {{"gpu", 543000000}, {"cpu", 700000}}},
        {633000000, {{"gpu", 350000000}, {"cpu", 600000}}},
        {728000000, {{"gpu", 350000000}, {"cpu", 500000}}},
        {825000000, {{"gpu", 177000000}, {"cpu", 400000}}}
    };

    governor_settings cpu_nu05_cluster1 = {
        {200000,  {{"gpu", 480000000}, {"mem", 543000000}}},
        {300000,  {{"gpu", 480000000}, {"mem", 633000000}}},
        {400000,  {{"gpu", 177000000}, {"mem", 825000000}}},
        {500000,  {{"gpu", 350000000}, {"mem", 543000000}}},
        {600000,  {{"gpu", 350000000}, {"mem", 543000000}}},
        {700000,  {{"gpu", 350000000}, {"mem", 633000000}}},
        {800000,  {{"gpu", 350000000}, {"mem", 543000000}}},
        {900000,  {{"gpu", 177000000}, {"mem", 633000000}}},
        {1000000, {{"gpu", 420000000}, {"mem", 728000000}}},
        {1100000, {{"gpu", 350000000}, {"mem", 633000000}}},
        {1200000, {{"gpu", 350000000}, {"mem", 825000000}}},
        {1300000, {{"gpu", 350000000}, {"mem", 728000000}}},
        {1400000, {{"gpu", 177000000}, {"mem", 633000000}}}
    };

    // Seems right
    CRAVEGovernor run_governor(1, 2, 1000, cpu_cluster);

    // //should be 1
    // std::cout << "ols_scheduler.cpu_id_: " << ols_scheduler.cpu_id_ << std::endl;
    // //should be 2
    // std::cout << "ols_scheduler.gpu_id_: " << ols_scheduler.gpu_id_ << std::endl;
    // // Should be 1000
    // std::cout << "ols_scheduler.polling_time_: " << ols_scheduler.polling_time_ << std::endl;
    // // Should be 420000000
    // std::cout << "ols_scheduler.cluster_[1000000][\"gpu\"]: " << ols_scheduler.cluster_[1000000]["gpu"] << std::endl;
    // // Should be 275000000
    // std::cout << "ols_scheduler.cluster_[500000][\"mem\"]: " << ols_scheduler.cluster_[500000]["mem"] << std::endl;

    // // Should be "/sys/devices/system/cpu"
    // std::cout << ols_scheduler.cpu_man_.path_ << std::endl;
    // // Should be 1
    // std::cout << ols_scheduler.cpu_man_.cpu_id_ << std::endl;
    // // Should be 8
    // std::cout << ols_scheduler.cpu_man_.dev_count_ << std::endl;
    // // Should be 0
    // std::cout << ols_scheduler.cpu_man_.cpu_freq_ << std::endl;
    // // Should be 0
    // std::cout << ols_scheduler.cpu_man_.cpu_util_ << std::endl;

    // // Should be "/sys/devices/system/cpu"
    // std::cout << ols_scheduler.gpu_man_.path_ << std::endl;
    // // Should be 0
    // std::cout << ols_scheduler.gpu_man_.gpu_freq_ << std::endl;
    // // Should be 0
    // std::cout << ols_scheduler.gpu_man_.gpu_util_ << std::endl;

    // // Should be "/sys/devices/system/cpu"
    // std::cout << ols_scheduler.mem_man_.path_ << std::endl;
    // // Should be 0
    // std::cout << ols_scheduler.mem_man_.mem_freq_ << std::endl;
    // // Should be 0
    // std::cout << ols_scheduler.mem_man_.mem_util_ << std::endl;

    // CpuClock cpu_clock(1);
    // GpuClock gpu_clock;
    // MemClock mem_clock;

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
    // cat: /sys/devices/system/cpu/cpu1/cpufreq/cpuinfo_cur_freq: No such file or directory
    // std::cout << cpu_clock.GetClock() << std::endl;
    // std::cout << cpu_clock.cpu_freq_ << std::endl;

    // char command[256];
    // sprintf(command, "bash ../scripts/gpu_set_clock.sh %d %d", 123456789, 0);
    // std::cout << command << std::endl;

    // Returns 0 if succeeds
    // std::cout << system("bash ../scripts/1_test_get_num_script.sh") << std::endl;

    // Testing SetClock analogue on example script and file
    
    // Increase works!!!!
    // int cpu_num = 1;
    // long long new_freq = 12345;
    // int increase_flag = 1;

    // char command[256];
    // sprintf(command, "bash ../scripts/2_test_add_to_file.sh %d %lld %d", cpu_num, new_freq, increase_flag);
    // if (system(command) != 0) {
    //     std::cout << "Could not use example clock setting script from C++!" << std::endl;
    // }

    // Decrease Works!!!!
    // int cpu_num = 1;
    // long long new_freq = 3579;
    // int increase_flag = 0;

    // char command[256];
    // sprintf(command, "bash ../scripts/2_test_add_to_file.sh %d %lld %d", cpu_num, new_freq, increase_flag);
    // if (system(command) != 0) {
    //     std::cout << "Could not use example clock setting script from C++!" << std::endl;
    // }



    return 0;
}