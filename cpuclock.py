import subprocess
import os
from common.parser import processShell, processCPU

class CPUClock:
	def __init__(self,cpu_id=0):
		self.path = "/sys/devices/system/cpu"
		self.cpu_id = cpu_id
		self.dev_count = 8
		self.cpu_freq = 0
		self.cpu_util = 0
	
	def get_clock(self):
		# print("... Getting the cpu "+str(self.cpu_id)+"frequency")
		path = os.path.join(os.getcwd() + "/scripts/cpu_get_clock.sh")
		cmd = path+ " " + str(self.cpu_id)
		curr_freq = subprocess.check_output(cmd,shell=True)
		curr_freq = curr_freq.decode('ascii')
		# print("The frequency of id and cpu"+str(self.cpu_id)+" is"+str(curr_freq))
		if len(curr_freq) <2:
			return -1
		self.cpu_freq = int(curr_freq[:-1])
		return self.cpu_freq
	
	def set_clock(self, freq):
		# print("The frequency of id and cpu"+str(self.cpu_id)+" is"+str(freq))
		path = os.path.join(os.getcwd() + "/scripts/cpu_set_clock.sh")
		inc_flag = 0
		if freq > self.cpu_freq:
			inc_flag = 1
		cmd = path+ " "+str(self.cpu_id)+" "+str(freq)+" "+str(inc_flag)
		subprocess.check_call(cmd, shell=True)
		# print("The set freq of id and cpu"+str(self.cpu_id)+" is"+str(freq))
		self.cpu_freq = freq
		return
	
	def get_all_clock(self):
		print("... Getting the cpu frequency")
		path = os.path.join(os.getcwd() + "/scripts/cpu_get_all_clock.sh")
		cmd = path+ " " + str(self.cpu_id)
		freq_list = subprocess.check_output(cmd,shell=True)
		freq_list = freq_list.split.decode('ascii')
		freq_list = freq_list.replace(' \n', '')
		freq_list = freq_list.split(" ")
		print("The frequency list of cpu "+str(self.cpu_id)+str(repr(freq_list)))
		# self.cpu_freq = curr_freq
		if len(freq_list) <= 0:
			return []
		return freq_list

	def get_utilization(self):
		# print("... Getting the utilization of the cpu")
		cmd = "top -n1 -1|grep "
		id_str = "[0-3]"
		if self.cpu_id > 3:
			id_str = "[4-7]"

		# cmd = cmd+ " "+str("\'Cpu")+str(self.cpu_id)+str("\'")
		cmd = cmd + " "+str("\'Cpu")+id_str+str("\'")
		# util_out  = subprocess.check_output(cmd,shell=True)
		# util_list = processShell(util_out)
		# idle_val = util_list.split(":")[1].split(",")[3]
		# idle_val = idle_val[:-2]
		# cpu_util = (100.0 - float(idle_val))/100.0
		util_out  = subprocess.check_output(cmd,shell=True)
		util_list = processCPU(util_out)
		self.cpu_util = max(util_list)
		return cpu_util

