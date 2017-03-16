#!/usr/bin/python3
import random
import os
import time
DEBUG = True
SEED = 42
N_REPETITIONS = 2
datasets = ["ml-100k","lastfm-2k"]

#algorithms is a map String -> List of maps (name -> range)
algorithms = dict()
algorithms["funksvd"] = {'itercount':{'max':500,'min':100},'featcount':{'max':100,'min':3}}
algorithms["user-user"] = {'neighborhood':{'max':80,'min':3}}
algorithms["item-item"] = {'neighborhood':{'max':80,'min':3}}

random.seed(SEED)

for dataset in datasets:
	for algorithm in algorithms:
		base_cmd = "./gradlew evaluateOneAlgorithm -Pdataset="+dataset
		base_cmd+= " -Pmethod="+algorithm
		for i in range(N_REPETITIONS):
			cmd = base_cmd
			hyperparameters = algorithms[algorithm]
			#add hyperparameters according to range
			for hyperparam in hyperparameters:
				hyperparam_range = hyperparameters[hyperparam]
				cmd += " -P"+hyperparam+"="
				cmd += str(random.randint(hyperparam_range["min"],hyperparam_range["max"]))
			#now we add the suffix
			cmd+=" -Psuffix="+str(int(time.time()))
			
			print(cmd)
			if not DEBUG:
				os.system(cmd)
			else: time.sleep(1)
		
