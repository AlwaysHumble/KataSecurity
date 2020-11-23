import time
import os
import multiprocessing

print("Running io flooder")

def func(dur):
	os.system("stress --io 6 --timeout 40s")
	
for _ in range(10):
	process=multiprocessing.Process(target=func,args=(1,),)
	process.start()
	time.sleep(3)

