# Contact Book: Choosing the Right Structure
# Every cell of the notebook, in order, as one script (run: python Contact_Book__Choosing_the_Right_Structure.py)

# Contact book: list of tuples

people = []
people.append(("Asha", "555-0101", "Pune"))
people.append(("Ben", "555-0102", "Delhi"))
print(len(people))

# Dictionary: find a phone by name

book = {}
for name, phone, city in people:
    book[name] = phone
print(book)

# Look up a contact with input

name = input("Name? ")
print(book.get(name, "Not found"))

# Add a new contact to list and dictionary

name = input("New name? ")
phone = input("Phone? ")
city = input("City? ")
people.append((name, phone, city))
book[name] = phone

# Count unique cities with a set

cities = set()
for name, phone, city in people:
    cities.add(city)
print(len(cities))

# Show the whole contact book

for name, phone in book.items():
    print(name, phone)
