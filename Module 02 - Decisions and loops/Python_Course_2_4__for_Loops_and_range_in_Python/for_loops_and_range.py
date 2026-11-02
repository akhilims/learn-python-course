# for loops and range
# Every cell of the notebook, in order, as one script (run: python for_loops_and_range.py)

# ## Counting with for and range

for number in range(5):
    print("Hello", number)

# ## Start and stop with range

for day in range(1, 6):
    print("Day", day)

# ## A common mistake: a loop needs a range

for day in 5:
    print(day)

# ## Adding a week of bus fares

total = 0
for day in range(1, 6):
    total = total + 20
    print("Day", day, "total", total)

# ## Counting down with a step

for second in range(5, 0, -1):
    print(second)
print("Go!")
