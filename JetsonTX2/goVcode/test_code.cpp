#include <iostream>
#include <stdlib.h>
#include <stdio.h>
#include <vector>
#include <string>
#include <chrono>
#include <thread>

#include "cpuclock.h"

int main(int argc, char** argv){
    CpuClock myCPU(0);
    std::cout<< "The CPU Utilization " << myCPU.GetUtilization() << std::endl;
    std::cout<< "The CPU Clock: " << myCPU.GetClock() << std::endl;
    std::this_thread::sleep_for(std::chrono::milliseconds(1000));
    std::cout<< "The CPU Utilization: " << myCPU.GetUtilization() << std::endl;
    myCPU.SetClock(1113600);
    std::this_thread::sleep_for(std::chrono::milliseconds(1000));
    std::cout<< "The CPU Utilization " << myCPU.GetUtilization() << std::endl;
    std::cout<< "The CPU Clock: " << myCPU.GetClock() << std::endl;
    
    return 0;
}
