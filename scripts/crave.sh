#!/bin/bash
# get the cluster for in for of data
declare -A cpu2gpu
cpu2gpu[1]=5
cpu2gpu[2]=10
cpu2gpu[3]=15

for key in "${!cpu2gpu[@]}"; do
  printf "%s: %s\n" "$key" "${cpu2gpu[$key]}"
done

# 2D matrix

declare -A RIM=()
RIM[0,0]=0.92
RIM[0,1]=0.63
RIM[0,2]=0.77
RIM[1,0]=0.15
RIM[1,1]=0.74
RIM[1,2]=0.07
RIM[2,0]=-0.13
RIM[2,1]=0.04
RIM[2,2]=0.54
num_rows=3
num_columns=3

# for ((i=1;i<=num_rows;i++)) do
#     for ((j=1;j<=num_columns;j++)) do
#         matrix[$i,$j]=$RANDOM
#     done
# done

f1="%$((${#num_rows}+1))s"
f2=" %9s"

printf "$f1" ''
for ((i=1;i<=num_rows;i++)) do
    printf "$f2" $i
done
echo

for ((j=0;j<num_columns;j++)) do
    printf "$f1" $j
    for ((i=0;i<num_rows;i++)) do
        printf "$f2" ${RIM[$i,$j]}
    done
    echo
done

# Getting the util and the frequency data from the system

cpufreqs=$(./cpu_get_clock.sh 0)
cpufreqb=$(./cpu_get_clock.sh 4)
memfreq=$(./mem_get_clock.sh)
gpufreq=$(./gpu_get_clock.sh)
printf "$memfreq\n"
printf "$cpufreqs\n"
printf "$cpufreqb\n"
printf "$gpufreq\n"

cpuutils=$(./cpu_get_util.sh 0)
cpuutilb=$(./cpu_get_util.sh 4)
memutil=$(./mem_get_util.sh)
gpuutil=$(./gpu_get_util.sh)
printf "$memutil\n"
printf "$cpuutils\n"
printf "$cpuutilb\n"
printf "$gpuutil\n"




# Idea 1. get all util and freq 2. Get normalized util 3. find dom res 4. set the freq of all