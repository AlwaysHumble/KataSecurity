import os
import subprocess
import time

class container_management:

	def __init__(self):
		print("Running container management")
		self.__docker_current_location="home"
		#os.system("mkdir proc/containers")
		
	#Detach the container after running it
	def run_container(self,container_name="Default",args="-d -it ubuntu"):
		if container_name=="Default":
			os.system("docker run "+args)
		else:	
			os.system("docker run --name "+container_name+" "+args)
		
		return container_name

	#It will also help to shift folder		
	def add_filein_container(self,container_name,host_file_address,target_file_address):
		os.system("docker cp "+host_file_address+" "+container_name+":/"+target_file_address)
		
	#It will also help to shift folder
	def get_filefrom_container(self,container_name,host_file_address,target_file_address):
		os.system("docker cp "+container_name+":/"+host_file_address+" "+target_file_address)

	def exec_commandin_container(self,container_name,command):
		os.system("docker exec -u 0 -it "+container_name+" "+command+" > proc/containers/"+container_name+"_output.txt")

	#For stopping and removing a container
	#container id can also passed in place of container name
	def remove_container(self,container_name):
		os.system("docker stop "+container_name)
		os.system("docker rm "+container_name)

	def run_test_case(self,test_case_name,path_to_test_case):
        
		#Starting container
		container_name="Test_"+test_case_name
		self.run_container(container_name)
		
		#Adding folder with all tests
		self.add_filein_container(container_name,path_to_test_case,"home/")
        
		output_file_name=test_case_name+"_output.txt"
		
		#Running test case
		command="bash home/"+test_case_name+"/run.sh"
		self.exec_commandin_container(container_name,command)
        
		#deleting the container
		self.remove_container(container_name)
		