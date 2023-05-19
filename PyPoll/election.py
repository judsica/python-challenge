# To import and get the needed information from the cvs file
import os
import csv

# Path to collect data from the Resources folder
election_data_csv = 'election_data.csv'

#To read CSV file
with open(election_data_csv, 'r') as csvfile:

    #Splitting the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    data = list(csvreader)
    votes_total = len(data)
    candidates = list(set(row[2]for row in data))
    count_vote = {}
    percent_votes = {}
#now creating a for loop to find the top candidates
    for row in data:
        candidate = row[2]
        count_vote[candidate] = count_vote.get(candidate, 0) + 1

    for candidate, count in count_vote.items():
       
        percent_vote = (count / votes_total) * 100
        percent_votes[candidate] = percent_vote
    
#To find the winner of the election
    winner = max(count_vote, key=count_vote.get)

#Printing the results in the terminal
print("Election Results")
print(f"-------------------------")
print(f"Total Votes: {votes_total}")
print(f"-------------------------")
for candidate in candidates:
    print(f"{candidate}: {percent_votes[candidate]: .3f}% ({count_vote[candidate]})")
print("-------------------------")
print(f"Winner: {winner}")
print(f"-------------------------")

#Printing my results in a textfile
election_data_csv = 'PyPoll_Results.txt'
with open(election_data_csv, "w") as text_file:
    print("Election Results", file=text_file)
    print(f"-------------------------", file=text_file)
    print(f"Total Votes: {votes_total}", file=text_file)
    print(f"-------------------------", file=text_file)
    for candidate in candidates:
        print(f"{candidate}: {percent_votes[candidate]: .3f}% ({count_vote[candidate]})", file=text_file)
    print("-------------------------", file=text_file)
    print(f"Winner: {winner}", file=text_file)
    print(f"-------------------------", file=text_file)