#Python module to update dataframe "all_data.csv" to store all the data
import pandas as pd

def func():
	all_data=pd.read_csv("data/all_data.csv")
	current=pd.read_csv("data/current.csv")
	
	frames=[all_data,current]
	result=pd.concat(frames)
	result.to_csv("data/all_data.csv",index=False)
	print(result.shape)
	
	return
	print(all_data.shape)
	all_data.append(current,ignore_index = True,sort=True)
	print(all_data.shape)
	all_data.to_csv("data/all_data.csv",index=False)
	
	print(current.shape)
	
func()