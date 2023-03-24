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
    print(f"CSV Header: {csv_header}")

    totalmonths = 0 
    totalProfitLoss = 0
    AvgProfitLoss = 0
    counter = 0 
    minValue = 0 
    maxValue = 0 
    MaxValMontth = 0 
    MinValMonth = 0 
    months = list()
    diffMonths = list()
    total = 0
    valueInt= 0
    oldMonthValue = 0  


    for row in csvreader: 
        totalmonths = totalmonths + 1 #calculate the total number of months included in the dataset
        totalProfitLoss = totalProfitLoss + int(row[1]) #calculate the net total amount of "Profit/Losses" over the entire period
        AvgProfitLoss = totalProfitLoss / totalmonths #calculat the average profitloss
       
        valueInt = int(row[1])
        if counter == 0:
            minValue = valueInt
            maxValue = valueInt
            maxMonth = row[0]
            minMonth = row[0]
        
        # else: 
		#     if counter > 0:
        #         diffMonths.append(valueInt - oldMonthValue)
        #         oldMonthValue = valueInt
        # #     total += valueInt
        # #     counter  += 1
        # #     months.append(row[0])

print(totalProfitLoss)
print(totalmonths)
print(AvgProfitLoss)
print(valueInt)
print(counter)







    


















