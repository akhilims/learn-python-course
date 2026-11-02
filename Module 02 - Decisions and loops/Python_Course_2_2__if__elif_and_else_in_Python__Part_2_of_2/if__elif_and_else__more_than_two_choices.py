# if, elif and else: more than two choices
# Every cell of the notebook, in order, as one script (run: python if__elif_and_else__more_than_two_choices.py)

# elif: a movie ticket price

age = 67
if age < 12:
    price = 5
elif age >= 65:
    price = 6
else:
    price = 10
print(f"Ticket: {price} dollars")

# Order matters: a grade from a score

score = 82
if score >= 90:
    print("Grade A")
elif score >= 75:
    print("Grade B")
elif score >= 50:
    print("Grade C")
else:
    print("Try again")
