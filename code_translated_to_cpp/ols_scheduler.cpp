#include "ols_scheduler.h"

using std::chrono::duration;
using std::chrono::milliseconds;
using std::chrono::steady_clock;
using std::chrono::time_point;
using std::this_thread::sleep_until;

OlsScheduler::OlsScheduler(int set_cpu_id, int set_gpu_id, int set_polling_time, governor_settings set_cluster)
    : cpu_man_(set_cpu_id) {
    
    this->cpu_id_       = set_cpu_id;
    this->gpu_id_       = set_gpu_id;
    this->polling_time_ = set_polling_time;
    this->cluster_      = set_cluster;
}

void OlsScheduler::SetPolicyCpuFreq() {
    long long cpu_freq = this->cpu_man_.GetClock();

    // Present but commented out????
    // Not there for GPU, there for memory??????
    // std::cout << "CPU utilization is " << this->cpu_man_.GetUtilization() << std::endl;

    long long gpu_freq = this->cluster_[cpu_freq]["gpu"];
    long long mem_freq = this->cluster_[cpu_freq]["mem"];

    this->gpu_man_.SetClock(gpu_freq);
    this->mem_man_.SetClock(mem_freq);

    // std::cout << "Set GPU frequency to " << gpu_freq
    //           << " and memory frequency to " << mem_freq
    //           << " based on the CPU frequency of " << cpu_freq
    //           << std::endl;
    

    return;
}

void OlsScheduler::SetPolicyGpuFreq() {
    long long gpu_freq = this->gpu_man_.GetClock();

    long long cpu_freq = int(this->cluster_[gpu_freq]["cpu"]);
    long long mem_freq = int(this->cluster_[gpu_freq]["mem"]);

    this->cpu_man_.SetClock(cpu_freq);
    this->mem_man_.SetClock(mem_freq);

    // std::cout << "Set CPU frequency to " << cpu_freq
    //           << " and memory frequency to " << mem_freq
    //           << " based on the GPU frequency of " << gpu_freq
    //           << std::endl;

    return;
}

void OlsScheduler::SetPolicyMemFreq() {
    long long mem_freq = this->mem_man_.GetClock();

    // std::cout << "Memory utilization is " << this->mem_man_.GetUtilization() << std::endl;

    long long cpu_freq = int(this->cluster_[mem_freq]["cpu"]);
    long long gpu_freq = int(this->cluster_[mem_freq]["gpu"]);

    this->cpu_man_.SetClock(cpu_freq);
    this->gpu_man_.SetClock(gpu_freq);

    // std::cout << "Set CPU frequency to " << cpu_freq
    //           << " and GPU frequency to " << gpu_freq
    //           << " based on the memory frequency of " << mem_freq
    //           << std::endl;
}

void OlsScheduler::SetPolicyCpuUtil() {
    double cpu_util = this->cpu_man_.GetUtilization();

    std::vector<long long> cpu_freq_list{200000, 300000, 400000, 500000, 600000, 700000, 800000, 900000, 1000000, 1100000, 1200000, 1300000, 1400000};

    long long cpu_freq = cpu_freq_list[5];

    if (cpu_util > 0.5) {
        cpu_freq = cpu_freq_list[10];
    }
    else if (cpu_util > 0.3) {
        cpu_freq = cpu_freq_list[5];
    }
    else {
        cpu_freq = cpu_freq_list[0];
    }            

    this->cpu_man_.SetClock(cpu_freq);
    
    long long gpu_freq = this->cluster_[cpu_freq]["gpu"];
    long long mem_freq = this->cluster_[cpu_freq]["mem"];
    this->gpu_man_.SetClock(gpu_freq);
    this->mem_man_.SetClock(mem_freq);

    return;
}

void OlsScheduler::SetPolicyMemUtil() {
    double mem_util = this->mem_man_.GetUtilization();
    
    // Not present for SetPolicyCpuUtil???
    // std::cout << "Memory utilization is: " << mem_util << std::endl;
    std::vector<long long> mem_freq_list{165000000, 206000000, 275000000, 413000000, 543000000, 633000000, 728000000, 825000000};
    
    long long mem_freq = mem_freq_list[3];

    if (mem_util > 0.6) {
        mem_freq = mem_freq_list[5];
    }
    else if (mem_util > 0.3) {
        mem_freq = mem_freq_list[3];
    }
    else {
        mem_freq = mem_freq_list[0];
    }

    this->mem_man_.SetClock(mem_freq);

    long long cpu_freq = this->cluster_[mem_freq]["cpu"];
    long long gpu_freq = this->cluster_[mem_freq]["gpu"];

    this->cpu_man_.SetClock(cpu_freq);
    this->gpu_man_.SetClock(gpu_freq);

    return;
}

void OlsScheduler::SetCluster(governor_settings new_cluster) {
    this->cluster_ = new_cluster;
}

void OlsScheduler::Schedule() {
    std::cout << "Starting the Scheduler" << std::endl;
    
    while (true) {
    	time_point<steady_clock> start = steady_clock::now();
        time_point<steady_clock> wake_time = start + std::chrono::milliseconds(1000);
        
        this->SetPolicyCpuUtil();
        sleep_until(wake_time);
        
        duration<double> elapsed_seconds = steady_clock::now() - start;
        std::cout << "Time elapsed for one cycle: " << elapsed_seconds.count() << std::endl;
    }
}