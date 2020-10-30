import os
from include.bounds import bounds
from include.run_all_tests import run_all_tests
from include.container_management import container_management
#import multiprocessing

class Main:
	def __init__(self):
		
		self.__setup_env()
		refresh_time=2#change it later
		number_of_loops=100#change it later
		
		os.system("gnome-terminal -- python include/docker_data_management.py "+str(refresh_time)+" "+str(number_of_loops))
		os.system("gnome-terminal -- python include/container_data_management.py "+str(refresh_time)+" "+str(number_of_loops))
		
		run_all_tests(refresh_time)
		
	#General folder for all applications
	def __setup_env(self):
		#For data management
		os.system('rm -r data')
		os.system('mkdir data')
		
		#For temperary variables and their output
		os.system("rm -r proc")
		os.system("mkdir proc")

if __name__ == "__main__": 
    obj=Main()
else:
	print("Something is wrong, please check main.py")

		#os.system("gnome-terminal -- python include/test_case_running.py "+str(refresh_time))==0
		#if(os.system("gnome-terminal -- python include/test_case_running.py "+str(refresh_time))==0):
		#	os.system("gnome-terminal -- python include/bounds.py")