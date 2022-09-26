#pragma once

// !!! Related Header, C system headers, C++ standard library headers, 
// other library headers, your project's headers.
#include <string>
#include <vector>

/**
 * An class for representing the clock of a GPU
 *
 */
class GpuClock {
private:
	// Meanings???? Types????
	std::string path_;
	int         gpu_freq_;
	int         gpu_util_;
public:
	/**
	 * Creates a GpuClock object with a path_ of "/sys/devices/system/cpu",
	 * a gpu_freq_ of 0, and a gpu_util_ of 0.
	 *
	 */
	GpuClock();

	/**
	 * Gets the current frequency for the GPU, stores it in gpu_freq_, and returns it
	 *
	 * @return The current GPU frequency
	 */
	int GetClock(); //What is type of gpu_freq????? string???? -> we get all but last character
	
	/**
	 * Sets the GPU's frequency
	 *
	 * @param new_freq If this is greater than gpu_freq_, we set the GPU frequency to this value,
	 *				   and store it in gpu_freq_
	 */
	void SetClock(int new_freq);

	std::vector<int> GetAllClock(); // Not implemented
	
	int GetUtilization(); // Not implemented
};