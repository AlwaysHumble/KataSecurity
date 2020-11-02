#Python module to run model/algos to get insights on data

#under development
import pandas as pd
from sklearn.model_selection import train_test_split

class model:
	
	def __init__(self):
			
		self.__bounds_dict={}
		
		
	def start_model(self,train_df,model_location,store_location):	
		self.__run_model(train_df)
		
		self.__store_csv(store_location)
		self.__store_model(model_location)
		
		#add functionalities to update model
		
	def __run_model(self,train_df):
		for x in train_df.columns:
			try:
				train_df[x]=pd.to_numeric(train_df[x])
				self.__bounds_dict[x]=(train_df[x].min()-1,train_df[x].min(),train_df[x].max(),train_df[x].max()+1)
			except:
				continue
		
	#Change if later, it is temporary solution
	def __store_model(self,model_location):
		file_pointer=open(model_location,"w")

		for x in self.__bounds_dict:
			file_pointer.write(x+" "+str(self.__bounds_dict[x])+"\n")
	
		file_pointer.close()
	
	def get_bounds(self):
		return self.__bounds_dict
	
	def get_bound(self,attr):
		return self.__bounds_dict[attr]
	
	#Store location contains location to store the file and name of the file
	def __store_csv(self,store_location):
		store_df=pd.DataFrame(self.__bounds_dict)
		store_df.to_csv(store_location)
		
		
		
		
		
		
		
		
'''
file_pointer=open("proc/bounds/dockerbounds.txt","w")
for x in self.__bounds_dict:
file_pointer.write(x+" "+str(self.__bounds_dict[x])+"\n")
'''
		
		
