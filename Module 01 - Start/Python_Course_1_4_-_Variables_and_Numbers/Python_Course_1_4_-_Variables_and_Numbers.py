# Python Course 1.4 - Variables and Numbers
# Every cell of the notebook, in order, as one script (run: python Python_Course_1_4_-_Variables_and_Numbers.py)

# # Variables and numbers

# A variable is a labelled box
meal_price = 20
restaurant = "Luigi's Kitchen"
print(restaurant)
print(meal_price)

# ## Good names

# Good names: lowercase, words joined by underscores
tip_percent = 10
number_of_guests = 4
table_2 = 55
# Bad names (they would fail):
# 2table = 55   starts with a digit
# my price = 5  has a space
print(tip_percent)
print(number_of_guests)
print(table_2)

# ## int and float

whole = 7
decimal = 7.5
print(whole)
print(decimal)
# Division with / always gives a float
print(10 / 5)
print(10 / 4)

a = 17
b = 5
print(a + b)
print(a - b)
print(a * b)
print(a / b)

# Floor division, remainder and power
print(17 // 5)
print(17 % 5)
print(2 ** 10)
minutes = 135
print(minutes // 60)
print(minutes % 60)

# A variable can change
score = 10
print(score)
score = 15
print(score)
score = score + 5
print(score)

# ## A typo on purpose

# Oops: one extra letter in the name
print(meal_pricee)

# Fixed, now the restaurant bill
print(meal_price)
quantity = 3
subtotal = meal_price * quantity
discount = 10
discount_amount = subtotal * discount / 100
total = subtotal - discount_amount
print(subtotal)
print(discount_amount)
print(total)

# Split the bill with a tip
tip = total * tip_percent / 100
grand_total = total + tip
per_person = grand_total / number_of_guests
print(tip)
print(grand_total)
print(per_person)
