# numpy Arrays: Honey Jars Part 1
# Every cell of the notebook, in order, as one script (run: python numpy_Arrays__Honey_Jars_Part_1.py)

# Import numpy as np

import numpy as np
print("numpy is ready as np")

# A plain list of jars sold

jars = [12, 9, 15, 11]
print(jars)

# A list times 2 repeats the list

print(jars * 2)

# np.array: turn the list into an array

sold = np.array(jars)
print(sold)

# An array times 2 doubles every number

print(sold * 2)

# sum and mean: total and average

print(sold.sum(), sold.mean())
