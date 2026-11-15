# Type Hints: list[int] and dict[str, int]
# Every cell of the notebook, in order, as one script (run: python Type_Hints__list_int__and_dict_str__int.py)

# Type hint for a list: list[int]

def best(laps: list[int]) -> int:
    return min(laps)

print(best.__annotations__)

# Calling a function with a list hint

print(best([62, 58, 61]))

# Type hint for a dictionary: dict[str, int]

def top(times: dict[str, int]) -> int:
    return min(times.values())

print(top.__annotations__)

# Race-day results as a dictionary

times = {"Asha": 58, "Chen": 55}
print(times)

# Calling a function with a dictionary hint

print(top(times))

# Type hint on a variable

fast: int = top(times)
print(fast)
