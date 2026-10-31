# Dinner bill splitter, Part 1
# Every cell of the notebook, in order, as one script (run: python Dinner_bill_splitter__Part_1.py)

# Settings: restaurant, bill, tip and people

# Dinner bill splitter
restaurant = "pizza palace"
bill = 92.50
tip_percent = 20
people = 4
print(restaurant)

# Tip, total and what each person pays

tip = bill * tip_percent / 100
total = bill + tip
each = total / people
print(each)

# A heading with title() and len()

title = f"Bill at {restaurant.title()}"
print(title)
print("=" * len(title))

# Money lines with f-strings and two decimals

print(f"Bill:      ${bill:.2f}")
print(f"Tip:       ${tip:.2f}")
print(f"Total:     ${total:.2f}")
print(f"Each of {people} pays: ${each:.2f}")

# A real error: case matters

print(Bill)

# The fix: the same spelling as the variable

print(bill)
