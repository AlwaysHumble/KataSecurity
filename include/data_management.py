#Python module to dealing with dataframe and keeping an updated database
import requests
import pandas as pd
import time
import os
import sys

#There should be about 1609 columns in dataframe
class data_management:
	def __init__(self,sleep_time,number_of_iterations):
		print("Starting Data Management Sytem")
		
		#clear data folder to store fresh data
		self.__setup_data_folder()
		
		#To store current data frame
		self.all_data=0#default initialization would be changed to dataframe later
		
		#Make current.csv and all_data.csv
		self.__get_data(True)
		
		#Loop to update dataset
		for cnt in range(1,number_of_iterations):#To be run for infinite time later
			self.__get_data(False)
			print("Dataset updated %s times"%cnt)
			time.sleep(sleep_time)
	
	
	#Return shape of current data
	def get_shape(self):
		return self.all_data.shape

		
	#Get data from 9323 port as text file and send to make dataframe
	def __get_data(self,make_all_data):
		data=requests.get("http://localhost:9323/metrics")#apurvalt can also be used instead of localhost
		self.__make_data_frame(data.text,make_all_data)
		
	#Make dataframe from text and 
	def __make_data_frame(self,txt,make_all_data):
		
		#Dictionary to make dataframe from text
		Dict={}
		
		for line in txt.splitlines():
			if line[0]!='#' and line[:25]!="engine_daemon_engine_info":		
				sp=line.find(" ")
				try:
					Dict[line[:sp]]=float(line[sp+1:])
				except:
					print("metrices text file could not be converted to dictionary\nCheck data_management.py make_data_frame function.")
					return
				
		#Making dataframe from dictionary
		df=pd.DataFrame([Dict])
		df.to_csv("data/current.csv",index=False)
		
		#Saving in snapshot folder
		current_time=time.strftime("%d %b %Y %H:%M:%S",time.localtime())
		df.to_csv("data/snapshots/"+current_time+".csv",index=False)
		
		#Updating current and all_data csv files
		if(make_all_data==True):
			df.to_csv("data/all_data.csv")
			self.all_data=df
			print("Made dataset")
		else:
			self.__update_data(df)
	
	#Update all data_csv
	def __update_data(self,curr):
		frames=[self.all_data,curr]
		try:
			self.all_data=pd.concat(frames,sort=True)
		except:
			print("Update data frame failed.\nCurrent data frame is not of the shape/format as the previous ones.\nCheck __update_data function in data_management.py")
			return
		self.all_data.to_csv("data/all_data.csv",index=False)
		
	#Clear data folder to store fresh data	
	def __setup_data_folder(self):
		os.system('rm -r data')
		os.system('mkdir data')
		os.system('mkdir data/snapshots')
		

		
#Inititialization of Data Management System
if __name__ == "__main__":
	c_dataframe_obj=data_management(int(sys.argv[1]),int(sys.argv[2]))#time update data base is send by the main.py 
else:
	print("Data Management System could not be initialized\nPlease check data_management.py")
	
	
	
	
	
#inside make data
'''
for line in txt[:6614].splitlines():
			if(line[0]!='#'):
				sp=line.find(" ")
				Dict[line[:sp]]=float(line[sp+1:])

		for line in txt[7006:].splitlines():
			if(line[0]!='#'):
				sp=line.find(" ")
				Dict[line[:sp]]=float(line[sp+1:])


'''
	
	
	
	
	
	
	
	