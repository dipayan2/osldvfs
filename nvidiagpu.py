import subprocess
import os

from py3nvml.py3nvml import *

class NvdaGPUClock:
		def __init__(self, device_id):
	        nvmlInit()
	        self.device_id = device_id
	        self.device_count = nvmlDeviceGetCount()
	        self.dev_handle = nvmlDeviceGetHandleByIndex(device_id)

        def get_freq(self):
	        mem_clock = nvmlDeviceGetApplicationsClock(self.dev_handle, NVML_CLOCK_MEM)
	        gpx_clock = nvmlDeviceGetApplicationsClock(self.dev_handle, NVML_CLOCK_SM)
	        print("Application NVML_CLOCK_SM: {}, NVML_CLOCK_Memory: {}".format(gpx_clock, mem_clock))

	        return mem_clock, gpx_clock

	    def set_freq(self,mem_clock, gpx_clock, device_id):
	    	path = os.path.join(os.getcwd() + "/scripts/set_clock.sh")
	    	cmd = path + " " + str(device_id) + " " + str(mem_clock) + " " + str(gpx_clock)
	    	subprocess.check_call(cmd, shell=True)

	    def get_list_freq(self):
	    	path = os.path.join(os.getcwd() + "/scripts/get_clock_list.sh")
	    	cmd = path+ " " + str(self.device_id)
	    	print(f"List of clock speed for device : {self.device_id}")
	    	freq_list = subprocess.check_output(cmd,shell=True)
	    	return freq_list

	    def get_util(self):
	    	path = os.path.join(os.getcwd() + "/scripts/get_util.sh")
	    	cmd = path+ " " + str(self.device_id)
	    	print(f"List of clock speed for device : {self.device_id}")
	    	util = subprocess.check_output(cmd,shell=True)
	    	return util

