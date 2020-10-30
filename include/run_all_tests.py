#Python module to run all test cases

import os
import time
import sys

from include.container_management import container_management

#These should always run in serial order never in parallel
def run_all_tests(sleep_time):
	print("Running all test cases")
	container_obj=container_management()
	
	sleep_time=2*sleep_time
	all_tests=os.listdir("test_cases")
	for test_case_name in all_tests:
		print("Running test case "+test_case_name)
		container_obj.run_test_case(test_case_name,"test_cases/"+test_case_name)
		time.sleep(sleep_time)
	
	
'''
if __name__ == "__main__":
	run_all_tests(int(sys.argv[1]))
else:
	print("Test cases running could not be initialized\nPlease check test_case_running.py")		
'''
	
	
'''
	all_tests=os.listdir("test_cases")
	for test in all_tests:
		#Check matrices during execution of each test cases
		#latter change it to run for all types of files
		print(test)
		
		print("Running test case "+test)
		if os.system("python test_cases/"+test)==0:
			print("Test case ran succesfully")
		else:
			print("Test case did not run succesfully")
			
		time.sleep(sleep_time)
		'''
