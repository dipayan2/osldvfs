#!/bin/bash
# ./runcmd.sh <interval in sec> <filename> <repeat> <cmd in string>
watch -n $1  "sudo ./get_data.sh >> $2" >/dev/null 2>/dev/null &
pids=$!
echo $pids
n=$3
for ((i=1; i<=n; i++))
do
	eval "$4"
	sleep 0.5
done
sudo kill -9 $pids
