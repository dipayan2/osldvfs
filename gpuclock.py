import subprocess
import os

class GPUClock:
	def __init__(self):
		self.path = "/sys/devices/system/cpu"
		self.gpu_freq = 0
		self.gpu_util = 0
	
	def get_clock(self):
		print("... Getting the GPU frequency")
		path = os.path.join(os.getcwd() + "/scripts/gpu_get_clock.sh")
		cmd = path 
		gpu_freq = subprocess.check_output(cmd,shell=True)
		gpu_freq = gpu_freq.decode('ascii')
		gpu_freq = int(gpu_freq)
		print(f"The GPU frequency is {gpu_freq}")
		if len(gpu_freq) < 2:
			return -1
		self.gpu_freq = int(gpu_freq[:-1])
		return self.gpu_freq
	
	def set_clock(self, freq):
		print(f"... Setting the GPU to {freq} ")
		path = os.path.join(os.getcwd() + "/scripts/gpu_set_clock.sh")
		cmd = path+" "+str(freq)
		subprocess.check_call(cmd, shell=True)
		print(f"The clock is in GPU to {freq}")
		self.gpu_freq = freq
		return
	
	def get_all_clock(self):
		print(f"... Getting the GPU all frequency")
		# path = os.path.join(os.getcwd() + "/scripts/gpu_get_all_clock.sh")
		# cmd = path
		# freq_list = subprocess.check_output(cmd,shell=True)
		# freq_list = freq_list.split(" ")
		# print(f"The frequency list of {freq_list}")
		# self.cpu_freq = curr_freq
		# if len(freq_list) <= 0:
		#     return []
		# return freq_list
		return []

	def get_utilization(self):
		print(f"... Getting the utilization of the gpu")
		# path = os.path.join(os.getcwd() + "/scripts/gpu_get_util.sh")
		# cmd = path
		# gpu_util  = subprocess.check_output(cmd,shell=True)
		gpu_util = -1
		return gpu_util


