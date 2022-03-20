import csv
import os
from operator import indexOf

# Define function
def average(nums):
    return sum(nums) / len(nums)

# Create paths and empty lists 
text_path = ('Analysis', 'pybank.txt')
csvpath = ('Resources', 'budget_data.csv'
with open(csvpath) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    months = []
    profit_loss = []

    # Ignore the first line with the headers
    next(csv_reader)

    for row in csv_reader:
        months.append(row[0])
        profit_loss.append(int(row[1]))

    # Calculate total months and total profit loss (length and sum respectively)
    total_months = len(months)
    total_profit_loss = sum(profit_loss)

    # Calculate the month to month change in profit / loss (next month - current month) (remember lists start at 0)
    changes = []
    for index in range(len(profit_loss) - 1):
        changes.append(profit_loss[index + 1] - profit_loss[index])

    # Calculate average change
    average_change = average(changes)

    # Calculate the biggest increase and find the month it happened in
    greatest_increase = max(changes)
    greatest_increase_month = months[indexOf(changes, greatest_increase)]

    # Calculate the biggest decrease and find the month it happened in
    greatest_decrease = min(changes)
    greatest_decrease_month = months[indexOf(changes, min(changes))]

# Print analysis 
print("Financial Analysis")
print("--------------------")
print("Total Months: " + str(total_months))
print("Total: " + str(total_profit_loss))
print("Average Change: " + str(int(average_change)))
print("Greatest Increase in Profits: " + greatest_increase_month + str(greatest_increase))
print("Greatest Decrease in Profits: " + greatest_decrease_month + str(greatest_decrease))

# Write analysis to text file
with open(text_path, "w") as file:
    file.write("Financial Analysis\n") 
    file.write("--------------------\n")
    file.write("Total Months: " + str(total_months))
    file.write("Total: " + str(total_profit_loss))
    file.write("Average Change: " + str(int(average_change)))
    file.write("Greatest Increase in Profits: " + greatest_increase_month + str(greatest_increase))
    file.write("Greatest Decrease in Profits: " + greatest_decrease_month + str(greatest_decrease))
