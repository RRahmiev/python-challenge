import os
import csv

csvpath = os.path.join('.', 'Resources', 'election_data.csv')

with open(csvpath, encoding='utf') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=",")

    rowcount  = -1

    for row in csvreader:

      rowcount+= 1

print("Election Results")
print("-------------------------")
print("Total Votes: ", rowcount)

with open(csvpath, encoding='utf') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=",")

    total1 = 0
    total2 = 0
    total3 = 0

    for row in csvreader:
 
      if row[2] == "Charles Casper Stockham":

        total1+= 1

        perc1 = total1/rowcount * 100

      elif row[2] == "Diana DeGette":

        total2+= 1

        perc2 = total2/rowcount * 100

      elif row[2] == "Raymon Anthony Doane":

        total3+= 1

        perc3 = total3/rowcount * 100

print("-------------------------")
print(f"Charles Casper Stockham: ", round(perc1,3), "%", "(",total1,")")
print(f"Diana DeGette: ", round(perc2,3), "%", "(",total2,")")
print(f"Raymon Anthony Doane: ", round(perc3,3), "%", "(",total3,")")
print("-------------------------")

if total1 > total2:

  print("Winner: Charles Casper Stockham", )

elif total2 > total3:

  print("Winner: Diana DeGette")

else:

  print("Winner: Anthony Doane")

print("-------------------------")
