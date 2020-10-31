import os
from include.bounds import bounds
from include.run_all_tests import run_all_tests
from include.container_management import container_management
from include.docker_data_management import docker_data_management
#import multiprocessing
import pandas as pd

PYTHON_VERSION = "python"


class Main:
	def __init__(self):
		
		self.__setup_env()
		refresh_time=2#change it later
		number_of_loops=50#change it later

		os.system("gnome-terminal -- "+PYTHON_VERSION+" include/docker_data_management.py "+str(refresh_time)+" "+str(number_of_loops))
		os.system("gnome-terminal -- "+PYTHON_VERSION+" include/container_data_management.py "+str(refresh_time)+" "+str(number_of_loops))
		run_all_tests(refresh_time)
		
	#General folder for all applications
	def __setup_env(self):
		#For data management
		#os.system('rm -r data')
		os.system('mkdir -p data')
		
		#For temperary variables and their output
		#os.system("rm -r proc")
		os.system("mkdir -p proc")

if __name__ == "__main__": 
    obj=Main()
    '''df1 = pd.read_csv('/home/karan/KataSecurity/data/docker/snapshots/31 Oct 2020 12:25:29.csv')
    df2 = pd.read_csv('/home/karan/KataSecurity/data/docker/current_docker.csv')
    print(df1.shape)
    print(df2.shape)
    os.system("sudo systemctl restart docker")
    dat = docker_data_management(1,1)
    print(dat.all_data.shape)
    print(list(set(df2.columns)-set(dat.all_data.columns)))
    print(list(set(dat.all_data.columns)-set(df2.columns)))
    print(list(set(df1.columns)-set(df2.columns)))'''
    




else:
	print("Something is wrong, please check main.py")

		#os.system("gnome-terminal -- python include/test_case_running.py "+str(refresh_time))==0
		#if(os.system("gnome-terminal -- python include/test_case_running.py "+str(refresh_time))==0):
		#	os.system("gnome-terminal -- python include/bounds.py")