#Python module to raise flags when finding malicious behaviour

#under development
import pandas as pd


def flagging_docker():
	df=pd.read_csv("proc/bounds/docker_bounds.csv")
	
def flagging_containers():
	df=pd.read_csv("proc/bounds/container_bounds.csv")

def flagging_all():
	flagging_docker()
	flagging_containers()