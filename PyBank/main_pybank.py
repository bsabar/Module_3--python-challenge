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

    totalmonths = 0 
    totalProfitLoss = 0
    AvgProfitLoss = 0
    valueInt= 0
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
        #profit_change += totalProfitLoss
        #AvgProfitLoss = totalProfitLoss / totalmonths #calculate the average profitloss
        
        # if totalProfitLoss > 0:
        #     #profit_change += totalProfitLoss
        #     profit_change = totalProfitLoss
        #     profit_change = current_mo_PL
        #     profit_change = previous_mo_PL
        #     profit_change = previous_mo_PL + current_mo_PL
        #     profit_change = current_mo_PL
        #     diffMonths.append(row[0])
        #     net_PL.append(profit_change)

        # else:
        #     profit_change = totalProfitLoss
        #     profit_change = current_mo_PL
        #     profit_change = previous_mo_PL
        #     profit_change = previous_mo_PL - current_mo_PL
        #     profit_change = current_mo_PL
        #     diffMonths.append(row[0])
        #     net_PL.append(profit_change)


        # if totalmonths == 1: 
        #     previous_mo_PL = current_mo_PL
        #     continue
        # else: 
        #     profit_change = current_mo_PL - previous_mo_PL
        #     diffMonths.append(row[0])
        #     net_PL.append(profit_change)
        #     previous_mo_PL = current_mo_PL

            # #valueInt = int(row[1])
            # if valueInt < 0: 
            #     valueInt =  valueInt + int(row[1])
            #     diffMonths.append(valueInt)
            # else: 
            #     valueInt = valueInt - int(row[1])
            #     diffMonths.append(valueInt)

        if totalProfitLoss > 0:
            totalProfitLoss -= int(row[1])
            totalProfitLoss = previous_mo_PL
            diffMonths.append(row[0])
            net_PL.append(totalProfitLoss)

        
           
net_PL.pop(0)
print(net_PL)
print(diffMonths)
def Average (net_PL): 
    return sum(net_PL)/len(net_PL)
average = Average(net_PL)
print("Average of the list = ", round(average, 2))

high_change = max(net_PL)
print(high_change)
low_change = min (net_PL)
print(low_change)


print("Total Months: ", totalmonths)
print("Total Profit Loss: ", totalProfitLoss)
#print("Average Profit Loss: ", AvgProfitLoss)
#print("ValueInt: ", valueInt)
#print("Average Change: ", AvgIncrease)








    


















