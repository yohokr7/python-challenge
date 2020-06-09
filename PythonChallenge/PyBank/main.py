#Import Module
import os
import csv

#Create CSV Pathway
budgetcsvpath = os.path.join(".", "Resources", "budget_data.csv")

#Open CSV, Create CSV Reader, Skip Header
with open(budgetcsvpath, newline='') as budgetcsv:
    budgetreader = csv.reader(budgetcsv, delimiter = ',')
    budgetheader = next(budgetreader)
    
    #Define Variables and Lists
    totalamount = 0
    totalmonths = 0
    monthlyamount = []
    changeamount = []
    months = []
    
    #Calculate Total Months and Total P&L, Create Separate Lists for Months and Profits/Losses
    for row in budgetreader:
        amount = int(row[1])
        totalmonths = totalmonths + 1
        totalamount = totalamount + amount
        monthlyamount.append(amount)
        months.append(row[0])
        
    #Calculate Change Between Each Month Into a List
    for amountindex in range(len(monthlyamount)):
        if amountindex == 0:
            current = 0
            past = 0
        else:
            current = int(monthlyamount[amountindex])
            past = int(monthlyamount[amountindex - 1])
        
        changeamount.append(current - past)
    
    #Calculate the Average Change, Biggest Increase, and Biggest Decrease
    avgchange = sum(changeamount)/ (len(changeamount)-1)
    incchange = max(changeamount)
    decchange = min(changeamount)
    
    #Capture the List Index for Biggest Increase and Biggest Decrease
    for changeindex in range(len(changeamount)):
        if changeamount[changeindex] == incchange:
            incindex = changeindex
        if changeamount[changeindex] == decchange:
            decindex = changeindex
            
    #Find the Months Linked to the Biggest Increase and Biggest Decrease
    for monthindex in range(len(months)):
        if monthindex == incindex:
            incmonth = months[monthindex]
        if monthindex == decindex:
            decmonth = months[monthindex]
    
    #Making Financial Analysis String
    line1 = f'Financial Analysis'
    line2 = f'----------------------------'
    line3 = f'Total Months: {totalmonths}'
    line4 = f'Total: ${totalamount}'
    line5 = f'Average Change: ${avgchange}'
    line6 = f'Greatest Increase in Profits: {incmonth} (${incchange})'
    line7 = f'Greatest Decrease in Profits: {decmonth} (${decchange})'

    #Printing Financial Analysis in Terminal
    print(f'{line1}\n{line2}\n{line3}\n{line4}\n{line5}\n{line6}/n{line7}')
    
    #Determining if Analysis.txt exists in Analysis SubDirectory
    filepath = os.path.join(".","analysis","Analysis.txt")
    isfile = os.path.isfile(filepath)
    path = os.path.join(".","analysis")
    
    #If Analysis.txt Does Not Exist, Creates Analysis.txt and Populates
    if isfile == False:
        with open(os.path.join(path, "Analysis.txt"), "w") as analysis:
            analysis.write(f'{line1}\n')
            analysis.write(f'{line2}\n')
            analysis.write(f'{line3}\n')
            analysis.write(f'{line4}\n')
            analysis.write(f'{line5}\n')
            analysis.write(f'{line6}\n')
            analysis.write(f'{line7}')