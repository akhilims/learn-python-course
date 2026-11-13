# Recursion and Docstrings
# Every cell of the notebook, in order, as one script (run: python Recursion_and_Docstrings.py)

# Python recursion explained

def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)
print(factorial(5))

# RecursionError: a function with no base case

def bad(n):
    return bad(n - 1)
print(bad(3))

# Python docstrings

def word_count(text):
    """Return how many words are in text."""
    return len(text.split())
print(word_count("to be or not"))
