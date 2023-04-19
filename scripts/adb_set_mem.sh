#!/bin/sh
adb shell "cd /sys/class/devfreq/exynos5-devfreq-mif && echo $1 > max_freq && echo $1 > min_freq "
if [ "$2" -eq "1" ]
then 
    # echo "Increase"
    adb shell "cd /sys/class/devfreq/exynos5-devfreq-mif && echo $1 > max_freq && echo $1 > min_freq "
else
    # echo "Decrease"
    adb shell "cd /sys/class/devfreq/exynos5-devfreq-mif && echo $1 > min_freq && echo $1 > max_freq "
fi
