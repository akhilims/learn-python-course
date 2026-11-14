# Special Methods: __repr__ and __eq__
# Every cell of the notebook, in order, as one script (run: python Special_Methods____repr___and___eq.py)

# ## __repr__: how objects show in a list

class Book:
    def __init__(self, title):
        self.title = title
    def __repr__(self):
        return f"Book('{self.title}')"
print([Book("Python 101")])

# ## __eq__: what == means for our books

class Book:
    def __init__(self, title):
        self.title = title
    def __eq__(self, other):
        return self.title == other.title

# ## == versus is: equal or the same object

a = Book("Python 101")
b = Book("Python 101")
print(a == b)
print(a is b)
