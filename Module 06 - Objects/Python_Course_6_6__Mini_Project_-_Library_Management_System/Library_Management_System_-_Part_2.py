# Library Management System - Part 2
# Every cell of the notebook, in order, as one script (run: python Library_Management_System_-_Part_2.py)

# Setup: the Library class again

class Library:
    def __init__(self):
        self.books = {}
    def add(self, title):
        self.books[title] = False

print("Library class defined:", Library)
print("Methods:", [m for m in dir(Library) if not m.startswith("__")])

# Inheritance: LendingLibrary with borrow and give_back

class LendingLibrary(Library):
    def borrow(self, title):
        self.books[title] = True
    def give_back(self, title):
        self.books[title] = False

print("LendingLibrary inherits from:", LendingLibrary.__bases__[0].__name__)
print("Methods:", [m for m in dir(LendingLibrary) if not m.startswith("__")])

# Borrowing a book from the lending library

lib = LendingLibrary()
lib.add("Python")
lib.borrow("Python")
print(lib.books)

# Report: which books are out

for title in lib.books:
    if lib.books[title]:
        print(title, "is out")
