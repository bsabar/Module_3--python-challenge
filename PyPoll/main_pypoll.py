#Ask:
# - The total number of votes cast
# - A complete list of candidates who received votes
# - The percentage of votes each candidate won
# - The total number of votes each candidate won
# - The winner of the election based on popular vote

import os
import csv

csvpath = os.path.join("Resources", "election_data.csv")

with open(csvpath, newline = "") as pypoll:
    csvreader = csv.reader(pypoll, delimiter = ",")
    # print(csvreader)
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

#declared variables
    totalvotes = 0
    winner = 0
    BallotID = []
    nameCounty = []
    politicians = []
    nameCandidate = {}
    percentCandidate ={}
    
    for row in csvreader:
        BallotID.append(row[0])
        nameCounty.append(row[1])
        politicians.append(row[2])
        totalvotes += 1 #how to calculate the total votes casts

        #how to calculate the total of votes per candidate and list all the names   
        if row[2] in nameCandidate.keys():
            nameCandidate[row[2]] = nameCandidate[row[2]] +1 
        else:
            nameCandidate[row[2]] = 1

    
    print("Total Votes: ", totalvotes)

    # how to calculate the percentage of votes each candidate won
    for row[2], value in nameCandidate.items():
        percent = format((value/totalvotes) * 100, ".3f")
        print(f"{row[2]}: {percent}% ({value})")

    #how to display the winner of the election based on popular vote
    for row[2] in nameCandidate.keys():
        if nameCandidate[row[2]] > winner:
            winner_name = row[2]
            winner = nameCandidate[row[2]]

print("Winner:", winner_name)
    


