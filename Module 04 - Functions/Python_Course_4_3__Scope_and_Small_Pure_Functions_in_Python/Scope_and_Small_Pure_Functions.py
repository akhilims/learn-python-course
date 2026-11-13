# Scope and Small Pure Functions
# Every cell of the notebook, in order, as one script (run: python Scope_and_Small_Pure_Functions.py)

# Python variable scope: local variables

def double(n):
    result = n * 2
    return result
print(double(4))

# The NameError: using a local variable outside

print(result)

# Reading an outside variable in a function

rate = 5
def price(qty):
    return qty * rate
print(price(3))

# Pure functions in Python

def add_tax(amount, tax):
    return amount + amount * tax
print(add_tax(100, 0.1))
