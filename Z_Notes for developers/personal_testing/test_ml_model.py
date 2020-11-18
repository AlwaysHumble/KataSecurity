#Importing non ML libraries
import os
import math

#Importing ML Libraries
import pandas as pd
import torch
import torch.nn as nn
import torch.utils.data as data_utils
from torch import optim

import numpy as np
from sklearn.model_selection import train_test_split



io_res=["blkio_stats__io_service_bytes_recursive", "blkio_stats__io_serviced_recursive", "blkio_stats__io_queue_recursive", "blkio_stats__io_service_time_recursive", "blkio_stats__io_wait_time_recursive", "blkio_stats__io_merged_recursive", "blkio_stats__io_service_time_recursive","blkio_stats__sectors_recursive"]

#Think of num procs
cpu_res=["cpu_total_usage", "cpu_usage_in_kernelmode", "cpu_usage_in_usermode", "system_cpu_usage", "online_cpus", "cpu_periods", "cpu_throttled_periods", "cpu_throttled_time", "precpu_total_usage", "precpu_usage_in_kernelmode", "precpu_usage_in_usermode", "cpu_system_cpu_usage", "precpu_periods", "precpu_throttled_periods", "precpu_throttled_time"]

mem_res=["memory_usage", "memory_max_usage", "memory_active_anon", "memory_active_file", "memory_cache", "memory_dirty", "memory_hierarchical_memory_limit", "memory_hierarchical_memsw_limit", "memory_inactive_anon", "memory_inactive_file", "memory_mapped_file", "memory_pgfault", "memory_pgmajfault", "memory_pgpgin", "memory_pgpgout", "memory_rss", "memory_rss_huge", "memory_total_active_anon", "memory_total_active_file", "memory_total_cache", "memory_total_dirty", "memory_total_inactive_anon", "memory_total_inactive_file", "memory_total_mapped_file", "memory_total_pgfault", "memory_total_pgmajfault", "memory_total_pgpgin", "memory_total_pgpgout", "memory_total_rss", "memory_total_rss_huge", "memory_total_unevictable", "memory_total_writeback", "memory_unevictable", "memory_writeback", "memory_limit"]

network_res=["networks_rx_bytes", "networks_rx_packets", "networks_rx_errors", "networks_rx_dropped", "networks_tx_bytes", "networks_tx_packets", "networks_tx_errors", "networks_tx_dropped"]


cols=['cpu_periods', 'cpu_throttled_periods', 'cpu_throttled_time', 'cpu_total_usage', 'cpu_usage_in_kernelmode', 'cpu_usage_in_usermode', 'memory_active_anon', 'memory_active_file', 'memory_cache', 'memory_dirty', 'memory_hierarchical_memory_limit', 'memory_hierarchical_memsw_limit', 'memory_inactive_anon', 'memory_inactive_file', 'memory_limit', 'memory_mapped_file', 'memory_max_usage', 'memory_pgfault', 'memory_pgmajfault', 'memory_pgpgin', 'memory_pgpgout', 'memory_rss', 'memory_rss_huge', 'memory_total_active_anon', 'memory_total_active_file', 'memory_total_cache', 'memory_total_dirty', 'memory_total_inactive_anon', 'memory_total_inactive_file', 'memory_total_mapped_file', 'memory_total_pgfault', 'memory_total_pgmajfault', 'memory_total_pgpgin', 'memory_total_pgpgout', 'memory_total_rss', 'memory_total_rss_huge', 'memory_total_unevictable', 'memory_total_writeback', 'memory_unevictable', 'memory_usage', 'memory_writeback', 'networks_rx_bytes', 'networks_rx_dropped', 'networks_rx_errors', 'networks_rx_packets', 'networks_tx_bytes', 'networks_tx_dropped', 'networks_tx_errors', 'networks_tx_packets', 'num_procs', 'online_cpus', 'precpu_periods', 'precpu_throttled_periods', 'precpu_throttled_time', 'precpu_total_usage', 'precpu_usage_in_kernelmode', 'precpu_usage_in_usermode', 'system_cpu_usage']


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
				
	print(new_df.head(50))
	return new_df

#Check if there is a need of add change in resource utilized rather than absolute on
def pre_processing(df):
	#Removing all columns with no values
	df=df.dropna(axis=1,how="all",inplace=False)
	
	#Removing name, id, pids_stats and first column which are not useful for running ML algorithms
	df=df.drop([df.columns[0],"name","id","pids_stats"],axis=1,inplace=False)
	
	#Removing all columns with constant value
	#It is not very effective check memory active file in cpu eater
	#Keep it to make sure that all models have same length
	#df=df.loc[:,(df!=df.iloc[0]).any()]

	#Removing all rows with NULL values
	df=df.dropna(axis="rows",inplace=False)
	
	#Removing first and last row as they are outliers and they are the stage where container is getting started or getting destroyed
	df=df.drop(df.head(1).index,axis="rows",inplace=False)
	df=df.drop(df.tail(1).index,axis="rows",inplace=False)
	
	for col in df.columns:
		df[col]=df[col].astype("float64")
	
	print(df.head(21))
	print("------------------------------------------------------------------------------------")
	
	df=augmentaion(df)
	
	print(df.columns)
	
	return df


train=pd.read_csv("../../data/all_containers/Test_packet_flooder/all_data.csv")
train=pre_processing(train)

#print(train.info())

def train_model(model,X,y,loss_fn,optimizer,iterations=100,print_every=50,lr=0.001):
	optimizer.lr = lr
	
	x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.25)
	
	x_train=torch.from_numpy(np.array(x_train))
	x_test=torch.from_numpy(np.array(x_test))
	y_train=torch.from_numpy(np.array(y_train))
	y_test=torch.from_numpy(np.array(y_test))
	
	for i in range(iterations):
		model.train()
		out = model(x_train)
		loss = loss_fn(y_train, out)
		optimizer.zero_grad()
		loss.backward()
		optimizer.step()
				
		if i % print_every == 0:
			with torch.no_grad():
				model.eval()
				out = model(x_test)
				test_loss = loss_fn(y_test, out)
				if math.log10(loss.item())>25:
					print("Red flag")
				elif math.log10(loss.item())>15:
					print("Orange flag")
				#print(math.log10(loss.item()), math.log10(test_loss))	
'''
class ml_model(nn.Module):
	def __init__(self,shape):
		vertical=shape[0]
		horizontal=shape[1]-1#yahi main hai
		super().__init__()
		self.layers = nn.Sequential(
			nn.Linear(horizontal,vertical),
			nn.ReLU(inplace=True),
			nn.Linear(vertical,3),
		)
	
	def forward(self,X):
		X=X.float()
		out = self.layers(X)
		# ensure tensors are have [batch_size, 1]
		# that's why [..., None] is used, to introduce an extra dimension
		mean=out[..., 0][..., None] # use first index as the mean
		std=torch.clamp(out[..., 1][..., None], min=0.01) # use second index as the std
		# Note the use of clamp, it's super important because otherwise you might
		# have negative values as the standard deviation and end up having nans,
		# by using this little trick we ensure we always have a positive std.
        
		norm_dist = torch.distributions.Normal(mean,std)
		return norm_dist
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
	
#model=ml_model(train.shape)
model=model_2(train.shape)
adam = optim.Adam(params=model.parameters(), lr=0.01)


for col in train.columns:
	y=train[col]
	X=train.drop([col],axis="columns",inplace=False)
	print("Loss of ",col)
	train_model(model,X,y, nll_loss, adam, iterations=50, print_every=50)







