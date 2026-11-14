# Library Management System - Part 1
# Every cell of the notebook, in order, as one script (run: python Library_Management_System_-_Part_1.py)

# ## A Library class with a dictionary of books

class Library:
    def __init__(self):
        self.books = {}
    def add(self, title):
        self.books[title] = False

# ## Create a library and add books

lib = Library()
lib.add("Python")
lib.add("Maths")
print(lib.books)

# ## Show the library shelf with a for loop

for title in lib.books:
    print(title, lib.books[title])
