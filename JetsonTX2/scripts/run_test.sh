#!/bin/bash
source ~/.bashrc
# We used this to run a bunch of benchmarks and collect data. We will start with chai and rodinia and move to others
python3 run_analysis.py /home/dipayan2/Desktop/Efficient_DVFS/chai/CUDA-D/SSSP sssp D0 20
python3 run_analysis.py /home/dipayan2/Desktop/Efficient_DVFS/chai/CUDA-D/SSSP sssp D1 5
python3 run_analysis.py /home/dipayan2/Desktop/Efficient_DVFS/chai/CUDA-D/SSSP sssp D2 10
