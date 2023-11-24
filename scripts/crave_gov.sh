#!/bin/bash

def_mem() {
    echo "Here I am"
    # local mem_max=825000000
    # sudo echo $mem_max > /sys/class/devfreq/10c20000.memory-controller/max_freq
    # local mem_min=165000000
    # sudo echo $mem_min > /sys/class/devfreq/10c20000.memory-controller/min_freq
}

def_cpu0() {
    local cpu_max=1400000
    sudo echo $cpu_max > /sys/devices/system/cpu/cpu0/cpufreq/scaling_max_freq
    local cpu_min=200000
    sudo echo $cpu_min > /sys/devices/system/cpu/cpu0/cpufreq/scaling_min_freq
}

def_gpu() {
    local gpu_max=600000000
    sudo echo $gpu_max > /sys/class/devfreq/11800000.gpu/max_freq
    local gpu_min=177000000
    sudo echo $gpu_min > /sys/class/devfreq/11800000.gpu/min_freq
}



declare -A MFreqConf
MFreqConf[165000000]="200000,177000000"
MFreqConf[206000000]="400000,177000000"
MFreqConf[275000000]="600000,266000000"
MFreqConf[413000000]="800000,350000000"
MFreqConf[543000000]="1000000,420000000"
MFreqConf[633000000]="1100000,480000000"
MFreqConf[728000000]="1200000,543000000"
MFreqConf[825000000]="1400000,600000000"

key1=$(./mem_get_clock.sh)
printf "$key1\n"
value1="${MFreqConf["$key1"]}"
IFS=',' read -r value1_1 value1_2 <<< "$value1"
echo "Value for $key1: ($value1_1, $value1_2)"
def_mem

cpufreqs=$(./cpu_get_clock.sh 0)
printf "$cpufreqs\n"
def_cpu0
cpufreqs=$(./cpu_get_clock.sh 0)
printf "$cpufreqs\n"

