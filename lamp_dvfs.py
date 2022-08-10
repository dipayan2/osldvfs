from __future__ import print_function
import os
import gpuclock
import memclock
import cpuclock
from common import executor
import threading
import time
import subprocess

# starting with a single object for each resource
class OSLScheduler:
    def __init__(self, cpu_dev=0, gpu_dev=0, polling_s=10):
        self.cpu_id = cpu_dev
        self.gpu_id = gpu_dev
        self.polling = polling_s
        # set_up the managers
        self.cpu_man = cpuclock.CPUClock()
        self.gpu_man = gpuclock.GPUClock()
        self.mem_man = memclock.MemClock()
        self.cluster = {} # We will hardcode this

    
    def policy(self):
        '''
        In this code: we are selecting the best configuration for all the resources
        '''

        cpu_freq = self.cpu_man.get_clock() # we have the CPU freq 
        # Set the rest of the two frequency
        gpu_freq = self.cluster[cpu_freq]['gpu']
        mem_freq = self.cluster[cpu_freq]['mem']
        self.gpu_man.set_clock(gpu_freq)
        self.mem_man.set_clock(mem_freq)
        print("The freq are , cpu : {}, gpu: {} and mem: {}".format(cpu_freq,gpu_freq,mem_freq))  
        return

    def set_cluster(self, clk_cluster):
        self.cluster = clk_cluster

    def schedule(self):
        print("Starting the scheduler")
        self.policy()
        threading.Timer(self.polling, self.schedule()).start()
        
    def run(self):
        self.schedule()
    
