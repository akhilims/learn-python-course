# Expense Tracker Part 1
# Every cell of the notebook, in order, as one script (run: python Expense_Tracker_Part_1.py)

# Keeping expenses in memory: a list of tuples

expenses = []
expenses.append(("tea", 20))
expenses.append(("bus", 35))

# Adding up expenses with a for loop

total = 0
for name, cost in expenses:
    total = total + cost
print("Total:", total)

# Saving expenses to a csv file

import csv
with open("expenses.csv", "w", newline="") as f:
    writer = csv.writer(f)
    for name, cost in expenses:
        writer.writerow([name, cost])
print(open("expenses.csv").read())
