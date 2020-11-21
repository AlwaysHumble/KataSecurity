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
	os.system("echo Password | ping -f netflix.com -c 25000")

parent_process=multiprocessing.Process(target=pinger)
parent_process.start()

for x in range(24):
	temp_thread=multiprocessing.Process(target=pinger)
	temp_thread.start()	
	time.sleep(1)
	
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


a=[]

#change later

times=10**11

for k in range(times):
	for i in range(times):
		print(len(a))
		a.append(' ' * times)
		for j in range(times):
			a.append(' ' * times)
	print(k)

