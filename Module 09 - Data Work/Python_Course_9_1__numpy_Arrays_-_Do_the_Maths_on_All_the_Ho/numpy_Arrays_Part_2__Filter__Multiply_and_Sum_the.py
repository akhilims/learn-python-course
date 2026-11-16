# numpy Arrays Part 2: Filter, Multiply and Sum the Honey Jars
# Every cell of the notebook, in order, as one script (run: python numpy_Arrays_Part_2__Filter__Multiply_and_Sum_the.py)

# Import numpy again in a new notebook

import numpy as np
print(np.__name__, "imported")

# Store the jar counts in a numpy array

sold = np.array([12, 9, 15, 11])
print(sold)

# Boolean filter: keep markets above ten jars

print(sold[sold > 10])

# Element by element maths: jars times price

price = np.array([8, 8, 9, 9])
print(sold * price)

# A 2-D array: rows and columns

grid = np.array([[12, 9], [15, 11]])
print(grid)

# Shape and sum with axis 0

print(grid.shape, grid.sum(axis=0))
