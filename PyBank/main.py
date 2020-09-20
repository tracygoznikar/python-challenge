#import modules
import os
import csv

budgetdate = 0
profit_loss = 0
increase_profit = 0
decrease_profit = 0
average_profit = 0

#write file path
csvpath = os.path.join('Resources', 'budget_data.csv')
outpath = os.path.join('analysis', 'output.txt')

# identify values
with open(csvpath) as csvfile:
    # CSV reader and specify delimiter, print
    csvreader = csv.DictReader(csvfile, delimiter=',')
    print(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    for row in csvreader.fieldnames:
    
        
        
        break
        #total number of months in the dataset


#the net total amount of "Profit/Losses" over the entire period


#the average of the changes in "Profit/Losses" over the entire period


#the greatest increase in profits (date and amount) over the entire period


#the greatest decrease in losses (date and amount) over the entire 