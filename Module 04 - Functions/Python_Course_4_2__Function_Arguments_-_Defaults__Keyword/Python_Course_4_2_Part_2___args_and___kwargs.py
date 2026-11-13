# Python Course 4.2 Part 2: *args and **kwargs
# Every cell of the notebook, in order, as one script (run: python Python_Course_4_2_Part_2___args_and___kwargs.py)

# Python *args: any number of values

def total(*nums):
    return sum(nums)
print(total(1, 2, 3))

# Python **kwargs: any labeled values

def show(**info):
    print(info)
show(name="Asha", age=21)

# Mixing defaults and **kwargs in one function

def make_order(item, qty=1, **notes):
    print(item, qty, notes)
make_order("tea", qty=2, sugar="no")

# Calling with and without extras

make_order("coffee")
make_order("milk", 3)
