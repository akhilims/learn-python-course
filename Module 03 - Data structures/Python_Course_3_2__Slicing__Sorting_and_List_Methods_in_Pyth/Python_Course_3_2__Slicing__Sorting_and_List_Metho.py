# Python Course 3.2: Slicing, Sorting and List Methods
# Every cell of the notebook, in order, as one script (run: python Python_Course_3_2__Slicing__Sorting_and_List_Metho.py)

# List slicing: take part of a list

days = ["Monday", "Tuesday", "Wednesday",
        "Thursday", "Friday", "Saturday"]
print(days[1:4])
print(days[:3])
print(days[-2:])

# Step, reverse and copying a slice

print(days[::2])
print(days[::-1])
part = days[:3]
part[0] = "Holiday"
print(part)
print(days)

# sort() vs sorted(): put a list in order

scores = [72, 95, 60, 88, 79]
print(sorted(scores))
print(scores)
scores.sort(reverse=True)
print(scores)

# Common mistake: print(scores.sort()) shows None

print(scores.sort())
scores.sort()
print(scores)

# Useful list methods: count, index, extend, reverse

cart = ["milk", "eggs", "milk", "bread"]
print(cart.count("milk"))
print(cart.index("eggs"))
cart = cart + ["tea"]
cart.extend(["jam", "rice"])
cart.reverse()
print(cart)

# Common error: index() of a missing item

print(cart.index("honey"))

# The fix: check with in before index()

item = "honey"
if item in cart:
    print(cart.index(item))
else:
    print(item, "is not in the list")

# Real example: a top 3 leaderboard

scores = [72, 95, 60, 88, 79, 91]
scores.sort(reverse=True)
top3 = scores[:3]
print("Top 3:", top3)
print("Best:", max(scores))
print("Lowest:", min(scores))
print("Total:", sum(scores))
