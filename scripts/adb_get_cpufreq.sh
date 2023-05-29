#!/bin/sh
adb shell cat /sys/devices/system/cpu/cpu$1/cpufreq/scaling_cur_freq
