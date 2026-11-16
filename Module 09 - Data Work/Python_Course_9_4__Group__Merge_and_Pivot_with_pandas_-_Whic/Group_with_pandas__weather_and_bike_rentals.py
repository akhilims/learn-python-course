# Group with pandas: weather and bike rentals
# Every cell of the notebook, in order, as one script (run: python Group_with_pandas__weather_and_bike_rentals.py)

# Import pandas, the tool for tables

import pandas as pd

# read_csv: load day.csv into a table

days = pd.read_csv("day.csv")

# shape: rows and columns of the table

print(days.shape)

# mean: one average for all days

print(days["cnt"].mean().round(0))

# groupby: split the days into weather piles

by_sky = days.groupby("weathersit")["cnt"]

# mean per pile: clear, misty, rainy

print(by_sky.mean().round(0))

# agg: count, mean and max at once

print(by_sky.agg(["count", "mean", "max"]).round(0))
