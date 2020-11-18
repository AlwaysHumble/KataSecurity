#Program to eat RAM

print("Running RAM eater")

import time

a=[]

#change later

times=10**8
for k in range(times):
	for i in range(times):
		print(len(a))
		a.append(' ' * times)
		for j in range(times):
			a.append(' ' * times)
	#time.sleep(1)
	print(k)