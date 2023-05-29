#!/bin/sh
adb shell "cd /sys/devices/11800000.mali && echo $1 > dvfs_governor"
