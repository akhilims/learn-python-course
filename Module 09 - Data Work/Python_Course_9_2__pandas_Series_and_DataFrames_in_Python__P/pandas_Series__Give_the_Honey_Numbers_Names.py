# pandas Series: Give the Honey Numbers Names
# Every cell of the notebook, in order, as one script (run: python pandas_Series__Give_the_Honey_Numbers_Names.py)

# Import pandas as pd: the library for tables

import pandas as pd
print("pandas imported as pd:", pd.__name__)

# Two plain lists: jar counts and market names

sold = [12, 9, 15, 11]
names = ["Mill", "Hill", "Park", "Dock"]
print(sold)
print(names)

# Series: every number gets a name

jars = pd.Series(sold, index=names)
print(jars)

# Look up a value by its name

print(jars["Hill"])

# max and idxmax: find the best market

print(jars.max(), jars.idxmax())

# Filter a Series with a condition

print(jars[jars > 10])
