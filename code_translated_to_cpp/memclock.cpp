#include "memclock.h"

MemClock::MemClock() {
    this->path_     = "/sys/devices/system/cpu";
    this->mem_freq_ = 0;
    this->mem_util_ = 0;
}