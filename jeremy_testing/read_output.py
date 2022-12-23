import os
import pandas as pd
import re
import subprocess
import sys

# Get the functions for getting and setting frequencies for CPU, GPU, and memory
# https://stackoverflow.com/a/40612922
sys.path.append("../")
import cpuclock
import gpuclock
import memclock

# Good to assume just one call of the benchmark executible, repeat multiple times?

script_path = "/home/jbao8899/Desktop/osldvfs/jeremy_testing/print_script.sh"
output = subprocess.check_output(script_path, shell = True).decode('ascii')

# initialization_time_index = output.find("Initialization Time (ms):") + 26
# print(output[initialization_time_index:])

# Always have decimal?
# Units for frequencies?
# All benchmarks use same fields (initialization time, allocation time, etc???)

df = pd.DataFrame({"CPU Frequencies":          pd.Series(dtype = "int"),
                   "GPU Frequencies":          pd.Series(dtype = "int"),
                   "Mem Frequencies":          pd.Series(dtype = "int"),
                   "Initialization Time":      pd.Series(dtype = "float"),
                   "Allocation Time":          pd.Series(dtype = "float"),
                   "Copy To Device Time":      pd.Series(dtype = "float"),
                   "Kernel Time":              pd.Series(dtype = "float"),
                   "Copy Back and Merge Time": pd.Series(dtype = "float"),
                   "Deallocation Time":        pd.Series(dtype = "float"),
                   "Real Time":                pd.Series(dtype = "float"),
                   "User Time":                pd.Series(dtype = "float"),
                   "System Time":              pd.Series(dtype = "float")})

chai_benchmark_times = re.findall(": [0-9]+.[0-9]+", output)
chai_benchmark_times = [float(time[2:]) for time in chai_benchmark_times]
# print(chai_benchmark_times)

time_command_times = re.findall("[0-9]+m[0-9]+.[0-9]+s", output)
# List of tuples of minutes and seconds for real, user, and sys from the "time" command
time_command_times = [time.split("m") for time in time_command_times]
# List of real, user, and sys times (in milliseconds) from the "time" command
time_command_times = [(1000 * ((float(minutes_seconds[0]) * 60) + float(minutes_seconds[1][:(len(minutes_seconds[1]) - 1)]))) for minutes_seconds in time_command_times]
# print(time_command_times)

df.loc[len(df)] = [200000, 177000000, 165000000] + chai_benchmark_times + time_command_times

df.to_csv("results.csv")

# If I try to call the benchmark from a different directory, I get:
# root@odroid:/home/odroid/Desktop# time run 1 taskset -c 0 /home/odroid/benchmark/chai/OpenCL-D/SSSP/sssp
# Mali-T628	Unable to open ./kernel.cl. Exiting...
path_to_benchmark = "/home/odroid/benchmark/chai/OpenCL-D/SSSP/sssp"
command = "time run 1 taskset -c 0 " + path_to_benchmark
print(command)

def get_benchmark_information(path_to_benchmark = "/home/odroid/benchmark/chai/OpenCL-D/SSSP/sssp",
                              path_to_output_file = "results.csv",
                              trials_per_combination = 1):
    """
    For every combination of low, medium, and high frequencies for the CPU, GPU, and memory,
    run the provided Chai OpenCL-D benchmark some number of times.

    Low, medium, and high frequencies for the CPU are defined to be
    200000, 800000, and 1400000, respectively

    Low, medium, and high frequencies for the GPU are defined to be
    177000000, 420000000, and 600000000, respectively

    Low, medium, and high frequencies for the memory are defined to be
    165000000, 543000000, and 825000000, respectively

    The initialization time, allocation time, copy to device time, kernel time,
    copy back and merge time, and deallocation time (all in milliseconds) will be stored
    in the indicated location

    Set all governors to ondemand (or simple_ondemand) before running this!

    :param str path_to_benchmark:      A path to the Chai OpenCL-D benchmarking executible to be run
    :param str path_to_output_file:    A path to the CSV file where results are to be stored. If it already exists,
                                       it will be overwritten. If not, it will be created.
    :param int trials_per_combination: The number of times the given benchmark is to be run for each combination
                                       of frequencies. Should be a positive integer. Equals 1 by default
    """
    # These are the low, medium, and high frequencies for each component
    cpu_frequencies = [200000,    800000,    1400000  ]
    gpu_frequencies = [177000000, 420000000, 600000000]
    mem_frequencies = [165000000, 543000000, 825000000]

    # Here, we create the command that will be called to do the requested benchmarking test
    # Or set working directory and change it back at the end?
    command = "time run 1 taskset -c 0 ./" + path_to_benchmark

    # What do all of these mean???
    # Kernel time in output does not equal "sys" from "time" command???
    # This table contains the results of running the indicated benchmark a single time
    # It records which combination of CPU, GPU, and memory frequencies were used,
    # various times returned by the benchmarking program itself (in milliseconds), and
    # the real, user, and sys runtimes from the "time" command, converted to milliseconds
    df = pd.DataFrame({"CPU Frequencies":          pd.Series(dtype = "int"),
                       "GPU Frequencies":          pd.Series(dtype = "int"),
                       "Mem Frequencies":          pd.Series(dtype = "int"),
                       "Initialization Time":      pd.Series(dtype = "float"),
                       "Allocation Time":          pd.Series(dtype = "float"),
                       "Copy To Device Time":      pd.Series(dtype = "float"),
                       "Kernel Time":              pd.Series(dtype = "float"),
                       "Copy Back and Merge Time": pd.Series(dtype = "float"),
                       "Deallocation Time":        pd.Series(dtype = "float"),
                       "Real Time":                pd.Series(dtype = "float"),
                       "User Time":                pd.Series(dtype = "float"),
                       "System Time":              pd.Series(dtype = "float")})

    # Create instances of the classes for controlling clock frequencies
    cpu_clock = cpuclock.CPUClock(0)
    cpu_clock.get_clock()
    gpu_clock = gpuclock.GPUClock()
    gpu_clock.get_clock()
    mem_clock = memclock.MemClock()
    mem_clock.get_clock()

    for cpu_freq in cpu_frequencies:
        for gpu_freq in gpu_frequencies:
            for mem_freq in mem_frequencies:
                # Set the frequencies
                cpu_clock.set_clock(cpu_freq)
                gpu_clock.set_clock(gpu_freq)
                mem_clock.set_clock(mem_freq)

                # Run the requested test
                output = subprocess.check_output(path_to_benchmark, shell = True).decode('ascii')                

# FOR BFS:
# Mali-T628    Number of nodes = 264346    Number of edges = 733846    Initialization Time (ms): 14009.010000
# Allocation Time (ms): 80.845000
# Copy To Device Time (ms): 1827.828000
# Kernel Time (ms): 1819.228000
# Copy Back and Merge Time (ms): 1310.447000
# Deallocation Time (ms): 152.994000
# Test Passed

# real    0m30.554s
# user    0m22.316s
# sys    0m5.477s

# root@odroid:/home/odroid/benchmark/chai/OpenCL-D/SSSP# time run 2 taskset -c 0 ./sssp
# Mali-T628	Number of nodes = 264346	Number of edges = 733846	Initialization Time (ms): 2055.342000
# Allocation Time (ms): 7.905000
# Copy To Device Time (ms): 678.461000
# Kernel Time (ms): 1891.677000
# Copy Back and Merge Time (ms): 356.091000
# Deallocation Time (ms): 24.491000
# Test Passed
# Mali-T628	Number of nodes = 264346	Number of edges = 733846	Initialization Time (ms): 2017.273000
# Allocation Time (ms): 5.160000
# Copy To Device Time (ms): 693.501000
# Kernel Time (ms): 1928.634000
# Copy Back and Merge Time (ms): 361.867000
# Deallocation Time (ms): 24.837000
# Test Passed

# real	0m18.261s
# user	0m8.065s
# sys	0m3.254s
