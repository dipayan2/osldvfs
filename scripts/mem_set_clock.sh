#!/bin/sh

if [ "$2" -eq "1" ]
then
    echo "Increase"
    sudo echo $1 > /sys/class/devfreq/10c20000.memory-controller/max_freq
    sudo echo $1 > /sys/class/devfreq/10c20000.memory-controller/min_freq
else
    echo "Decrease"
    sudo echo $1 > /sys/class/devfreq/10c20000.memory-controller/min_freq
    sudo echo $1 > /sys/class/devfreq/10c20000.memory-controller/max_freq
fi
