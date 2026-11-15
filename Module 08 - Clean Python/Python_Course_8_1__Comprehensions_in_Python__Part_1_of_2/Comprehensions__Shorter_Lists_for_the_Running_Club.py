# Comprehensions: Shorter Lists for the Running Club
# Every cell of the notebook, in order, as one script (run: python Comprehensions__Shorter_Lists_for_the_Running_Club.py)

# ## Weekly kilometres of five runs

runs = [3, 8, 5, 10, 2]

# ## The old way: empty list, loop, append

points = []
for km in runs:
    points.append(km * 10)
print(points)

# ## List comprehension: the same result in one line

points = [km * 10 for km in runs]
print(points)

# ## The condition: keep only the long runs

long_runs = [km for km in runs if km >= 5]
print(long_runs)

# ## Change and filter in one comprehension

bonus = [km * 10 for km in runs if km >= 5]
print(bonus)
