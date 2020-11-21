#Python module to get bounds on resources used to detect malicious behaviour

#Under development
import pandas as pd
import os
import multiprocessing
from include.model import model	
	
class bounds:
	
	def __init__(self):
		print("Setting all bounds")
		
		#Setting up bounds folder in proc
		os.system("rm -rf proc/bounds")
		os.system("mkdir proc/bounds")
		
		#os.system("rm -rf proc/models")
		#os.system("mkdir proc/models")
	
		docker_df=pd.read_csv("data/docker/all_data.csv")
		
		docker_model_obj=model()
		docker_model_obj.start_model(docker_df,"proc/models/docker_model.txt","proc/bounds/docker_bounds.csv")
		
		container_df=self.__make_container_df()
		
		container_model_obj=model()
		container_model_obj.start_model(container_df,"proc/models/container_model.txt","proc/bounds/container_bounds.csv")
		
	def __make_container_df(self):
		path="data/all_containers"
		containers_list=os.listdir(path)
		
		#Defining variable to store dataframe
		df=0
		if len(containers_list)==0:
			print("No container data available")
			return
		else:#setting the dataframe
			df=pd.read_csv("data/all_containers/"+containers_list[0]+"/all_data.csv")
		
		#Iteratively adding all dataframes
		for fol_ind in range(1,len(containers_list)):
			temp_df=pd.read_csv("data/all_containers/"+containers_list[fol_ind]+"/all_data.csv")
			frames=[df,temp_df]
			try:
				df=pd.concat(frames,sort=True)
			except:
				print("Update data frame failed.\nCurrent data frame is not of the shape/format as the previous ones.\nCheck __make_container function in bounds.py")
				return
			
		df.to_csv("proc/system/all_containers_data.csv")
		return df
			
			
		
'''
if __name__ == "__main__":
	obj=bounds()
	print("Bounds completed sucessfuly")
else:
	print("Bounding failed\nPlease check bounds.py")
'''