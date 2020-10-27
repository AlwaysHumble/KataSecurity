import os
import subprocess

class Container:

    def __init__(self):
        self.testcaseslist = []
        self.curr_dir = os.getcwd()
        #print(self.curr_dir)
        self.test_cases_path = self.curr_dir+"/test_cases"
        self.include_folder = self.curr_dir+"/include"
        self.shellscripts = self.include_folder+"/ShellScripts"
        self.container_make = self.shellscripts+"/make_containers.sh"
        self.container_test = self.shellscripts+"/test_scripts.sh"
        self.container_remove = self.shellscripts+"/remove_containers.sh"
        self.number_of_containers = len(os.listdir(self.test_cases_path))
        self.containersmade = 0

    def get_test_cases(self):
        self.testcaseslist = os.listdir(self.test_cases_path)
        
    def make_containers(self):
        self.get_test_cases()
        for i in range(self.number_of_containers):
            container_name = "Container_"+str(i+1)
            test_case_name = self.testcaseslist[i]
            subprocess.call(["bash",self.container_make,container_name,test_case_name],shell=False)
            
        self.containersmade = 1

    def test_containers(self):
        if(self.containersmade):
            for i in range(self.number_of_containers):
                container_name = "Container_"+str(i+1)
                test_case_name = self.testcaseslist[i]
                subprocess.call(["bash",self.container_test,container_name,test_case_name],shell=False)

    def remove_containers(self):
        if(self.containersmade):
            for i in range(self.number_of_containers):
                container_name = "Container_"+str(i+1)
                subprocess.call(["bash",self.container_remove,container_name],shell=False)
        self.containersmade = 0

    def initial_test(self):
        self.make_containers()
        self.test_containers()
        self.remove_containers()

if __name__=="__main__":
    container = Container()
    container.initial_test()
