# Cleaning Messy Data with pandas, Part 1
# Every cell of the notebook, in order, as one script (run: python Cleaning_Messy_Data_with_pandas__Part_1.py)

# Load pandas, the tool for tables

import pandas as pd

# Five messy lines of the honey order sheet

market = ["Mill", "mill ", "HILL"]
market += ["Park", "Park"]
jars = [12, 9, None, 15, 15]

# Build the DataFrame and see every problem

data = {"market": market, "jars": jars}
table = pd.DataFrame(data)
print(table)

# Count the missing values with isna().sum()

print(table.isna().sum())

# Drop rows with gaps using dropna

table = table.dropna()
print(table)

# Find duplicate rows with duplicated().sum()

print(table.duplicated().sum())

# Remove repeats with drop_duplicates

table = table.drop_duplicates()
print(table)

# Make spelling the same with str.strip and str.title

names = table["market"].str.strip()
table["market"] = names.str.title()
print(table)
