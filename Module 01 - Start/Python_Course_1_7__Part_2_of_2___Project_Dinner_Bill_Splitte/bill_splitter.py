# The finished bill splitter
# packages: none (standard library)

restaurant = "pizza palace"
bill = 92.50
tip_percent = 20
people = 4
pizza_slices = 9
tip = bill * tip_percent / 100
total = bill + tip
each = total / people
title = f"Bill at {restaurant.title()}"
print(title)
print("=" * len(title))
print(f"Bill:      ${bill:.2f}")
print(f"Tip ({tip_percent}%): ${tip:.2f}")
print(f"Total:     ${total:.2f}")
print(f"Each of {people} pays: ${each:.2f}")
print(f"Pizza: {pizza_slices // people} slices each, {pizza_slices % people} left over")

# real output:
# Bill at Pizza Palace
# ====================
# Bill:      $92.50
# Tip (20%): $18.50
# Total:     $111.00
# Each of 4 pays: $27.75
# Pizza: 2 slices each, 1 left over
