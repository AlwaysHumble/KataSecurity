#Program to stress CPU
import time
import os
import multiprocessing


print("Running cpu eater")

#increase later
def put_stress(dur):
	os.system("stress --vm 1 --timeout "+str(dur)+"s")


dur=30
process_1=multiprocessing.Process(target=put_stress,args=(dur,),)
process_1.start()
time.sleep(5)


process_2=multiprocessing.Process(target=put_stress,args=(dur,),)
process_2.start()
time.sleep(5)

process_3=multiprocessing.Process(target=put_stress,args=(dur,),)
process_3.start()
time.sleep(5)

process_4=multiprocessing.Process(target=put_stress,args=(dur,),)
process_4.start()
time.sleep(5)

process_5=multiprocessing.Process(target=put_stress,args=(dur,),)
process_5.start()
time.sleep(5)

process_5=multiprocessing.Process(target=put_stress,args=(dur,),)
process_5.start()
time.sleep(5)

process_5=multiprocessing.Process(target=put_stress,args=(dur,),)
process_5.start()
time.sleep(5)