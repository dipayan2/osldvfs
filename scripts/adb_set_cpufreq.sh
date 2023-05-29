#!/bin/sh
if [ "$3" -eq "1" ]
then 
    echo "Increase"
    adb shell "cd /sys/devices/system/cpu/cpu$1/cpufreq && echo $2 > scaling_max_freq && echo $2 > scaling_min_freq"
else
    echo "Decrease"
    adb shell "cd /sys/devices/system/cpu/cpu$1/cpufreq && echo $2 > scaling_min_freq && echo $2 > scaling_max_freq"
fi



