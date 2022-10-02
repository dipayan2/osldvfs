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
    int               cpu_id_; // Why do we need this????? cpu_man_.cpu_id_?????
    int               gpu_id_; // Why do we need this????? gpu_man_.gpu_id_????? GpuClock has no id??????
    int               polling_time_; //vs polling_s???? What unit is this in???
    CpuClock          cpu_man_; // https://stackoverflow.com/a/12927220 Initialize member objects!!!
    GpuClock          gpu_man_;
    // std::thread       my_thread_; //https://stackoverflow.com/a/25525465
    MemClock          mem_man_;
    governor_settings cluster_;

    // Allow setting cluster here????
    OlsScheduler(int set_cpu_id, int set_gpu_id, int set_polling_time, governor_settings set_cluster);
};