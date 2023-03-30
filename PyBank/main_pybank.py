# Ask: 
# (1) The total number of months included in the dataset
# (2) The net total amount of "Profit/Losses" over the entire period
# (3) The changes in "Profit/Losses" over the entire period, and then the average of those changes
# (4) The greatest increase in profits (date and amount) over the entire period
# (5) The greatest decrease in profits (date and amount) over the entire period

import os
import csv

csvpath = os.path.join("Resources", "budget_data.csv")

with open(csvpath, newline = "") as pybank:
    csvreader = csv.reader(pybank, delimiter = ",")

    # print(csvreader)
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

#declared variables
    totalmonths = 0 
    totalProfitLoss = 0
    AvgProfitLoss = 0
    current_mo_PL = 0 
    previous_mo_PL = 0 
    profit_change = 0 
    high_change = 0 
    low_change = 0 
    diffMonths = list()
    net_PL = list()

   
    for row in csvreader: 
        totalmonths += 1 #calculate the total number of months included in the dataset
        totalProfitLoss += int(row[1]) #calculate the net total amount of "Profit/Losses" over the entire period
        # calculate the changes in "Profit/Losses" over the entire period, and then the average of those changes
        current_mo_PL = int(row[1])
        profit_change = current_mo_PL - previous_mo_PL
        previous_mo_PL = current_mo_PL
        net_PL.append(profit_change)
        diffMonths.append(row[0])

#removing the values that you don't need after appending your lists
net_PL.pop(0)
diffMonths.pop(0)

#calculating the average
def Average (net_PL): 
    return sum(net_PL)/len(net_PL)
average = Average(net_PL)

#calculating the high and lowest profits
high_change = max(net_PL)
low_change = min (net_PL)
maxindex = net_PL.index(high_change)
minindex = net_PL.index(low_change)

#printing the end results
print("Financial Anaysis: ")
print("Total Months: ", totalmonths)
print("Total: $", totalProfitLoss)
print("Average Change: = ", round(average, 2))
print("Greatest Increase in Profits: " + diffMonths[maxindex] + " (" + "$" + str(high_change) + ")")
print("Lowest Decrese in Profits: " + diffMonths[minindex] + " (" +  "$" + str(low_change) + ")")









    


















