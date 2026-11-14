# Errors: try and except
# Every cell of the notebook, in order, as one script (run: python Errors__try_and_except.py)

# ## Catching errors with try and except

try:
    n = int("abc")
except ValueError:
    print("Not a number")

# ## Reading the error message with as e

try:
    print(10 / 0)
except ZeroDivisionError as e:
    print("Error:", e)

# ## Handling a missing file: FileNotFoundError

try:
    open("missing.txt")
except FileNotFoundError:
    print("No such file")
