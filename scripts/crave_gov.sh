#!/bin/bash
declare -A FreqConf
FreqConf[165000000]="200000,177000000"
FreqConf[206000000]="400000,177000000"
FreqConf[275000000]="600000,266000000"
FreqConf[413000000]="800000,350000000"
FreqConf[543000000]="1000000,420000000"
FreqConf[633000000]="1100000,480000000"
FreqConf[728000000]="1200000,543000000"
FreqConf[825000000]="1400000,600000000"

key1=$(./mem_get_clock.sh)
printf "$key1\n"
value1="${FreqConf["$key1"]}"
IFS=',' read -r value1_1 value1_2 <<< "$value1"
echo "Value for $key1: ($value1_1, $value1_2)"
