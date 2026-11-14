# Classes and Objects, Part 1
# Every cell of the notebook, in order, as one script (run: python Classes_and_Objects__Part_1.py)

# A class is a blueprint

class Dog:
    pass

# Make an object from a class

d = Dog()
print(type(d))

# Give an object its own values

d.name = "Rex"
d.age = 3
print(d.name, d.age)
