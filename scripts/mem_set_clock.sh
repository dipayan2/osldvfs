#!/bin/sh
sudo echo $1 > /sys/class/devfreq/10c20000.memory-controller/max_freq
sudo echo $1 > /sys/class/devfreq/10c20000.memory-controller/min_freq