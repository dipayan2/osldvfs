#pragma once

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include <iostream>
#include <string>
#include <vector>

/**
 * An class for representing the clock of a memory
 *
 */
class MemClock {
private:
public:
	// Move to private
	std::string path_;
	long long   mem_freq_;
	double      mem_util_;

	/**
	 * Creates a MemClock object with a path_ of "/sys/devices/system/cpu",
	 * a mem_freq_ of 0, and a mem_util_ of 0.
	 *
	 */
	MemClock();

	/**
	 * Gets the current frequency for the memory, stores it in mem_freq_, and returns it
	 *
	 * @return The current memory frequency
	 */
	long long GetClock();
	
	/**
	 * Sets the memory's frequency
	 *
	 * @param new_freq We set the memory frequency to this value and store it in mem_freq_
	 *				   
	 */
	void SetClock(long long new_freq);

	std::vector<long long> GetAllClock(); // Not implemented
	
	double GetUtilization(); // Not implemented

};