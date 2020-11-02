import multiprocessing
import time
import os

#do better

class func():
	
	def __init__(self):
		for i in range(50):
			file=open("temp/file_"+str(i)+".txt","w")
			file.write("asdf")
			file.close()
			time.sleep(1)

def f2():
	obj=func()	

os.system("rm -rf temp")
os.system("mkdir temp")

proc=multiprocessing.Process(target=f2,args=(),)
proc.start()
time.sleep(5)
proc.terminate()