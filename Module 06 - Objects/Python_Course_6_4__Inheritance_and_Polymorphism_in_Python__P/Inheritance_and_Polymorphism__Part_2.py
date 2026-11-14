# Inheritance and Polymorphism, Part 2
# Every cell of the notebook, in order, as one script (run: python Inheritance_and_Polymorphism__Part_2.py)

# Setting up the Animal and Dog classes

class Animal:
    def speak(self):
        print("...")
class Dog(Animal):
    def speak(self):
        print("Woof")
Dog().speak()

# Adding a Cat class

class Cat(Animal):
    def speak(self):
        print("Meow")
Cat().speak()

# Polymorphism: one call, many answers

for a in [Dog(), Cat()]:
    a.speak()

# super(): build on the parent's method

class Puppy(Dog):
    def speak(self):
        super().speak()
        print("Yip")
Puppy().speak()
