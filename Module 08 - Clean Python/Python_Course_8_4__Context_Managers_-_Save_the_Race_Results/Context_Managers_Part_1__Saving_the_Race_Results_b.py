# Context Managers Part 1: Saving the Race Results by Hand
# Every cell of the notebook, in order, as one script (run: python Context_Managers_Part_1__Saving_the_Race_Results_b.py)

# The current folder with Path.cwd()

from pathlib import Path
print(Path.cwd().name)

# open() in write mode creates finish.txt

f = open("finish.txt", "w")
print(f.name, f.mode, f.closed)

# writelines() writes the first results

f.writelines(["Asha 58\n", "Ben 61"])
print("written, closed:", f.closed)

# The empty file problem: read_text and len

text = Path("finish.txt").read_text()
print(len(text))

# close() sends the buffer to the file

f.close()
print("closed:", f.closed)

# Read the file again: the results are saved

text = Path("finish.txt").read_text()
print(len(text))
