#script to rename users and books(ISBNs) with different numbers
#as they appear they are added into a dictionary with
#increasing primary key
#also, optionally, removes a percentage of the data
from __future__ import division
import csv

CUT_USERS = True
CUT_PERC = 0.3 # 0.3 == 30% of data is removed

entrada = "BX-Book-Ratings.csv"
salida = "BX-Book-Ratings_.csv"

data = list()

with open(entrada) as f:
	reader = csv.reader(f,delimiter=";")
	reader.next()
	data = list(reader)

#ID maps
users = dict()
books = dict()
users_id = books_id = 0

for row in data:
	if row[0] not in users:
		users[row[0]] = users_id
		users_id+=1
	if row[1] not in books:
		books[row[1]] = books_id
		books_id+=1
	row[0] = users[row[0]]
	row[1] = books[row[1]]

if CUT_USERS:	
	cut = len(users)*(1-CUT_PERC)
	data = [row for row in data if row[0]<cut]


with open(salida,"w") as f:
	writer = csv.writer(f,delimiter=",")
	writer.writerows(data)	