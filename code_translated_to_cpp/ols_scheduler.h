#pragma once

#include <chrono>
#include <unordered_map>
#include <thread>

#include "cpuclock.h"
#include "gpuclock.h"
#include "memclock.h"

// what is this????

typedef std::unordered_map<long long, std::unordered_map<std::string, long long>> governor_settings;

class OlsScheduler {
private:
public:
    // Move to private
    int               cpu_id_; 
    int               gpu_id_; 
    int               polling_time_; //vs polling_s???? What unit is this in???
    CpuClock          cpu_man_; // https://stackoverflow.com/a/12927220 Initialize member objects!!!
    GpuClock          gpu_man_;
    // std::thread       my_thread_; //https://stackoverflow.com/a/25525465
    MemClock          mem_man_;
    governor_settings cluster_;

    // Allow setting cluster here????
    /**
     * Creates an OlsScheduler object containing a cpu_id_ of set_cpu_id,
     * a CpuClock with a cpu_id_ of set_cpu_id, a gpu_id_ of set_gpu_id
     * (even though GpuClock has no gpu_id_ member variable), a polling_time_
     * of set_polling_time, a GpuClock and a MemClock created with the default
     * constructors, and a a cluster_ of cluster
     * 
     * @param set_cpu_id       Set cpu_id_ to this value.
     *     Also makes cpu_man_ have this value as its cpu_id_.
     * @param set_gpu_id       Set gpu_id_ to this value.
     * @param set_polling_time Set polling_time_ to this value.
     * @param set_cluster      Set cluster_ to this value.
     *
     */
    OlsScheduler(int set_cpu_id, int set_gpu_id, int set_polling_time, governor_settings set_cluster);

    /**
     * We select the best configuration for all resources based
     * on the current CPU frequency
     * 
     */
    void SetPolicyCpuFreq();

    /**
     * We select the best configuration for all resources based
     * on the current GPU frequency
     * 
     */
    void SetPolicyGpuFreq();

    /**
     * We select the best configuration for all resources based
     * on the current memory frequency
     * 
     */
    void SetPolicyMemFreq();

    /**
     * We select the best configuration for all resources based
     * on the current CPU utilization
     * 
     */
    void SetPolicyCpuUtil();

    /**
     * We select the best configuration for all resources based
     * on the current memory utilization
     * 
     */
    void SetPolicyMemUtil();
        
    /**
     * Setter for cluster_
     * 
     * @param set_cluster      Set cluster_ to this value.
     *
     */
    void SetCluster(governor_settings new_cluster);
    
    /**
     * Sets frequencies based on the current cluster_ 
     * every polling_time_ milliseconds
     *
     */
    void Schedule();
};