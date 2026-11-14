# Errors: finally and raise
# Every cell of the notebook, in order, as one script (run: python Errors__finally_and_raise.py)

# finally: code that always runs

try:
    n = int("42")
except ValueError:
    print("bad")
finally:
    print("done")

# raise: report your own error

def set_age(age):
    if age < 0:
        msg = "age cannot be negative"
        raise ValueError(msg)
    return age

# Catching your own error with try and except

try:
    set_age(-1)
except ValueError as e:
    print(e)
