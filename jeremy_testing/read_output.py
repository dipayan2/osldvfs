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

# Good to assume just one call of the benchmark executible, repeat multiple times????

def get_benchmark_information(benchmark_to_run = "sssp",
                              trials_per_combination = 1):
    """
    For every combination of low, medium, and high frequencies for the CPU, GPU, and memory,
    run the provided Chai OpenCL-D benchmark some number of times.

    Call "sudo su" beore running this file

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

    :param str benchmark_to_run:       The name of the Chai OpenCL-D benchmark tobe run
                                       (such as sssp, hsti, hsto, bfs, etc.)
                                       Capitalization does not matter
    :param str output_file_name:       The name of the CSV file where results are to be stored. If it already exists,
                                       it will be overwritten. If not, it will be created.
                                       Is letting the user specify this risky? I don't know.
    :param int trials_per_combination: The number of times the given benchmark is to be run for each combination
                                       of frequencies. Should be a positive integer. Equals 1 by default
    """
    # Determine name of output file
    # Originally, you could specify this as an argument, but we
    # need a way to remember what tests were run, so it will now
    # be determined automatically
    output_file_name = str(trials_per_combination) + "_trials_" + benchmark_to_run.lower() + "_results.csv"

    # These are the low, medium, and high frequencies for each component
    cpu_frequencies = [200000,    800000,    1400000  ]
    gpu_frequencies = [177000000, 420000000, 600000000]
    mem_frequencies = [165000000, 543000000, 825000000]

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

    # Record which directory we were originally in, so we can return to it to save our results
    original_directory = os.getcwd()

    # Record the directory we have to go to in order to use the various clock commands (which rely on)
    # relative paths to access the scripts they use
    os.chdir("..")
    directory_for_clock_functions = os.getcwd()

    # Here, we figure out the path to the directory containing the test to be run
    directory_of_benchmark = "/home/odroid/benchmark/chai/OpenCL-D/" + benchmark_to_run.upper()
    # Here, we generate the command to be used to run our test 1 or more times
    # for each combination of frequencies (call this command once each time)
    command_for_test = "time taskset -c 0 ./" + benchmark_to_run.lower()

    # We move to the directory containing the benchmark
    # Because I see "Mali-T628	Unable to open ./kernel.cl. Exiting..."
    # when I try to use one of the testing executibles from a different directory
    os.chdir(directory_of_benchmark)

    # Create instances of the taskset -c 7classes for controlling clock frequencies
    os.chdir(directory_for_clock_functions)
    cpu_clock = cpuclock.CPUClock(0)
    cpu_clock.get_clock()
    gpu_clock = gpuclock.GPUClock()
    gpu_clock.get_clock()
    mem_clock = memclock.MemClock()
    mem_clock.get_clock()

    # For each combination of frequencies, we run the requested test the specified
    # number of times and store the results
    for cpu_freq in cpu_frequencies:
        for gpu_freq in gpu_frequencies:
            for mem_freq in mem_frequencies:
                for i in range(trials_per_combination):
                    # Set the frequencies
                    os.chdir(directory_for_clock_functions)
                    cpu_clock.set_clock(cpu_freq)
                    gpu_clock.set_clock(gpu_freq)
                    mem_clock.set_clock(mem_freq)

                    # Run the requested test
                    os.chdir(directory_of_benchmark)
                    output = subprocess.check_output(command_for_test, shell = True, executable="/bin/bash").decode('ascii')                
                    
                    # Extract all times provided by Chai
                    chai_benchmark_times = re.findall(": [0-9]+.[0-9]+", output)
                    chai_benchmark_times = [float(time[2:]) for time in chai_benchmark_times]

                    # Extract all times provided by the "time" command in the shell
                    time_command_times = re.findall("[0-9]+m[0-9]+.[0-9]+s", output)
                    # List of tuples of minutes and seconds for real, user, and sys from the "time" command
                    time_command_times = [time.split("m") for time in time_command_times]
                    # List of real, user, and sys times (in milliseconds) from the "time" command
                    time_command_times = [(1000 * ((float(minutes_seconds[0]) * 60) + float(minutes_seconds[1][:(len(minutes_seconds[1]) - 1)]))) for minutes_seconds in time_command_times]

                    # Store all the times, as well as the frequencies used for all components
                    df.loc[len(df)] = [cpu_freq, gpu_freq, mem_freq] + chai_benchmark_times + time_command_times
    
    # Go back to the original directory
    os.chdir(original_directory)       

    # Store the results in the file "output_file_name".
    # If it exists, overwrite it. If not, create it 
    df.to_csv(output_file_name)

# Run SSSP once for each combination of frequencies, store to results.csv
get_benchmark_information()

# Exploratory code:

# script_path = "/home/jbao8899/Desktop/osldvfs/jeremy_testing/print_script.sh"
# output = subprocess.check_output(script_path, shell = True).decode('ascii')

# # initialization_time_index = output.find("Initialization Time (ms):") + 26
# # print(output[initialization_time_index:])

# # Always have decimal?
# # Units for frequencies?
# # All benchmarks use same fields (initialization time, allocation time, etc???)

# df = pd.DataFrame({"CPU Frequencies":          pd.Series(dtype = "int"),
#                    "GPU Frequencies":          pd.Series(dtype = "int"),
#                    "Mem Frequencies":          pd.Series(dtype = "int"),
#                    "Initialization Time":      pd.Series(dtype = "float"),
#                    "Allocation Time":          pd.Series(dtype = "float"),
#                    "Copy To Device Time":      pd.Series(dtype = "float"),
#                    "Kernel Time":              pd.Series(dtype = "float"),
#                    "Copy Back and Merge Time": pd.Series(dtype = "float"),
#                    "Deallocation Time":        pd.Series(dtype = "float"),
#                    "Real Time":                pd.Series(dtype = "float"),
#                    "User Time":                pd.Series(dtype = "float"),
#                    "System Time":              pd.Series(dtype = "float")})

# chai_benchmark_times = re.findall(": [0-9]+.[0-9]+", output)
# chai_benchmark_times = [float(time[2:]) for time in chai_benchmark_times]
# # print(chai_benchmark_times)

# time_command_times = re.findall("[0-9]+m[0-9]+.[0-9]+s", output)
# # List of tuples of minutes and seconds for real, user, and sys from the "time" command
# time_command_times = [time.split("m") for time in time_command_times]
# # List of real, user, and sys times (in milliseconds) from the "time" command
# time_command_times = [(1000 * ((float(minutes_seconds[0]) * 60) + float(minutes_seconds[1][:(len(minutes_seconds[1]) - 1)]))) for minutes_seconds in time_command_times]
# # print(time_command_times)

# df.loc[len(df)] = [200000, 177000000, 165000000] + chai_benchmark_times + time_command_times

# df.to_csv("results.csv")

# # If I try to call the benchmark from a different directory, I get:
# # root@odroid:/home/odroid/Desktop# time run 1 taskset -c 0 /home/odroid/benchmark/chai/OpenCL-D/SSSP/sssp
# # Mali-T628	Unable to open ./kernel.cl. Exiting...
# benchmark_to_run = "bfs"

# original_directory = os.getcwd()

# directory_of_benchmark = "/home/odroid/benchmark/chai/OpenCL-D/" + benchmark_to_run.upper()
# command = "time run 1 taskset -c 0 ./" + benchmark_to_run.lower()
# print(directory_of_benchmark)
# print(command)

# print(os.listdir())
# os.chdir("..") # os.chdir("/home/jbao8899/Desktop/Testing") # Single / works
# print(os.listdir())
# os.chdir(original_directory)
# print(os.listdir())


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
