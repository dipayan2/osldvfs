#pragma once

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <string>
#include <vector>
#include <iostream>

/**
 * An class for representing the clock of a CPU
 *
 */
class CpuClock {
private:
public:
	// Meanings???? Types???
    // TODO: MOVE TO PRIVATE
	std::string path_; //Never used????
    int         cpu_id_;
    int         dev_count_;
	int         cpu_freq_;
	int         cpu_util_;

    /**
	 * Creates a CpuClock object with a path_ of "/sys/devices/system/cpu",
	 * a cpu_id_ equal to set_cpu_id, a dev_count_ of 8, a cpu_freq_ of 0,
     * and a cpu_util_ of 0.
     * 
     * @param set_cpu_id Set cpu_id_ to this value.
	 *
	 */
    CpuClock(int set_cpu_id);

	/**
	 * Gets the current frequency for this GPU, stores it in cpu_freq_, and returns it
	 *
	 * @return The current CPU frequency
	 */
    int GetClock();

	/**
	 * Sets this CPU's frequency
	 *
	 * @param new_freq We set the CPU frequency to this value and store it in cpu_freq_
	 *				   
	 */
    void SetClock(int new_freq);

	std::vector<int> GetAllClock(); // Not implemented
	
	int GetUtilization(); // Not implemented
};