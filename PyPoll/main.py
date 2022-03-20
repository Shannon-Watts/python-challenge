import csv

text_path = "pypoll.txt"
with open('election_data.csv') as data_file:
    csv_reader = csv.reader(data_file, delimiter=',')

    county_data = {}
    candidate_data = {}

    # Ignore the first line with the headers
    next(csv_reader)

    # Read all the data into lists 
    for row in csv_reader:
        id = int(row[0])
        county_data[id] = row[1]
        candidate_data[id] = row[2]

    # Calculate total number of votes
    num_votes = len(county_data)
    
    # Find out who the candidates were
    candidates = set(candidate_data.values())

    # Create an empty dictionary for counting the votes they got
    votes = { candidate : 0 for candidate in candidates }

    # Count the votes each candidate got (1 per entry in the original data)
    for candidate in candidate_data.values():
        votes[candidate] += 1

    # Calculate the percentage of the toal vote each candidate got
    vote_percentages = {}
    for candidate in candidates:
        vote_percentages[candidate] = (votes[candidate] / num_votes) * 100

    # Find winner based on popular vote
    winner = ''
    winning_percentage = 0.0
    for candidate in vote_percentages.keys():
        if vote_percentages[candidate] > winning_percentage:
            winner = candidate
            winning_percentage = vote_percentages[candidate]

# Print analysis
print("Election Results")
print("-------------------")
print("Total Votes: " + str(num_votes))
print("-------------------")
print("Votes per canditate: " + str(votes))
#print("Charles Casper Stockham: " + str(int(vote_percentages[Charles Kasper Stockham])) + str(votes[Charles Casper Stockham]))
#print("Diana DeGette: " + str(int(vote_percentages[Diana DeGette])) + str(votes[Diana DeGette]))
#print("Raymon Anthony Doane: " + str(int(vote_percentages[Raymon Anthony Doane]) + str(votes[Rayom Anthony Doane])))
print("-------------------")
print("Winner: " + winner)

# Print to text file 
with open(text_path, "w") as file:
    file.write("Election Results")
    file.write("-------------------")
    file.write("Total Votes: " + str(num_votes))
    file.write("-------------------")
    file.write("Votes per canditate: " + str(votes))
    #file.write("Charles Casper Stockham: " + str(int(vote_percentages[Charles Kasper Stockham])) + str(votes[Charles Casper Stockham]))
    #file.write("Diana DeGette: " + str(int(vote_percentages[Diana DeGette])) + str(votes[Diana DeGette]))
    #file.write("Raymon Anthony Doane: " + str(int(vote_percentages[Raymon Anthony Doane]) + str(votes[Rayom Anthony Doane])))
    file.write("-------------------")
    file.write("Winner: " + winner)
