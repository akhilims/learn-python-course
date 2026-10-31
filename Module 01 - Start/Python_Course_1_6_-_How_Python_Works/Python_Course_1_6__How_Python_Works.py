# Python Course 1.6: How Python Works
# Every cell of the notebook, in order, as one script (run: python Python_Course_1_6__How_Python_Works.py)

# The Python interpreter runs code line by line

# The interpreter reads one line, runs it, then moves on
print("Step 1: Python reads this line")
print("Step 2: then this one")
print("Step 3: and this one last")

# Top to bottom: why the order of lines matters

# Python always starts at the top and walks down
score = 5
print("Score:", score)
score = score * 2
print("Score after doubling:", score)

# Case matters: city and City are different variables

# Python is case-sensitive: city and City are two names
city = "Paris"
City = "Tokyo"
print(city)
print(City)

# Case matters inside strings too

# Small and capital letters are different characters
word = "Python"
print(word.replace("p", "J"))
print(word.replace("P", "J"))
print(word.upper())

# Real-world example: a café receipt in Python

# A cafe receipt, built top to bottom
coffee = 3.5
cake = 6.5
total = coffee + cake
print(f"Total: {total}")

# A real NameError: errors stop the run

# One wrong letter: Total instead of total
print("Printing the receipt...")
print(f"You pay {Total}")
print("Thank you, come again!")

# Fixing the NameError with the exact spelling

# Fixed: the exact same spelling as the variable
print("Printing the receipt...")
print(f"You pay {total}")
print("Thank you, come again!")

# Order of steps: compute the tip first

# Order matters: compute first, then use the result
tip = total * 0.1
grand_total = total + tip
print(f"Tip: {tip}")
print(f"Grand total: {grand_total}")

# The full café receipt, printed top to bottom

# The whole receipt in one cell, read top to bottom
print("--- Cafe Receipt ---")
print(f"Coffee: {coffee}")
print(f"Cake: {cake}")
print(f"Tip: {tip}")
print(f"Grand total: {grand_total}")
print("Thank you, come again!")
