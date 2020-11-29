#Python module for final deployment

import os
import time
import sys
import multiprocessing

import pandas as pd
import numpy as np
#import torch
#import torch.nn as nn
#import torch.utils.data as data_utils
#from torch import optim

import math	
import pickle

from include.container_management import container_management

def pre_processing(df):
	#Removing all columns with no values
	df=df.dropna(axis=1,how="all",inplace=False)
	
	#Removing name, id, pids_stats and first column which are not useful for running ML algorithms
	df=df.drop([df.columns[0],"name","id","pids_stats"],axis=1,inplace=False)

	#Removing all rows with NULL values
	df=df.dropna(axis="rows",inplace=False)
		
	for col in df.columns:
		df[col]=df[col].astype("float64")

	return df



#from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
def predict(df):
	
	#df=pd.read_csv("../data/all_containers/Test_ram_eater/current.csv")		
	df=pre_processing(df)
	
	orange_flags=0
	red_flags=0
	
	all_models=os.listdir("proc/models")
	for col in df.columns:
		total_loss=0
		for model_fol in all_models:		
			try:
				with open("proc/models/"+model_fol+"/"+model_fol[6:]+"_"+col+".pkl", 'rb') as file:
					model=pickle.load(file)

				ll=[x for x in df.columns if x!=col]
				y=df[col]
				total_loss=total_loss+math.sqrt(mean_squared_error(df[col],model.predict(df)))
			except:
				x=1#something
				#print("model not compatible")
		
		if total_loss>0:
			total_loss=math.log(total_loss)
		#print(total_loss)
		if total_loss > 18:
			#print("red flag in "+col)(
			red_flags=red_flags+1
		elif total_loss > 16.5:#.31
			#print("orange flag in "+col)
			orange_flags=orange_flags+1
			
	#print("Number of orange flags is ",orange_flags)
	#print("Number of red flags is ",red_flags)
	
	if red_flags > 4:
		print("Red flag please have a look\n",flush=True)
	elif orange_flags > 4:
		print("Orange flag please have a look\n",flush=True)
	
		
#predict(10)
		

def get_current_matrice(loc):
	df=pd.read_csv(loc+"/current.csv")
	return df
	
def run_container(arg_1,arg_2):
	container_obj=container_management()
	container_obj.run_test_case("bada_case","deploy/bada_case")

#These should always run in serial order never in parallel
def deploy(sleep_time):
	print("Deploying the containers")
	
	process_1=multiprocessing.Process(target=run_container,args=("bada_case","deploy/bada_case"),)
	process_1.start()
	
	time.sleep(4)
	#use current.csv to get latest data and use it for detection
	loc="data/all_containers/Test_bada_case"
	
	for _ in range(3):
		train=get_current_matrice(loc)
		time.sleep(sleep_time)
		#print(train.info())
	
	for _ in range(200):
		train=get_current_matrice(loc)
		predict(train)
		time.sleep(sleep_time)
		
		
#deploy(1)

#How to build a final model as an ensemble of all the models




'''

class model_2(nn.Module):
	def __init__(self,shape):
		vertical=shape[0]
		horizontal=shape[1]-1#yahi main hai
		super().__init__()
		self.backbone = nn.Sequential(
			nn.BatchNorm1d(horizontal), # trick to normalize the input automatically
			nn.Linear(horizontal,300),
			nn.ReLU(inplace=True),
			nn.BatchNorm1d(300),
			nn.Linear(300, 612),
		)
		
		nn.init.kaiming_normal_(self.backbone[1].weight.data)
		nn.init.ones_(self.backbone[1].bias.data)
		nn.init.kaiming_normal_(self.backbone[4].weight.data)
		nn.init.ones_(self.backbone[4].bias.data)
    
	#Add a skewed function
	def forward(self, X):
		X=X.float()
		out = self.backbone(X)
		mean = out[..., 0][..., None]
		# ensure we always obtain a possitive value for the std
		std = torch.clamp(out[..., 1][..., None], min=1)#Zero is giving some error
		norm_dist = torch.distributions.Normal(mean, std)
		return norm_dist
	
def nll_loss(observations, dists):
	return -dists.log_prob(observations).sum()
'''