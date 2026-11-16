# Choosing the Right Chart: Scatter for the Bike Depot
# Every cell of the notebook, in order, as one script (run: python Choosing_the_Right_Chart__Scatter_for_the_Bike_Dep.py)

# Load pandas and matplotlib again

import pandas as pd
import matplotlib.pyplot as plt

# Read day.csv, 731 real days

days = pd.read_csv("day.csv")

# Scatter chart: do warm days rent more bikes?

plt.scatter(days["temp"], days["cnt"])
plt.title("Warmer days, more bikes")
plt.xlabel("Temperature")
plt.ylabel("Bikes")
plt.show()
