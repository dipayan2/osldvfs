#!/bin/bash
source ~/.bashrc
sudo date
# We used this to run a bunch of benchmarks and collect data. We will start with chai and rodinia and move to others
# This is running the code with the default governor
python3 run_analysis.py /home/dipayan2/Desktop/Efficient_DVFS/gpu-rodinia/cuda/nw run NW D0 20
python3 run_analysis.py /home/dipayan2/Desktop/Efficient_DVFS/gpu-rodinia/cuda/nw run NW D1 10
python3 run_analysis.py /home/dipayan2/Desktop/Efficient_DVFS/gpu-rodinia/cuda/nw run NW D2 5
python3 run_analysis.py /home/dipayan2/Desktop/Efficient_DVFS/gpu-rodinia/cuda/nw run NW D3 5

echo "NW Done"

python3 run_analysis.py /home/dipayan2/Desktop/Efficient_DVFS/gpu-rodinia/cuda/streamcluster run STCLUST D0 15
python3 run_analysis.py /home/dipayan2/Desktop/Efficient_DVFS/gpu-rodinia/cuda/streamcluster run STCLUST D1 10
python3 run_analysis.py /home/dipayan2/Desktop/Efficient_DVFS/gpu-rodinia/cuda/streamcluster run STCLUST D2 5
python3 run_analysis.py /home/dipayan2/Desktop/Efficient_DVFS/gpu-rodinia/cuda/streamcluster run STCLUST D3 2

echo "SCLUST Done"

python3 run_analysis.py /home/dipayan2/Desktop/Efficient_DVFS/gpu-rodinia/cuda/pathfinder run PFIND D0 10
python3 run_analysis.py /home/dipayan2/Desktop/Efficient_DVFS/gpu-rodinia/cuda/pathfinder run PFIND D1 5
python3 run_analysis.py /home/dipayan2/Desktop/Efficient_DVFS/gpu-rodinia/cuda/pathfinder run PFIND D2 3
python3 run_analysis.py /home/dipayan2/Desktop/Efficient_DVFS/gpu-rodinia/cuda/pathfinder run PFIND D3 2

echo "PFIND Done"

python3 run_analysis.py /home/dipayan2/Desktop/Efficient_DVFS/gpu-rodinia/cuda/gaussian run GAUSS D0 20
python3 run_analysis.py /home/dipayan2/Desktop/Efficient_DVFS/gpu-rodinia/cuda/gaussian run GAUSS D1 10
python3 run_analysis.py /home/dipayan2/Desktop/Efficient_DVFS/gpu-rodinia/cuda/gaussian run GAUSS D2 5
python3 run_analysis.py /home/dipayan2/Desktop/Efficient_DVFS/gpu-rodinia/cuda/gaussian run GAUSS D3 5

echo "GAUSS Done"

python3 run_analysis.py /home/dipayan2/Desktop/Efficient_DVFS/gpu-rodinia/cuda/bfs run BFS D0 20
python3 run_analysis.py /home/dipayan2/Desktop/Efficient_DVFS/gpu-rodinia/cuda/bfs run BFS D1 10
python3 run_analysis.py /home/dipayan2/Desktop/Efficient_DVFS/gpu-rodinia/cuda/bfs run BFS D2 5
python3 run_analysis.py /home/dipayan2/Desktop/Efficient_DVFS/gpu-rodinia/cuda/bfs run BFS D3 5

echo "BFS Done"



echo "Run in CRAVE Mode"

sudo -b taskset -c 0 /home/dipayan2/Desktop/Efficient_DVFS/goVcode/run_crave >/dev/null
PID=$(ps aux | grep 'goVcode/run_crave' | head -1 | awk '{print $2}')
echo "CRAVE PID"
echo $PID

python3 run_analysis.py /home/dipayan2/Desktop/Efficient_DVFS/gpu-rodinia/cuda/nw run NW C0 20
python3 run_analysis.py /home/dipayan2/Desktop/Efficient_DVFS/gpu-rodinia/cuda/nw run NW C1 10
python3 run_analysis.py /home/dipayan2/Desktop/Efficient_DVFS/gpu-rodinia/cuda/nw run NW C2 5
python3 run_analysis.py /home/dipayan2/Desktop/Efficient_DVFS/gpu-rodinia/cuda/nw run NW C3 5

echo "NW Cone"

python3 run_analysis.py /home/dipayan2/Desktop/Efficient_DVFS/gpu-rodinia/cuda/streamcluster run STCLUST C0 15
python3 run_analysis.py /home/dipayan2/Desktop/Efficient_DVFS/gpu-rodinia/cuda/streamcluster run STCLUST C1 10
python3 run_analysis.py /home/dipayan2/Desktop/Efficient_DVFS/gpu-rodinia/cuda/streamcluster run STCLUST C2 5
python3 run_analysis.py /home/dipayan2/Desktop/Efficient_DVFS/gpu-rodinia/cuda/streamcluster run STCLUST C3 2

echo "SCLUST Cone"

python3 run_analysis.py /home/dipayan2/Desktop/Efficient_DVFS/gpu-rodinia/cuda/pathfinder run PFIND C0 10
python3 run_analysis.py /home/dipayan2/Desktop/Efficient_DVFS/gpu-rodinia/cuda/pathfinder run PFIND C1 5
python3 run_analysis.py /home/dipayan2/Desktop/Efficient_DVFS/gpu-rodinia/cuda/pathfinder run PFIND C2 3
python3 run_analysis.py /home/dipayan2/Desktop/Efficient_DVFS/gpu-rodinia/cuda/pathfinder run PFIND C3 2

echo "PFIND Cone"

python3 run_analysis.py /home/dipayan2/Desktop/Efficient_DVFS/gpu-rodinia/cuda/gaussian run GAUSS C0 20
python3 run_analysis.py /home/dipayan2/Desktop/Efficient_DVFS/gpu-rodinia/cuda/gaussian run GAUSS C1 10
python3 run_analysis.py /home/dipayan2/Desktop/Efficient_DVFS/gpu-rodinia/cuda/gaussian run GAUSS C2 5
python3 run_analysis.py /home/dipayan2/Desktop/Efficient_DVFS/gpu-rodinia/cuda/gaussian run GAUSS C3 5

echo "GAUSS Cone"

python3 run_analysis.py /home/dipayan2/Desktop/Efficient_DVFS/gpu-rodinia/cuda/bfs run BFS C0 20
python3 run_analysis.py /home/dipayan2/Desktop/Efficient_DVFS/gpu-rodinia/cuda/bfs run BFS C1 10
python3 run_analysis.py /home/dipayan2/Desktop/Efficient_DVFS/gpu-rodinia/cuda/bfs run BFS C2 5
python3 run_analysis.py /home/dipayan2/Desktop/Efficient_DVFS/gpu-rodinia/cuda/bfs run BFS C3 5

echo "BFS Cone"


sudo kill -INT $PID
echo "Killed It"


