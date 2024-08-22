#!/bin/sh
sudo echo 1 > /sys/kernel/debug/bpmp/debug/clk/emc/mrq_rate_locked
sudo echo 1 > /sys/kernel/debug/bpmp/debug/clk/emc/state
sudo echo $1 > /sys/kernel/debug/bpmp/debug/clk/emc/rate

