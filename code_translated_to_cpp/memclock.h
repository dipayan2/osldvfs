#pragma once

#include <string>
#include <vector>

/**
 * An class for representing the clock of a memory
 *
 */
class MemClock {
private:
	// Meanings???? Types????
	std::string path_;
	int         mem_freq_;
	int         mem_util_;
public:
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
	int GetClock();
	
	/**
	 * Sets the memory's frequency
	 *
	 * @param new_freq If this is greater than mem_freq_, we set the memory frequency to this value,
	 *				   and store it in mem_freq_
	 */
	void SetClock(int new_freq);

	std::vector<int> GetAllClock(); // Not implemented
	
	int GetUtilization(); // Not implemented

};