#!/bin/sh
if [ "$2" -eq "1" ]
then
    sudo echo $1 > /sys/devices/17000000.gp10b/devfreq/17000000.gp10b/max_freq
    sudo echo $1 > /sys/devices/17000000.gp10b/devfreq/17000000.gp10b/min_freq
else
    sudo echo $1 > /sys/devices/17000000.gp10b/devfreq/17000000.gp10b/min_freq
    sudo echo $1 > /sys/devices/17000000.gp10b/devfreq/17000000.gp10b/max_freq
fi