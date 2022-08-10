#!/bin/sh
sudo echo $1 > /sys/class/devfreq/11800000.gpu/max_freq
sudo echo $1 > /sys/class/devfreq/11800000.gpu/min_freq