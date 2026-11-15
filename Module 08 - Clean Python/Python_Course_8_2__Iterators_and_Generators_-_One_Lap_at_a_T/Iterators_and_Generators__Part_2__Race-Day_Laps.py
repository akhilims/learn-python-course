# Iterators and Generators, Part 2: Race-Day Laps
# Every cell of the notebook, in order, as one script (run: python Iterators_and_Generators__Part_2__Race-Day_Laps.py)

# Lap times: a fresh notebook

times = [62, 58, 61, 55]
print(times)

# A generator function with yield

def fast_laps(times):
    for t in times:
        if t < 60:
            yield t

print(list(fast_laps(times)))

# Asking a generator for values with next()

g = fast_laps(times)
print(next(g))
print(next(g))

# sum() asks a generator for every value

print(sum(fast_laps(times)))

# Generator expressions: a million values, no memory

big = (n * 2 for n in range(1000000))
print(next(big))
print(next(big))
