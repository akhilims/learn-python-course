# Booleans and Comparisons in Python
# Every cell of the notebook, in order, as one script (run: python Booleans_and_Comparisons_in_Python.py)

# True and False: the bool type

is_open = True
print(is_open)
print(type(is_open))

# Comparing numbers with comparison operators

price = 40
budget = 50
print(price < budget)
print(price == budget)
print(price != budget)
print(price >= 45)

# Comparing strings: case matters

print("apple" == "apple")
print("apple" == "Apple")

# Common mistake: one equals sign versus two

print(price = budget)

# Real-world check with and, or, not

price = 40
budget = 50
in_stock = True
can_buy = price <= budget and in_stock
print(can_buy)
print(not in_stock)
print(price > 100 or in_stock)
