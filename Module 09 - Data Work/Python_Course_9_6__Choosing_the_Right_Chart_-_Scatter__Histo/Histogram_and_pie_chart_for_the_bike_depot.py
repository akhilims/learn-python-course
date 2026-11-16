# Histogram and pie chart for the bike depot
# Every cell of the notebook, in order, as one script (run: python Histogram_and_pie_chart_for_the_bike_depot.py)

# Load pandas and matplotlib

import pandas as pd
import matplotlib.pyplot as plt

# Read the real day.csv file

days = pd.read_csv("day.csv")

# Histogram: how many bikes on a normal day

plt.hist(days["cnt"], bins=20)
plt.title("Bikes rented per day")
plt.xlabel("Bikes")
plt.ylabel("Days")
plt.show()

# Season totals with groupby

season = days.groupby("season")["cnt"].sum()

# Season names for the pie labels

names = ["Winter","Spring","Summer","Fall"]

# Pie chart: share of bikes by season

plt.pie(season, labels=names)
plt.title("Share of bikes by season")
plt.show()
