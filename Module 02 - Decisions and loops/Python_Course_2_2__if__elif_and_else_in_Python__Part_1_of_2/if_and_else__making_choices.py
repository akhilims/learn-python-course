# if and else: making choices
# Every cell of the notebook, in order, as one script (run: python if_and_else__making_choices.py)

# ## The if statement: run code only when True

is_raining = True
if is_raining:
    print("Take an umbrella")
print("Have a nice day")

# ## if and else: jacket or T-shirt

temperature = 12
if temperature < 15:
    print("Wear a jacket")
else:
    print("A T-shirt is fine")

# ## if and else: even or odd number

number = 7
if number % 2 == 0:
    print("Even number")
else:
    print("Odd number")

# ## if and else: a password check

password = "sunflower"
if password == "sunflower":
    print("Welcome back!")
else:
    print("Wrong password")

# ## Common error: the missing colon

if number > 5
    print("Big number")
