import subprocess
import os

class MemClock:
    def __init__(self):
        self.mem_freq = 0

    def get_clock(self):
        cmd = os.path.join(os.getcwd() + "/mem_get_clock.sh")
        curr_freq = subprocess.check_output(cmd,shell=True)
        curr_freq = curr_freq.decode('ascii')
        if len(curr_freq) <2:
            return -1
        self.mem_freq = int(curr_freq[:-1])
        return self.mem_freq
    
    def set_clock(self, freq):
        path = os.path.join(os.getcwd() + "/mem_set_clock.sh")
        cmd = path+ " "+str(freq)
        subprocess.check_call(cmd, shell=True)
        self.mem_freq = freq
        return