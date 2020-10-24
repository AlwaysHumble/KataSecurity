#Python module to run all test cases

import os
import time
import sys

#These should always run in serial order never in parallel
def run_all_tests(sleep_time):
	print("Running all test cases")
	all_tests=os.listdir("test_cases")
	for test in all_tests:
		#Check matrices during execution of each test cases
		#latter change it to run for all types of files
		print("Running test case "+test)
		if os.system("python test_cases/"+test)==0:
			print("Test case ran succesfully")
		else:
			print("Test case did not run succesfully")
			
		time.sleep(sleep_time)
		#return
'''
if __name__ == "__main__":
	run_all_tests(int(sys.argv[1]))
else:
	print("Test cases running could not be initialized\nPlease check test_case_running.py")		
'''