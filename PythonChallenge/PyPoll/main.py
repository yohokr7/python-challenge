#Import Module
import os
import csv

#Create CSV Pathway
electionpath = os.path.join(".", "Resources", "election_data.csv")

#Open CSV, Create CSV Reader, Skip Header
with open(electionpath, newline='') as electioncsv:
    electionreader = csv.reader(electioncsv, delimiter = ',')
    electionheader = next(electionreader)
    
    #Define Variables
    totalvotes = 0
    votes = []
    candidates = []
    votecount = []
    candidatevotes = {}
    sortedcandidatevotes = {}
    
    #Create Votes List and Tally Total Votes
    for row in electionreader:
        totalvotes= totalvotes + 1
        votes.append(row[2])
    
    #Find Candidate Names: Found Online https://www.geeksforgeeks.org/python-get-unique-values-list/
    candidates_set = set(votes)
    candidates = (list(candidates_set))
    
    #Find Vote Count per Candidate
    for can in candidates:
        votecount.append(votes.count(can))
        
    #Link Candidates and Vote Counts in Dictionary
    candidatevotes = {candidates[j]:votecount[j] for j in range(len(candidates))}
    
    #Sort Candidates by Votes: Found Online https://youtu.be/MGD_b2w_GU4
    sortedcandidatevotes = dict(sorted(candidatevotes.items(), key=lambda t:t[1], reverse = True))
    #Find Winner: Found Online https://www.geeksforgeeks.org/python-get-the-first-key-in-dictionary/
    winner = next(iter(sortedcandidatevotes))
    
    #Create Voting Analysis Non-Variable Strings
    line1 = f'Election Results'
    line2 = f'-------------------------'
    line3 = f'Total Votes: {totalvotes}'
    line4 = f'-------------------------'
    line5 = f'-------------------------'
    line6 = f'Winner: {winner}'
    line7 = f'-------------------------'

    #Print Voting Analysis
    print(f'{line1}\n{line2}\n{line3}\n{line4}')
    for key,value in sortedcandidatevotes.items():
        percentvote = ((value*100/totalvotes))
        print(f'{key}: {round(percentvote, 3)}00% ({value})')
    print(f'{line5}\n{line6}\n{line7}\n')
    
    #Check if Analysis.txt Exists in SubDirectory
    filepath = os.path.join(".","analysis","Analysis.txt")
    isfile = os.path.isfile(filepath)
    path = os.path.join(".","analysis")
    
    #If Analysis.txt Does Not Exist, Creates and Populates It
    if isfile == False:
        with open(os.path.join(path, "Analysis.txt"), "w") as analysis:
            analysis.write(f'{line1}\n')
            analysis.write(f'{line2}\n')
            analysis.write(f'{line3}\n')
            analysis.write(f'{line4}\n')
            for key,value in sortedcandidatevotes.items():
                percentvote = ((value*100/totalvotes))
                analysis.write(f'{key}: {round(percentvote, 3)}00% ({value})\n')
            analysis.write(f'{line5}\n')
            analysis.write(f'{line6}\n')
            analysis.write(f'{line7}')