# Python Course 6.2: __init__ and Attributes
# Every cell of the notebook, in order, as one script (run: python Python_Course_6_2____init___and_Attributes.py)

# ## Defining __init__ and self in a class

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# ## Creating an object: values go into __init__

d = Dog("Rex", 3)
print(d.name, d.age)

# ## Changing an attribute later

d.age = d.age + 1
print(d.age)
