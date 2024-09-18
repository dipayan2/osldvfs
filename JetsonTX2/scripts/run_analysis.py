import os
import pandas as pd
import re
import subprocess
import sys
import time


print(sys.argv) #Testing benchmarks to run order [directory, excutable name, benchmark name ,iteration ID, loop_count]
def runAnalysis(benchmark_dir, benchmark_run,benchmark_name,itr_id = 'D0',loop_count=20):
    # Create a file name for combined time data 
    output_file_name = str(benchmark_name).upper()
    df = pd.DataFrame({"BenchmarkName":            pd.Series(dtype = "str"),
                       "IterationID":              pd.Series(dtype="str"),
                       "Loop Count":               pd.Series(dtype="int"),
                       "Real Time":                pd.Series(dtype = "float"),
                       "User Time":                pd.Series(dtype = "float"),
                       "System Time":              pd.Series(dtype = "float"),})

    original_directory = os.getcwd()
    # directory_of_benchmark = "/home/dipayan2/Desktop/Efficient_DVFS/chai/CUDA-D/" + benchmark_to_run.upper()
    command_for_test = "source ~/.bashrc && time runosl "+str(loop_count)+" taskset -c 3 ./" + benchmark_run.lower()
        # Create instances of the taskset -c 7classes for controlling clock frequencies
    init_milisecond = round(time.time()*1000)
    tegraLogName = "/home/dipayan2/Desktop/Efficient_DVFS/TegraDataAnalysis/"+"Tegra_"+str(benchmark_name).upper()+"_Itr_"+str(itr_id)+"_L_"+str(loop_count)
    os.chdir(benchmark_dir)
    start_time = round(time.time()*1000)-init_milisecond
    tegracmd = "sudo -b tegrastats --interval 100 --logfile "+str(tegraLogName)
    tegraStop = "sudo -b tegrastats --stop"
    subprocess.check_call(tegracmd, shell=True) # tegra start
    # output = subprocess.check_output(command_for_test,
    #                 shell = True, 
    #                 executable="/bin/bash",
    #                 stderr = subprocess.STDOUT).decode('ascii')  
    output = subprocess.check_output(['bash', '-c', command_for_test], stderr=subprocess.STDOUT).decode('ascii')

    subprocess.check_call(tegraStop, shell=True)
    end_time = round(time.time()*1000) - init_milisecond
    # chai_benchmark_times = re.findall(": [0-9]+.[0-9]+", output)
    # chai_benchmark_times = [float(time[2:]) for time in chai_benchmark_times]
    time_command_times = re.findall("[0-9]+m[0-9]+.[0-9]+s", output)
    # List of tuples of minutes and seconds for real, user, and sys from the "time" command
    time_command_times = [time.split("m") for time in time_command_times]
    # List of real, user, and sys times (in milliseconds) from the "time" command
    time_command_times = [(1000 * ((float(minutes_seconds[0]) * 60) + float(minutes_seconds[1][:(len(minutes_seconds[1]) - 1)]))) for minutes_seconds in time_command_times]

    # Store all the times, as well as the frequencies used for all components
    df.loc[len(df)] = [benchmark_name.upper(),str(itr_id),int(loop_count) ] + time_command_times 
    # Go back to the original directory
    os.chdir(original_directory)       

    # Store the results in the file "output_file_name".
    # If it exists, overwrite it. If not, create it 
    if not os.path.isfile(output_file_name):
        df.to_csv(output_file_name)
    else:
        df.to_csv(output_file_name,mode='a',header=False)

runAnalysis(sys.argv[1],sys.argv[2],sys.argv[3],int(sys.argv[4]),int(sys.argv[5]))












