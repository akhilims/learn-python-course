# Expense Tracker That Saves to a File - Part 2
# Every cell of the notebook, in order, as one script (run: python Expense_Tracker_That_Saves_to_a_File_-_Part_2.py)

# Setup: save the starting expenses to a csv file

import csv
expenses = [("tea", 20), ("bus", 35)]
with open("expenses.csv", "w",
          newline="") as f:
    csv.writer(f).writerows(expenses)

# Add an expense with input() and int()

name = input("Expense? ")
cost = int(input("Cost? "))
expenses.append((name, cost))

# Load the saved expenses with csv.reader

with open("expenses.csv") as f:
    for row in csv.reader(f):
        print(row[0], row[1])

# Handle a missing file with try and except

try:
    open("old.csv")
except FileNotFoundError:
    print("No old file yet")
