# Classes and Objects, Part 2
# Every cell of the notebook, in order, as one script (run: python Classes_and_Objects__Part_2.py)

# # Setting up Rex again

class Dog:
    pass
d = Dog()
d.name = "Rex"
print(d.name)

# # A second object with its own name

e = Dog()
e.name = "Bella"
print(e.name)

# # A list of objects with a for loop

pets = [d, e]
for p in pets:
    print(p.name)

# # isinstance: was it made from this class?

print(isinstance(d, Dog))
print(d.name == e.name)
