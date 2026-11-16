# pandas DataFrames: the honey market table
# Every cell of the notebook, in order, as one script (run: python pandas_DataFrames__the_honey_market_table.py)

# Import pandas again in a new notebook

import pandas as pd
print("pandas imported as pd")

# Three plain lists: jars, market names, prices

sold = [12, 9, 15, 11]
names = ["Mill", "Hill", "Park", "Dock"]
price = [8, 8, 9, 9]
print(sold, names, price)

# Build a DataFrame table with jars and price

data = {"jars": sold, "price": price}
table = pd.DataFrame(data, index=names)
print(table)

# Add a money column made from two columns

money = table["jars"] * table["price"]
table["money"] = money
print(table)

# Look up one row with loc

print(table.loc["Park"])

# Total money with sum

print(table["money"].sum())
