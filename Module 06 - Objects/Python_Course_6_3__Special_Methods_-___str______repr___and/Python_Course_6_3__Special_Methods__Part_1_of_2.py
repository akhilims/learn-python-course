# Python Course 6.3: Special Methods (Part 1 of 2)
# Every cell of the notebook, in order, as one script (run: python Python_Course_6_3__Special_Methods__Part_1_of_2.py)

# A simple Book class

class Book:
    def __init__(self, title):
        self.title = title

# Printing an object without __str__

b = Book("Python 101")
print(b)

# Printing objects nicely with __str__

class Book:
    def __init__(self, title):
        self.title = title
    def __str__(self):
        return self.title
print(Book("Python 101"))
