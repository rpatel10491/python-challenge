#import necessary dependencies for os.path.join() 
import csv
import os

#read budget.data.csv file
budget_data = os.path.join("..", "Resources", "budget_data.csv")

#number of months
total_months = 0
#total profit loss
total_profitLoss = 0
#average change
change = 0
#initialize titles/rows list
date = []
profit = []




#read CSV file and create csv reader
with open(budget_data) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    csv_header = next(csvreader)

print(csvreader)








#print("Financial Analysis")
#print("----------------------------")
#print("Total Months: ")
#print("Total: ")
#print("Average Change: ")
#print("Greatest Increase in Profits: ")
#print("Greatest Decrease in Profits: ")