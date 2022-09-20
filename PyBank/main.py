import os
import csv

csvpath = os.path.join('.', 'Resources', 'budget_data.csv')

with open(csvpath, encoding='utf') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=",")

    next(csvreader, None)

    rowcount  = 0

    for row in csvreader:

      rowcount+= 1
      #counting rows

print("Financial Analysis")
print("----------------------------")
print("Total Months: ", rowcount)
