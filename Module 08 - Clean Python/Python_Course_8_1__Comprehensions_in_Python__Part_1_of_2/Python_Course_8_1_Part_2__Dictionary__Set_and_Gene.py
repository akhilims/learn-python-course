# Python Course 8.1 Part 2: Dictionary, Set and Generator Comprehensions
# Every cell of the notebook, in order, as one script (run: python Python_Course_8_1_Part_2__Dictionary__Set_and_Gene.py)

# Setup: the running club data again

runs = [3, 8, 5, 10, 2]
totals = {
    "Asha": 3, "Ben": 8,
    "Chen": 5, "Dev": 10,
    "Esha": 2}
cities = ["Pune", "Goa", "Pune",
          "Delhi", "Goa"]

# Dictionary comprehension: build a lookup table

points = {name: km * 10
          for name, km in totals.items()}
print(points)

# Dictionary comprehension with a condition

long = {name: km
        for name, km in totals.items()
        if km >= 5}
print(long)

# Set comprehension: remove duplicate cities

unique = {c.upper() for c in cities}
print(sorted(unique))

# Round brackets make a generator expression

tens = (km * 10 for km in runs)
print(type(tens))

# Get a real tuple with tuple()

print(tuple(km * 10 for km in runs))
