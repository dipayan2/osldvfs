import subprocess
import os

class GPUClock:
    def __init__(self):
        self.cpu_freq = 0

    def get_clock(self):
        cmd = os.path.join(os.getcwd() + "/gpu_get_clock.sh")
        curr_freq = subprocess.check_output(cmd,shell=True)
        curr_freq = curr_freq.decode('ascii')
        if len(curr_freq) <2:
            return -1
        self.cpu_freq = int(curr_freq[:-1])
        return self.cpu_freq
    
    def set_clock(self, freq):
        path = os.path.join(os.getcwd() + "/gpu_set_clock.sh")
        inc_flag = 0
        if freq > self.cpu_freq:
            inc_flag = 1
        cmd = path+" "+str(freq)+" "+str(inc_flag)
        subprocess.check_call(cmd, shell=True)
        self.cpu_freq = freq
        return


    

