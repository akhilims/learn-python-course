# Cleaning the honey sales file (Part 3 of 3)
# Every cell of the notebook, in order, as one script (run: python Cleaning_the_honey_sales_file__Part_3_of_3.py)

# Load pandas in a new notebook

import pandas as pd

# Read the messy honey file

raw = pd.read_csv("honey_raw.csv")

# Fix market spelling with str.strip and str.title

names = raw["market"].str.strip()
raw["market"] = names.str.title()
print(raw["market"].value_counts())

# Fill missing prices with the median

mid = raw["price"].median()
raw["price"] = raw["price"].fillna(mid)
print(raw["price"].isna().sum())

# Remove repeated rows with drop_duplicates

clean = raw.drop_duplicates()
print(clean.shape)

# Drop rows with missing jars using dropna

clean = clean.dropna(subset=["jars"])
print(clean.shape)

# Keep only possible jar counts with a condition

clean = clean[clean["jars"] > 0]
print(clean.shape)

# Convert jars to whole numbers with astype

whole = clean["jars"].astype("int64")
clean["jars"] = whole
print(clean.dtypes)

# Save the clean table with to_csv

clean.to_csv("honey_clean.csv", index=False)
print(clean.head())

# Read the clean file back as proof

print(pd.read_csv("honey_clean.csv").shape)
