#!/bin/sh
# cpu_id = "$1"
# cpu_clock = "$2"
sudo echo $2 > /sys/devices/system/cpu/cpu$cpu_id/cpufreq/scaling_max_freq
sudo echo $2 > /sys/devices/system/cpu/cpu$cpu_id/cpufreq/scaling_min_freq
