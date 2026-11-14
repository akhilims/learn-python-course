# Inheritance and Polymorphism, Part 1
# Every cell of the notebook, in order, as one script (run: python Inheritance_and_Polymorphism__Part_1.py)

# The parent class: a general Animal

class Animal:
    def speak(self):
        print("...")

# A child class inherits from its parent

class Dog(Animal):
    pass
d = Dog()
d.speak()

# Overriding a method in the child class

class Dog(Animal):
    def speak(self):
        print("Woof")
Dog().speak()
