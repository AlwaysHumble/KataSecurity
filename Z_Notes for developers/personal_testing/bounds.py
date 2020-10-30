import os

#These should always run in serial order never in parallel
def run_all_tests():
	all_tests=os.listdir("test_cases")
	for test in all_tests:
		#Check matrices during execution of each test cases
		os.system("python test_cases/"+test)





