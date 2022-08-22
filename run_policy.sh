#!/bin/sh
chmod u+x scripts/*.sh
sudo taskset -c 7 python3 profile_dvfs.py
# python3 profile_dvfs.py