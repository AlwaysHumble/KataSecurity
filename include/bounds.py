#Python module to get bounds on resources used to detect malicious behaviour

import pandas as pd
import os

class bounds():
	
	def __init__(self):
		train=pd.read_csv("data/docker/all_data.csv")
		self.__bounds_dict={}
		for x in train.columns:
			self.__bounds_dict[x]=(train[x].min(),train[x].max())#change it to list if necessary
			
		print("Bounds are ready")
		self.__store()
			
	def get_bounds(self):
		return self.__bounds_dict
	
	def get_bound(self,attr):
		return self.__bounds_dict[attr]
	
	def __store(self):
		os.system("rm -rf proc/bounds")
		os.system("mkdir proc/bounds")
		file_pointer=open("proc/bounds/dockerbounds.txt","w")
		for x in self.__bounds_dict:
			file_pointer.write(x+" "+str(self.__bounds_dict[x])+"\n")
	
'''
if __name__ == "__main__":
	obj=bounds()
	print("Bounds completed sucessfuly")
else:
	print("Bounding failed\nPlease check bounds.py")
'''