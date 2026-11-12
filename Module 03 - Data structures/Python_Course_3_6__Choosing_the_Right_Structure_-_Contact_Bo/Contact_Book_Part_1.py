# Contact Book Part 1
# Every cell of the notebook, in order, as one script (run: python Contact_Book_Part_1.py)

# Contact book: a list of tuples

people = []
people.append(("Asha", "555-0101", "Pune"))
people.append(("Ben", "555-0102", "Delhi"))
print(len(people))

# Dictionary lookup: find a phone by name

book = {}
for name, phone, city in people:
    book[name] = phone
print(book)

# Ask for a name with input and get

name = input("Name? ")
print(book.get(name, "Not found"))
