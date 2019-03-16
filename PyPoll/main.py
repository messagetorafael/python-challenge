#STUDENT: RAFAEL SANTOS         #HOME WORK 3
#Data Analystics and Visualization Cohort 3

#PYPOLL-VERSION 1
#### THIS VERSION IS THE SAME USED WITHIN 2in1-v1 and 2in1-v2 SCRIPTS.

###############################################################
# PROMPT MESSAGE SO THAT USER KNOWS THE CODE IS RUNNING....
###############################################################
print("\nOK!: PyPoll code is now running!!!\n\n\n\n")

# IMPORT MODULES
#--------------------------------------------------------------
import os
import csv
from collections import Counter

# Set path for file
#--------------------------------------------------------------
csvfile = os.path.join("..", "PyPoll\Resources", "election_data.csv")

###############################################################
# MAIN CODE
###############################################################

# Store Voter ID and Candidate data on specific lists
#--------------------------------------------------------------
VoterID = []                        
Candidate = []                      
with open(csvfile,'r') as csvfile:  
    csvreader = csv.reader(csvfile, delimiter=",")
    csvheader = next(csvfile,None)

    for row in csvreader:
        VoterID.append(row[0])          
        Candidate.append(row[2])

# Determine total of votes
#--------------------------------------------------------------
TotalVotes = len(VoterID)                                   #>print output>> Total Votes: 3,521,001

# Determine consolidated votes per candidate
#--------------------------------------------------------------
votestotals =[]
                                    #imported module for this command Counter
votestotals = Counter(Candidate)    #data stored >>> Counter({'Khan': 2218231, 'Correy': 704200, 'Li': 492940, "O'Tooley": 105630})

# Create lists to split Candidate Names, Total Votes by Candidate, 
# and Percentage [from Total Votes] of Votes by Candidate 
#--------------------------------------------------------------
names = [name for name in votestotals.keys()]               #holds candidate names
counts = [count for count in votestotals.values()]          #holds number votes of each candidate
percentages = [round(percentage/TotalVotes,4) for percentage in counts] #calculates and holds percentage [decimal] number of votes of each candidate

# Identify Winner - Candidate Name with most votes
#--------------------------------------------------------------
winnercounts = max(counts)                                  #identify the greatest number of votes
winnerindex = [i for i in range (len(counts)) if counts[i] == winnercounts]
winnerindex = int(winnerindex.pop(0))                       #identify index/position of greatest number of votes in the list

winnername = names[winnerindex]     #use  index above to find correspondent position within the names list


# Print the results
#--------------------------------------------------------------

## The total number of votes cast
multiplelines = ("Election Results" + "\t(Total Votes: " + \
                "{:,.0f}".format(TotalVotes) + ")"\
                "\n-----------------------------------------------\n" +\
                "\nCandidate\t(Votes Received)\t| %"
                "\n-----------------------------------------------\n"
                )   

##  * A complete list of candidates who received votes (x in names)
##  * The percentage of votes each candidate won       (z in percentages)
##  * The total number of votes each candidate won     (y in counts)

for x,y,z in zip(names[0::],counts[0::],percentages[0::]):
    multiplelines = multiplelines + (""+ str(x) + ": \t\t " + "(" + "{:,.0f}".format(y) + ")" +\
                                    "\t| " "{:,.0%}".format(z) + "\n"
                                    )
        
##  * The winner of the election based on popular vote.  
multiplelines = (multiplelines + \
                    "-----------------------------------------------\n" + \
                    "Winner:\t" + winnername + \
                    "\n-----------------------------------------------\n")

print (multiplelines)  

# Write the results to a file in disk
#--------------------------------------------------------------

outputfile = open('PYPOLL-VERSION1-Output-PyPoll-RafaelSantos.txt', 'w+' )

## Prompt user that file is being created
print ("\n ***** Exporting to text file *****\n")

outputfile.write("\nStudent: Rafael Santos\nHomework 3\n\n" + multiplelines)
outputfile.close()

## Prompt user process ended
print ("\n ***** Text File saved. End of the code execution *****\n")

###############################################################
# END OF CODE
###############################################################