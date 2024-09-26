'''Write a program to read in the data and output each line as a list'''
# Author: Irene Kilgannon

import csv

FILE_NAME = 'data.csv'

DATA_DIR = "../Week01 - data representation/"

with open(DATA_DIR + FILE_NAME, 'rt') as csv_file:
    reader = csv.reader(csv_file, delimiter= ",")
    for line in reader:
        print(line)
