#Python module to get bounds on resources used to detect malicious behaviour

import pandas as pd

class bounds():
	
	__bounds_dict={}
	def __init__(self):
		train=pd.read_csv("data/all_data.csv")
		for x in train.columns:
			self.__bounds_dict[x]=(train[x].min(),train[x].max())#change it to list if necessary
			
		print("Bounds are ready")
			
	def get_bounds(self):
		return self.__bounds_dict
	
	def get_bound(self,attr):
		return self.__bounds_dict[attr]
	
	def store(self):
		file_pointer=open("bounds.txt","w")
		for x in self.__bounds_dict:
			file_pointer.write(x+" "+str(self.__bounds_dict[x])+"\n")
	
'''
if __name__ == "__main__":
	obj=bounds()
	print("Bounds completed sucessfuly")
else:
	print("Bounding failed\nPlease check bounds.py")
'''