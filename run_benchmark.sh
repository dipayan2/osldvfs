#!/bin/sh

# This code works with the mac zsh system
# for ((i=1; i<=$2;i++))
# do 
#     $1
# done

# This code works with the odroid system
# Usage ./run_benchmark.sh command #repitition
for i in $(seq "$2")
do
    $1
done