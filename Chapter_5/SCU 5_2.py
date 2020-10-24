# Done by Carlos Amaral (2020/09/29)


import csv

# read from the SCU 5_2.csv file using csv_reader from the csv module
# and print all the lines
with open('SCU 5_2.csv', 'r') as f:
    csv_reader = csv.reader(f, delimiter=',')

    for line in csv_reader:
        print(line)

