# Module 2 Project: Bus Ticket Desk
# Every cell of the notebook, in order, as one script (run: python Module_2_Project__Bus_Ticket_Desk.py)

# Ask the age and choose the fare

age = int(input("Passenger age? "))
if age < 5:
    fare = 0
elif age < 18:
    fare = 10
else:
    fare = 20
print("Fare:", fare)

# Ask again until the age is valid

age = int(input("Passenger age? "))
while age < 0:
    age = int(input("Age cannot be negative, again: "))
print("Age accepted:", age)

# Serve several passengers with a for loop

people = int(input("How many passengers? "))
total = 0
for person in range(people):
    total = total + 20
print("Total for", people, "passengers:", total)

# Print a receipt with a running total

total = 0
for ticket in range(1, 4):
    total = total + 20
    print("Ticket", ticket, "- running total", total)
print("Thank you, pay", total)
