#!/bin/sh
date +%s.%N
echo "sCPU"
cat /sys/devices/system/cpu/cpufreq/policy0/util && cat /sys/devices/system/cpu/cpufreq/policy0/scaling_cur_freq
echo "bCPU"
cat /sys/devices/system/cpu/cpufreq/policy4/util && cat /sys/devices/system/cpu/cpufreq/policy4/scaling_cur_freq
echo "Mem"
cat /sys/class/devfreq/10c20000.memory-controller/utilization && cat /sys/class/devfreq/10c20000.memory-controller/cur_freq
echo "GPU"
cat /sys/class/devfreq/11800000.gpu/utilization && cat /sys/class/devfreq/11800000.gpu/cur_freq
