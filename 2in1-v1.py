#STUDENT: RAFAEL SANTOS         #HOME WORK 3
#Data Analystics and Visualization Cohort 3

#2in1-VERSION 1
#### THIS VERSION CONTAINS PYPOLL-V1 AND PYBANK-VERSION2 SCRIPTS + WITH AN INTERACTIVE MENU. 
#### THIS VERSION OF INTERACTIVE MENU DOES NOT CLEAR THE SCREEN AS MENU OPTIONS ARE SELECTED (DONE IN VERSION 2)
#### NOTE: THIS VERSION IS AVAILABLE IN CASE THERE ARE ISSUES RUNNING THE CODE ON A MAC COMPUTER.


print("\n '2in1' code is running\n\n")

# IMPORT MODULES
#--------------------------------------------------------------
import os
import csv
from collections import Counter

###############################################################
#BEGIN: PYPOLL FUNCTION (USER DEFINED) - MAIN SUB ROUTINE
###############################################################

def PyPoll(py):
    
    print("\nOK!" + str(py) + ": PyPoll code is now running!!!\n\n\n\n")
    
    # Set path for file
    #--------------------------------------------------------------
    csvfile = os.path.join("..", "Python-challenge\PyPoll\Resources", "election_data.csv")

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

    # Determine consolidated votes per candidate [use of dictionary]
    #--------------------------------------------------------------
    votestotals =[]
                                        #imported module for this command Counter
    votestotals = Counter(Candidate)    #output=Counter({'Khan': 2218231, 'Correy': 704200, 'Li': 492940, "O'Tooley": 105630})

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

    # Write the results to a file in disk, creating if not existent.
    #--------------------------------------------------------------
    outputfile = open('..\Python-challenge\PyPoll\.2in1outputPyPoll-RafaelSantos.txt', 'w+' )

    ## Prompt user that file is being created
    print ("\n ***** Exporting to text file *****\n")

    outputfile.write("\nStudent: Rafael Santos\nHomework 3\n\n" + multiplelines)
    outputfile.close()

    ## Prompt user process ended
    print ("\n ***** Text File saved. End of the PyPoll code execution *****\n")

###############################################################
#END: PYPOLL FUNCTION (USER DEFINED) - SUBROUTINE
###############################################################

#*********************************************************************************************   

###############################################################
#BEGIN: PYBANK FUNCTION (USER DEFINED) - SUBROUTINE
###############################################################

def PyBank(py):
    print("\nOK!" + str(py) + ": PyBank code is now running!!!\n\n\n\n")
    
    # Set path for file
    #--------------------------------------------------------------
    csvfile = os.path.join("..", "Python-challenge\PyBank\Resources", "budget_data.csv")

    # lists to store data
    #--------------------------------------------------------------
    DateList = []                   #list to hold the split of data with DateList
    ProfitLossList = []             #list to hold the split of data with Profit/Loss
    AvgChg = []                     #list for the difference Month-over-Month


    # Store "Dates" and "Profit/Loss" data on specific lists
    #--------------------------------------------------------------
    with open(csvfile,'r') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=",")
    
        csvheader = next(csvfile,None)

        for row in csvreader:
            
            DateList.append(row[0])
            ProfitLossList.append(int(row[1]))   

    # Determine the total number of months reported in the list
    #--------------------------------------------------------------
    TotalMonths = len(DateList)                                 #calculate Total Months

    # Calculate and store month-over-month "Profit/Loss" difference
    #--------------------------------------------------------------
    for x,y in zip(ProfitLossList[0::],ProfitLossList[1::]):    #calculate the difference Month-over-Month

        AvgChg.append (y-x)

    # Then determine the Average of these monthly differences
    #--------------------------------------------------------------
    Avg = sum(AvgChg) / len(AvgChg)                             #calculate Average Change

    # Then determine the Greatest Decrease or Increase
    #--------------------------------------------------------------
    AvgGDecrease = min(AvgChg)                                  #calculate Greatest Decrease "Profit/Loss" value
    AvgGIncrease = max(AvgChg)                                  #calculate Greatest Increase "Profit/Loss" value

    ##identify index for Greatest Increase in Profits
    AvgGIncreaseIndex = [i+1 for i in range(len(AvgChg)) if AvgChg[i]==AvgGIncrease]    
    AvgGIncreaseIndex = AvgGIncreaseIndex.pop(0)

    ##identify index for Greatest Decrease in Profits
    AvgGDecreaseIndex = [i+1 for i in range(len(AvgChg)) if AvgChg[i]==AvgGDecrease]
    AvgGDecreaseIndex = AvgGDecreaseIndex.pop(0)

    ##use index values identified to determine respective value within Dates list [array]
    aabb = AvgGIncreaseIndex
    AvgGIncreaseDate = DateList[aabb]               #identifying Greatest Decrease "Profit/Loss" Month

    aacc = AvgGDecreaseIndex        
    AvgGDecreaseDate = DateList[aacc]               #identifying Greatest Increase "Profit/Loss" Month


    # Create string to print Summary
    #--------------------------------------------------------------
    summarytop = ("\n \n Financial Analysis - PyBank \n ---------------------------------------")
    summarytotals = (" Total Months: " + str(TotalMonths) + "\n Total: $" + "{:,.2f}".format(sum(ProfitLossList)))
    averagechange = (" Average Change: $" + "{:,.2f}".format(Avg))
    gdpnumber = (" Greatest Decrease in Profits: $"+"{:,.0f}".format(AvgGDecrease))
    gipnumber = (" Greatest Increase in Profits: $"+"{:,.0f}".format(AvgGIncrease))
    greatest =  (gdpnumber + " (" + AvgGDecreaseDate + ")" + "\n" + gipnumber + " (" + AvgGIncreaseDate + ")")

    multilines = (summarytop +"\n"+ summarytotals +"\n"+ averagechange +"\n"+  greatest)
    print (multilines)

    # Export Summary to a file on disk, creating if not existent.
    #--------------------------------------------------------------
    outputfile = open('..\Python-challenge\PyBank\.2in1outputPyBank-RafaelSantos.txt', 'w+' )

    ## Prompt user that file is being created
    print ("\n ***** Exporting to text file *****\n")

    outputfile.write("\nStudent: Rafael Santos\nHomework 3\n\n" + multilines)
    outputfile.close()

    ## Prompt user process ended
    print ("\n ***** Text File saved. End of the PyBank code execution *****\n")


################################################################
#END: PYBANK FUNCTION (USER DEFINED) - MAIN SUBROUTINE
###############################################################

#*********************************************************************************************

###############################################################
# MAIN CODE  - MAIN WHILE LOOP
###############################################################
abc = 0
aacc = 0
endcode = False
while (endcode == False and aacc != 3):

    menuoptions =  ("\n\t\t *** MAIN MENU ***\n\n" + \
                "Type the number of the data you want to review:\n\n"+ \
                "(1)\t PyBank\n" +\
                "(2)\t PyPoll\n" +\
                "(3)\t None of the above (exit code).\n\n" +\
                "Your choice is option number: ")

    option = input(menuoptions)
    aacc = int(option)

    if aacc == 3:
        print("\t\tOK!!!")
        endcode = True
    else:
        abc = aacc
    # SECONDARY WHILE LOOP - MAIN MENU TO CALL USER DEFINED FUNCTIONS
    ###############################################################

        while abc != 3:
        
            if abc == 1:        # calls the subroutine AND forces to exit this loop and go to the Main Loop
                py = str(abc)
                PyBank(py)
                abc = 3
                aacc = 0

            elif abc == 2:      # calls the subroutine AND forces to exit this loop and go to the Main Loop
                py = str(abc)
                PyPoll(py)
                abc = 3
                aacc = 0
            else:               # this prompts the user to type a valid option
                print ("\n\t\t***TYPO CAUSED ERROR!***\n Please follow the instruction below.")
                option = input(menuoptions)
                abc = int(option)

    # SECONDARY WHILE LOOP - PROMPT USER TO RESTART OR EXIT MAIN LOOP
    ##################################################################

    while abc == 3:
        # allow user to return to the main menu to run another or same subroutine
        optionexit = input("\n\n\n **You are about to exit the main program**.\n\n\n" + \
                           "\tGo back to MAIN MENU?\n" + \
                           "\tType:\n" + \
                            "\t 1 = yes\n" + \
                            "\t 2 = no, let me out, right now!\n\n" +\
                            "\t Your choice is option number: ")
        
        optionexit = int(optionexit)
        
        if optionexit == 1:     # this forces to exit this loop AND and return to MAIN loop (main menu)
            abc = 0
            endcode = False
        elif optionexit == 2:   # this forces to exit all loops AND end the code execution
            abc = 0
            endcode = True
        else:                   # this prompts the user to type a valid option
            print ("\n\t\t***TYPO CAUSED ERROR!***\n Please follow the instruction below.\n")
            optionexit = input("\n\n\n\t Go back to MAIN MENU?\n" + \
                               "\tType:\n" + \
                               "\t 1 = yes\n" + \
                               "\t 2 = no\n\n")
        
            optionexit = int(optionexit)

print("\n\t This is end of '2in1'code execution. See you later!")

#*********************************************************************************************   

###############################################################
# END OF MAIN CODE  - MAIN WHILE LOOP
###############################################################