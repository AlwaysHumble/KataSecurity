#This module contains methods for data management for each individual container

import pandas as pd
import os
import docker
import time
import multiprocessing
import sys

		
class one_container_data_management:
	
	
	def __init__(self,container_object):
		self.__Dict={}
		self.__make_dictionary(container_object)
		#Used to define if the database is made for the first time
		made_database=self.__setup_data_folder(self.get_attribute_value("name"))
		self.__make_dataframe(made_database)
		
	def get_attribute_value(self,attribute):	
		return self.__Dict[attribute]	
	
	
	#Wrtting in dataframe functions
	#Rewritten part same as in docker_data_management
	def __make_dataframe(self,make_all_data):
		df=pd.DataFrame([self.__Dict])
		df.to_csv("data/all_containers/"+self.get_attribute_value("name")+"/current_container.csv",index=False)
		
		#Saving in snapshot folder
		current_time=time.strftime("%d %b %Y %H:%M:%S",time.localtime())
		df.to_csv("data/all_containers/"+self.get_attribute_value("name")+"/snapshots/"+str(current_time)+".csv",index=False)
		
		#Updating current and all_data csv files
		if(make_all_data==True):
			df.to_csv("data/all_containers/"+self.get_attribute_value("name")+"/all_data_container.csv")
			self.all_data=df
			print("Made dataset of "+self.get_attribute_value("name"))
		else:
			self.__update_data(df)
	
	#Rewritten part same as in docker_data_management
	def __update_data(self,curr):
		
		all_data=pd.read_csv("data/all_containers/"+self.get_attribute_value("name")+"/all_data_container.csv")
		frames=[all_data,curr]
		try:
			self.all_data=pd.concat(frames,sort=True)
		except:
			print("Update data frame failed.\nCurrent data frame is not of the shape/format as the previous ones.\nCheck __update_data function in container_data_management.py")
			return
		
		self.all_data.to_csv("data/all_containers/"+self.__Dict["name"]+"/all_data_container.csv",index=False)
		
	#Rewritten part same as in docker_data_management
	def __setup_data_folder(self,container_name):
		if not os.path.isdir("data/all_containers/"+container_name):
			os.system('mkdir data/all_containers/'+container_name)
			os.system('mkdir data/all_containers/'+container_name+'/snapshots')
			return True
		else:
			return False
	
	
	#Making Dictionary functions
	
	def __get_container_name(self,txt):
		name_ind_start=txt.find("name")
		#+8 is used to skip to the starting part of the container name
		#-1 is to reach till the index before comma(',')
		return txt[name_ind_start+8:txt.find(',',name_ind_start)-1]
	
	def __get_container_id(self,txt):
		#id is also present in pid, so starting after 100 helps to skip it and help to each the id of container
		id_ind_start=txt.find("id",100)
		#+5 is used to skip to the starting part of the container id
		#-1 is to reach till the index before comma(',')
		return txt[id_ind_start+5:txt.find(',',id_ind_start)-1]
	
	def __nums_only(self,val):
		ans=0
		for x in val:
			if(x>='0' and x<='9'):
				ans=ans*10+int(x)
		return ans
			
	def __get_num(self,txt,val,shift):

		ind=txt.find("\""+val+"\"",shift)
		if(ind==-1):
			return "NULL"
		else:
			end_ind=min(txt.find(",",ind),txt.find("}",ind))
			return self.__nums_only(txt[ind+len(val)+3:end_ind])


	def __make_dictionary(self,container_object):
		
		txt=""
		#To get the latest stats
		for x in container_object.stats():
			txt=x.decode()
			break
			
		#All the attributes are hardcoded to ensure the size of dataframe remains the same
		shift=0
		self.__Dict["pids_stats"]=self.__get_num(txt,"pids_stats",shift)

		shift=txt.find("io_service_bytes_recursive")+len("io_service_bytes_recursive")
		self.__Dict["blkio_stats__io_service_bytes_recursive"]=self.__get_num(txt,"Total",shift)

		shift=txt.find("io_serviced_recursive")+len("io_serviced_recursive")
		self.__Dict["blkio_stats__io_serviced_recursive"]=self.__get_num(txt,"Total",shift)

		shift=txt.find("io_queue_recursive")+len("io_queue_recursive")
		self.__Dict["blkio_stats__io_queue_recursive"]=self.__get_num(txt,"Total",shift)

		shift=txt.find("io_service_time_recursive")+len("io_service_time_recursive")
		self.__Dict["blkio_stats__io_service_time_recursive"]=self.__get_num(txt,"Total",shift)

		shift=txt.find("io_wait_time_recursive")+len("io_wait_time_recursive")
		self.__Dict["blkio_stats__io_wait_time_recursive"]=self.__get_num(txt,"Total",shift)

		shift=txt.find("io_merged_recursive")+len("io_merged_recursive")
		self.__Dict["blkio_stats__io_merged_recursive"]=self.__get_num(txt,"Total",shift)

		shift=txt.find("io_time_recursive")+len("io_time_recursive")
		self.__Dict["blkio_stats__io_service_time_recursive"]=self.__get_num(txt,"value",shift)

		shift=txt.find("sectors_recursive")+len("sectors_recursive")
		self.__Dict["blkio_stats__sectors_recursive"]=self.__get_num(txt,"value",shift)

		self.__Dict["num_procs"]=self.__get_num(txt,"num_procs",shift)

		shift=txt.find("cpu_stats")+len("cpu_stats")
		self.__Dict["cpu_total_usage"]=self.__get_num(txt,"total_usage",shift)
		self.__Dict["cpu_usage_in_kernelmode"]=self.__get_num(txt,"usage_in_kernelmode",shift)
		self.__Dict["cpu_usage_in_usermode"]=self.__get_num(txt,"usage_in_usermode",shift)
		self.__Dict["system_cpu_usage"]=self.__get_num(txt,"system_cpu_usage",shift)
		self.__Dict["online_cpus"]=self.__get_num(txt,"online_cpus",shift)
		self.__Dict["cpu_periods"]=self.__get_num(txt,"periods",shift)
		self.__Dict["cpu_throttled_periods"]=self.__get_num(txt,"throttled_periods",shift)
		self.__Dict["cpu_throttled_time"]=self.__get_num(txt,"throttled_time",shift)

		shift=txt.find("precpu_stats")+len("precpu_stats")
		self.__Dict["precpu_total_usage"]=self.__get_num(txt,"total_usage",shift)
		self.__Dict["precpu_usage_in_kernelmode"]=self.__get_num(txt,"usage_in_kernelmode",shift)
		self.__Dict["precpu_usage_in_usermode"]=self.__get_num(txt,"usage_in_usermode",shift)
		self.__Dict["cpu_system_cpu_usage"]=self.__get_num(txt,"system_cpu_usage",shift)
		self.__Dict["precpu_periods"]=self.__get_num(txt,"periods",shift)
		self.__Dict["precpu_throttled_periods"]=self.__get_num(txt,"throttled_periods",shift)
		self.__Dict["precpu_throttled_time"]=self.__get_num(txt,"throttled_time",shift)

		shift=txt.find("memory_stats")+len("memory_stats")
		self.__Dict["memory_usage"]=self.__get_num(txt,"usage",shift)
		self.__Dict["memory_max_usage"]=self.__get_num(txt,"max_usage",shift)
		self.__Dict["memory_active_anon"]=self.__get_num(txt,"active_anon",shift)
		self.__Dict["memory_active_file"]=self.__get_num(txt,"active_file",shift)
		self.__Dict["memory_cache"]=self.__get_num(txt,"cache",shift)
		self.__Dict["memory_dirty"]=self.__get_num(txt,"dirty",shift)
		self.__Dict["memory_hierarchical_memory_limit"]=self.__get_num(txt,"hierarchical_memory_limit",shift)
		self.__Dict["memory_hierarchical_memsw_limit"]=self.__get_num(txt,"hierarchical_memsw_limit",shift)
		self.__Dict["memory_inactive_anon"]=self.__get_num(txt,"inactive_anon",shift)
		self.__Dict["memory_inactive_file"]=self.__get_num(txt,"inactive_file",shift)
		self.__Dict["memory_mapped_file"]=self.__get_num(txt,"mapped_file",shift)
		self.__Dict["memory_pgfault"]=self.__get_num(txt,"pgfault",shift)
		self.__Dict["memory_pgmajfault"]=self.__get_num(txt,"pgmajfault",shift)
		self.__Dict["memory_pgpgin"]=self.__get_num(txt,"pgpgin",shift)
		self.__Dict["memory_pgpgout"]=self.__get_num(txt,"pgpgout",shift)
		self.__Dict["memory_rss"]=self.__get_num(txt,"rss",shift)
		self.__Dict["memory_rss_huge"]=self.__get_num(txt,"rss_huge",shift)
		self.__Dict["memory_total_active_anon"]=self.__get_num(txt,"total_active_anon",shift)
		self.__Dict["memory_total_active_file"]=self.__get_num(txt,"total_active_file",shift)
		self.__Dict["memory_total_cache"]=self.__get_num(txt,"total_cache",shift)
		self.__Dict["memory_total_dirty"]=self.__get_num(txt,"total_dirty",shift)
		self.__Dict["memory_total_inactive_anon"]=self.__get_num(txt,"total_inactive_anon",shift)
		self.__Dict["memory_total_inactive_file"]=self.__get_num(txt,"total_inactive_file",shift)
		self.__Dict["memory_total_mapped_file"]=self.__get_num(txt,"total_mapped_file",shift)
		self.__Dict["memory_total_pgfault"]=self.__get_num(txt,"total_pgfault",shift)
		self.__Dict["memory_total_pgmajfault"]=self.__get_num(txt,"total_pgmajfault",shift)
		self.__Dict["memory_total_pgpgin"]=self.__get_num(txt,"total_pgpgin",shift)
		self.__Dict["memory_total_pgpgout"]=self.__get_num(txt,"total_pgpgout",shift)
		self.__Dict["memory_total_rss"]=self.__get_num(txt,"total_rss",shift)
		self.__Dict["memory_total_rss_huge"]=self.__get_num(txt,"total_rss_huge",shift)
		self.__Dict["memory_total_unevictable"]=self.__get_num(txt,"total_unevictable",shift)
		self.__Dict["memory_total_writeback"]=self.__get_num(txt,"total_writeback",shift)
		self.__Dict["memory_unevictable"]=self.__get_num(txt,"unevictable",shift)
		self.__Dict["memory_writeback"]=self.__get_num(txt,"writeback",shift)
		self.__Dict["memory_limit"]=self.__get_num(txt,"limit",shift)

		self.__Dict["name"]=self.__get_container_name(txt)
		self.__Dict["id"]=self.__get_container_id(txt)

		shift=txt.find("networks")+len("networks")
		self.__Dict["networks_rx_bytes"]=self.__get_num(txt,"rx_bytes",shift)
		self.__Dict["networks_rx_packets"]=self.__get_num(txt,"rx_packets",shift)
		self.__Dict["networks_rx_errors"]=self.__get_num(txt,"rx_errors",shift)
		self.__Dict["networks_rx_dropped"]=self.__get_num(txt,"rx_dropped",shift)
		self.__Dict["networks_tx_bytes"]=self.__get_num(txt,"tx_bytes",shift)
		self.__Dict["networks_tx_packets"]=self.__get_num(txt,"tx_packets",shift)
		self.__Dict["networks_tx_errors"]=self.__get_num(txt,"tx_errors",shift)
		self.__Dict["networks_tx_dropped"]=self.__get_num(txt,"tx_dropped",shift)	


class all_container_data_management:
	
	def __init__(self,sleep_time,number_of_iterations):
		print("Container Data management started")
		os.system('mkdir data/all_containers')
		self.client=docker.from_env()

		#only gets running containers
		for cnt in range(1,number_of_iterations):#To be run for infinite time later
			self.__update_all_container_matrices()
			print("All containers Dataset updated %s times "%cnt)
			time.sleep(sleep_time)

		
	def __update_all_container_matrices(self):
		list_of_all_containers=self.client.containers.list()
		
		if(len(list_of_all_containers)==0):
			print("There are no containers running currently")
			return
		
		for one_container in list_of_all_containers:
			temp=multiprocessing.Process(target=one_container_data_management,args=(one_container,))
			temp.start()
			temp.join()
			

#Inititialization of Docker Data Management System
if __name__ == "__main__":
	c_dataframe_obj=all_container_data_management(int(sys.argv[1]),int(sys.argv[2]))#time update data base is send by the main.py 
else:
	print("Container Data Management System could not be initialized\nPlease check container_data_management.py")
	
	
	
	
