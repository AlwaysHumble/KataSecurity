#Program to flood network resources
#Replace Password with root password

import os
import time
import multiprocessing
#import gc

print("Running packet flooder")

#increase later
def pinger():
	#add sudo -S before ping if want to run host rather than docker
	os.system("ping -f netflix.com -c 1500")

parent_process=multiprocessing.Process(target=pinger)
parent_process.start()
exit()
for x in range(24):
	temp_process=multiprocessing.Process(target=pinger)
	temp_process.start()
	if(x%4==0):
		time.sleep(2)

print("network testing done")
		
def put_stress(dur):
	os.system("stress --vm 1 --timeout "+str(dur)+"s")

dur=25
process_1=multiprocessing.Process(target=put_stress,args=(dur,),)
process_1.start()
time.sleep(3)


process_2=multiprocessing.Process(target=put_stress,args=(dur,),)
process_2.start()
time.sleep(3)

process_3=multiprocessing.Process(target=put_stress,args=(dur,),)
process_3.start()
time.sleep(3)

process_4=multiprocessing.Process(target=put_stress,args=(dur,),)
process_4.start()
time.sleep(3)

process_5=multiprocessing.Process(target=put_stress,args=(dur,),)
process_5.start()
time.sleep(3)

process_6=multiprocessing.Process(target=put_stress,args=(dur,),)
process_6.start()
time.sleep(3)

process_7=multiprocessing.Process(target=put_stress,args=(dur,),)
process_7.start()
time.sleep(3)

print("cpu testing done")

def func(dur):
	os.system("stress --vm 1 --timeout 12s --vm-bytes 1024M")
	
for _ in range(4):
	process=multiprocessing.Process(target=func,args=(1,),)
	process.start()
	time.sleep(3)

print("ram testing done")

def func(dur):
	os.system("stress --io 6 --timeout 40s")
	
for _ in range(10):
	process=multiprocessing.Process(target=func,args=(1,),)
	process.start()
	time.sleep(3)

print("io testing done")