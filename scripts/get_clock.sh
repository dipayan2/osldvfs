#!/bin/sh
device_id = $1
sudo nvidia-smi -i $device_id -q -d CLOCK