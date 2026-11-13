# Function Arguments Part 1: Defaults and Keyword Arguments
# Every cell of the notebook, in order, as one script (run: python Function_Arguments_Part_1__Defaults_and_Keyword_Ar.py)

# ## Python default arguments

def greet(name, greeting="Hello"):
    print(greeting, name)
greet("Asha")

# ## Python keyword arguments

greet("Ben", "Hi")
greet(name="Cara", greeting="Hey")

# ## Python TypeError: missing required argument

greet()
