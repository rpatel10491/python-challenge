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
    change = []
#use loop to read csv
    for row in csvreader:
#use append to add element to end of list, starts row 2; indexes are 0 and 1
        total_months.append(row[0])
        total_revenue.append(int(row[1]))
#print length of total months
    length = len(total_months)
    print(length)
#total profit/loss
    sum = (sum(total_revenue))
    revenue_changes = []
    for i in range(len(total_revenue) - 1)
#average of changes
    average = sum/length
    print(average)

#maximum increase in profits
    maximum = max(total_revenue)

print("Financial Analysis")
print("----------------------------")
print("Total Months: ", length)
print("Total: $", sum)
print("Average Change: ", average)
print("Greatest Increase in Profits: ")
print("Greatest Decrease in Profits: ")