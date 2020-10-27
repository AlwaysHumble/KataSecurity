import os
import subprocess

MAIN_PATH = "/home/karan/KataSecurity"
PYTHON_VERSION = "python3.8"
TEST_CASES_PATH = r"/home/karan/KataSecurity/test_cases"
NUMBER_OF_CONTAINERS = len(os.listdir(TEST_CASES_PATH))

class Container:

    def __init__(self):
        self.testcaseslist = []
        self.containersmade = 0

    def get_test_cases(self):
        self.testcaseslist = os.listdir(TEST_CASES_PATH)
        

    def make_containers(self):
        self.get_test_cases()
        for i in range(NUMBER_OF_CONTAINERS):
            container_name = "Container_"+str(i+1)
            test_case_name = self.testcaseslist[i]
            testpath = "/home/karan/KataSecurity/test_cases/"+test_case_name
            subprocess.call(["bash","/home/karan/KataSecurity/include/ShellScripts/make_containers.sh",container_name,test_case_name],shell=False)
            
        self.containersmade = 1

    def test_containers(self):
        if(self.containersmade):
            for i in range(NUMBER_OF_CONTAINERS):
                container_name = "Container_"+str(i+1)
                test_case_name = self.testcaseslist[i]
                subprocess.call(["bash","/home/karan/KataSecurity/include/ShellScripts/test_scripts.sh",container_name,test_case_name],shell=False)

    def remove_containers(self):
        if(self.containersmade):
            for i in range(NUMBER_OF_CONTAINERS):
                container_name = "Container_"+str(i+1)
                subprocess.call(["bash","/home/karan/KataSecurity/include/ShellScripts/remove_containers.sh",container_name],shell=False)
        self.containersmade = 0

    def initial_test(self):
        self.make_containers()
        self.test_containers()
        self.remove_containers()

if __name__=="__main__":
    container = Container()
    container.initial_test()
