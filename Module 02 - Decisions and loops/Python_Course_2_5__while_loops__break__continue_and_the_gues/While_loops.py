# While loops
# Every cell of the notebook, in order, as one script (run: python While_loops.py)

# ## While loop with a counter

count = 1
while count <= 3:
    print("Round", count)
    count = count + 1

# ## Real example: a water tank filling

level = 0
while level < 50:
    level = level + 20
    print("Water level", level)

# ## Keep asking until the answer is right

answer = int(input("What is 2 + 3? "))
while answer != 5:
    answer = int(input("Try again: "))
print("Correct!")

# ## Wrong answer first, then the right one

code = int(input("Enter the secret number: "))
while code != 5:
    code = int(input("Wrong, try again: "))
print("Door open")
