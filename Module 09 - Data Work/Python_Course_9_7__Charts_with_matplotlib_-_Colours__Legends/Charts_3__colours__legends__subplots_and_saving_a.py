# Charts 3: colours, legends, subplots and saving a PNG
# Every cell of the notebook, in order, as one script (run: python Charts_3__colours__legends__subplots_and_saving_a.py)

# Load pandas and matplotlib

import pandas as pd
import matplotlib.pyplot as plt

# Read the bike sharing file day.csv

days = pd.read_csv("day.csv")

# Bikes per month and year with pivot_table

table = days.pivot_table("cnt", "mnth",
    "yr", aggfunc="sum")
print(table.head(3))

# Two lines, colours, labels and a legend

plt.plot(table[0], color="orange",
         label="2011")
plt.plot(table[1], color="blue",
         label="2012")
plt.legend()
plt.show()

# Subplots: two charts side by side

fig, ax = plt.subplots(1, 2)
ax[0].plot(table[0], color="orange")
ax[0].set_title("2011")
ax[1].plot(table[1], color="blue")
ax[1].set_title("2012")
plt.show()

# Save the chart as a PNG with savefig

fig.savefig("years.png")
