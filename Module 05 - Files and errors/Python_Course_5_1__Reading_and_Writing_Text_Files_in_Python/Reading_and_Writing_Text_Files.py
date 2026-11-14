# Reading and Writing Text Files
# Every cell of the notebook, in order, as one script (run: python Reading_and_Writing_Text_Files.py)

# Write a text file with open and write

with open("notes.txt", "w") as f:
    f.write("Hello file\n")
    f.write("Second line\n")

# Read a whole text file with read

with open("notes.txt") as f:
    text = f.read()
    print(text)

# Read a file line by line with a for loop

with open("notes.txt") as f:
    for line in f:
        print(line.strip())

# Append to a file and count its lines

with open("notes.txt", "a") as f:
    f.write("Third line\n")

with open("notes.txt") as f:
    print(len(f.readlines()))

# FileNotFoundError: the most common file mistake

with open("missing.txt") as f:
    print(f.read())
