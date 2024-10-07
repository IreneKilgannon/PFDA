# Modify the program to calculate the average age reading the csv file as a dictionary
# Author Irene Kilgannon

import csv

FILE_NAME = 'data.csv'

DATA_DIR = "../Week01 - data representation/"

with open(DATA_DIR + FILE_NAME, 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter= ",", quoting= csv.QUOTE_NONNUMERIC)

    total = 0
    count = 0
    for line in csv_reader:
        total += line['age']
        count += 1
    print(f'average age is {total/(count)}')



# To modify data and write the data to a new csv file
    with open('new_data.csv', 'w') as new_file:
        fieldnames = ['age', 'name']

        csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames)

        csv_writer.writeheader()

        for line in csv_reader:
            del line['id']
            csv_writer.writerow(line)
