# Cleaning messy data, Part 2: make a messy file and look at it
# Every cell of the notebook, in order, as one script (run: python Cleaning_messy_data__Part_2__make_a_messy_file_and.py)

# Load pandas and random in a new notebook

import pandas as pd
import random

# Setting up the messy spellings and values

random.seed(7)
names = ["Mill", "mill ", "HILL"]
names += ["Park", " park", "Dock"]
jars = ["12", "9", "15", "", "n/a", "-5"]
price = ["8", "8.5", "9", ""]

# Writing 1200 messy sales lines with a loop

rows = ["id,market,jars,price"]
for i in range(1200):
    m = random.choice(names)
    j = random.choice(jars)
    p = random.choice(price)
    rows.append(f"{i},{m},{j},{p}")
    if random.random() < 0.03:
        rows.append(rows[-1])

# Saving the pretend export as honey_raw.csv

with open("honey_raw.csv", "w") as f:
    f.write("\n".join(rows))

# Reading the CSV with read_csv: shape and head

raw = pd.read_csv("honey_raw.csv")
print(raw.shape)
print(raw.head())

# Counting gaps with isna().sum()

print(raw.isna().sum())

# Finding repeated rows with duplicated().sum()

print(raw.duplicated().sum())

# Counting spellings with value_counts

print(raw["market"].value_counts())
