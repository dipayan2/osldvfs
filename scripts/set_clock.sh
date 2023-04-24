#!/bin/sh

device_id = $1
mem_clock = $2
gpx_clock = $3

sudo nvidia-smi -i $device_id -pm 1
sudo nvidia-smi -i $device_id -ac  $mem_clock,$gpx_clock