import os
from include.bounds import bounds
from include.test_case_running import run_all_tests

class Main:
	def __init__(self):
		refresh_time=2#change it later
		number_of_loops=10#change it later
		os.system("gnome-terminal -- python include/data_management.py "+str(refresh_time)+" "+str(number_of_loops))
		
		tests_obj=run_all_tests(refresh_time)
		bounds_obj=bounds()
		bounds_obj.store()	

if __name__ == "__main__": 
    obj=Main()
else:
	print("Something is wrong, please check main.py")

		#os.system("gnome-terminal -- python include/test_case_running.py "+str(refresh_time))==0
		#if(os.system("gnome-terminal -- python include/test_case_running.py "+str(refresh_time))==0):
		#	os.system("gnome-terminal -- python include/bounds.py")