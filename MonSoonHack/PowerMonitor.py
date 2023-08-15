import time
import Monsoon.HVPM as HVPM
import Monsoon.sampleEngine as sampleEngine
import Monsoon.Operations as op

mon = HVPM.Monsoon()
mon.setup_usb()
mon.setVout(5.0)
engine = sampleEngine.SampleEngine(mon)
engine.enableCSVOutput("TestPow.csv")
engine.ConsoleOutput(False)
numSamp = 100000
print(time.time())
engine.startSampling(numSamp)
#time.sleep(2)
#mon.stopSampling()
print("Done")
