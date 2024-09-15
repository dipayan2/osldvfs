#include "crave_governor.h"

using std::chrono::duration;
using std::chrono::milliseconds;
using std::chrono::steady_clock;
using std::chrono::time_point;
using std::this_thread::sleep_until;

CRAVEGovernor::CRAVEGovernor(int set_cpu_id, int set_gpu_id, int set_polling_time, governor_settings c_clust, governor_settings m_clust, governor_settings g_clust);
    : cpu_man_(set_cpu_id) {
    
    this->cpu_id_       = set_cpu_id;
    this->gpu_id_       = set_gpu_id; // Not used in this analysis
    this->polling_time_ = set_polling_time;
    this->cpu_cluster_  = c_clust;
    this->mem_cluster_  = m_clust;
    this->gpu_cluster_  = g_clust;
    this->max_freq[CPU] = 1420800;
    this->max_freq[MEM] = 1866000000;
    this->max_freq[GPU] = 1300500000;
    // Set the matrix for our analysis

    this->RI[0][0] = 0.75; this->RI[0][1] = 0.36; this->RI[0][2] = 0.01;
    this->RI[1][0] = 0.48; this->RI[1][1] = 0.87; this->RI[1][2] = 0.69;
    this->RI[2][0] = 0.00; this->RI[2][1] = 0.00; this->RI[2][2] = 0.49;
}

void CRAVEGovernor::getDominantResource(double (&Utility)[3]){
    // Get the utilzation of the three resources

    double util_[3];
    long long cur_freq[3];

    double util_[CPU] = this->cpu_man_.GetUtilization(); 
    long long cur_freq[CPU] = this->cpu_man_.GetClock();
    double util_[MEM] = this->mem_man_.GetUtilization();
    long long cur_freq[MEM] = this->mem_man_.GetClock();
    double util_[GPU] = this->gpu_man_.GetUtilization();
    long long cur_freq[GPU] = this->gpu_man_.GetClock();

    // Get the cost of the resource

    double cost_[3];

    for (int dev = CPU; dev < OTH; ++dev ){
        cost_[dev] = (util_[dev] * (double) cur_freq[dev])/((double) this->max_freq[dev]);
    }

    // double Utility[3];

    for (int dev = CPU; dev < OTH ; ++dev ){
        Utility[dev] = cost_[CPU] * this->RI[dev][CPU] + cost_[MEM] * this->RI[dev][MEM] + cost_[GPU] * this->RI[dev][GPU];
    }

    return;
}

void CRAVEGovernor::SetPolicyCpuFreq() {
    long long cpu_freq = this->cpu_man_.GetClock();

    std::cout << "CPU utilization is " << this->cpu_man_.GetUtilization() << std::endl;

    long long gpu_freq = this->cluster_[cpu_freq]["gpu"];
    long long mem_freq = this->cluster_[cpu_freq]["mem"];

    this->gpu_man_.SetClock(gpu_freq);
    this->mem_man_.SetClock(mem_freq);

    return;
}

void CRAVEGovernor::SetPolicyGpuFreq() {
    long long gpu_freq = this->gpu_man_.GetClock();

    long long cpu_freq = int(this->cluster_[gpu_freq]["cpu"]);
    long long mem_freq = int(this->cluster_[gpu_freq]["mem"]);

    this->cpu_man_.SetClock(cpu_freq);
    this->mem_man_.SetClock(mem_freq);

    return;
}

void CRAVEGovernor::SetPolicyMemFreq() {
    long long mem_freq = this->mem_man_.GetClock();

    std::cout << "Memory utilization is " << this->mem_man_.GetUtilization() << std::endl;

    long long cpu_freq = int(this->cluster_[mem_freq]["cpu"]);
    long long gpu_freq = int(this->cluster_[mem_freq]["gpu"]);

    this->cpu_man_.SetClock(cpu_freq);
    this->gpu_man_.SetClock(gpu_freq);

    return;
}

void CRAVEGovernor::SetPolicyCRAVE(){
    // Set a vector which will have the dominant resource of the system
    double Utility[3] = {0.0, 0.0, 0.0};
    // Get the utility vector which will be used to get the dominant reosurce of the system
    this->getDominantResource(Utility);

    // We will use the Utility metric to get the actual dominant reosurce
    double maxUtil = Utility[CPU];
    int marArg = CPU;

    for (int dev = CPU ; dev < OTH; ++dev){
        if (Utility[dev] > maxUtil){
            maxUtil = Utility[dev];
            maxArg = dev;
        }
    }
    std::cout << "[To be removed] The dominant resource is "<< maxArg << std::endl;

    // unSet the max resource and then set the frequenchy of the rest using the relevant value

    return;
}

void CRAVEGovernor::SetPolicyCpuUtil() {
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

void CRAVEGovernor::SetPolicyMemUtil() {
    double mem_util = this->mem_man_.GetUtilization();
    
    // Not present for SetPolicyCpuUtil???
    // std::cout << "Memory utilization is: " << mem_util << std::endl;
    std::vector<long long> mem_freq_list{165000000, 206000000, 275000000, 413000000, 543000000, 633000000, 728000000, 825000000};
    
    long long mem_freq = mem_freq_list[3];

    // This was a stupid logic, and I don't know why we did it this way????

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

void CRAVEGovernor::SetCluster(governor_settings new_cluster) {
    this->other_cluster_ = new_cluster;
}

void CRAVEGovernor::Schedule() {
    std::cout << "Starting the Scheduler" << std::endl;

    while (true) {
    	time_point<steady_clock> start = steady_clock::now();
        time_point<steady_clock> wake_time = start + std::chrono::milliseconds(this->polling_time_);
        
        this->SetPolicyCpuUtil();
        sleep_until(wake_time);
        
        duration<double> elapsed_seconds = steady_clock::now() - start;
        // Want overhead of 10 milliseconds or less
        std::cout << "Time elapsed for one cycle: " << elapsed_seconds.count() << std::endl;
    }
}