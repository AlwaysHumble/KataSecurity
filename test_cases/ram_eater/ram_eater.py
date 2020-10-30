#Program to eat RAM

print("Running RAM eater")

import time

a=[]

#change later

times=10**1
for i in range(100):
	print(len(a))
	a.append(' ' * times)
	#for i in range(times):
	#	a.append(' ' * times)
	#time.sleep(1)
	print(i)