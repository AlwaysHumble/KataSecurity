#Program to eat RAM

print("Running RAM eater")

import time
import os
import multiprocessing

def func(dur):
	os.system("stress --vm 1 --timeout 12s --vm-bytes 824M")#1024M
	
for _ in range(6):
	process=multiprocessing.Process(target=func,args=(1,),)
	process.start()
	time.sleep(3)