# Iterators: one lap at a time
# Every cell of the notebook, in order, as one script (run: python Iterators__one_lap_at_a_time.py)

# Iterable: a list of lap times

laps = [62, 58, 61]

# iter() and next(): ask for one lap

it = iter(laps)
print(next(it))

# next() again: the iterator remembers

print(next(it))
print(next(it))

# The default value of next()

print(next(it, "done"))

# The for loop uses iter() and next()

for lap in laps:
    print(lap)
