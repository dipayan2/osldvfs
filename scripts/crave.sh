#!/bin/sh
declare -A my_dict
my_dict[1]=5
my_dict[2]=10
my_dict[2]=15

for key in "${!my_dict[@]}"; do
  printf "%s: %s\n" "$key" "${my_dict[$key]}"
done