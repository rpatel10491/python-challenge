#import necessary dependencies for os.path.join() 
import csv
import os

#read budget.data.csv file
budget_data = os.path.join("Resources", "budget_data.csv")

#read CSV file and create csv reader
with open(budget_data) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
  #  print(csvreader)
    csv_header = next(csvreader)
    print(csv_header)

#number of months
#first, create variables for total months and total revenue
    total_months = []
    total_revenue = []
#use loop to read csv
    for row in csvreader:
#use append to add element to end of list, starts row 2; indexes are 0 and 1
        total_months.append(row[0])
        total_revenue.append(row[1])
#print length of total months
    print(len(total_months))

#calculate net total amount of profit/losses
    total_revenue + (sum())

#print("Financial Analysis")
#print("----------------------------")
#print("Total Months: ")
#print("Total: ")
#print("Average Change: ")
#print("Greatest Increase in Profits: ")
#print("Greatest Decrease in Profits: ")