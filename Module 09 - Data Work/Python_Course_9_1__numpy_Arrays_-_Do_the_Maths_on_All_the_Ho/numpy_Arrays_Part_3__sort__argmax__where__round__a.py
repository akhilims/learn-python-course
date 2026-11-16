# numpy Arrays Part 3: sort, argmax, where, round, arange, cumsum
# Every cell of the notebook, in order, as one script (run: python numpy_Arrays_Part_3__sort__argmax__where__round__a.py)

# Import numpy in a new notebook

import numpy as np

# Store the jar counts in an array

sold = np.array([12, 9, 15, 11])

# np.sort: jar counts in order

print(np.sort(sold))

# np.argmax: the position of the biggest

print(np.argmax(sold))

# np.where: label markets good or slow

print(np.where(sold > 10, "good", "slow"))

# Prices per jar as an array

price = np.array([8.4, 8.4, 9.2, 9.2])

# np.round: money in whole numbers

print(np.round(sold * price))

# np.arange: counting numbers made for you

weeks = np.arange(1, 5)
print(weeks)

# np.cumsum: the running total

weekly = np.array([47, 52, 44, 60])
print(np.cumsum(weekly))

# Index: one number by its position

print(sold[0], sold[-1])

# Slicing: a piece of the array

print(sold[1:3])
