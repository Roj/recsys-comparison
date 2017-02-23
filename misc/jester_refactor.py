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

last_user = i + 1
data = get_data("jester-data-2.xls")
matrix = data["jester-data-2-new"]

for i in range(len(matrix)):
	for j in range(len(matrix[i])):
		if j==0: continue
		if matrix[i][j]!=99:
			new_list.append([i+last_user,j,matrix[i][j]])

last_user = last_user + i + 1
data = get_data("jester-data-3.xls")
matrix = data["jester-data-3-new"]

for i in range(len(matrix)):
	for j in range(len(matrix[i])):
		if j==0: continue
		if matrix[i][j]!=99:
			new_list.append([i+last_user,j,(matrix[i][j])])


with open('jester.tsv','w') as file:
	writer = csv.writer(file,delimiter = '\t')
	writer.writerows(new_list)
