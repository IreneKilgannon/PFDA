# Modify the program to calculate the average age
# Author Irene Kilgannon

import csv

FILE_NAME = 'data.csv'

DATA_DIR = "../Week01 - data representation/"

with open(DATA_DIR + FILE_NAME, 'rt') as csv_file:
    reader = csv.reader(csv_file, delimiter= ",", quoting= csv.QUOTE_NONNUMERIC)
    linecount = 0
    total = 0
    for line in reader:
        if not linecount:
            pass
        else:
            total += line[1]
        linecount += 1
    print(f'average is {total/(linecount-1)}')
