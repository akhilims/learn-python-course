# Decorators: Stamp Every Announcement (Part 2)
# Every cell of the notebook, in order, as one script (run: python Decorators__Stamp_Every_Announcement__Part_2.py)

# ## A decorator that returns the answer

def stamp(fn):
    def wrapper(*args):
        print("start")
        result = fn(*args)
        print("end")
        return result
    return wrapper

print("stamp is ready:", callable(stamp))

# ## The @ shortcut on announce

@stamp
def announce(msg):
    print("Runner", msg)

print("announce is now wrapped:", announce.__name__)

# ## Calling the decorated announcer

announce("Dev")

# ## One decorator, a second function

@stamp
def add(a, b):
    return a + b

print("add is now wrapped:", add.__name__)

# ## Using the returned answer

print(add(30, 8))
