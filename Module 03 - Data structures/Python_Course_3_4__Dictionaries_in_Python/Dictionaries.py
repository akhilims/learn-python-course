# Dictionaries
# Every cell of the notebook, in order, as one script (run: python Dictionaries.py)

# Python dictionaries: store key and value pairs

ages = {"Asha": 21, "Ben": 25}
print(ages["Asha"])
ages["Cara"] = 30
print(ages)

# KeyError: a missing key is an error

print(ages["Zed"])

# Dictionary get(): avoid KeyError

print(ages.get("Zed", 0))
print("Asha" in ages)
del ages["Ben"]

# Loop over a dictionary with items()

for name, age in ages.items():
    print(name, age)
