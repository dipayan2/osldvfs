#!/bin/bash
source ~/.bashrc
MDR=$(pwd)
sudo -b taskset -c 0 /home/dipayan2/Desktop/Efficient_DVFS/goVcode/run_crave >/dev/null
PID=$(ps aux | grep 'goVcode/run_crave' | head -1 | awk '{print $2}')
echo "Did I get the PID"
echo $PID
sleep 10
echo "Killing It"
sudo kill -INT $PID
echo "Killed It"
cd $MDR
