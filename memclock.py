import subprocess
import os
from common.parser import processShell

class MemClock:
	def __init__(self):
		self.path = "/sys/devices/system/cpu"
		self.mem_freq = 0
		self.mem_util = 0
	
	def get_clock(self):
		# print("... Getting the memory frequency")
		path = os.path.join(os.getcwd() + "/scripts/mem_get_clock.sh")
		cmd = path 
		mem_freq = subprocess.check_output(cmd,shell=True)
		mem_freq = mem_freq.decode('ascii')
		# print("The memory frequency is:"+ str (mem_freq))
		if len(mem_freq) < 2:
			return -1
		self.mem_freq = int(mem_freq[:-1])
		return self.mem_freq
	
	def set_clock(self, freq):
		# print("... Setting the mem to{}".format(freq))
		if self.mem_freq != freq:
			path = os.path.join(os.getcwd() + "/scripts/mem_set_clock.sh")
			inc_flag = 0
			if freq > self.mem_freq:
				inc_flag = 1
			cmd = path+" "+str(freq)+" "+str(inc_flag)
			subprocess.check_call(cmd, shell=True)
			# print("The clock is in Mem to "+str(freq))
			self.mem_freq = freq
		return
	
	def get_all_clock(self):
		print("... Getting the mem all frequency")
		path = os.path.join(os.getcwd() + "/scripts/mem_get_all_clock.sh")
		cmd = path
		freq_list = subprocess.check_output(cmd,shell=True)
		freq_list = freq_list.split(" ")
		print("The mem frequency list of "+str(repr(freq_list)))
		# self.cpu_freq = curr_freq
		if len(freq_list) <= 0:
			return []
		return freq_list

	def get_utilization(self):
		# print("... Getting the utilization of the memory")
		cmd = "top -n1 -1|grep "
		cmd = cmd+ " "+str("\'MiB Mem \'")
		mem_util  = subprocess.check_output(cmd,shell=True)
		mem_util = processShell(mem_util)
		if len(mem_util) <= 0:
			return -1
		mem_util = mem_util.split(':')[1]
		util_list = mem_util.split(",")
		tot_mem = float(util_list[0][:-5])
		used_mem = float(util_list[2][:-4])
		self.mem_util = used_mem/tot_mem
		return self.mem_util



