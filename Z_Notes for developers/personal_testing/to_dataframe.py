#Python module to get data from a specific port
import requests
import pandas as pd

def func(txt):
	dc={}
	cnt=0
	for line in txt.splitlines():
		if line[0]!='#' and line[:25]!="engine_daemon_engine_info" and line[:21]!="engine_daemon_network" and line[:19]!="http_requests_total":			
			sp=line.find(" ")
			try:
				dc[line[:sp]]=float(line[sp+1:])
			except:
				print("metrices text file could not be converted to dictionary\nCheck data_management.py make_data_frame function.")
			cnt=cnt+1		
		#print(cnt)
		#cnt=cnt+1
	
	print(len(dc))
	'''
	file=open("len_more_3.txt",'wt')
	file.write(str(dc)) 
	file.close() 
	'''
	#df=pd.DataFrame([dc])
	#df.to_csv("data/current.csv",index=False)
	
#get datafrom local host
data=requests.get("http://localhost:9323/metrics")#apurvalt can also be used instead of local
func(data.text)#to get all the data in the file
