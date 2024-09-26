'''Modify 1.2data.py to deal with the header line seperately'''
# Author: Irene Kilgannon

import csv

FILE_NAME = 'data.csv'

DATA_DIR = "../Week01 - data representation/"

with open(DATA_DIR + FILE_NAME, 'rt') as csv_file:
    reader = csv.reader(csv_file, delimiter= ",")
    linecount = 0
    for line in reader:
        if not linecount:
            print(f'{line}\n-----------------')
        else:
            print(line)
        linecount += 1

# To remove the header the following works
#with open(Data_dir + File_name, 'rt') as csv_file:
#    reader = csv.reader(csv_file, delimiter= ",")
#    first_line = True
#    for line in reader:
#        if first_line:
#            first_line = False
#            continue
#        print(line)
