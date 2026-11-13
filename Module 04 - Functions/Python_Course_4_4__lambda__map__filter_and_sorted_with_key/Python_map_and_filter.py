# Python map and filter
# Every cell of the notebook, in order, as one script (run: python Python_map_and_filter.py)

# Our list of numbers

nums = [1, 2, 3, 4]
print(nums)

# Python map: change every item

doubled = list(map(lambda n: n * 2, nums))
print(doubled)

# A named test for filter

is_even = lambda n: n % 2 == 0
print(is_even(4))

# Python filter: keep what passes

evens = list(filter(is_even, nums))
print(evens)

# filter with a lambda inside

big = list(filter(lambda n: n > 2, nums))
print(big)

# Combine filter and map

step = filter(lambda n: n > 2, nums)
result = list(map(lambda n: n * 3, step))
print(result)
