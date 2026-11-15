# Context Managers: Save the Race Results Safely (Part 2)
# Every cell of the notebook, in order, as one script (run: python Context_Managers__Save_the_Race_Results_Safely__Pa.py)

# ## Setup: bring Path back into a new notebook

from pathlib import Path
print("Path is ready:", Path("finish.txt"))

# ## Write the race results with a with block

with open("finish.txt", "w") as f:
    f.writelines(["Asha 58\n", "Ben 61"])

# ## Read the file back with read_text

print(Path("finish.txt").read_text())

# ## Read a file line by line with a for loop

with open("finish.txt") as f:
    for line in f:
        print(line.strip())

# ## Add a late runner with append mode

with open("finish.txt", "a") as f:
    f.write("\nChen 55")
print("Appended Chen 55")

# ## Check the results file after appending

print(Path("finish.txt").read_text())
