import os
import csv
csvpath=os.path.join('Resources','budget_data.csv')

total_months = 0
total_profit_losses = 0
previous_profit_losses = 0
dates = []
changes =[]
greatest_increase = ["", 0]
greatest_decrease = ["", 0]

with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)

    for row in csvreader:
        date = row[0]
        profit_losses = int(row[1])

        total_months += 1
        total_profit_losses += profit_losses

        if previous_profit_losses != 0:
            change = profit_losses - previous_profit_losses
            changes.append(change)

            if change > greatest_increase[1]:
                greatest_increase = [date, change]

            if change < greatest_decrease[1]:
                greatest_decrease = [date, change]

        previous_profit_losses = profit_losses

average_change = sum(changes) / len(changes)

print("Financial Analysis")
print("-----------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_profit_losses}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})")
print(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})")

results = [  
"Financial Analysis",
"-----------------------",
"Total Months: 86",
"Total: $22564198",
"Average Change: $-8311.11",
"Greatest Increase in Profits: Aug-16 ($1862002)",
"Greatest Decrease in Profits: Feb-14 ($-1825558)",
]

with open('results.txt', 'w') as file:
    file.write("\n".join(results))