import csv
import os

#read election.data.csv file
election_data = os.path.join("Resources", "election_data.csv")

#read CSV file and create csv reader
with open(election_data) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
  #  print(csvreader)
    csv_header = next(csvreader)
    print(csv_header)

    voter_id = []
    county = []
    candidate = []

    for row in csvreader:
      voter_id.append(row[0])
      county.append(row[1])
      candidate.append(row[2])

    length = len(voter_id)
    print(length)