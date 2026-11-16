# Bar charts for the bike depot
# Every cell of the notebook, in order, as one script (run: python Bar_charts_for_the_bike_depot.py)

# Load pandas and matplotlib again

import pandas as pd
import matplotlib.pyplot as plt

# Read the real day.csv file

days = pd.read_csv("day.csv")

# Total bikes per season with groupby

season = days.groupby("season")["cnt"].sum()
names = ["Winter", "Spring",
         "Summer", "Fall"]

# A bar chart compares the seasons

plt.bar(names, season)
plt.show()

# Bar chart with a title and axis name

plt.bar(names, season)
plt.title("Bikes rented per season")
plt.ylabel("Bikes")
plt.show()
