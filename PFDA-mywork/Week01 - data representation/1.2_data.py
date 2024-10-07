'''Write a program to read in the data and output each line as a list'''
# Author: Irene Kilgannon

import csv
import json

FILE_NAME = 'data.csv'

DATA_DIR = "../Week01 - data representation/"

# To open the csv file and read the contents of the file
with open(DATA_DIR + FILE_NAME, 'rt') as csv_file:
    reader = csv.reader(csv_file, delimiter= ",")
    for line in reader:
       print(line)


# To open and read the contents of the csv file without the headers
# https://www.youtube.com/watch?v=LeFDBRAhRls&list=PL2VXyKi-KpYs_f1gu30AGqy0H6x97Vomf&index=6
with open(DATA_DIR + FILE_NAME, 'rt') as csv_file:
    reader = csv.reader(csv_file, delimiter= ",")
    next(reader)
    for line in reader:
        print(line)


# To convert the csv file into a json file
with open(DATA_DIR + FILE_NAME, 'rt') as csv_file:
    reader = csv.reader(csv_file, delimiter= ",", quoting= csv.QUOTE_NONNUMERIC)
    next(reader)
    data = []
    for row in reader:
        data.append({"id":row[0], "age": row[1], "name": row[2]})

# Convert csv file to json file
with open("data.json", "w") as f:
    json.dump(data, f, indent= 2)