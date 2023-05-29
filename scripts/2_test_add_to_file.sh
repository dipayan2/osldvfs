#!/bin/sh
# cpu_id = "$1"
# cpu_clock = "$2"

if [ "$3" -eq "1" ]
then 
    echo "Increase"
    sudo echo $2 > /home/jbao8899/Desktop/osldvfs/scripts/2_EXAMPLE_FILE_TO_ADD_TO_$1.txt
else
    echo "Decrease"
    sudo echo $2 > /home/jbao8899/Desktop/osldvfs/scripts/2_EXAMPLE_FILE_TO_ADD_TO_$1.txt
fi

