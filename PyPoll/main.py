import csv
import os

#read election.data.csv file
election_data = os.path.join("Resources", "budget_data.csv")

#read CSV file and create csv reader
with open(election_data) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
  #  print(csvreader)
    csv_header = next(csvreader)
    print(csv_header)

#1 - count length of the list
#2 - https://stackoverflow.com/questions/12282232/how-do-i-count-unique-values-inside-a-list
#3 - #2 votes/#1 total 
#4 - #3 * #2
#5 - max total