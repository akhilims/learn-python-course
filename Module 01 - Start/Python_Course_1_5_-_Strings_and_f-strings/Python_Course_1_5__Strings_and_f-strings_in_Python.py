# Python Course 1.5: Strings and f-strings in Python
# Every cell of the notebook, in order, as one script (run: python Python_Course_1_5__Strings_and_f-strings_in_Python.py)

# ## Strings and quotes: single or double

greeting = "Hello"
name = 'Maya'
print(greeting)
print(name)
print("It's a string")

# ## Joining with + and repeating with *

first = "Python"
second = "rocks"
print(first + " " + second)
print("ha" * 3)
print("-" * 20)

# ## len(): counting the beads on the thread

word = "Python"
print(len(word))
sentence = "I love Python"
print(len(sentence))

# ## String methods: upper(), lower(), title()

messy = "maya LOPEZ"
print(messy.upper())
print(messy.lower())
print(messy.title())

# ## strip() and replace(): cleaning text

messy = "   fresh pasta   "
print("[" + messy + "]")
print("[" + messy.strip() + "]")
print("fresh pasta".replace("fresh", "baked"))

# ## A TypeError: adding text and a number with +

item = "Pasta"
price = 12
print("The " + item + " costs " + price)

# ## The fix: f-strings with {variable}

item = "Pasta"
price = 12
print(f"The {item} costs {price}")

# ## Two decimals with {number:.2f}

share = 100 / 3
print(share)
print(f"Each person pays {share:.2f}")

# ## Real-world example: a friendly receipt

customer = "maya lopez".title()
item = "pasta"
price = 14.5
line = f"Thanks, {customer}! One {item} costs ${price:.2f}."
print(line)
print("=" * len(line))
