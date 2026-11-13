# Python Course 4.1: Defining Functions and Return Values
# Every cell of the notebook, in order, as one script (run: python Python_Course_4_1__Defining_Functions_and_Return_V.py)

# # Python functions: def and call

def greet(name):
    print("Hello,", name)
greet("Asha")
greet("Ben")

# # return vs print in Python

def add(a, b):
    return a + b
print(add(2, 3))

# # Using the returned value

total = add(4, 5)
print(total)
print(total * 2)

# # A function that answers yes or no

def is_even(n):
    return n % 2 == 0
print(is_even(10))
