#pragma once

#include <unordered_map>
#include <thread>
#include "cpuclock.h"
#include "gpuclock.h"
#include "memclock.h"

// what is this????

class OlsScheduler {
private:
    // Meanings??? Types??? One of each device?????
    int         cpu_id_;
    int         gpu_id_;
    int         polling_time_; //vs polling_s???? What unit is this in???
    CpuClock    cpu_man_; // https://stackoverflow.com/a/12927220 Initialize member objects!!!
    GpuClock    gpu_man_;
    std::thread my_thread_; //https://stackoverflow.com/a/25525465
    MemClock    mem_man_;
    std::unordered_map<int, std::unordered_map<std::string, int>> cluster;
public:

};