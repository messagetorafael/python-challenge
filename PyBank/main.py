###############################################################
# PROMPT MESSAGE SO THAT USER KNOWS THE CODE IS RUNNING....
###############################################################

print("\nOK!: PyBank code is now running!!!\n\n\n\n")

# IMPORT MODULES
#--------------------------------------------------------------
import os
import csv
    
# Set path for file
#--------------------------------------------------------------
csvfile = os.path.join("..", "PyBank\Resources", "budget_data.csv")

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
outputfile = open('outputPyBank-RafaelSantos.txt', 'w+' )

## Prompt user that file is being created
print ("\n ***** Exporting to text file *****\n")

outputfile.write("\nStudent: Rafael Santos\nHomework 3\n\n" + multilines)
outputfile.close()

## Prompt user process ended
print ("\n ***** Text File saved. End of the PyBank code execution *****\n")


################################################################
#END 
###############################################################
