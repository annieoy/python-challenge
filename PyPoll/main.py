import os
import csv
csvpath=os.path.join('Resources','election_data.csv')

total_votes = 0
candidates = {}
total_votes_won = 0
winner = ""
winner_votes = 0

with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)

    for row in csvreader:
        total_votes += 1
        candidate_name = row [2]

        if candidate_name not in candidates:
            candidates[candidate_name] = 0

        candidates[candidate_name] += 1

print("Election Results")
print("-----------------------")
print(f"Total votes: {total_votes}")
print("-----------------------")

for candidate, votes in candidates.items():
    vote_percentage = (votes / total_votes) * 100
    print(f"{candidate}: {vote_percentage:.3f}% ({votes})")
    if votes > winner_votes:
        winner = candidate
        winner_votes = votes
print("-------------------------")
print(f"Winner: {winner}")