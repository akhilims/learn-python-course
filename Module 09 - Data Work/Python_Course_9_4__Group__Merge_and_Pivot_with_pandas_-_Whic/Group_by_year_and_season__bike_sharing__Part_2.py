# Group by year and season: bike sharing, Part 2
# Every cell of the notebook, in order, as one script (run: python Group_by_year_and_season__bike_sharing__Part_2.py)

# Load pandas and day.csv again

import pandas as pd
days = pd.read_csv("day.csv")

# groupby: one pile per year

by_year = days.groupby("yr")["cnt"]

# sum: total bikes per year

print(by_year.sum())

# A list of two keys: year then season

both = days.groupby(["yr", "season"])

# Total bikes for each year and season

print(both["cnt"].sum())

# Check the season codes with dteday

dates = days.groupby("season")["dteday"]

# first: the first date of each season

print(dates.first())
