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
# create variables 
    voter_id = []
    county = []
    candidate = []
#create loop to read csv 
    for row in csvreader:
      voter_id.append(row[0])
      county.append(row[1])
      candidate.append(row[2])
#create new variable for total votes
    length = len(voter_id)
    print(length)
#create dictionary to count individual votes
    voter_dictionary = {}
    for name in candidate:
      if name not in voter_dictionary:
        voter_dictionary[name] = 1
      else:
        voter_dictionary[name] += 1
    #print(voter_dictionary)

    for cand in voter_dictionary.items():
      print(cand[0])
      print(str(cand[1]))
      print(str((cand[1]/length) * 100))
#calculate winner  
    winner = max(voter_dictionary.items(), key=lambda item: item[1])


print("Election Results ")
print("----------------------------")
print("Total Votes: " + str(length))
print("----------------------------")
for cand in voter_dictionary.items():
      print((cand[0]) + ": " + (str(cand[1])) + " " + (str((cand[1]/length) * 100)))
print("----------------------------")
print("Winner: " + str(winner[0]))


f = open("election_data.txt", "w")
f.write("Election Results \n")
f.write("---------------------------- \n")
f.write("Total Votes: " + str(length) + "\n")
f.write("---------------------------- \n")
for cand in voter_dictionary.items():
    f.write((cand[0]) + ": " + (str(cand[1])) + " " + (str((cand[1]/length) * 100) + "\n"))
f.write("---------------------------- \n")
f.write("Winner: " + str(winner[0]) + "\n")
f.close()