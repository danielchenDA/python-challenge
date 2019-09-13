# import dependencies
import os
import csv

# define variables
total_months = 0
net_profit_or_losses = 0
greatest_profit_increase = 0
greatest_profit_increase_month = ""
greatest_profit_decrease = 0
greatest_profit_decrease_month = ""
average_change = 0

# assign csv file path to a variable
csv_budget_data_path = os.path.join('..','PyBank','budget_data.csv')

# open csv file using csvreader
with open(csv_budget_data_path, newline='') as csv_budget_data:
    # define csvreader to read the file
    csvreader = csv.reader(csv_budget_data, delimiter=',')
    # checks to see if the file is read in correctly
    # print(csvreader)
    # read header to skip the header information
    csv_header = next(csvreader)
    # read each row of data after the csv_header
    for row in csvreader:
        # calculate total # of months included in the dataset
        total_months += 1
        # calculate net total amount of "Profit/Losses" over the entire period
        net_profit_or_losses += int(row[1])
        # find greatest profit increase over the entire period
        if int(row[1]) >= greatest_profit_increase:
            greatest_profit_increase = int(row[1])
            greatest_profit_increase_month = row[0]
        # find greatest profit decrease over the entire period
        if int(row[1]) <= greatest_profit_decrease:
            greatest_profit_decrease = int(row[1])
            greatest_profit_decrease_month = row[0]

# calculate average changes in "Profit/Losses" over the entire period
average_change = net_profit_or_losses / total_months

# print to results to terminal
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_profit_or_losses}")
print("")
print(f"Average Change: ${int(average_change)}")
print(f"Greatest Increase in Profits: {greatest_profit_increase_month} (${greatest_profit_increase})")
print(f"Greatest Decrease in Profits: {greatest_profit_decrease_month} (${greatest_profit_decrease})")
print("----------------------------")

# designate file path and file name
file = "../PyBank/Financial_Analysis.txt"

# open and write to file
with open(file, "w") as Financial_Analysis_txt:
    Financial_Analysis_txt.write("Financial Analysis\n")
    Financial_Analysis_txt.write("----------------------------\n")
    Financial_Analysis_txt.write(f"Total Months: {total_months}\n")
    Financial_Analysis_txt.write(f"Total: ${net_profit_or_losses}\n")
    Financial_Analysis_txt.write("\n")
    Financial_Analysis_txt.write(f"Average Change: ${int(average_change)}\n")
    Financial_Analysis_txt.write(f"Greatest Increase in Profits: {greatest_profit_increase_month} (${greatest_profit_increase})\n")
    Financial_Analysis_txt.write(f"Greatest Decrease in Profits: {greatest_profit_decrease_month} (${greatest_profit_decrease})\n")
    Financial_Analysis_txt.write("----------------------------")
