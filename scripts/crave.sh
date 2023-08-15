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

declare -A matrix
num_rows=4
num_columns=5

for ((i=1;i<=num_rows;i++)) do
    for ((j=1;j<=num_columns;j++)) do
        matrix[$i,$j]=$RANDOM
    done
done

f1="%$((${#num_rows}+1))s"
f2=" %9s"

printf "$f1" ''
for ((i=1;i<=num_rows;i++)) do
    printf "$f2" $i
done
echo

for ((j=1;j<=num_columns;j++)) do
    printf "$f1" $j
    for ((i=1;i<=num_rows;i++)) do
        printf "$f2" ${matrix[$i,$j]}
    done
    echo
done

freq=$(./cpu_get_clock.sh 0)
printf "$freq\n"