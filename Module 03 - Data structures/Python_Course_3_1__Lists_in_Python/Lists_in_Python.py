# Lists in Python
# Every cell of the notebook, in order, as one script (run: python Lists_in_Python.py)

# # Lists: store many values in one variable

movies = ["Up", "Coco", "Frozen", "Cars"]
print(movies)
print(type(movies))
print(len(movies))

# # Index numbers: why counting starts at 0

print(movies[0])
print(movies[2])
print(movies[-1])

# # IndexError: index out of range

print(movies[4])

# # The fix: use a valid index

print(movies[3])

# # Change a list: append, insert, remove, pop

scores = [10, 25, 40]
scores.append(55)
scores.insert(0, 5)
scores[0] = 8
scores.remove(25)
last = scores.pop()
print(last, scores)

# # The in keyword and len

print("Coco" in movies)
print("Shrek" in movies)
print(len(movies))

# # Loop through a list with range and len

for i in range(len(movies)):
    print(i + 1, movies[i])

# # Real example: a weekend to-do list

todo = ["wash car", "call mum", "buy milk"]
todo.append("clean room")
todo.remove("call mum")
for i in range(len(todo)):
    print(i + 1, todo[i])
