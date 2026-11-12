# Python sets
# Every cell of the notebook, in order, as one script (run: python Python_sets.py)

# Python sets: store unique items

tickets = {7, 3, 7, 5}
print(tickets)
print(len(tickets))

# Changing a set: add, remove, discard

tickets.add(9)
tickets.add(7)
print(tickets)

# Fast checks and removing duplicates

print(7 in tickets)
nums = [1, 2, 2, 3, 3, 3]
print(set(nums))

# Set operations: union and intersection

a = {1, 2, 3}
b = {2, 3, 4}
print(a | b)
print(a & b)
