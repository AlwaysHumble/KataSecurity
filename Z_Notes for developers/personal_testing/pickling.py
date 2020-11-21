#Importing non ML libraries
import os
import math
import pickle


#Importing ML Libraries
import pandas as pd
import torch
import torch.nn as nn
import torch.utils.data as data_utils
from torch import optim

import numpy as np
from sklearn.model_selection import train_test_split

def augmentaion(df):
	vertical=df.shape[0]
	horizontal=df.shape[1]
	
	if vertical<3 or horizontal<2:
		return NULL
	
	new_len=(vertical-1)*10
	
	new_df=pd.DataFrame(np.zeros([new_len,horizontal]),columns=list(df.columns))
	
	for ind in range(0,vertical-1):
		for col in range(len(df.columns)):
			prev=df.iloc[ind,col]
			nxt=df.iloc[ind+1,col]
			d=(nxt-prev)/10
			for i in range(10):
				new_df.iloc[(ind*10)+i,col]=df.iloc[ind,col]+(d*i)
				
	#print(new_df.head(50))
	return new_df

#Check if there is a need of add change in resource utilized rather than absolute on
def pre_processing(df):
	#Removing all columns with no values
	df=df.dropna(axis=1,how="all",inplace=False)
	
	#Removing name, id, pids_stats and first column which are not useful for running ML algorithms
	df=df.drop([df.columns[0],"name","id","pids_stats"],axis=1,inplace=False)

	#Removing all rows with NULL values
	df=df.dropna(axis="rows",inplace=False)
	
	#Removing first and last row as they are outliers and they are the stage where container is getting started or getting destroyed
	df=df.drop(df.head(1).index,axis="rows",inplace=False)
	df=df.drop(df.tail(1).index,axis="rows",inplace=False)
	
	for col in df.columns:
		df[col]=df[col].astype("float64")
	
	df=augmentaion(df)

	return df

	
	
from sklearn.linear_model import LinearRegression
def func(model,X,y):	
	
	x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.25,random_state=1) 
	
	model.fit(x_train, y_train)
	pred=model.predict(x_test)
	#print(pred)
	with open("temp.pkl", 'wb') as file:  
		pickle.dump(model, file)
	
	return x_test

def f2(x_test):
	with open("temp.pkl", 'rb') as file:
		model=pickle.load(file)
	
	print(model.predict(x_test))
	

train=pd.read_csv("all_data.csv")
train=pre_processing(train)
	
for col in train.columns:
	#y=train[col]
	#ll=[x for x in train.columns if x!=col]
	#y=train[col]
	#model=LinearRegression()
	#t=func(model,train[ll],y)
	t=pd.read_csv("current.csv")
	ll=[x for x in t.columns if x!=col]
	
	f2(t[ll])
	#break
	
'''
	
if __name__=="__main__":
	
	
	all_tests=os.listdir("data/all_containers")
	for test_case_name in all_tests:
		print("Building model for test case "+test_case_name)
		model_case="proc/models/model_"+str(test_case_name[5:])
		os.system("mkdir "+model_case)
		
		train=pd.read_csv("data/all_containers/"+test_case_name+"/all_data.csv")
		train=pre_processing(train)
		
		model=model_2(train.shape)
		adam = optim.Adam(params=model.parameters(), lr=0.01)

		for col in train.columns:
			y=train[col]
			X=train.drop([col],axis="columns",inplace=False)
			model_name=model_case+"/"+str(test_case_name[5:])+"_"+col+".pkl"
			#print("Loss of ",col)
			train_model(model,model_name,X,y, nll_loss, adam, iterations=50, print_every=50)
		
		
		
else:
	print("ML model building could not run.\nCheck ml_model.py for more details")


'''




