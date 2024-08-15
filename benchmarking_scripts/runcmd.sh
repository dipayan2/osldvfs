#!/bin/sh
#sudo ./runcmd.sh SPD9 "cd benchmark/chai/OpenCL-D/SSSP/; ./sssp"
watch -n 0.5  "sudo ./get_data.sh >> $1" >/dev/null 2>/dev/null &
pids=$!
echo $pids
eval "$2"
sudo kill -9 $pids
