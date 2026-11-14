# Dataclasses: a shortcut for data-holding classes
# Every cell of the notebook, in order, as one script (run: python Dataclasses__a_shortcut_for_data-holding_classes.py)

# ## Dataclass: the Book blueprint

from dataclasses import dataclass
@dataclass
class Book:
    title: str
    pages: int

# ## Creating and printing a dataclass

b = Book("Python", 300)
print(b)

# ## Equality and changing fields

print(b == Book("Python", 300))
b.pages = 350
print(b.pages)
