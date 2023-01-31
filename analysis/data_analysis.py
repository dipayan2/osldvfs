import csv
import pandas as pd
import matplotlib.pyplot as plt
import os
import shutil

CPU_FREQ_COL = "CPU Frequencies"
GPU_FREQ_COL = "GPU Frequencies"
MEM_FREQ_COL = "Mem Frequencies"
INIT_TIME_COL = "Initialization Time"
ALLOC_TIME_COL = "Allocation Time"
CP_HTD_COL = "Copy To Device Time"
KERNEL_TIME_COL = "Kernel Time"
CP_DTH_COL = "Copy Back and Merge Time"
DALLOC_TIME_COL = "Deallocation Time"
REAL_TIME_COL = "Real Time"
USR_TIME_COL = "User Time"
SYS_TIME_COL = "System Time"
TOT_DATA_TRANSFER_LATENCY_COL = "Total Data Transfer Latency"
TOT_LATENCY_COL = "Total Latency"
TRANS_PERCENT_COL = "Transfer Percentage"
KERNEL_STD_COL = "Kernel STD"
TRANSFER_STD_COL = "Transfer STD"
KERNEL_SCORE_COL = "Kernel Score"
TRANSFER_SCORE_COL = "Transfer Score"
TOT_SCORE = "Total Score"

cpu_freq_list = [200000,300000,400000,500000,600000,700000,800000,900000,1000000,1100000,1200000,1300000,1400000]
gpu_freq_list = [177000000,266000000,350000000,420000000,480000000,543000000,600000000]
mem_freq_list = [165000000,206000000,275000000,413000000,543000000,633000000,728000000,825000000]

cpu_freq_display_list = [200,300,400,500,600,700,800,900,1000,1100,1200,1300,1400]
gpu_freq_display_list = [177,266,350,420,480,543,600]
mem_freq_display_list = [165,206,275,413,543,633,728,825]

results_directory = "results/"
directories_names = ['fixedcpu_allgpu_mem', 
                     'fixedcpu_allmem_gpu', 
                     'fixedgpu_allcpu_mem', 
                     'fixedgpu_allmem_cpu',
                     'fixedmem_allcpu_gpu',
                     'fixedmem_allgpu_cpu']

print("Loading Data File....")
data = pd.read_csv("2_trials_sssp_results.csv")
data = data[::2]
data_cols = data.columns.tolist()

print("Processing Data File....")
data_cols.append('Total Data Transfer Latency')
data_cols.append("Total Latency")
data_cols.append("Transfer Percentage")
data_cols.append("Kernel STD")
data_cols.append("Transfer STD")
data_cols.append("Kernel Score")
data_cols.append("Transfer Score")
data_cols.append("Total Score")

data[TOT_DATA_TRANSFER_LATENCY_COL] = data[CP_HTD_COL] + data[CP_DTH_COL]
data[TOT_LATENCY_COL] = data[TOT_DATA_TRANSFER_LATENCY_COL] + data[KERNEL_TIME_COL]
data[TRANS_PERCENT_COL] = round((data[TOT_DATA_TRANSFER_LATENCY_COL] / data[TOT_LATENCY_COL]) * 100, 2)

avg_kernel = data[KERNEL_TIME_COL].mean()
avg_tot_data_transfer_latency = data[TOT_DATA_TRANSFER_LATENCY_COL].mean()

std_kernel = data[KERNEL_TIME_COL].std()
std_tot_data_transfer_latency = data[TOT_DATA_TRANSFER_LATENCY_COL].std()

data[KERNEL_STD_COL] = (data[KERNEL_TIME_COL] - avg_kernel) / std_kernel
data[TRANSFER_STD_COL] = (data[TOT_DATA_TRANSFER_LATENCY_COL] - avg_tot_data_transfer_latency) / std_tot_data_transfer_latency

kernel_std_min = data[KERNEL_STD_COL].min()
transfer_std_min = data[TRANSFER_STD_COL].min()

data[KERNEL_SCORE_COL] = round(std_kernel*(1/(data[KERNEL_STD_COL]+2*abs(kernel_std_min)))+avg_kernel, 3)
data[TRANSFER_SCORE_COL] = round(std_tot_data_transfer_latency*(1/(data[TRANSFER_STD_COL]+2*abs(transfer_std_min)))+avg_tot_data_transfer_latency, 3)
data[TOT_SCORE] = data[KERNEL_SCORE_COL] + data[TRANSFER_SCORE_COL]

print("Data processing Done.")

print("Generting Necessary Data Directories....")

def generate_result_directories():
    try:
        shutil.rmtree(results_directory)
    except:
        print("Results/ Directory Does not Already Exist. Creating Such Directory...")

    os.mkdir(results_directory)
    for directory in directories_names:
        os.mkdir(results_directory+directory)
    print("Results Directories Generated.")
        
generate_result_directories()

print("Generating Graphs....")
def get_fixedcpu_allgpu_mem():
    # all data points @ Fixed CPU settings analyzing different GPU settings across all MEM settings
    for i, cpu_freq in enumerate(cpu_freq_list):
        for j, gpu_freq in enumerate(gpu_freq_list):
            data_mean = round(data.loc[(data[CPU_FREQ_COL] == cpu_freq) & (data[GPU_FREQ_COL] == gpu_freq)][TRANS_PERCENT_COL].mean(), 1)
            data_min = round(data.loc[(data[CPU_FREQ_COL] == cpu_freq) & (data[GPU_FREQ_COL] == gpu_freq)][TRANS_PERCENT_COL].min(), 1)
            data_max = round(data.loc[(data[CPU_FREQ_COL] == cpu_freq) & (data[GPU_FREQ_COL] == gpu_freq)][TRANS_PERCENT_COL].max(), 1)
            plt.plot(range(len(mem_freq_list)), data.loc[(data[CPU_FREQ_COL] == cpu_freq) & (data[GPU_FREQ_COL] == gpu_freq)][TOT_SCORE], label="@ {}MHz GPU, {}, {}, {}".format(gpu_freq_display_list[j], data_mean, data_min, data_max))
        plt.xticks(range(len(mem_freq_list)), mem_freq_display_list)
        plt.title("Overall Scores @ {}MHz CPU".format(cpu_freq_display_list[i]))
        plt.xlabel("Memory Frequency")
        plt.ylabel("Overall Score")
        plt.legend()
        plt.savefig('{}/{}_{}.png'.format(results_directory + directories_names[0], cpu_freq_display_list[i], directories_names[0]))
        plt.close()
    print("Generated {} Graphs".format(directories_names[0]))

def get_fixedcpu_allem_gpu():
    # all data points @ Fixed CPU settings analyzing different MEM settings across all GPU settings
    # print(data.loc[(data[CPU_FREQ_COL] == cpu_freq_list[0]) & (data[MEM_FREQ_COL] == mem_freq_list[0])][TOT_SCORE])
    for i, cpu_freq in enumerate(cpu_freq_list):
        for j, mem_freq in enumerate(mem_freq_list):
            plt.plot(range(len(gpu_freq_list)), data.loc[(data[CPU_FREQ_COL] == cpu_freq) & (data[MEM_FREQ_COL] == mem_freq)][TOT_SCORE][::-1], label="@ {}MHz MEM".format(mem_freq_display_list[j]))
        plt.xticks(range(len(gpu_freq_list)), gpu_freq_display_list)
        plt.title("Overall Scores @ {}MHz CPU".format(cpu_freq_display_list[i]))
        plt.xlabel("GPU Frequency")
        plt.ylabel("Overall Score")
        plt.legend()
        plt.savefig('{}/{}.png'.format(results_directory + directories_names[1], str(cpu_freq_display_list[i]) + directories_names[1]))
        plt.close()
    print("Generated {} Graphs".format(directories_names[1]))

def get_fixedgpu_allcpu_mem():
    # all data points @ Fixed GPU settings analyzing different CPU settings across all MEM settings
    # print(data.loc[(data[[GPU_FREQ_COL]] == gpu_freq_list[0]) & (data[[CPU_FREQ_COL]] == cpu_freq_list[0])])
    for i, gpu_freq in enumerate(gpu_freq_list):
        for j, cpu_freq in enumerate(cpu_freq_list):
            plt.plot(range(len(mem_freq_list)), data.loc[(data[GPU_FREQ_COL] == gpu_freq) & (data[CPU_FREQ_COL] == cpu_freq)][TOT_SCORE], label="@ {}MHz CPU".format(cpu_freq_display_list[j]))
        plt.xticks(range(len(mem_freq_list)), mem_freq_display_list)
        plt.title("Overall Scores @ {}MHz GPU".format(gpu_freq_display_list[i]))
        plt.xlabel("Memory Frequency")
        plt.ylabel("Overall Score")
        plt.legend()
        plt.savefig('{}/{}.png'.format(results_directory + directories_names[2], str(gpu_freq_display_list[i]) + directories_names[2]))
        plt.close()
    print("Generated {} Graphs".format(directories_names[2]))

def get_fixedgpu_allmem_cpu():
    # all data points @ Fixed GPU settings analyzing different CPU settings across all MEM settings
    # print(data.loc[(data[[GPU_FREQ_COL]] == gpu_freq_list[0]) & (data[[CPU_FREQ_COL]] == cpu_freq_list[0])])
    for i, gpu_freq in enumerate(gpu_freq_list):
        for j, mem_freq in enumerate(mem_freq_list):
            plt.plot(range(len(cpu_freq_list)), data.loc[(data[GPU_FREQ_COL] == gpu_freq) & (data[MEM_FREQ_COL] == mem_freq)][TOT_SCORE], label="@ {}MHz MEM".format(mem_freq_display_list[j]))
        plt.xticks(range(len(cpu_freq_list)), cpu_freq_display_list)
        plt.title("Overall Scores @ {}MHz GPU".format(gpu_freq_display_list[i]))
        plt.xlabel("CPU Frequency")
        plt.ylabel("Overall Score")
        plt.legend()
        plt.savefig('{}/{}.png'.format(results_directory + directories_names[3], str(gpu_freq_display_list[i]) + directories_names[3]))
        plt.close()
    print("Generated {} Graphs".format(directories_names[3]))

def get_fixedmem_allcpu_gpu():
    # all data points @ Fixed GPU settings analyzing different CPU settings across all MEM settings
    # print(data.loc[(data[[GPU_FREQ_COL]] == gpu_freq_list[0]) & (data[[CPU_FREQ_COL]] == cpu_freq_list[0])])
    for i, mem_freq in enumerate(mem_freq_list):
        for j, cpu_freq in enumerate(cpu_freq_list):
            plt.plot(range(len(gpu_freq_list)), data.loc[(data[MEM_FREQ_COL] == mem_freq) & (data[CPU_FREQ_COL] == cpu_freq)][TOT_SCORE][::-1], label="@ {}MHz CPU".format(cpu_freq_display_list[j]))
        plt.xticks(range(len(gpu_freq_list)), gpu_freq_display_list)
        plt.title("Overall Scores @ {}MHz MEM".format(mem_freq_display_list[i]))
        plt.xlabel("GPU Frequency")
        plt.ylabel("Overall Score")
        plt.legend()
        plt.savefig('{}/{}.png'.format(results_directory + directories_names[4], str(mem_freq_display_list[i]) + directories_names[4]))
        plt.close()
    print("Generated {} Graphs".format(directories_names[4]))

def get_fixedmem_allgpu_cpu():
    # all data points @ Fixed GPU settings analyzing different CPU settings across all MEM settings
    # print(data.loc[(data[[GPU_FREQ_COL]] == gpu_freq_list[0]) & (data[[CPU_FREQ_COL]] == cpu_freq_list[0])])
    for i, mem_freq in enumerate(mem_freq_list):
        for j, gpu_freq in enumerate(gpu_freq_list):
            plt.plot(range(len(cpu_freq_list)), data.loc[(data[MEM_FREQ_COL] == mem_freq) & (data[GPU_FREQ_COL] == gpu_freq)][TOT_SCORE], label="@ {}MHz GPU".format(gpu_freq_display_list[j]))
        plt.xticks(range(len(cpu_freq_list)), cpu_freq_display_list)
        plt.title("Overall Scores @ {}MHz MEM".format(mem_freq_display_list[i]))
        plt.xlabel("CPU Frequency")
        plt.ylabel("Overall Score")
        plt.legend()
        plt.savefig('{}/{}.png'.format(results_directory + directories_names[5], str(mem_freq_display_list[i]) + directories_names[5]))
        plt.close()
    print("Generated {} Graphs".format(directories_names[5]))


get_fixedcpu_allgpu_mem()
get_fixedcpu_allem_gpu()
get_fixedgpu_allcpu_mem()
get_fixedgpu_allmem_cpu()
get_fixedmem_allcpu_gpu()
get_fixedmem_allgpu_cpu()

print("Graph Generation Done.")