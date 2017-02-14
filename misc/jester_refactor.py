#script to reformat data from jester-data-1.zip (http://www.ieor.berkeley.edu/~goldberg/jester-data/)
#input: xls matrix [users x (1+jokes)] (first column = #jokes) 
#output: tsv (user,joke,rating)

from pyexcel_xls import get_data
import csv
import json

data = get_data("jester-data-1.xls")
matrix = data["jester-data-1-new"]
new_list = []

for i in range(len(matrix)):
	for j in range(len(matrix[i])):
		if j==0: continue
		if matrix[i][j]!=99:
			new_list.append([i,j,matrix[i][j]])

with open('jester-1.tsv','w') as file:
	writer = csv.writer(file,delimiter = '\t')
		for list in new_list:
			writer.writerow(list)