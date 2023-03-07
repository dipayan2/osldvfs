#!/bin/bash
cpuId="$1"
#echo "$cpuId"
secVar='/Cpu'$cpuId'/ {print $8,$9}'
#echo "$secVar"
cpuIdle=$(top -bn1 -1 | awk "$secVar" | awk -F"[ ,]+" '{print $2}')
echo "$cpuIdle"
