# Modify the program to calculate the average age reading the csv file as a dictionary
# Author Irene Kilgannon

import csv

FILE_NAME = 'data.csv'

DATA_DIR = "../Week01 - data representation/"

with open(DATA_DIR + FILE_NAME, 'rt') as csv_file:
    reader = csv.DictReader(csv_file, delimiter= ",", quoting= csv.QUOTE_NONNUMERIC)
    total = 0
    count = 0
    for line in reader:
          total += line['age']
          count +=1
    print(f'average age is {total/(count)}')
