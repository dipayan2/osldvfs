#!/bin/bash
source ~/.bashrc
sudo date
# We used this to run a bunch of benchmarks and collect data. We will start with chai and rodinia and move to others
# This is running the code with the default governor
# python3 run_analysis.py /home/dipayan2/Desktop/Efficient_DVFS/chai/CUDA-D/SSSP sssp SSSP D0 20
# python3 run_analysis.py /home/dipayan2/Desktop/Efficient_DVFS/chai/CUDA-D/SSSP sssp SSSP D1 10
# python3 run_analysis.py /home/dipayan2/Desktop/Efficient_DVFS/chai/CUDA-D/SSSP sssp SSSP D2 5
# python3 run_analysis.py /home/dipayan2/Desktop/Efficient_DVFS/chai/CUDA-D/SSSP sssp SSSP D3 5

# echo "SSSP Done"

# python3 run_analysis.py /home/dipayan2/Desktop/Efficient_DVFS/chai/CUDA-D/HSTI hsti HSTI D0 100
# python3 run_analysis.py /home/dipayan2/Desktop/Efficient_DVFS/chai/CUDA-D/HSTI hsti HSTI D1 50
# python3 run_analysis.py /home/dipayan2/Desktop/Efficient_DVFS/chai/CUDA-D/HSTI hsti HSTI D2 20
# python3 run_analysis.py /home/dipayan2/Desktop/Efficient_DVFS/chai/CUDA-D/HSTI hsti HSTI D3 10

# echo "HSTI Done"

# python3 run_analysis.py /home/dipayan2/Desktop/Efficient_DVFS/chai/CUDA-D/HSTO hsto HSTO D0 20
# python3 run_analysis.py /home/dipayan2/Desktop/Efficient_DVFS/chai/CUDA-D/HSTO hsto HSTO D1 10
# python3 run_analysis.py /home/dipayan2/Desktop/Efficient_DVFS/chai/CUDA-D/HSTO hsto HSTO D2 5
# python3 run_analysis.py /home/dipayan2/Desktop/Efficient_DVFS/chai/CUDA-D/HSTO hsto HSTO D3 5

# echo "HSTI Done"

# python3 run_analysis.py /home/dipayan2/Desktop/Efficient_DVFS/chai/CUDA-D/TRNS trns TRNS D0 20
# python3 run_analysis.py /home/dipayan2/Desktop/Efficient_DVFS/chai/CUDA-D/TRNS trns TRNS D1 10
# python3 run_analysis.py /home/dipayan2/Desktop/Efficient_DVFS/chai/CUDA-D/TRNS trns TRNS D2 5
# python3 run_analysis.py /home/dipayan2/Desktop/Efficient_DVFS/chai/CUDA-D/TRNS trns TRNS D3 5

# echo "TRNS Done"

# python3 run_analysis.py /home/dipayan2/Desktop/Efficient_DVFS/chai/CUDA-D/SC sc SC D0 20
# python3 run_analysis.py /home/dipayan2/Desktop/Efficient_DVFS/chai/CUDA-D/SC sc SC D1 10
# python3 run_analysis.py /home/dipayan2/Desktop/Efficient_DVFS/chai/CUDA-D/SC sc SC D2 5
# python3 run_analysis.py /home/dipayan2/Desktop/Efficient_DVFS/chai/CUDA-D/SC sc SC D3 5

# echo "SC Done"

# python3 run_analysis.py /home/dipayan2/Desktop/Efficient_DVFS/chai/CUDA-D/TQ tq TQ D0 100
# python3 run_analysis.py /home/dipayan2/Desktop/Efficient_DVFS/chai/CUDA-D/TQ tq TQ D1 50
# python3 run_analysis.py /home/dipayan2/Desktop/Efficient_DVFS/chai/CUDA-D/TQ tq TQ D2 20
# python3 run_analysis.py /home/dipayan2/Desktop/Efficient_DVFS/chai/CUDA-D/TQ tq TQ D3 20

# echo "TQ Done"

# python3 run_analysis.py /home/dipayan2/Desktop/Efficient_DVFS/chai/CUDA-D/CEDD cedd CEDD D0 10
# python3 run_analysis.py /home/dipayan2/Desktop/Efficient_DVFS/chai/CUDA-D/CEDD cedd CEDD D1 5
# python3 run_analysis.py /home/dipayan2/Desktop/Efficient_DVFS/chai/CUDA-D/CEDD cedd CEDD D2 2
# python3 run_analysis.py /home/dipayan2/Desktop/Efficient_DVFS/chai/CUDA-D/CEDD cedd CEDD D3 2

# echo "Run in CRAVE Mode"

# sudo -b taskset -c 0 /home/dipayan2/Desktop/Efficient_DVFS/goVcode/run_crave >/dev/null
# PID=$(ps aux | grep 'goVcode/run_crave' | head -1 | awk '{print $2}')
# echo "CRAVE PID"
# echo $PID

# python3 run_analysis.py /home/dipayan2/Desktop/Efficient_DVFS/chai/CUDA-D/SSSP sssp SSSP C0 20
# python3 run_analysis.py /home/dipayan2/Desktop/Efficient_DVFS/chai/CUDA-D/SSSP sssp SSSP C1 10
# python3 run_analysis.py /home/dipayan2/Desktop/Efficient_DVFS/chai/CUDA-D/SSSP sssp SSSP C2 5
# python3 run_analysis.py /home/dipayan2/Desktop/Efficient_DVFS/chai/CUDA-D/SSSP sssp SSSP C3 5

# echo "SSSP Cone"

# python3 run_analysis.py /home/dipayan2/Desktop/Efficient_DVFS/chai/CUDA-D/HSTI hsti HSTI C0 100
# python3 run_analysis.py /home/dipayan2/Desktop/Efficient_DVFS/chai/CUDA-D/HSTI hsti HSTI C1 50
# python3 run_analysis.py /home/dipayan2/Desktop/Efficient_DVFS/chai/CUDA-D/HSTI hsti HSTI C2 20
# python3 run_analysis.py /home/dipayan2/Desktop/Efficient_DVFS/chai/CUDA-D/HSTI hsti HSTI C3 10

# echo "HSTI Cone"

# python3 run_analysis.py /home/dipayan2/Desktop/Efficient_DVFS/chai/CUDA-D/HSTO hsto HSTO C0 20
# python3 run_analysis.py /home/dipayan2/Desktop/Efficient_DVFS/chai/CUDA-D/HSTO hsto HSTO C1 10
# python3 run_analysis.py /home/dipayan2/Desktop/Efficient_DVFS/chai/CUDA-D/HSTO hsto HSTO C2 5
# python3 run_analysis.py /home/dipayan2/Desktop/Efficient_DVFS/chai/CUDA-D/HSTO hsto HSTO C3 5

# echo "HSTI Cone"

# python3 run_analysis.py /home/dipayan2/Desktop/Efficient_DVFS/chai/CUDA-D/TRNS trns TRNS C0 20
# python3 run_analysis.py /home/dipayan2/Desktop/Efficient_DVFS/chai/CUDA-D/TRNS trns TRNS C1 10
# python3 run_analysis.py /home/dipayan2/Desktop/Efficient_DVFS/chai/CUDA-D/TRNS trns TRNS C2 5
# python3 run_analysis.py /home/dipayan2/Desktop/Efficient_DVFS/chai/CUDA-D/TRNS trns TRNS C3 5

# echo "TRNS Cone"

# python3 run_analysis.py /home/dipayan2/Desktop/Efficient_DVFS/chai/CUDA-D/SC sc SC C0 20
# python3 run_analysis.py /home/dipayan2/Desktop/Efficient_DVFS/chai/CUDA-D/SC sc SC C1 10
# python3 run_analysis.py /home/dipayan2/Desktop/Efficient_DVFS/chai/CUDA-D/SC sc SC C2 5
# python3 run_analysis.py /home/dipayan2/Desktop/Efficient_DVFS/chai/CUDA-D/SC sc SC C3 5

# echo "SC Cone"

# python3 run_analysis.py /home/dipayan2/Desktop/Efficient_DVFS/chai/CUDA-D/TQ tq TQ C0 100
# python3 run_analysis.py /home/dipayan2/Desktop/Efficient_DVFS/chai/CUDA-D/TQ tq TQ C1 50
# python3 run_analysis.py /home/dipayan2/Desktop/Efficient_DVFS/chai/CUDA-D/TQ tq TQ C2 20
# python3 run_analysis.py /home/dipayan2/Desktop/Efficient_DVFS/chai/CUDA-D/TQ tq TQ C3 20

# echo "TQ Cone"

# python3 run_analysis.py /home/dipayan2/Desktop/Efficient_DVFS/chai/CUDA-D/CEDD cedd CEDD C0 10
# python3 run_analysis.py /home/dipayan2/Desktop/Efficient_DVFS/chai/CUDA-D/CEDD cedd CEDD C1 5
# python3 run_analysis.py /home/dipayan2/Desktop/Efficient_DVFS/chai/CUDA-D/CEDD cedd CEDD C2 2
# python3 run_analysis.py /home/dipayan2/Desktop/Efficient_DVFS/chai/CUDA-D/CEDD cedd CEDD C3 2



# sudo kill -INT $PID
# echo "Killed It"

echo "Run in COCAP Mode"

sudo -b taskset -c 0 /home/dipayan2/Desktop/Efficient_DVFS/goVcode/run_crave 1 >/dev/null
PIDA=$(ps aux | grep 'goVcode/run_crave' | head -1 | awk '{print $2}')
echo "COCAP PID"
echo $PIDA

python3 run_analysis.py /home/dipayan2/Desktop/Efficient_DVFS/chai/CUDA-D/SSSP sssp SSSP COP0 20
python3 run_analysis.py /home/dipayan2/Desktop/Efficient_DVFS/chai/CUDA-D/SSSP sssp SSSP COP1 10
python3 run_analysis.py /home/dipayan2/Desktop/Efficient_DVFS/chai/CUDA-D/SSSP sssp SSSP COP2 5
python3 run_analysis.py /home/dipayan2/Desktop/Efficient_DVFS/chai/CUDA-D/SSSP sssp SSSP COP3 5

echo "SSSP COPone"

python3 run_analysis.py /home/dipayan2/Desktop/Efficient_DVFS/chai/CUDA-D/HSTI hsti HSTI COP0 100
python3 run_analysis.py /home/dipayan2/Desktop/Efficient_DVFS/chai/CUDA-D/HSTI hsti HSTI COP1 50
python3 run_analysis.py /home/dipayan2/Desktop/Efficient_DVFS/chai/CUDA-D/HSTI hsti HSTI COP2 20
python3 run_analysis.py /home/dipayan2/Desktop/Efficient_DVFS/chai/CUDA-D/HSTI hsti HSTI COP3 10

echo "HSTI COPone"

python3 run_analysis.py /home/dipayan2/Desktop/Efficient_DVFS/chai/CUDA-D/HSTO hsto HSTO COP0 20
python3 run_analysis.py /home/dipayan2/Desktop/Efficient_DVFS/chai/CUDA-D/HSTO hsto HSTO COP1 10
python3 run_analysis.py /home/dipayan2/Desktop/Efficient_DVFS/chai/CUDA-D/HSTO hsto HSTO COP2 5
python3 run_analysis.py /home/dipayan2/Desktop/Efficient_DVFS/chai/CUDA-D/HSTO hsto HSTO COP3 5

echo "HSTI COPone"

python3 run_analysis.py /home/dipayan2/Desktop/Efficient_DVFS/chai/CUDA-D/TRNS trns TRNS COP0 20
python3 run_analysis.py /home/dipayan2/Desktop/Efficient_DVFS/chai/CUDA-D/TRNS trns TRNS COP1 10
python3 run_analysis.py /home/dipayan2/Desktop/Efficient_DVFS/chai/CUDA-D/TRNS trns TRNS COP2 5
python3 run_analysis.py /home/dipayan2/Desktop/Efficient_DVFS/chai/CUDA-D/TRNS trns TRNS COP3 5

echo "TRNS COPone"

python3 run_analysis.py /home/dipayan2/Desktop/Efficient_DVFS/chai/CUDA-D/SC sc SC COP0 20
python3 run_analysis.py /home/dipayan2/Desktop/Efficient_DVFS/chai/CUDA-D/SC sc SC COP1 10
python3 run_analysis.py /home/dipayan2/Desktop/Efficient_DVFS/chai/CUDA-D/SC sc SC COP2 5
python3 run_analysis.py /home/dipayan2/Desktop/Efficient_DVFS/chai/CUDA-D/SC sc SC COP3 5

echo "SC COPone"

python3 run_analysis.py /home/dipayan2/Desktop/Efficient_DVFS/chai/CUDA-D/TQ tq TQ COP0 100
python3 run_analysis.py /home/dipayan2/Desktop/Efficient_DVFS/chai/CUDA-D/TQ tq TQ COP1 50
python3 run_analysis.py /home/dipayan2/Desktop/Efficient_DVFS/chai/CUDA-D/TQ tq TQ COP2 20
python3 run_analysis.py /home/dipayan2/Desktop/Efficient_DVFS/chai/CUDA-D/TQ tq TQ COP3 20

echo "TQ COPone"

python3 run_analysis.py /home/dipayan2/Desktop/Efficient_DVFS/chai/CUDA-D/CEDD cedd CEDD COP0 10
python3 run_analysis.py /home/dipayan2/Desktop/Efficient_DVFS/chai/CUDA-D/CEDD cedd CEDD COP1 5
python3 run_analysis.py /home/dipayan2/Desktop/Efficient_DVFS/chai/CUDA-D/CEDD cedd CEDD COP2 2
python3 run_analysis.py /home/dipayan2/Desktop/Efficient_DVFS/chai/CUDA-D/CEDD cedd CEDD COP3 2



sudo kill -INT $PIDA
echo "Killed It"



