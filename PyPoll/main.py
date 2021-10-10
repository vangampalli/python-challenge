import os 
import csv 

poll_csv = os.path.join("..", "python-challenge", "PyPoll", "Resources", "election_data.csv")

with open (poll_csv, "r") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ",")
    csv_header = next(csv_file)

    voterID = []
    column_3 = []
    candidate_khan = 0
    candidate_correy = 0
    candidate_li = 0
    candidate_tooley = 0

    for row in csv_reader:
        voterID.append(row[0])
        column_3.append(row[2])

    len_voterID = len(voterID)
    
    for candidate in column_3: 
        if candidate == "Khan": 
            candidate_khan += 1 
        elif candidate == "Correy":
            candidate_correy += 1 
        elif candidate == "Li":
            candidate_li += 1
        elif candidate == "O'Tooley":
            candidate_tooley += 1 


    khan_cent = ((candidate_khan)/(len_voterID))*100
    correy_cent = ((candidate_correy)/(len_voterID))*100
    li_cent = ((candidate_li)/(len_voterID))*100
    tooley_cent = ((candidate_tooley)/(len_voterID))*100

    votes_list = [candidate_khan, candidate_correy, candidate_li, candidate_tooley]
    candidate_str = ["Khan", "Correy", "Li", "O'Tooley"]
    winner_vote_count = max(votes_list)
    winner_loc = votes_list.index(winner_vote_count)
    winner = candidate_str[winner_loc]


print("Election Results")
print(f"Total Votes: {len_voterID}")
print(f"Khan: {round(khan_cent, 2)} ({candidate_khan})")
print(f"Correy: {round(correy_cent, 2)} ({candidate_correy})")
print(f"Li: {round(li_cent, 2)} ({candidate_li})")
print(f"O'Tooley: {round(tooley_cent, 2)} ({candidate_tooley})")
print(f"Winner: {winner}")

with open("/Users/Vanga/Desktop/python-challenge/PyPoll/Analysis/Election_Results.txt", "w") as data:
    data.write(f"Election Results")
    data.write("\n") 
    data.write("-------------------------")
    data.write("\n") 
    data.write(f"Total Votes: {len_voterID}")
    data.write("\n") 
    data.write("-------------------------")
    data.write("\n") 
    data.write(f"Khan: {round(khan_cent, 2)} ({candidate_khan})")
    data.write("\n") 
    data.write(f"Correy: {round(correy_cent, 2)} ({candidate_correy})")
    data.write("\n") 
    data.write(f"Li: {round(li_cent, 2)} ({candidate_li})")
    data.write("\n") 
    data.write(f"O'Tooley: {round(tooley_cent, 2)} ({candidate_tooley})")
    data.write("\n") 
    data.write("-------------------------")
    data.write("\n") 
    data.write(f"Winner: {winner}")
    data.write("\n") 
    data.write("-------------------------")

