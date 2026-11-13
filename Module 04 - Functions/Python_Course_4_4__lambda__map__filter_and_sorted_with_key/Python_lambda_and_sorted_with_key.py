# Python lambda and sorted with key
# Every cell of the notebook, in order, as one script (run: python Python_lambda_and_sorted_with_key.py)

# Python lambda functions

square = lambda n: n * n
print(square(5))

# Python sorted with key

words = ["pear", "fig", "banana"]
print(sorted(words))
print(sorted(words, key=len))

# Python sorted with key and lambda

people = [("Asha", 21), ("Ben", 19)]
print(sorted(people, key=lambda p: p[1]))
