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
    def __init__(self, cpu_dev=0, gpu_dev=0, polling_s=10000):
        self.cpu_id = cpu_dev
        self.gpu_id = gpu_dev
        self.polling = polling_s
        # set_up the managers
        self.cpu_man = cpuclock.CPUClock(0)
        self.gpu_man = gpuclock.GPUClock()
        self.mem_man = memclock.MemClock()
        self.cluster = {} # We will hardcode this
        self.my_thread = None

    
    def policy_cpu(self):
        '''
        In this code: we are selecting the best configuration for all the resources based on the state of cpu operating point
        '''

        cpu_freq = self.cpu_man.get_clock() # we have the CPU freq 
        # Set the rest of the two frequency
        # print(" Util : "+str(self.cpu_man.get_utilization()))
        gpu_freq = int(self.cluster[cpu_freq]['gpu'])
        mem_freq = int(self.cluster[cpu_freq]['mem'])
        self.gpu_man.set_clock(gpu_freq)
        self.mem_man.set_clock(mem_freq)
        # print("The freq are , cpu : {}, gpu: {} and mem: {}".format(cpu_freq,self.gpu_man.get_clock(),self.mem_man.get_clock()))
        return

    def policy_mem(self):
        '''
        In this code: we are selecting the best configuration for all the resources based on the state of memory operating point
        '''

        mem_freq = self.mem_man.get_clock() # we have the CPU freq 
        print("Util : "+str(self.mem_man.get_utilization()))
        # Set the rest of the two frequency
        gpu_freq = int(self.cluster[mem_freq]['gpu'])
        cpu_freq = int(self.cluster[mem_freq]['cpu'])
        self.gpu_man.set_clock(gpu_freq)
        self.cpu_man.set_clock(cpu_freq)
        # print("The freq are , mem: {}, cpu : {}, gpu: {} ".format(mem_freq,self.cpu_man.get_clock(),self.gpu_man.get_clock()))
        return

    def policy_gpu(self):
        '''
        In this code: we are selecting the best configuration for all the resources based on the state of gpu operating point
        '''

        gpu_freq = self.gpu_man.get_clock() # we have the CPU freq 
        # Set the rest of the two frequency
        mem_freq = int(self.cluster[gpu_freq]['mem'])
        cpu_freq = int(self.cluster[gpu_freq]['cpu'])
        self.mem_man.set_clock(mem_freq)
        self.cpu_man.set_clock(cpu_freq)
        print("The freq are  gpu: {}, cpu: {}, mem : {} ".format(gpu_freq,self.cpu_man.get_clock(),self.mem_man.get_clock()))
        return
    
    def policy_util(self):
        ''' 
        Currently uses mem_cluster
        In this we will start to analyze the frequency transition along with other states of the resources
        1. start with the optimization
        2. find a clustering method
        '''

        # get memory util and set the rest as follows
        mem_util  = self.mem_man.get_utilization()
        mem_freq_list = [165000000,206000000,275000000,413000000,543000000,633000000,728000000,825000000]
        mem_freq = mem_freq_list[3]
        if mem_util > 0.6:
            mem_freq = mem_freq_list[5]
        elif mem_util > 0.3:
            mem_freq = mem_freq_list[3]
        else:
            mem_freq = mem_freq_list[0]
        self.mem_man.set_clock(mem_freq)
        gpu_freq = int(self.cluster[mem_freq]['gpu'])
        cpu_freq = int(self.cluster[mem_freq]['cpu'])
        self.gpu_man.set_clock(gpu_freq)
        self.cpu_man.set_clock(cpu_freq)
            


    def set_cluster(self, clk_cluster):
        self.cluster = clk_cluster

    def schedule(self):
        # print("Starting the scheduler")
        self.my_thread = threading.Timer(1, self.schedule)
        # self.my_thread.daemon = True
        self.my_thread.start()
        start_time = time.time()
        # self.policy_cpu()
        self.policy_mem()
        #self.policy_gpu()
        print(" Overhead is {} second".format(time.time()-start_time))
        
    def run(self):
        self.schedule()
    
