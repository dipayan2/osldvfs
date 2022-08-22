#!/bin/sh

if [ "$2" -eq "1" ]
then
    sudo echo $1 > /sys/class/devfreq/11800000.gpu/max_freq
    sudo echo $1 > /sys/class/devfreq/11800000.gpu/min_freq
else
    sudo echo $1 > /sys/class/devfreq/11800000.gpu/min_freq
    sudo echo $1 > /sys/class/devfreq/11800000.gpu/max_freq
fi
