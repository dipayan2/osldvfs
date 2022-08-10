import subprocess
import os
from common import parser

class CPUClock:
	def __init__(self,cpu_id=0):
		self.path = "/sys/devices/system/cpu"
		self.cpu_id = cpu_id
		self.dev_count = 8
		self.cpu_freq = 0
		self.cpu_util = 0
	
	def get_clock(self):
		print(f"... Getting the cpu {self.cpu_id} frequency")
		path = os.path.join(os.getcwd() + "/scripts/cpu_get_clock.sh")
		cmd = path+ " " + str(self.cpu_id)
		curr_freq = subprocess.check_output(cmd,shell=True)
		curr_freq = curr_freq.decode('ascii')
		print(f"The frequency of cpu {self.cpu_id} is {curr_freq}")
		if len(curr_freq) <2:
			return -1
		self.cpu_freq = int(curr_freq[:-1])
		return self.curr_freq
	
	def set_clock(self, freq):
		print(f"... Setting the cpu {self.cpu_id} to {freq} ")
		path = os.path.join(os.getcwd() + "/scripts/cpu_set_clock.sh")
		cmd = path+ " "+str(self.cpu_id)+" "+str(freq)
		subprocess.check_call(cmd, shell=True)
		print(f"The clock is in CPU {self.cpu_id} to {freq}")
		self.cpu_freq = freq
		return
	
	def get_all_clock(self):
		print(f"... Getting the cpu {self.cpu_id} frequency")
		path = os.path.join(os.getcwd() + "/scripts/cpu_get_all_clock.sh")
		cmd = path+ " " + str(self.cpu_id)
		freq_list = subprocess.check_output(cmd,shell=True)
		freq_list = freq_list.split.decode('ascii')
		freq_list = freq_list.replace(' \n', '')
		freq_list = freq_list.split(" ")
		print(f"The frequency list of cpu {self.cpu_id} is {freq_list}")
		# self.cpu_freq = curr_freq
		if len(freq_list) <= 0:
			return []
		return freq_list

	def get_utilization(self):
		print(f"... Getting the utilization of the cpu")
		cmd = "top -n1 -1|grep "
		cmd = cmd+ " "+str("\'Cpu")+str(self.cpu_id)+str("\'")
		util_out  = subprocess.check_output(cmd,shell=True)
		util_list = processShell(util_out)
		idle_val = util_list.split(":")[1].split(",")[3]
		idle_val = idle_val[:-2]
		cpu_util = (100.0 - float(idle_val))/100.0
		self.cpu_util = cpu_util
		return cpu_util
