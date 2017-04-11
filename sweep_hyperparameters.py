#!/usr/bin/python3
import random
import os
import time
import argparse

parser = argparse.ArgumentParser() 
parser.add_argument('--repetitions', type=int, default = 10)
parser.add_argument('--datasets', nargs='*', default = [
"amazon-CDs-vinyl",
"amazon-android-apps",
"amazon-automotive",
"amazon-baby",
"amazon-beauty",
"amazon-books",
"amazon-cell-phones-accessories",
"amazon-clothing-shoes-jewelry",
"amazon-digital-music",
"amazon-electronics",
"amazon-grocery-gourmet-food",
"amazon-health-personal-care",
"amazon-home-kitchen",
"amazon-instant-video",
"amazon-kindle-store",
"amazon-movies-TV",
"amazon-musical-instruments",
"amazon-office-products",
"amazon-patio-lawn-garden",
"amazon-pet-supplies",
"amazon-sports-outdoors",
"amazon-tools-home-improvement",
"amazon-toys-games",
"amazon-video-games",
"bookcrossings",
"jester",
"lastfm-2k",
"ml-100k",
"ml-20m"])
parser.add_argument("--debug", type=bool, default=False)

args = parser.parse_args()

DEBUG = parser.debug
SEED = 42
N_REPETITIONS = int(args.repetitions)
datasets = args.datasets
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
		
