#!/bin/bash
#Note: always run in sudo 
# GPU setting done
cd /sys/class/devfreq/11800000.gpu/device; 
echo devfreq > core_availability_policy;
echo always_on > power_policy;
echo $1 > dvfs_period;
cd /sys/class/devfreq/11800000.gpu;
echo $1 > polling_interval;
#Memory setting
cd /sys/class/devfreq/10c20000.memory-controller;
echo $1 > polling_interval;
#CPU Setting
n=$1
cpu_poll=$((n*1000))
#echo $cpu_poll
cd /sys/devices/system/cpu/cpufreq/policy0;
echo ondemand > scaling_governor;
cd /sys/devices/system/cpu/cpufreq/policy4;
echo ondemand > scaling_governor;
cd /sys/devices/system/cpu/cpufreq/ondemand;
echo $cpu_poll > sampling_rate;
