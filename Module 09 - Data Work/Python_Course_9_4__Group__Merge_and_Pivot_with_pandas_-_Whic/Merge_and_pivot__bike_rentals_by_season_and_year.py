# Merge and pivot: bike rentals by season and year
# Every cell of the notebook, in order, as one script (run: python Merge_and_pivot__bike_rentals_by_season_and_year.py)

# Load pandas and day.csv again

import pandas as pd
days = pd.read_csv("day.csv")

# Lookup lists: season codes and names

codes = [1, 2, 3, 4]
words = ["Winter", "Spring", "Summer", "Fall"]

# Build a lookup table with a dictionary

data = {"season": codes}
data["season_name"] = words
names = pd.DataFrame(data)
print(names)

# Merge: add season names to every day

both = days.merge(names, on="season")
cols = ["dteday", "season_name", "cnt"]
print(both[cols].head(3))

# Groupby with real season names

by_name = both.groupby("season_name")["cnt"]
print(by_name.mean().round(0))

# pivot_table: season by year

table = both.pivot_table("cnt", "season_name", "yr")
print(table.round(0))
