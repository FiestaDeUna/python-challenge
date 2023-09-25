import os
import csv

#Set path 

csvpath = os.path.join("Resources", "election_data.csv")

poll_data = []

#Open reader 

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
   
    csv_header =  next(csvreader)   #separate headers from 
    print(f"Header: {csv_header}")  #print header 

#Initialize the total number of votes cast and votes per person 

    vote_count= 0
    c_votes = 0 
    d_votes = 0 
    r_votes = 0
    c_percent = 0
    d_percent = 0
    r_percent = 0

#calculate total votes cast 

    for c in csvreader: 
        poll_data.append(c)
        vote_count += 1

#calculate total votes per candidate 

        if c[2] == "Charles Casper Stockham": 
            c_votes += 1 
        elif c[2] == "Diana DeGette": 
            d_votes += 1
        elif c[2] == "Raymon Anthony Doane": 
            r_votes += 1

#calculate percentages per vandidate 

        c_percent = round(c_votes/vote_count * 100, 2) 
        d_percent = round(d_votes/vote_count * 100, 2) 
        r_percent = round(r_votes/vote_count * 100, 2) 


#determine the overall winner 

        if c_votes > d_votes and c_votes > r_votes: 
            election_winner= "Charles Casper Stockham"
        elif d_votes > c_votes and d_votes > r_votes: 
            election_winner = "Diana DeGette"
        else: 
            election_winner = "Raymon Anthony Doane"


#collect and print all results           


overall_analysis=(
 f"\n Election Results \n\n" 
 f"-----------------------------------\n\n"
 f"Total Votes: {vote_count}\n\n" 
 f"Charles Casper Stockhham: {c_percent}% ({c_votes})\n\n"
 f"Diant Degette: {d_percent}%  ({d_votes})\n\n"
 f"Raymon Antony Doane: {r_percent}% ({r_votes})\n\n"
 f"-----------------------------------\n\n"
 f"Winner: {election_winner}\n\n"
 f"-----------------------------------\n\n")

print(overall_analysis)

#write sults to csvfile 

analysis_path = os.path.join("Resources", "ElectionResults.csv")
with open(analysis_path, 'w') as file: 
    file.write(overall_analysis)








    














#A complete list of candidates who received votes

    
            






##unique function 

#The percentage of votes each candidate won

## ??/total votes cast x 100 

#The total number of votes each candidate won



#The winner of the election based on popular vote