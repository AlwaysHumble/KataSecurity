import os
#from include.bounds import all_bounds
from include.run_all_tests import run_all_tests
from include.bounds import bounds
from include.container_data_management import all_container_data_management 
from include.docker_data_management import docker_data_management
import gc
import time
import multiprocessing


class Main:
	
	#Default is set for testing phase
	def __init__(self,production_version=False):
		
		self.__production_version=production_version
		self.__setup_env()
		self.__refresh_time=2#change it later
		self.__number_of_loops=180#change it later
		
		
		#Creating processes
		if(production_version):
			print("Running in production version.")
			print("All the logs of running process can be found in proc folder.")
			
			#Running data management system
			docker_data_management_process=multiprocessing.Process(target=self.__run_systems,args=("docker_data_management.py","proc/system/docker_data_management_output.txt",True),)
			docker_data_management_process.start()
			container_data_management_process=multiprocessing.Process(target=self.__run_systems,args=("container_data_management.py","proc/system/container_data_management_output.txt",False),)
			container_data_management_process.start()
			
			#Wating for data management systems to get started
			time.sleep(self.__refresh_time)
			#Running all tests
			run_all_tests(self.__refresh_time)
			#if(self.__production_version):
			time.sleep(self.__refresh_time)
			print("Stopping docker management process")
			docker_data_management_process.terminate()
			print("Stopping container management process")
			container_data_management_process.terminate()

		#Testing
		else:
			print("Running in testing version")
			
			#Running data management system
			os.system("gnome-terminal -- python include/docker_data_management.py "+str(self.__refresh_time)+" "+str(self.__number_of_loops))
			os.system("gnome-terminal -- python include/container_data_management.py "+str(self.__refresh_time)+" "+str(self.__number_of_loops))
			
			#Wating for data management systems to get started
			time.sleep(self.__refresh_time)
			#Running all tests
			run_all_tests(self.__refresh_time)
		
		
		obj=bounds()
			
	def __del__(self):		
		print("Thank you.")
		gc.collect()
		
	def __run_systems(self,file_location,output_location,fl):
		#print("Started "+file_location[:len(file_location)-3])
		
		os.system("python include/"+file_location+" "+str(self.__refresh_time)+" "+str(self.__number_of_loops)+" > "+output_location)
		#print("Stopped "+file_location[:len(file_location)-3])
		#return
		#if(fl):
		#	docker_management_obj=docker_data_management(self.__refresh_time,self.__number_of_loops)
		#else:
		#	container_management_obj=all_container_data_management(self.__refresh_time,self.__number_of_loops)
		
	#General folder for all applications
	def __setup_env(self):
		
		os.system("clear")
		os.system("rm -rf include/__pycache__")
		
		print("Welcome to container_securer")
		
		#For data management
		os.system('rm -rf data')
		os.system('mkdir data')
		
		#For temperary variables and their output
		os.system("rm -rf proc")
		os.system("mkdir proc")
		
		#For storing data of output of each terminal
		os.system("mkdir proc/system")
		
		#Juggad to make sure length 
		#cont_mng_obj=container_management()
		#_=cont_mng_obj.run_container("temp")
		#cont_mng_obj.remove_container("temp")

if __name__ == "__main__": 
	production_version=True
	obj=Main(production_version)
else:
	print("Something is wrong, please check main.py")
