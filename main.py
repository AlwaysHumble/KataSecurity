import os
import subprocess
from include.containers import Container
from include.bounds import bounds
from include.test_case_running import run_all_tests

class Main:
	def __init__(self):
		self.refresh_time=2# change it later
		self.number_of_loops=10 #change it later
	def run_tests(self):
		#os.system("gnome-terminal -- python include/data_management.py "+str(refresh_time)+" "+str(number_of_loops))
		tests_obj=run_all_tests(self.refresh_time)
		bounds_obj=bounds()
		bounds_obj.store()
		test_container = Container()
		test_container.initial_test()	

if __name__ == "__main__":
	obj = Main()
	obj.run_tests()
else:
	print("Something is wrong, please check main.py")

		#os.system("gnome-terminal -- python include/test_case_running.py "+str(refresh_time))==0
		#if(os.system("gnome-terminal -- python include/test_case_running.py "+str(refresh_time))==0):
		#	os.system("gnome-terminal -- python include/bounds.py")