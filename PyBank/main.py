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
    net_sum = (sum(total_revenue))
    revenue_changes = []
    for i in range(len(total_revenue) - 1):
        current_revenue = total_revenue[i]
        next_revenue = total_revenue[i+1]
        change_in_revenue = next_revenue - current_revenue
        revenue_changes.append(change_in_revenue)
    print(revenue_changes)
    
    average = sum(revenue_changes)/len(revenue_changes)
    print(average)
    

#maximum increase in profits
    maximum = max(revenue_changes)
    print(maximum)

#greatest decrease in profits
    minimum = min(revenue_changes)
    print(minimum)

#print analysis
print("Financial Analysis")
print("----------------------------")
print("Total Months: ", length)
print("Total: $", net_sum)
print("Average Change: ", round(average, 2))
print("Greatest Increase in Profits: ", maximum)
print("Greatest Decrease in Profits: ", minimum)

#write txt file
f = open("budget_data.txt", "w")
f.write("Financial Analyis \n")
f.write("---------------------------- \n")
f.write("Total Months: " + str(length) + "\n")
f.write("Total: $" + str(net_sum) + "\n")
f.write("Average Change: " + str(round(average, 2)) + "\n")
f.write("Greatest Increase in Profits: " + str(maximum) + "\n")
f.write("Greatest Decrease in Profits: " + str(minimum) + "\n")
f.close()