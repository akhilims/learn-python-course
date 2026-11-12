# Tuples and Unpacking
# Every cell of the notebook, in order, as one script (run: python Tuples_and_Unpacking.py)

# Tuples: a list that cannot change

point = (3, 7)
print(point)
print(point[0])

# The TypeError: tuples cannot be changed

point[0] = 9
point = (9, 7)
print(point)

# Tuple unpacking: split a tuple into names

x, y = point
print(x, y)
x, y = y, x
print(x, y)

# Real example: unpacking a cinema ticket

ticket = ("Inception", "B12", 9.5)
movie, seat, price = ticket
print(f"{movie} {seat} ${price:.2f}")
