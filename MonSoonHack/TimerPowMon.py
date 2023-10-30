import signal
import subprocess
import time

command = "python3 PowerMonitor.py"
print(time.time())
proc = subprocess.Popen(command.split(),stdout=subprocess.PIPE,stdin=subprocess.PIPE)#,creationflags=subprocess.CREATE_NEW_PROCESS_GROUP) 
time.sleep(2.42)
proc.send_signal(signal.SIGINT)
time.sleep(0.2)
proc.kill()

