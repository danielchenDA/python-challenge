# Import Dependencies
import csv
import os

# assign variables
win_votes = 0
election_data_dict = {}
total_votes = 0
candidate_holder = ""
winner = ""
vote_holder = 0

# assign csv file path to a variable
election_data_path = os.path.join('..','PyPoll','election_data.csv')

# open csv file using csvreader
with open(election_data_path, newline='') as election_data:
    # define csvreader to read the file
    csvreader = csv.reader(election_data, delimiter=',')
    # checks to see if the file is read in correctly
    # print(csvreader)
    # read header to skip the header information
    csv_header = next(csvreader)

    # read each row of data after the csv_header
    for row in csvreader:
        # adds to the total votes
        total_votes += 1

        # checks for blank dictionary
        if election_data_dict == {}:
            # creates the first key and assigns a value of 1
            election_data_dict[row[2]] = 1
        else:
            # sets found to false
            found = False
            # loops through all keys in the dictionary
            for candidate in election_data_dict.keys():
                # if the candidate name is equal to they key value in the dictionary...
                if row[2] == candidate:
                    # adds 1 to candidate key value
                    election_data_dict[candidate] += 1
                    # sets found to true
                    found = True
                    # break out of loop for efficiency
                    break
            # if found is equal to false...
            if found == False:
                # creates new key and assigns a value of 1
                election_data_dict[row[2]] = 1

#print(election_data_dict)
print("Election Results")
print("-------------------------------")
print(f'Total Votes: {total_votes}')
print("-------------------------------")

for candidate, vote in election_data_dict.items():
    print(f'{candidate}: {(vote / total_votes) * 100}% ({vote})')
    if vote > win_votes:
        winner = candidate
        win_votes = vote

print("-------------------------------")
print(f'Winner: {winner}')
print("-------------------------------")

# designate file path and file name
file = "../PyPoll/Election_Results.txt"

# open and write to file
with open(file, "w") as Election_Results_txt:
    Election_Results_txt.write("Election Results\n")
    Election_Results_txt.write("----------------------------\n")
    Election_Results_txt.write(f'Total Votes: {total_votes}\n')
    Election_Results_txt.write("----------------------------\n")
    for candidate, vote in election_data_dict.items():
        Election_Results_txt.write(f'{candidate}: {(vote / total_votes) * 100}% ({vote})\n')
        if vote > win_votes:
            winner = candidate
            win_votes = vote
    Election_Results_txt.write("-------------------------------\n")
    Election_Results_txt.write(f'Winner: {winner}\n')
    Election_Results_txt.write("-------------------------------\n")
