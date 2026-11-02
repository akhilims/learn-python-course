# Asking the user with input()
# Every cell of the notebook, in order, as one script (run: python Asking_the_user_with_input.py)

# ## Ask a name with input()

name = input("What is your name? ")
print("Hello,", name)

# ## The answer is always text

age = input("How old are you? ")
print(type(age))

# ## The common mistake: text plus number

age = input("How old are you? ")
print(age + 1)

# ## Convert the answer with int()

age = int(input("How old are you? "))
print("Next year you will be", age + 1)

# ## Bus fare: int and float together

rides = int(input("How many rides? "))
fare = float(input("Fare per ride? "))
total = rides * fare
print(f"Total: {total:.2f}")
