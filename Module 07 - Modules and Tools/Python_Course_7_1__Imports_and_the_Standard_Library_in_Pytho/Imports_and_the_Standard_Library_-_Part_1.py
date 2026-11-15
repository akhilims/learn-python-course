# Imports and the Standard Library - Part 1
# Every cell of the notebook, in order, as one script (run: python Imports_and_the_Standard_Library_-_Part_1.py)

# ## Import a module: math.ceil rounds up

import math
print(math.ceil(4300 / 1000))

# ## from-import and import as: floor and sqrt

from math import floor
print(floor(4300 / 1000))
import math as m
print(m.sqrt(64))

# ## round: halves go to the nearest even number

print(round(4300 / 1000, 1))
print(round(2.5))
print(round(3.5))

# ## Comparing decimals: why isclose beats ==

print(0.1 + 0.2 == 0.3)
print(math.isclose(0.1 + 0.2, 0.3))

# ## random.choice with a seed: who takes the call

import random
random.seed(7)
team = ['sara', 'omar', 'amit', 'lina']
print(random.choice(team))

# ## random.randint and random.sample

random.seed(7)
print(random.randint(1, 6))
print(random.sample(team, 2))

# ## random.shuffle: mix a list in place

random.seed(7)
random.shuffle(team)
print(team)
