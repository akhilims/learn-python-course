# Your own modules: parse.py, main.py, stats.py, report.py
# Every cell of the notebook, in order, as one script (run: python Your_own_modules__parse_py__main_py__stats_py__rep.py)

# Creating your own module: parse.py

# Importing your module from main.py

# Running python main.py in the terminal

# A second module: stats.py with a guard line

# Running stats.py directly runs its test

# A third file that imports stats

# Why the guard line stays quiet on import

# The `__name__` of an imported module

import stats
print(stats.__name__)
