import os
import csv

csvpath = os.path.join(
    '..', 'PyPoll', 'PyPoll_Resources_election_data.csv')

# total_votes = []
# candidate_list = []
# candidate_vote = []

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    first_row = next(csvreader)

    total_votes = 0
    candidate_vote = {}
    results = []

    for row in csvreader:

        total_votes += 1

        if row[2] not in candidate_vote.keys():
            candidate_vote[row[2]] = 1
        else:
            candidate_vote[row[2]] += 1


print("Election Results")
print("-----------------------")
print(f"Total Votes: {(total_votes)}")
print("-----------------------")

for candidates in candidate_vote.keys():

    candidates_info = candidates, "{:.2%}".format(
        candidate_vote[candidates] / total_votes), "(", candidate_vote[candidates], ")"
    print(candidates, "{:.2%}".format(
        candidate_vote[candidates] / total_votes), "(", candidate_vote[candidates], ")")

winner = max(candidate_vote, key=candidate_vote.get)

print("-----------------------")
print(f"Winner: {(winner)}")
print("-----------------------")
