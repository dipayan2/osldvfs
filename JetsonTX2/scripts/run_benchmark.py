import os
import pandas as pd
import re
import subprocess
import sys
import time

import cpuclock
import gpuclock
import memclock


def get_benchmark_information(benchmark_to_run = "sssp",trials_per_combination = 1, file_id=1):
    # Create a file name for combined time data 
    output_file_name = benchmark_to_run.lower()+"_trails_"+str(trials_per_combination) + "_results.csv"
    cpu_frequencies = [345600,499200,652800,806400,960000,1113600,1267200,1420800]
    gpu_frequencies = [114750000,216750000,318750000,420750000,522750000,624750000,726750000,854250000,930750000,1032750000,1122000000,1236750000,1300500000]
    mem_frequencies = [40800000,68000000,102000000,204000000,408000000,665600000,800000000,1062400000,1331200000,1600000000,1866000000]
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
                       "System Time":              pd.Series(dtype = "float"),
                       "Starttime":                pd.Series(dtype="int"),
                       "Endtime":                pd.Series(dtype="int"),})

    original_directory = os.getcwd()
    directory_for_clock_functions = os.getcwd()
    directory_of_benchmark = "/home/dipayan2/Desktop/Efficient_DVFS/chai/CUDA-D/" + benchmark_to_run.upper()
    command_for_test = "time taskset -c 3-5 ./" + benchmark_to_run.lower()
        # Create instances of the taskset -c 7classes for controlling clock frequencies
    os.chdir(directory_for_clock_functions)
    cpu_clock = cpuclock.CPUClock()
    cpu_clock.get_clock()
    gpu_clock = gpuclock.GPUClock()
    gpu_clock.get_clock()
    mem_clock = memclock.MemClock()
    mem_clock.get_clock()
    init_milisecond = round(time.time()*1000)
    for cpu_freq in cpu_frequencies:
        for gpu_freq in gpu_frequencies:
            for mem_freq in mem_frequencies:
                # Set the frequencies
                os.chdir(directory_for_clock_functions)
                cpu_clock.set_clock(cpu_freq)
                gpu_clock.set_clock(gpu_freq)
                mem_clock.set_clock(mem_freq)
                tegraLogName = "/home/dipayan2/Desktop/Efficient_DVFS/TegraData/"+"Tegra_"+benchmark_to_run.upper()+"_C_"+str(cpu_freq)+"_G_"+str(gpu_freq)+"_M_"+str(mem_freq)

                for i in range(trials_per_combination):
                    os.chdir(directory_of_benchmark)
                    start_time = round(time.time()*1000)-init_milisecond
                    tegracmd = "sudo -b tegrastats --interval 100 --logfile "+str(tegraLogName)
                    tegraStop = "sudo -b tegrastats --stop"
                    subprocess.check_call(tegracmd, shell=True) # tegra start
                    output = subprocess.check_output(command_for_test,
                                    shell = True, 
                                    executable="/bin/bash",
                                    stderr = subprocess.STDOUT).decode('ascii')  
                    subprocess.check_call(tegraStop, shell=True)
                    end_time = round(time.time()*1000) - init_milisecond
                    chai_benchmark_times = re.findall(": [0-9]+.[0-9]+", output)
                    chai_benchmark_times = [float(time[2:]) for time in chai_benchmark_times]
                    time_command_times = re.findall("[0-9]+m[0-9]+.[0-9]+s", output)
                    # List of tuples of minutes and seconds for real, user, and sys from the "time" command
                    time_command_times = [time.split("m") for time in time_command_times]
                    # List of real, user, and sys times (in milliseconds) from the "time" command
                    time_command_times = [(1000 * ((float(minutes_seconds[0]) * 60) + float(minutes_seconds[1][:(len(minutes_seconds[1]) - 1)]))) for minutes_seconds in time_command_times]

                    # Store all the times, as well as the frequencies used for all components
                    df.loc[len(df)] = [cpu_freq, gpu_freq, mem_freq] + chai_benchmark_times + time_command_times + [start_time, end_time]
    # Go back to the original directory
    os.chdir(original_directory)       

    # Store the results in the file "output_file_name".
    # If it exists, overwrite it. If not, create it 
    df.to_csv(output_file_name)

get_benchmark_information('sssp',1,1)












