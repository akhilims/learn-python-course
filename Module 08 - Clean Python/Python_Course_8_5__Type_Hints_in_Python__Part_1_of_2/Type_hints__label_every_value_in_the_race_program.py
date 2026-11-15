# Type hints: label every value in the race program (Part 1)
# Every cell of the notebook, in order, as one script (run: python Type_hints__label_every_value_in_the_race_program.py)

# A helper with no labels

def faster(lap, cut):
    return lap - cut

print("defined:", faster.__name__)

# Calling the unlabelled helper

print(faster(60, 5))

# Type hints: colon for inputs, arrow for result

def faster(lap: int, cut: int) -> int:
    return lap - cut

print(faster.__annotations__)

# Hints change nothing at run time

print(faster(60, 5))

# Another hinted helper: double

def double(x: int) -> int:
    return x * 2

print(double.__annotations__)

# Python does not check type hints

print(double("ab"))
