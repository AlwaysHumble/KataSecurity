#updates are almost every second
#Notes: There containers are in stack configuration. The first container is the one which has been started last. 
#While dealing with variables with multiple sub attributes, one solutions is to fix those attributes, if they are there, than add in the dataframe else keep them NULL


'''

To be ommitted

read->use python time instead
preread->no idea what it is
name->has a seperate function
id->has a seperate function

The major blocks to be converted to dataframe

pid_stats
blkio_stats
num_procs
storage_stats
cpu_stats
precpu_stats
memory_stats
networks
'''

#Dict used to make dataframe
Dict={}

def get_container_name(txt):
	name_ind_start=txt.find("name")
	#+8 is used to skip to the starting part of the container name
	#-1 is to reach till the index before comma(',')
	return txt[name_ind_start+8:txt.find(',',name_ind_start)-1]
	
def get_container_id(txt):
	#id is also present in pid, so starting after 100 helps to skip it and help to each the id of container
	id_ind_start=txt.find("id",100)
	#+5 is used to skip to the starting part of the container id
	#-1 is to reach till the index before comma(',')
	return txt[id_ind_start+5:txt.find(',',id_ind_start)-1]


def nums_only(val):
	ans=0
	for x in val:
		if(x>='0' and x<='9'):
			ans=ans*10+int(x)
	return ans
			
def get_num(txt,val,shift):
	
	ind=txt.find("\""+val+"\"",shift)
	if(ind==-1):
		return "NULL"
	else:
		end_ind=min(txt.find(",",ind),txt.find("}",ind))
		return nums_only(txt[ind+len(val)+3:end_ind])
	

def func(txt):
	
	shift=0
	Dict["pids_stats"]=get_num(txt,"pids_stats",shift)
	
	shift=txt.find("io_service_bytes_recursive")+len("io_service_bytes_recursive")
	Dict["blkio_stats__io_service_bytes_recursive"]=get_num(txt,"Total",shift)
	
	shift=txt.find("io_serviced_recursive")+len("io_serviced_recursive")
	Dict["blkio_stats__io_serviced_recursive"]=get_num(txt,"Total",shift)
	
	shift=txt.find("io_queue_recursive")+len("io_queue_recursive")
	Dict["blkio_stats__io_queue_recursive"]=get_num(txt,"Total",shift)
	
	shift=txt.find("io_service_time_recursive")+len("io_service_time_recursive")
	Dict["blkio_stats__io_service_time_recursive"]=get_num(txt,"Total",shift)
	
	shift=txt.find("io_wait_time_recursive")+len("io_wait_time_recursive")
	Dict["blkio_stats__io_wait_time_recursive"]=get_num(txt,"Total",shift)
	
	shift=txt.find("io_merged_recursive")+len("io_merged_recursive")
	Dict["blkio_stats__io_merged_recursive"]=get_num(txt,"Total",shift)
	
	shift=txt.find("io_time_recursive")+len("io_time_recursive")
	Dict["blkio_stats__io_service_time_recursive"]=get_num(txt,"value",shift)
	
	shift=txt.find("sectors_recursive")+len("sectors_recursive")
	Dict["blkio_stats__sectors_recursive"]=get_num(txt,"value",shift)
	
	Dict["num_procs"]=get_num(txt,"num_procs",shift)
	
	shift=txt.find("cpu_stats")+len("cpu_stats")
	Dict["cpu_total_usage"]=get_num(txt,"total_usage",shift)
	Dict["cpu_usage_in_kernelmode"]=get_num(txt,"usage_in_kernelmode",shift)
	Dict["cpu_usage_in_usermode"]=get_num(txt,"usage_in_usermode",shift)
	Dict["system_cpu_usage"]=get_num(txt,"system_cpu_usage",shift)
	Dict["online_cpus"]=get_num(txt,"online_cpus",shift)
	Dict["cpu_periods"]=get_num(txt,"periods",shift)
	Dict["cpu_throttled_periods"]=get_num(txt,"throttled_periods",shift)
	Dict["cpu_throttled_time"]=get_num(txt,"throttled_time",shift)
	
	shift=txt.find("precpu_stats")+len("precpu_stats")
	Dict["precpu_total_usage"]=get_num(txt,"total_usage",shift)
	Dict["precpu_usage_in_kernelmode"]=get_num(txt,"usage_in_kernelmode",shift)
	Dict["precpu_usage_in_usermode"]=get_num(txt,"usage_in_usermode",shift)
	Dict["cpu_system_cpu_usage"]=get_num(txt,"system_cpu_usage",shift)
	Dict["precpu_periods"]=get_num(txt,"periods",shift)
	Dict["precpu_throttled_periods"]=get_num(txt,"throttled_periods",shift)
	Dict["precpu_throttled_time"]=get_num(txt,"throttled_time",shift)
	
	shift=txt.find("memory_stats")+len("memory_stats")
	Dict["memory_usage"]=get_num(txt,"usage",shift)
	Dict["memory_max_usage"]=get_num(txt,"max_usage",shift)
	Dict["memory_active_anon"]=get_num(txt,"active_anon",shift)
	Dict["memory_active_file"]=get_num(txt,"active_file",shift)
	Dict["memory_cache"]=get_num(txt,"cache",shift)
	Dict["memory_dirty"]=get_num(txt,"dirty",shift)
	Dict["memory_hierarchical_memory_limit"]=get_num(txt,"hierarchical_memory_limit",shift)
	Dict["memory_hierarchical_memsw_limit"]=get_num(txt,"hierarchical_memsw_limit",shift)
	Dict["memory_inactive_anon"]=get_num(txt,"inactive_anon",shift)
	Dict["memory_inactive_file"]=get_num(txt,"inactive_file",shift)
	Dict["memory_mapped_file"]=get_num(txt,"mapped_file",shift)
	Dict["memory_pgfault"]=get_num(txt,"pgfault",shift)
	Dict["memory_pgmajfault"]=get_num(txt,"pgmajfault",shift)
	Dict["memory_pgpgin"]=get_num(txt,"pgpgin",shift)
	Dict["memory_pgpgout"]=get_num(txt,"pgpgout",shift)
	Dict["memory_rss"]=get_num(txt,"rss",shift)
	Dict["memory_rss_huge"]=get_num(txt,"rss_huge",shift)
	Dict["memory_total_active_anon"]=get_num(txt,"total_active_anon",shift)
	Dict["memory_total_active_file"]=get_num(txt,"total_active_file",shift)
	Dict["memory_total_cache"]=get_num(txt,"total_cache",shift)
	Dict["memory_total_dirty"]=get_num(txt,"total_dirty",shift)
	Dict["memory_total_inactive_anon"]=get_num(txt,"total_inactive_anon",shift)
	Dict["memory_total_inactive_file"]=get_num(txt,"total_inactive_file",shift)
	Dict["memory_total_mapped_file"]=get_num(txt,"total_mapped_file",shift)
	Dict["memory_total_pgfault"]=get_num(txt,"total_pgfault",shift)
	Dict["memory_total_pgmajfault"]=get_num(txt,"total_pgmajfault",shift)
	Dict["memory_total_pgpgin"]=get_num(txt,"total_pgpgin",shift)
	Dict["memory_total_pgpgout"]=get_num(txt,"total_pgpgout",shift)
	Dict["memory_total_rss"]=get_num(txt,"total_rss",shift)
	Dict["memory_total_rss_huge"]=get_num(txt,"total_rss_huge",shift)
	Dict["memory_total_unevictable"]=get_num(txt,"total_unevictable",shift)
	Dict["memory_total_writeback"]=get_num(txt,"total_writeback",shift)
	Dict["memory_unevictable"]=get_num(txt,"unevictable",shift)
	Dict["memory_writeback"]=get_num(txt,"writeback",shift)
	Dict["memory_limit"]=get_num(txt,"limit",shift)
	
	Dict["name"]=get_container_name(txt)
	Dict["id"]=get_container_id(txt)
	
	shift=txt.find("networks")+len("networks")
	Dict["networks_rx_bytes"]=get_num(txt,"rx_bytes",shift)
	Dict["networks_rx_packets"]=get_num(txt,"rx_packets",shift)
	Dict["networks_rx_errors"]=get_num(txt,"rx_errors",shift)
	Dict["networks_rx_dropped"]=get_num(txt,"rx_dropped",shift)
	Dict["networks_tx_bytes"]=get_num(txt,"tx_bytes",shift)
	Dict["networks_tx_packets"]=get_num(txt,"tx_packets",shift)
	Dict["networks_tx_errors"]=get_num(txt,"tx_errors",shift)
	Dict["networks_tx_dropped"]=get_num(txt,"tx_dropped",shift)	
	
	
	return Dict["id"]







import docker
client = docker.from_env()

#only gets running containers
l=client.containers.list()
cnt1=l[0]

for x in cnt1.stats():
	print(func(x.decode()))
	break
	
	
	

	
'''
Code dump

#Issue is what if there is no data in curley bracket
	
	#Get pids_stats
	#11 to skip first colon
	pid_stats_ind=txt.find("pids_stats")+12
	col_ind=txt.find(":",pid_stats_ind)+1
	Dict["pid_stats"]=int(txt[col_ind:txt.find("}",col_ind)])
	
	
Number of variables must not change to form proper csv file
#Find method to get attributes seperated by comma and recursively call functions to extract the attributes ins
def dict_attributes(key,s):
	
	if(s=="NULL"):
		return	
	
	#Take care of commas
	if(s.find(",")==-1):
		col_ind=s.find(":")
		if(s[0]=='"'):
			Dict[key+s[1:col_ind-1]]=s[col_ind+1:]
		else:
			Dict[key+s[:col_ind]]=s[col_ind+1:]
	else:
		dict_attributes(key,s[:s.find(",")])
		
	

def get_nested_data(txt,val):
	#2 to cover ":
	val_ind=txt.find(val)+len(val)+2
	comma_ind=txt.find(",",val_ind)
	brac_ind=txt.find("}",val_ind)
	
	if(brac_ind==val_ind+1):
		"NULL"	
	else if(comma_ind!=-1 and comma_ind<brac_ind):
		dict_attributes(val,txt[val_ind:comma_ind])		
	else:
		dict_attributes(val,txt[val_ind:brac_ind])
		
	
	
	if(txt[val_ind+1]=='}'):
		return "NULL"#change it to none
	else:
		return txt[val_ind:txt.find("}",val_ind)]

def func(txt):
	txt="{\"first\":1,\"second\":2,\"third\":3}"

	dict_attributes(get_nested_data(txt,"pids_stats"))
	
	
	return Dict
	
	
	#blk_ind=txt.find("blkio_stats")


def get_container_name(txt):
	name_ind_start=txt.find("name")
	#+8 is used to skip to the starting part of the container name
	#-1 is to reach till the index before comma(',')
	return txt[name_ind_start+8:txt.find(',',name_ind_start)-1]
	
def get_container_id(txt):
	#id is also present in pid, so starting after 100 helps to skip it and help to each the id of container
	id_ind_start=txt.find("id",100)
	#+5 is used to skip to the starting part of the container id
	#-1 is to reach till the index before comma(',')
	return txt[id_ind_start+5:txt.find(',',id_ind_start)-1]



'''
	