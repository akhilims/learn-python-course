# Line charts for the bike depot
# Every cell of the notebook, in order, as one script (run: python Line_charts_for_the_bike_depot.py)

# Import pandas and matplotlib pyplot

import pandas as pd
import matplotlib.pyplot as plt

# Load the real bike data with read_csv

days = pd.read_csv("day.csv")

# Monthly totals with groupby and sum

month = days.groupby("mnth")["cnt"].sum()
print(month.head(3))

# A first line chart with plt.plot

plt.plot(month)
plt.show()

# Chart title and axis labels

plt.plot(month)
plt.title("Bikes rented per month")
plt.xlabel("Month")
plt.ylabel("Bikes")
plt.show()
