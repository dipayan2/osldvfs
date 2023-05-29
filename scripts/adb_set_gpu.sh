#!/bin/sh
# adb shell "cd /sys/devices/11800000.mali && echo 1 > dvfs && echo $1 > dvfs_min_lock && echo $1 > dvfs_max_lock && echo 0 > dvfs"
if [ "$2" -eq "1" ]
then 
    # echo "Increase"
    adb shell "cd /sys/devices/11800000.mali && echo 1 > dvfs && echo $1 > dvfs_max_lock && echo $1 > dvfs_min_lock && echo 0 > dvfs"
else
    # echo "Decrease"
    adb shell "cd /sys/devices/11800000.mali && echo 1 > dvfs && echo $1 > dvfs_min_lock && echo $1 > dvfs_max_lock && echo 0 > dvfs"
fi
