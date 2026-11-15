# Decorators: Stamp Every Announcement (Part 1)
# Every cell of the notebook, in order, as one script (run: python Decorators__Stamp_Every_Announcement__Part_1.py)

# ## A plain announcer function

def announce(msg):
    print("Runner", msg)

print("Defined:", announce.__name__)

# ## Calling the announcer

announce("Asha")

# ## A function is a value

show = announce
show("Ben")

# ## The decorator: stamp and wrapper

def stamp(fn):
    def wrapper(*args):
        print("start")
        result = fn(*args)
        print("end")
    return wrapper

print("Defined:", stamp.__name__)

# ## Applying the decorator by hand

announce = stamp(announce)
announce("Chen")
